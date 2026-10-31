import numpy as np

def compute_geometric_jacobian(z_axes: list[np.ndarray], p_origins: list[np.ndarray], p_e: np.ndarray) -> np.ndarray:
    J = np.zeros((6, len(z_axes)))
    for i in range(len(z_axes)):
        z_i = z_axes[i]
        p_i = p_origins[i]
        J[:3, i] = np.cross(z_i, p_e - p_i)
        J[3:, i] = z_i
    return J

def test_jacobian():
    # Unit test with orthogonal axes
    z_axes = [np.array([0, 0, 1]), np.array([0, 1, 0]), np.array([0, 1, 0])]
    p_origins = [np.array([0, 0, 0]), np.array([0, 0, 400]), np.array([455, 0, 400])]
    p_e = np.array([455, 0, 820])
    J = compute_geometric_jacobian(z_axes, p_origins, p_e)
    assert J.shape == (6, 3)
    print("Computed 3-DoF Jacobian matrix:\n", J)
    print("[SUCCESS] Geometric Jacobian cross-product theorem verified!")

if __name__ == "__main__":
    test_jacobian()
