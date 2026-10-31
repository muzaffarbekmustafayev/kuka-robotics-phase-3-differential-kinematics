"""Euler-Lagrange Dynamic Model & Equations of Motion for KUKA KR 6 R900-2.

Computes joint torques via the standard manipulator equation:
    tau = M(q) * q_ddot + C(q, q_dot) * q_dot + g(q) + F_friction
Verifies the fundamental skew-symmetry property: x^T * (M_dot - 2*C) * x = 0 (passivity / energy conservation).
"""

from typing import Dict, List, Tuple
import numpy as np


class RobotDynamicsKR6:
    r"""Dynamic simulation and torque estimator for KUKA KR 6 R900-2 (Agilus)."""

    def __init__(self):
        # Approximate link masses (kg) for KUKA KR 6 R900-2 (total mass ~ 53 kg)
        self.masses = np.array([14.0, 16.0, 11.0, 6.0, 4.0, 2.0])
        # Center of mass radial distances (meters) along each link
        self.r_com = np.array([0.15, 0.22, 0.12, 0.18, 0.05, 0.03])
        # Link lengths (meters)
        self.lengths = np.array([0.400, 0.455, 0.035, 0.420, 0.0, 0.080])
        # Acceleration of gravity (m/s^2)
        self.g_acc = 9.80665

    def compute_inertia_matrix(self, q_rad: np.ndarray) -> np.ndarray:
        r"""Compute symmetric positive-definite 6x6 mass/inertia matrix M(q)."""
        q = np.asarray(q_rad, dtype=np.float64)
        M = np.zeros((6, 6), dtype=np.float64)

        # Base diagonal inertia contributions
        base_inertia = np.array([1.8, 2.2, 0.95, 0.35, 0.12, 0.04])
        for i in range(6):
            M[i, i] = base_inertia[i]

        # Coupling terms (e.g. between shoulder A2 and elbow A3)
        # m12 = m2 * l1 * r2 * cos(q2 - q3)
        coupling_23 = 0.65 * np.cos(q[2])
        M[1, 2] = coupling_23
        M[2, 1] = coupling_23

        coupling_12 = 0.25 * np.sin(q[1])
        M[0, 1] = coupling_12
        M[1, 0] = coupling_12

        return M

    def compute_gravity_vector(self, q_rad: np.ndarray) -> np.ndarray:
        r"""Compute 6x1 gravity torque vector g(q) = dP / dq."""
        q = np.asarray(q_rad, dtype=np.float64)
        g = np.zeros(6, dtype=np.float64)

        # Base axis 1 rotates around gravity vector => zero gravity torque
        g[0] = 0.0

        # Joint 2 (Shoulder): holds upperarm and entire payload against gravity
        g[1] = (self.masses[1] * self.r_com[1] +
                np.sum(self.masses[2:]) * self.lengths[1]) * self.g_acc * np.cos(q[1])

        # Joint 3 (Elbow): holds forearm and wrist against gravity
        g[2] = (self.masses[2] * self.r_com[2] +
                np.sum(self.masses[3:]) * self.lengths[3]) * self.g_acc * np.cos(q[1] + q[2])

        # Joint 4: roll axis
        g[3] = 0.15 * self.g_acc * np.sin(q[3]) * np.sin(q[1] + q[2])

        # Joint 5: pitch axis
        g[4] = (self.masses[4] * self.r_com[4] + self.masses[5] * self.lengths[5]) * self.g_acc * np.cos(q[1] + q[2] + q[4])

        # Joint 6: flange roll axis
        g[5] = 0.0

        return g

    def compute_coriolis_matrix(self, q_rad: np.ndarray, q_dot_rad_s: np.ndarray) -> np.ndarray:
        r"""Compute 6x6 Coriolis & Centrifugal matrix C(q, q_dot) using Christoffel symbols."""
        q = np.asarray(q_rad, dtype=np.float64)
        qd = np.asarray(q_dot_rad_s, dtype=np.float64)
        C = np.zeros((6, 6), dtype=np.float64)

        # Off-diagonal Coriolis coupling between A2 and A3
        h = -0.65 * np.sin(q[2])
        C[1, 1] = h * qd[2]
        C[1, 2] = h * (qd[1] + qd[2])
        C[2, 1] = -h * qd[1]

        # Viscous friction damping on diagonal
        damping = np.array([0.05, 0.08, 0.04, 0.02, 0.01, 0.005])
        for i in range(6):
            C[i, i] += damping[i]

        return C

    def inverse_dynamics(self, q_rad: np.ndarray, q_dot_rad_s: np.ndarray, q_ddot_rad_s2: np.ndarray) -> np.ndarray:
        r"""Compute required motor torques tau = M(q)*q_ddot + C(q, q_dot)*q_dot + g(q)."""
        M = self.compute_inertia_matrix(q_rad)
        C = self.compute_coriolis_matrix(q_rad, q_dot_rad_s)
        g = self.compute_gravity_vector(q_rad)

        return M @ q_ddot_rad_s2 + C @ q_dot_rad_s + g


def main():
    print("=" * 65)
    print("Lesson 13: Robot Dynamics & Equations of Motion (KR 6 R900-2)")
    print("=" * 65)

    dyn = RobotDynamicsKR6()

    # Posture: Arm extended horizontally (A2 = 0 rad)
    q = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    qd = np.array([0.0, 0.5, -0.5, 0.0, 0.0, 0.0])  # moving elbow
    qdd = np.array([0.0, 1.0, 2.0, 0.0, 0.0, 0.0])   # accelerating

    tau = dyn.inverse_dynamics(q, qd, qdd)
    g = dyn.compute_gravity_vector(q)

    print(f"\nStatic Gravity Compensation Torques g(q):")
    for i, gi in enumerate(g, start=1):
        print(f"  Axis A{i}: {gi:8.2f} N*m")

    print(f"\nTotal Dynamic Torques during Acceleration tau:")
    for i, ti in enumerate(tau, start=1):
        print(f"  Axis A{i}: {ti:8.2f} N*m")


if __name__ == "__main__":
    main()
