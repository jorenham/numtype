from typing import Any, Literal, TypeAlias
from typing_extensions import TypeVar, assert_type

import numpy as np
import numpy.typing as npt
from _numtype import Array, AtLeast2D
from numpy.linalg._linalg import EigResult, EighResult, QRResult, SVDResult, SlogdetResult

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_Array_2d: TypeAlias = Array[_ScalarT, tuple[int, int]]
_Array_2nd: TypeAlias = Array[_ScalarT, AtLeast2D]

###

AR_i8: npt.NDArray[np.int64]
AR_f8: npt.NDArray[np.float64]
AR_c16: npt.NDArray[np.complex128]
AR_O: npt.NDArray[np.object_]
AR_m: npt.NDArray[np.timedelta64]
AR_S: npt.NDArray[np.str_]
AR_b: npt.NDArray[np.bool]

###

assert_type(np.linalg.tensorsolve(AR_i8, AR_i8), npt.NDArray[np.float64])
assert_type(np.linalg.tensorsolve(AR_i8, AR_f8), npt.NDArray[np.float64])
assert_type(np.linalg.tensorsolve(AR_c16, AR_f8), npt.NDArray[np.complex128])

assert_type(np.linalg.solve(AR_i8, AR_i8), npt.NDArray[np.float64])
assert_type(np.linalg.solve(AR_i8, AR_f8), npt.NDArray[np.float64])
assert_type(np.linalg.solve(AR_c16, AR_f8), npt.NDArray[np.complex128])

assert_type(np.linalg.tensorinv(AR_i8), _Array_2nd[np.float64])
assert_type(np.linalg.tensorinv(AR_f8), _Array_2nd[np.float64])
assert_type(np.linalg.tensorinv(AR_c16), _Array_2nd[np.complex128])

assert_type(np.linalg.inv(AR_i8), _Array_2nd[np.float64])
assert_type(np.linalg.inv(AR_f8), _Array_2nd[np.float64])
assert_type(np.linalg.inv(AR_c16), _Array_2nd[np.complex128])

assert_type(np.linalg.matrix_power(AR_i8, -1), _Array_2nd[np.float64])
assert_type(np.linalg.matrix_power(AR_f8, 0), _Array_2nd[np.float64])
assert_type(np.linalg.matrix_power(AR_c16, 1), _Array_2nd[np.complex128])
assert_type(np.linalg.matrix_power(AR_O, 2), _Array_2nd[np.object_])

assert_type(np.linalg.cholesky(AR_i8), _Array_2nd[np.float64])
assert_type(np.linalg.cholesky(AR_f8), _Array_2nd[np.float64])
assert_type(np.linalg.cholesky(AR_c16), _Array_2nd[np.complex128])

assert_type(np.linalg.outer(AR_i8, AR_i8), _Array_2d[np.int64])
assert_type(np.linalg.outer(AR_f8, AR_f8), _Array_2d[np.float64])
assert_type(np.linalg.outer(AR_c16, AR_c16), _Array_2d[np.complex128])
assert_type(np.linalg.outer(AR_b, AR_b), _Array_2d[np.bool])
assert_type(np.linalg.outer(AR_O, AR_O), _Array_2d[np.object_])
assert_type(np.linalg.outer(AR_i8, AR_m), _Array_2d[np.timedelta64])

assert_type(np.linalg.qr(AR_i8), QRResult[np.float64])
assert_type(np.linalg.qr(AR_f8), QRResult[np.float64])
assert_type(np.linalg.qr(AR_c16), QRResult[np.complex128])

assert_type(np.linalg.eigvals(AR_i8), npt.NDArray[np.float64] | npt.NDArray[np.complex128])
assert_type(np.linalg.eigvals(AR_f8), npt.NDArray[np.float64] | npt.NDArray[np.complex128])
assert_type(np.linalg.eigvals(AR_c16), npt.NDArray[np.complex128])

assert_type(np.linalg.eigvalsh(AR_i8), npt.NDArray[np.float64])
assert_type(np.linalg.eigvalsh(AR_f8), npt.NDArray[np.float64])
assert_type(np.linalg.eigvalsh(AR_c16), npt.NDArray[np.float64])

