import numpy as np


def sum_pos_even(a: np.ndarray) -> int:
    """
    Compute sum of all even positive elements in the input array (can be multidimensional).

    For example:
    array([-3,  7,  0,  4, -2, 10])
    ->
    14

    :param a: input array
    :return: sum
    """
    flattened_arr = a.flatten()
    filtered_arr = flattened_arr[(flattened_arr > 0) & (flattened_arr % 2 == 0)]
    return np.sum(filtered_arr)
