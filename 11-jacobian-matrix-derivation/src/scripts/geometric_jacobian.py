"""Geometric Jacobian Solver & Static Force Mapping for KUKA KR 6 R900-2.

Computes the 6x6 Geometric Jacobian matrix J(q) mapping joint velocities to end-effector
twist (linear velocity v and angular velocity w):
    V_e = [v, w]^T = J(q) * q_dot
and the dual static force relationship via principle of virtual work:
    tau = J(q)^T * F_ext
"""

from typing import List, Tuple
import numpy as np


class GeometricJacobianKR6:
    """Analytical Geometric Jacobian Engine for KUKA KR 6 R900-2."""

    def __init__(self):
        # DH parameters of KR 6 R900-2: (theta_offset_deg, d_mm, a_mm, alpha_deg)
        self.dh_params = [
            (0.0,   400.0, 25.0,  -90.0),
            (-90.0, 0.0,   455.0, 0.0),
            (0.0,   0.0,   35.0,  90.0),
            (0.0,   420.0, 0.0,   -90.0),
            (0.0,   0.0,   0.0,   90.0),
            (0.0,   80.0,  0.0,   180.0),
        ]

    @staticmethod
    def dh_matrix(theta_deg: float, d: float, a: float, alpha_deg: float) -> np.ndarray:
        """Compute standard 4x4 DH transformation matrix."""
        th = np.radians(theta_deg)
        al = np.radians(alpha_deg)

        ct, st = np.cos(th), np.sin(th)
        ca, sa = np.cos(al), np.sin(al)

        return np.array([
            [ct, -st * ca,  st * sa, a * ct],
            [st,  ct * ca, -ct * sa, a * st],
            [0.0, sa,       ca,      d],
            [0.0, 0.0,      0.0,     1.0]
        ], dtype=np.float64)

    def compute_frames(self, joints_deg: List[float]) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """Compute origin positions p_i and z-axis unit vectors z_i for all frames 0..6."""
        T = np.eye(4, dtype=np.float64)
        origins = [np.array([0.0, 0.0, 0.0])]  # p_0 (base origin)
        z_axes = [np.array([0.0, 0.0, 1.0])]   # z_0 (base z axis)

        for q, (offset, d, a, alpha) in zip(joints_deg, self.dh_params):
            Ai = self.dh_matrix(q + offset, d, a, alpha)
            T = T @ Ai
            origins.append(T[:3, 3].copy())
            z_axes.append(T[:3, 2].copy())

        return origins, z_axes

    def compute_jacobian(self, joints_deg: List[float]) -> np.ndarray:
        r"""Compute 6x6 Geometric Jacobian matrix in Base frame.

        For revolute joint i:
            J_v,i = z_{i-1} x (p_e - p_{i-1})
            J_w,i = z_{i-1}
        """
        origins, z_axes = self.compute_frames(joints_deg)
        p_e = origins[-1]  # TCP position (flange)

        J = np.zeros((6, 6), dtype=np.float64)

        for i in range(6):
            z_prev = z_axes[i]
            p_prev = origins[i]

            # Linear velocity contribution (cross product)
            J_v = np.cross(z_prev, (p_e - p_prev))
            # Angular velocity contribution
            J_w = z_prev

            J[:3, i] = J_v
            J[3:, i] = J_w

        return J

    def compute_cartesian_velocity(self, joints_deg: List[float], joint_vel_rad_s: np.ndarray) -> np.ndarray:
        """Calculate Cartesian twist V = [v_x, v_y, v_z, w_x, w_y, w_z]^T (mm/s and rad/s)."""
        J = self.compute_jacobian(joints_deg)
        q_dot = np.asarray(joint_vel_rad_s, dtype=np.float64).flatten()
        return J @ q_dot

    def compute_joint_torques(self, joints_deg: List[float], wrench_ext: np.ndarray) -> np.ndarray:
        r"""Calculate static joint torques tau = J^T * F_ext via principle of virtual work.

        wrench_ext: [Fx, Fy, Fz, Mx, My, Mz]^T (N and N*mm)
        tau: [tau_1 .. tau_6]^T (N*mm)
        """
        J = self.compute_jacobian(joints_deg)
        w = np.asarray(wrench_ext, dtype=np.float64).flatten()
        return J.T @ w


def main():
    print("=" * 65)
    print("Lesson 11: Geometric Jacobian & Static Force Mapping (KR 6 R900-2)")
    print("=" * 65)

    jac_engine = GeometricJacobianKR6()

    # Home posture: [0, -90, 90, 0, 0, 0]
    q_home = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    J = jac_engine.compute_jacobian(q_home)

    print(f"\nConfiguration: {q_home}")
    print("Geometric Jacobian Matrix (6x6):")
    print(np.round(J, 2))

    # Test joint velocity [0, 0.1, 0.1, 0, 0, 0] rad/s
    q_dot = np.array([0.0, 0.1, 0.1, 0.0, 0.0, 0.0])
    twist = jac_engine.compute_cartesian_velocity(q_home, q_dot)
    print(f"\nEnd-Effector Twist [v (mm/s), w (rad/s)] for q_dot={q_dot}:")
    print(f"  Linear Vel:  {np.round(twist[:3], 2)} mm/s")
    print(f"  Angular Vel: {np.round(twist[3:], 4)} rad/s")

    # Static load: 50 N downward along Z (-Fz)
    wrench = np.array([0.0, 0.0, -50.0, 0.0, 0.0, 0.0])
    tau = jac_engine.compute_joint_torques(q_home, wrench)
    print(f"\nJoint Torques for external load Fz = -50 N:")
    print(f"  Torques: {np.round(tau / 1000.0, 2)} N*m")


if __name__ == "__main__":
    main()
