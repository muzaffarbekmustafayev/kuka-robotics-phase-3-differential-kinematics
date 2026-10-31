"""Unit tests for Singularity Analyzer and Yoshikawa Manipulability."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from singularity_analyzer import SingularityAnalyzerKR6


def test_wrist_singularity_detection():
    analyzer = SingularityAnalyzerKR6()
    # A5 = 0 degrees must trigger wrist singularity
    q_wrist_sing = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    res = analyzer.evaluate_posture(q_wrist_sing)
    assert res["is_wrist_singularity"] is True
    assert res["is_near_singularity"] is True

    # A5 = 45 degrees should not trigger wrist singularity
    q_normal = [0.0, -90.0, 90.0, 0.0, 45.0, 0.0]
    res_normal = analyzer.evaluate_posture(q_normal)
    assert res_normal["is_wrist_singularity"] is False


def test_manipulability_index_positive():
    analyzer = SingularityAnalyzerKR6()
    q = [10.0, -45.0, 75.0, 15.0, 50.0, -20.0]
    res = analyzer.evaluate_posture(q)

    assert res["manipulability_w"] > 0.0
    assert res["condition_number"] >= 1.0
    assert len(res["singular_values"]) == 6
