"""Kinematic Singularity Analyzer & Manipulability Evaluator for KUKA KR 6 R900-2.

Detects Wrist (A5=0), Shoulder (wrist on A1 axis), and Elbow boundary singularities.
Computes Yoshikawa Manipulability Measure w = sqrt(det(J * J^T)) and SVD condition number.
"""

from typing import Dict, List, Tuple
import numpy as np


class SingularityAnalyzerKR6:
    """Industrial Singularity Supervisor for KUKA 6-axis arms."""

    def __init__(self):
        # Import or reuse Jacobian calculation
        self.dh_params = [
            (0.0,   400.0, 25.0,  -90.0),
            (-90.0, 0.0,   455.0, 0.0),
            (0.0,   0.0,   35.0,  90.0),
            (0.0,   420.0, 0.0,   -90.0),
            (0.0,   0.0,   0.0,   90.0),
            (0.0,   80.0,  0.0,   180.0),
        ]

    def compute_jacobian(self, joints_deg: List[float]) -> np.ndarray:
        """Compute 6x6 geometric Jacobian."""
        T = np.eye(4, dtype=np.float64)
        origins = [np.array([0.0, 0.0, 0.0])]
        z_axes = [np.array([0.0, 0.0, 1.0])]

        for q, (offset, d, a, alpha) in zip(joints_deg, self.dh_params):
            th = np.radians(q + offset)
            al = np.radians(alpha)
            ct, st = np.cos(th), np.sin(th)
            ca, sa = np.cos(al), np.sin(al)
            Ai = np.array([
                [ct, -st * ca,  st * sa, a * ct],
                [st,  ct * ca, -ct * sa, a * st],
                [0.0, sa,       ca,      d],
                [0.0, 0.0,      0.0,     1.0]
            ], dtype=np.float64)
            T = T @ Ai
            origins.append(T[:3, 3].copy())
            z_axes.append(T[:3, 2].copy())

        p_e = origins[-1]
        J = np.zeros((6, 6), dtype=np.float64)
        for i in range(6):
            J[:3, i] = np.cross(z_axes[i], (p_e - origins[i]))
            J[3:, i] = z_axes[i]
        return J

    def evaluate_posture(self, joints_deg: List[float]) -> Dict[str, any]:
        r"""Evaluate kinematic dexterity, Yoshikawa manipulability, and specific singularity modes."""
        q = np.array(joints_deg, dtype=np.float64)
        J = self.compute_jacobian(joints_deg)

        # SVD of Jacobian: J = U * Sigma * V^T
        U, S, Vt = np.linalg.svd(J)

        # 1. Yoshikawa manipulability measure w = product(sigma_i)
        w_index = float(np.prod(S))

        # 2. Condition number kappa = sigma_max / sigma_min
        sigma_max = S[0]
        sigma_min = S[-1]
        condition_number = float(sigma_max / (sigma_min + 1e-12))

        # 3. Detect Specific Singularity Types
        # A. Wrist Singularity: A5 = 0 degrees (collinear A4 and A6 axes)
        is_wrist_singularity = bool(np.isclose(q[4], 0.0, atol=1.0))  # within 1 deg threshold

        # B. Shoulder Singularity: wrist center lies on base Z axis (x_w ~= 0, y_w ~= 0)
        # Check origins[4] (wrist center)
        T = np.eye(4)
        for qi, (offset, d, a, alpha) in zip(q[:4], self.dh_params[:4]):
            th = np.radians(qi + offset)
            al = np.radians(alpha)
            Ai = np.array([
                [np.cos(th), -np.sin(th)*np.cos(al),  np.sin(th)*np.sin(al), a*np.cos(th)],
                [np.sin(th),  np.cos(th)*np.cos(al), -np.cos(th)*np.sin(al), a*np.sin(th)],
                [0.0, np.sin(al), np.cos(al), d],
                [0.0, 0.0, 0.0, 1.0]
            ])
            T = T @ Ai
        p_w = T[:3, 3]
        radial_dist = np.sqrt(p_w[0]**2 + p_w[1]**2)
        is_shoulder_singularity = bool(radial_dist < 30.0)

        # C. Elbow Singularity: arm fully extended or retracted
        # For KR 6, arm extension is characterized by angle between upperarm and forearm
        is_elbow_singularity = bool(np.isclose(q[2], 0.0, atol=2.0) or np.isclose(q[2], 155.0, atol=2.0))

        is_near_singularity = bool(w_index < 1e3 or sigma_min < 1e-2)

        return {
            "manipulability_w": w_index,
            "condition_number": condition_number,
            "singular_values": S.tolist(),
            "is_near_singularity": is_near_singularity,
            "is_wrist_singularity": is_wrist_singularity,
            "is_shoulder_singularity": is_shoulder_singularity,
            "is_elbow_singularity": is_elbow_singularity,
            "wrist_radius_mm": float(radial_dist),
        }


def main():
    print("=" * 65)
    print("Lesson 12: Kinematic Singularity Analysis (KUKA KR 6 R900-2)")
    print("=" * 65)

    analyzer = SingularityAnalyzerKR6()

    # Posture 1: Dexterous configuration
    q_good = [0.0, -60.0, 110.0, 20.0, 45.0, 10.0]
    res1 = analyzer.evaluate_posture(q_good)
    print(f"\n[Posture 1 - Normal Dexterous Work]")
    print(f"  Manipulability w:    {res1['manipulability_w']:.2e}")
    print(f"  Condition number:    {res1['condition_number']:.2f}")
    print(f"  Near Singularity:    {res1['is_near_singularity']}")

    # Posture 2: Pure Wrist Singularity (A5 = 0)
    q_wrist = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    res2 = analyzer.evaluate_posture(q_wrist)
    print(f"\n[Posture 2 - Home with A5 = 0 (Wrist Singularity)]")
    print(f"  Wrist Singularity:   {res2['is_wrist_singularity']}")
    print(f"  Manipulability w:    {res2['manipulability_w']:.2e}")
    print(f"  Condition number:    {res2['condition_number']:.2e}")


if __name__ == "__main__":
    main()
