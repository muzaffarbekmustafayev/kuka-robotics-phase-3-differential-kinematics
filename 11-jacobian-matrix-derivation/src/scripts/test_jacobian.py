"""Unit tests for Geometric Jacobian matrix and virtual work static force mapping."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from geometric_jacobian import GeometricJacobianKR6


def test_jacobian_shape_and_base_z_axis():
    engine = GeometricJacobianKR6()
    q = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    J = engine.compute_jacobian(q)

    assert J.shape == (6, 6)
    # The first joint rotates about global Z axis, so J_w,1 = [0, 0, 1]
    assert np.allclose(J[3:, 0], [0.0, 0.0, 1.0])


def test_pure_joint_1_rotation():
    engine = GeometricJacobianKR6()
    q = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    # Rotate joint 1 with 1 rad/s
    q_dot = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    twist = engine.compute_cartesian_velocity(q, q_dot)

    # Angular velocity must be [0, 0, 1] rad/s
    assert np.allclose(twist[3:], [0.0, 0.0, 1.0])
    # In XHOME, the arm is in the X-Z plane (Y=0), so rotation around Z produces pure Y linear velocity
    assert np.isclose(twist[0], 0.0, atol=1e-4)  # v_x = 0
    assert abs(twist[1]) > 100.0                 # v_y != 0 (tangential velocity)
    assert np.isclose(twist[2], 0.0, atol=1e-4)  # v_z = 0


def test_principle_of_virtual_work_duality():
    engine = GeometricJacobianKR6()
    q = [15.0, -45.0, 60.0, 20.0, 30.0, -10.0]
    q_dot = np.array([0.1, -0.2, 0.15, -0.05, 0.1, -0.3])
    F_ext = np.array([10.0, -5.0, 20.0, 2.0, -1.0, 0.5])  # wrench

    # Mechanical power in Cartesian space: P_cart = F_ext^T * V_e
    twist = engine.compute_cartesian_velocity(q, q_dot)
    p_cart = float(np.dot(F_ext, twist))

    # Mechanical power in Joint space: P_joint = tau^T * q_dot
    tau = engine.compute_joint_torques(q, F_ext)
    p_joint = float(np.dot(tau, q_dot))

    # Virtual work theorem: P_cart == P_joint
    assert np.isclose(p_cart, p_joint, atol=1e-5)
