import pandas as pd


def categorical_mean_diff(df: pd.DataFrame) -> pd.Series:
    """
    Given a dataframe with columns `t` and `type`, compute average time span in seconds
    between two records of the same type. I.e., for each record of type A
    find previous record with the same type, compute time interval between them,
    find average duration of those intervals for each type separately.
    Output should be Series with average interval in seconds for every type.

    For example:
                        t type
    0 2022-11-22 14:00:00    A
    1 2022-11-22 14:00:00    B
    2 2022-11-22 14:10:00    A
    3 2022-11-22 15:00:00    A
    4 2022-11-22 15:20:00    B
    5 2022-11-22 17:30:00    A
    ->
        type
    A    4200.0
    B    4800.0

    :param df: DataFrame with columns `t` (pd.Timestamp) and `type` (object)
    :return: series with average time span for each type. Index should be sorted.
    """
    groups = df.groupby("type")
    return pd.Series(
        {group_name: group_df.t.diff().mean().total_seconds() for (group_name, group_df) in groups}
    )
