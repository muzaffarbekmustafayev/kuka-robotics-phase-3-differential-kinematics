"""Cartesian Admittance (Impedance) Controller for Contact Tasks.

Implements Mass-Spring-Damper compliance dynamics:
    M_d * (x_ddot_c - x_ddot_d) + D_d * (x_dot_c - x_dot_d) + K_d * (x_c - x_d) = F_ext
Used in surface finishing, polishing, grinding, and peg-in-hole assembly operations.
"""

from typing import Tuple, List
import numpy as np


class CartesianAdmittanceController:
    r"""Simulates a 6-DOF Cartesian Admittance Controller with discrete-time Euler integration."""

    def __init__(self,
                 mass_diag: np.ndarray,
                 damping_diag: np.ndarray,
                 stiffness_diag: np.ndarray,
                 dt_sec: float = 0.004):  # 4ms cycle time (typical KUKA RSI rate)
        """
        Args:
            mass_diag: Virtual desired inertia (6,) [kg, kg*m^2]
            damping_diag: Virtual damping (6,) [N*s/m, N*m*s/rad]
            stiffness_diag: Virtual stiffness (6,) [N/m, N*m/rad]
            dt_sec: Discrete sampling period in seconds.
        """
        self.M = np.diag(mass_diag)
        self.D = np.diag(damping_diag)
        self.K = np.diag(stiffness_diag)
        self.M_inv = np.linalg.inv(self.M)
        self.dt = dt_sec

        # State: Compliant position offset e = x_c - x_d, velocity e_dot
        self.e_pos = np.zeros(6, dtype=np.float64)
        self.e_vel = np.zeros(6, dtype=np.float64)

    def reset(self):
        """Reset internal compliant states to zero."""
        self.e_pos.fill(0.0)
        self.e_vel.fill(0.0)

    def update(self, F_ext: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        r"""Update controller state for one time step with external wrench F_ext.

        Returns:
            e_pos: Displacement delta [dx, dy, dz, da, db, dc] in mm and rad.
            e_vel: Velocity delta.
        """
        f = np.asarray(F_ext, dtype=np.float64)

        # Acceleration: e_ddot = M^-1 * (F_ext - D * e_dot - K * e)
        e_acc = self.M_inv @ (f - self.D @ self.e_vel - self.K @ self.e_pos)

        # Semi-implicit Euler integration
        self.e_vel += e_acc * self.dt
        self.e_pos += self.e_vel * self.dt

        return self.e_pos.copy(), self.e_vel.copy()

    def simulate_contact_step_response(self, force_z_newtons: float, duration_sec: float = 1.0) -> List[float]:
        """Simulate vertical penetration response under a step force."""
        self.reset()
        steps = int(duration_sec / self.dt)
        trajectory_z = []

        F_step = np.zeros(6)
        F_step[2] = force_z_newtons  # Contact force in Z

        for _ in range(steps):
            pos_offset, _ = self.update(F_step)
            trajectory_z.append(pos_offset[2])

        return trajectory_z


def main():
    print("=" * 65)
    print("Lesson 14: Cartesian Admittance / Compliance Controller")
    print("=" * 65)

    # Compliant parameters: M = 5 kg, D = 100 N*s/m, K = 500 N/m in Z axis
    m_diag = np.array([5.0, 5.0, 5.0, 0.5, 0.5, 0.5])
    d_diag = np.array([100.0, 100.0, 100.0, 10.0, 10.0, 10.0])
    k_diag = np.array([500.0, 500.0, 500.0, 50.0, 50.0, 50.0])

    controller = CartesianAdmittanceController(m_diag, d_diag, k_diag, dt_sec=0.004)

    # Apply 25 N contact force in Z
    applied_force = 25.0
    traj_z = controller.simulate_contact_step_response(applied_force, duration_sec=0.5)

    # Steady state offset: delta_z = F / K = 25 / 500 = 0.05 m = 50.0 mm
    final_offset_mm = traj_z[-1] * 1000.0
    expected_mm = (applied_force / 500.0) * 1000.0

    print(f"\nStep Force: {applied_force} N in Z direction")
    print(f"Virtual Stiffness K_z: {k_diag[2]} N/m")
    print(f"Final Deflection: {final_offset_mm:.2f} mm (Expected steady-state: {expected_mm:.2f} mm)")
    print(f"Relative Error: {abs(final_offset_mm - expected_mm):.4f} mm")


if __name__ == "__main__":
    main()
