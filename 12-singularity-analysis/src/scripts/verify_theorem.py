import numpy as np

def yoshikawa_manipulability(J: np.ndarray) -> float:
    return float(np.sqrt(max(0.0, np.linalg.det(J @ J.T))))

def test_singularity():
    # Regular Jacobian
    J_regular = np.eye(6)
    w_reg = yoshikawa_manipulability(J_regular)
    assert np.isclose(w_reg, 1.0)
    
    # Singular Jacobian (Wrist singularity: row 3 and 5 linearly dependent)
    J_singular = np.eye(6)
    J_singular[3] = J_singular[5]
    w_sing = yoshikawa_manipulability(J_singular)
    assert np.isclose(w_sing, 0.0)
    print(f"Regular Manipulability: {w_reg:.3f}, Singular Manipulability: {w_sing:.3f}")
    print("[SUCCESS] Singularity criterion and Yoshikawa measure verified!")

if __name__ == "__main__":
    test_singularity()
