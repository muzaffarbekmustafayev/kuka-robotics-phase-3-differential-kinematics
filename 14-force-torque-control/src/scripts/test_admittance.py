"""Unit tests for Cartesian Admittance controller."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from admittance_controller import CartesianAdmittanceController


def test_steady_state_deflection_hooke_law():
    # M = 2 kg, D = 40 N*s/m, K = 200 N/m
    m_diag = np.ones(6) * 2.0
    d_diag = np.ones(6) * 40.0
    k_diag = np.ones(6) * 200.0

    controller = CartesianAdmittanceController(m_diag, d_diag, k_diag, dt_sec=0.002)
    force_z = 20.0  # N

    traj = controller.simulate_contact_step_response(force_z, duration_sec=1.5)
    # Hooke's Law: delta = F / K = 20 / 200 = 0.1 m
    assert np.isclose(traj[-1], 0.1, atol=1e-3)


def test_zero_force_stability():
    m_diag = np.ones(6) * 5.0
    d_diag = np.ones(6) * 50.0
    k_diag = np.ones(6) * 500.0

    controller = CartesianAdmittanceController(m_diag, d_diag, k_diag, dt_sec=0.004)
    traj = controller.simulate_contact_step_response(0.0, duration_sec=0.5)

    # In zero force, deflection must remain strictly zero
    assert np.allclose(traj, 0.0, atol=1e-8)
