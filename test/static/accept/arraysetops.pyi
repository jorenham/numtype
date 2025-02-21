from typing import Any
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt
from _numtype import Array_1d
from numpy.lib._arraysetops_impl import UniqueAllResult, UniqueCountsResult, UniqueInverseResult

AR_b: npt.NDArray[np.bool]
AR_i_: npt.NDArray[np.intp]
AR_f8: npt.NDArray[np.float64]
AR_M: npt.NDArray[np.datetime64]
AR_O: npt.NDArray[np.object_]
AR_LIKE_f8: list[float]

###

assert_type(np.intersect1d(AR_i_, AR_i_), Array_1d[np.intp])
assert_type(np.intersect1d(AR_f8, AR_i_), Array_1d[np.float64])
assert_type(np.intersect1d(AR_M, AR_M, assume_unique=True), Array_1d[np.datetime64])
assert_type(
    np.intersect1d(AR_f8, AR_f8, return_indices=True),
    tuple[Array_1d[np.float64], Array_1d[np.intp], Array_1d[np.intp]],
)

assert_type(np.union1d(AR_i_, AR_i_), Array_1d[np.intp])
assert_type(np.union1d(AR_f8, AR_i_), Array_1d[np.float64])
assert_type(np.union1d(AR_M, AR_M), Array_1d[np.datetime64])

assert_type(np.ediff1d(AR_b), Array_1d[np.int8])
assert_type(np.ediff1d(AR_M), Array_1d[np.timedelta64])
assert_type(np.ediff1d(AR_O), Array_1d[np.object_])
assert_type(np.ediff1d(AR_i_, to_end=[1, 2, 3]), Array_1d[np.intp])
assert_type(np.ediff1d(AR_LIKE_f8, to_begin=[1, 1.5]), Array_1d[np.float64])

assert_type(np.setxor1d(AR_i_, AR_i_), Array_1d[np.intp])
assert_type(np.setxor1d(AR_f8, AR_i_), Array_1d[np.float64])
assert_type(np.setxor1d(AR_M, AR_M, assume_unique=True), Array_1d[np.datetime64])

assert_type(np.setdiff1d(AR_i_, AR_i_), Array_1d[np.intp])
assert_type(np.setdiff1d(AR_f8, AR_i_), Array_1d[np.float64])
assert_type(np.setdiff1d(AR_M, AR_M, assume_unique=True), Array_1d[np.datetime64])

assert_type(np.isin(AR_i_, AR_i_), npt.NDArray[np.bool])
assert_type(np.isin(AR_f8, AR_i_), npt.NDArray[np.bool])
assert_type(np.isin(AR_M, AR_M, assume_unique=True), npt.NDArray[np.bool])
assert_type(np.isin(AR_f8, AR_LIKE_f8, invert=True), npt.NDArray[np.bool])

assert_type(np.unique(AR_f8), npt.NDArray[np.float64])
assert_type(np.unique(AR_LIKE_f8, axis=0), npt.NDArray[Any])
assert_type(np.unique(AR_f8, return_index=True), tuple[npt.NDArray[np.float64], npt.NDArray[np.intp]])
assert_type(np.unique(AR_LIKE_f8, return_index=True), tuple[npt.NDArray[Any], npt.NDArray[np.intp]])
assert_type(np.unique(AR_f8, return_inverse=True), tuple[npt.NDArray[np.float64], npt.NDArray[np.intp]])
assert_type(np.unique(AR_LIKE_f8, return_inverse=True), tuple[npt.NDArray[Any], npt.NDArray[np.intp]])
assert_type(np.unique(AR_f8, return_counts=True), tuple[npt.NDArray[np.float64], npt.NDArray[np.intp]])
assert_type(np.unique(AR_LIKE_f8, return_counts=True), tuple[npt.NDArray[Any], npt.NDArray[np.intp]])
assert_type(
    np.unique(AR_f8, return_index=True, return_inverse=True),
    tuple[npt.NDArray[np.float64], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_f8, return_index=True, return_inverse=True),
    tuple[npt.NDArray[Any], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)
assert_type(
    np.unique(AR_f8, return_index=True, return_counts=True),
    tuple[npt.NDArray[np.float64], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_f8, return_index=True, return_counts=True),
    tuple[npt.NDArray[Any], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)
assert_type(
    np.unique(AR_f8, return_inverse=True, return_counts=True),
    tuple[npt.NDArray[np.float64], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_f8, return_inverse=True, return_counts=True),
    tuple[npt.NDArray[Any], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)
assert_type(
    np.unique(AR_f8, return_index=True, return_inverse=True, return_counts=True),
    tuple[npt.NDArray[np.float64], npt.NDArray[np.intp], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_f8, return_index=True, return_inverse=True, return_counts=True),
    tuple[npt.NDArray[Any], npt.NDArray[np.intp], npt.NDArray[np.intp], npt.NDArray[np.intp]],
)

assert_type(np.unique_all(AR_f8), UniqueAllResult[np.float64])
assert_type(np.unique_all(AR_LIKE_f8), UniqueAllResult[np.float64])
assert_type(np.unique_counts(AR_f8), UniqueCountsResult[np.float64])
assert_type(np.unique_counts(AR_LIKE_f8), UniqueCountsResult[np.float64])
assert_type(np.unique_inverse(AR_f8), UniqueInverseResult[np.float64])
assert_type(np.unique_inverse(AR_LIKE_f8), UniqueInverseResult[np.float64])
assert_type(np.unique_values(AR_f8), Array_1d[np.float64])
assert_type(np.unique_values(AR_LIKE_f8), Array_1d[np.float64])
