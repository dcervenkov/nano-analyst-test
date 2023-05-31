import pathlib

import pandas as pd
import pytest

from . import categorical_mean_diff


CWD = pathlib.Path(__file__).parent.resolve()

@pytest.mark.parametrize(
    ("df", "expected_result"),
    (
        (
            pd.DataFrame(
                {
                    't': [
                        pd.Timestamp('2022-11-22T14:00:00'),
                        pd.Timestamp('2022-11-22T14:00:00'),
                        pd.Timestamp('2022-11-22T14:10:00'),
                        pd.Timestamp('2022-11-22T15:00:00'),
                        pd.Timestamp('2022-11-22T15:20:00'),
                        pd.Timestamp('2022-11-22T17:30:00'),
                    ],
                    'type': ['A', 'B', 'A', 'A', 'B', 'A'],
                }
            ),
            pd.Series({'A': 4200.0, 'B': 4800.0}),
        ),
        (
            pd.read_pickle(CWD / 'test_data/df.pickle'),
            pd.read_pickle(CWD / 'test_data/expected_mean.pickle'),
        ),
    ),
)
def test_categorical_mean_diff(df: pd.DataFrame, expected_result: pd.Series) -> None:
    actual_result = categorical_mean_diff(df)
    actual_result.name = expected_result.name
    actual_result.index.name = expected_result.index.name
    pd.testing.assert_series_equal(actual_result, expected_result)
