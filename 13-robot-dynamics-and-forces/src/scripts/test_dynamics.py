"""Unit tests for Euler-Lagrange robot dynamics model."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from robot_dynamics import RobotDynamicsKR6


def test_mass_matrix_positive_definite():
    dyn = RobotDynamicsKR6()
    q = np.array([0.0, np.pi/4, -np.pi/3, 0.0, 0.0, 0.0])
    M = dyn.compute_inertia_matrix(q)

    # Symmetry check: M = M^T
    assert np.allclose(M, M.T, atol=1e-6)

    # Positive definiteness: eigenvalues > 0
    eigenvalues = np.linalg.eigvals(M)
    assert np.all(eigenvalues > 0.0)


def test_gravity_zero_for_vertical_rotation():
    dyn = RobotDynamicsKR6()
    q = np.array([np.pi/3, 0.0, 0.0, 0.0, 0.0, 0.0])
    g = dyn.compute_gravity_vector(q)

    # Axis 1 rotates perpendicular to gravity, so torque due to gravity must be strictly zero
    assert np.isclose(g[0], 0.0, atol=1e-5)


def test_static_arm_holding_torque():
    dyn = RobotDynamicsKR6()
    q = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    qd = np.zeros(6)
    qdd = np.zeros(6)

    tau_static = dyn.inverse_dynamics(q, qd, qdd)
    g = dyn.compute_gravity_vector(q)

    # In static equilibrium, required torque exactly equals gravity vector
    assert np.allclose(tau_static, g, atol=1e-6)
