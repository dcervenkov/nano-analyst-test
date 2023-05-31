import numpy as np
import pytest

from . import sum_pos_even


@pytest.mark.parametrize(
    ("a", "expected_result"),
    (
        (np.array([1, -3, 6, 0, -8, 2, 5, -3]), 8),
        (np.array(range(-40, 50)), 600),
        (np.array(range(-10, 62, 3)).reshape((4, 6)), 290),
    ),
)
def test_sum_pos_even(a: np.ndarray, expected_result: int) -> None:
    assert sum_pos_even(a) == expected_result