assert_type(np.linalg.eig(AR_i8), EigResult[np.float64] | EigResult[np.complex128])
assert_type(np.linalg.eig(AR_f8), EigResult[np.float64] | EigResult[np.complex128])
assert_type(np.linalg.eig(AR_c16), EigResult[np.complex128])

assert_type(np.linalg.eigh(AR_i8), EighResult[np.float64, np.float64])
assert_type(np.linalg.eigh(AR_f8), EighResult[np.float64, np.float64])
assert_type(np.linalg.eigh(AR_c16), EighResult[np.float64, np.complex128])

assert_type(np.linalg.svd(AR_i8), SVDResult[np.float64, np.float64])
assert_type(np.linalg.svd(AR_f8), SVDResult[np.float64, np.float64])
assert_type(np.linalg.svd(AR_c16), SVDResult[np.float64, np.complex128])
assert_type(np.linalg.svd(AR_i8, compute_uv=False), npt.NDArray[np.float64])
assert_type(np.linalg.svd(AR_f8, compute_uv=False), npt.NDArray[np.float64])
assert_type(np.linalg.svd(AR_c16, compute_uv=False), npt.NDArray[np.float64])

assert_type(np.linalg.cond([[1, 0], [0, 1]]), np.float64)
assert_type(np.linalg.cond([[[1, 0], [0, 1]]]), npt.NDArray[np.float64])
assert_type(np.linalg.cond(AR_i8), Any)
assert_type(np.linalg.cond(AR_f8), Any)
assert_type(np.linalg.cond(AR_c16), Any)

assert_type(np.linalg.matrix_rank(1), Literal[0, 1])
assert_type(np.linalg.matrix_rank([1]), Literal[0, 1])
assert_type(np.linalg.matrix_rank([[1]]), np.int_)
assert_type(np.linalg.matrix_rank([[[1]]]), npt.NDArray[np.int_])
assert_type(np.linalg.matrix_rank([[[[1]]]]), npt.NDArray[np.int_])
assert_type(np.linalg.matrix_rank(AR_i8), Any)
assert_type(np.linalg.matrix_rank(AR_f8), Any)
assert_type(np.linalg.matrix_rank(AR_c16), Any)

assert_type(np.linalg.pinv(AR_i8), _Array_2nd[np.float64])
assert_type(np.linalg.pinv(AR_f8), _Array_2nd[np.float64])
assert_type(np.linalg.pinv(AR_c16), _Array_2nd[np.complex128])

assert_type(np.linalg.slogdet([[1]]), SlogdetResult[np.float64, np.float64])
assert_type(np.linalg.slogdet([[1.0]]), SlogdetResult[np.float64, np.float64])
assert_type(np.linalg.slogdet([[1j]]), SlogdetResult[np.float64, np.complex128])
assert_type(
    np.linalg.slogdet([[[1]]]),
    SlogdetResult[npt.NDArray[np.float64], npt.NDArray[np.float64]],
)
assert_type(
    np.linalg.slogdet([[[1.0]]]),
    SlogdetResult[npt.NDArray[np.float64], npt.NDArray[np.float64]],
)
assert_type(  # type: ignore[assert-type]  # mypy bug?
    np.linalg.slogdet([[[1j]]]),
    SlogdetResult[npt.NDArray[np.float64], npt.NDArray[np.complex128]],
)
assert_type(np.linalg.slogdet(AR_i8), SlogdetResult)
assert_type(np.linalg.slogdet(AR_f8), SlogdetResult)
assert_type(np.linalg.slogdet(AR_c16), SlogdetResult)

assert_type(np.linalg.det(AR_i8), Any)
assert_type(np.linalg.det(AR_f8), Any)
assert_type(np.linalg.det(AR_c16), Any)

assert_type(
    np.linalg.lstsq(AR_i8, AR_i8),
    tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], np.int32, npt.NDArray[np.float64]],
)
assert_type(
    np.linalg.lstsq(AR_i8, AR_f8),
    tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], np.int32, npt.NDArray[np.float64]],
)
assert_type(
    np.linalg.lstsq(AR_f8, AR_c16),
    tuple[npt.NDArray[np.complex128], npt.NDArray[np.float64], np.int32, npt.NDArray[np.float64]],
)

assert_type(np.linalg.norm(AR_i8), np.float64)
assert_type(np.linalg.norm(AR_f8), np.float64)
assert_type(np.linalg.norm(AR_c16), np.float64)
assert_type(np.linalg.norm(AR_S), np.float64)
assert_type(np.linalg.norm(AR_f8, axis=0), npt.NDArray[np.float64])
assert_type(np.linalg.norm(AR_f8, keepdims=True), _Array_2nd[np.float64])

assert_type(np.linalg.matrix_norm([[True]]), np.float64)
assert_type(np.linalg.matrix_norm([[1]]), np.float64)
assert_type(np.linalg.matrix_norm([[1j]]), np.float64)
assert_type(np.linalg.matrix_norm([["1"]]), np.float64)
assert_type(np.linalg.matrix_norm([[b"1"]]), np.float64)
assert_type(np.linalg.matrix_norm([[[True]]]), npt.NDArray[np.float64])
assert_type(np.linalg.matrix_norm([[[1]]]), npt.NDArray[np.float64])
assert_type(np.linalg.matrix_norm([[[1j]]]), npt.NDArray[np.float64])
assert_type(np.linalg.matrix_norm([[["1"]]]), npt.NDArray[np.float64])
assert_type(np.linalg.matrix_norm([[[b"1"]]]), npt.NDArray[np.float64])
assert_type(np.linalg.matrix_norm(AR_i8), Any)
assert_type(np.linalg.matrix_norm(AR_f8), Any)
assert_type(np.linalg.matrix_norm(AR_c16), Any)
assert_type(np.linalg.matrix_norm(AR_S), Any)

assert_type(np.linalg.vector_norm(AR_i8), np.float64)
assert_type(np.linalg.vector_norm(AR_f8), np.float64)
assert_type(np.linalg.vector_norm(AR_c16), np.float64)
assert_type(np.linalg.vector_norm(AR_S), np.float64)

assert_type(np.linalg.multi_dot([[True], [True]]), np.bool)
assert_type(np.linalg.multi_dot([[1], [1]]), np.int_)
assert_type(np.linalg.multi_dot([[1.0], [1.0]]), np.float64)
assert_type(np.linalg.multi_dot([[1j], [1j]]), np.complex128)
assert_type(np.linalg.multi_dot([AR_i8, AR_i8]), Any)
assert_type(np.linalg.multi_dot([AR_i8, AR_f8]), Any)
assert_type(np.linalg.multi_dot([AR_f8, AR_c16]), Any)
assert_type(np.linalg.multi_dot([AR_O, AR_O]), Any)
assert_type(np.linalg.multi_dot([AR_m, AR_m]), Any)

assert_type(np.linalg.cross(AR_i8, AR_i8), npt.NDArray[np.int64])
assert_type(np.linalg.cross(AR_f8, AR_f8), npt.NDArray[np.float64])
assert_type(np.linalg.cross(AR_c16, AR_c16), npt.NDArray[np.complex128])

assert_type(np.linalg.matmul([True], [True]), np.bool)
assert_type(np.linalg.matmul([2], [2]), np.int_)
assert_type(np.linalg.matmul([2], [True]), np.int_)
assert_type(np.linalg.matmul([1.0], [1.0]), np.float64)
assert_type(np.linalg.matmul([1.0], [2]), np.float64)
assert_type(np.linalg.matmul([1j], [1j]), np.complex128)
assert_type(np.linalg.matmul([True], [1j]), np.complex128)
assert_type(np.linalg.matmul(AR_i8, AR_i8), Any)
assert_type(np.linalg.matmul(AR_f8, AR_f8), Any)
assert_type(np.linalg.matmul(AR_c16, AR_c16), Any)
