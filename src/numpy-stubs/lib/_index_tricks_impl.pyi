from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Final, Generic, Literal as L, SupportsIndex, final, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import Array, Is, Matrix, Sequence_nd, _ToArray1_nd
from numpy import ndenumerate, ndindex  # noqa: ICN003
from numpy._core.multiarray import ravel_multi_index, unravel_index
from numpy._typing import ArrayLike, DTypeLike, _DTypeLike, _SupportsDType as _HasDType

__all__ = [
    "c_",
    "diag_indices",
    "diag_indices_from",
    "fill_diagonal",
    "index_exp",
    "ix_",
    "mgrid",
    "ndenumerate",
    "ndindex",
    "ogrid",
    "r_",
    "ravel_multi_index",
    "s_",
    "unravel_index",
]

_T = TypeVar("_T")
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_TupleT = TypeVar("_TupleT", bound=tuple[object, ...])
_ArrayT = TypeVar("_ArrayT", bound=Array)

_BoolT_co = TypeVar("_BoolT_co", bound=bool, default=bool, covariant=True)

_AxisT_co = TypeVar("_AxisT_co", bound=int, default=L[0], covariant=True)
_MatrixT_co = TypeVar("_MatrixT_co", bound=bool, default=L[False], covariant=True)
_NDMinT_co = TypeVar("_NDMinT_co", bound=int, default=L[1], covariant=True)
_Trans1DT_co = TypeVar("_Trans1DT_co", bound=int, default=L[-1], covariant=True)

###

class nd_grid(Generic[_BoolT_co]):
    sparse: _BoolT_co
    def __init__(self, sparse: _BoolT_co = ...) -> None: ...
    @overload
    def __getitem__(self: nd_grid[L[False]], key: slice | Sequence[slice]) -> Array: ...
    @overload
    def __getitem__(self: nd_grid[L[True]], key: slice | Sequence[slice]) -> tuple[Array, ...]: ...

@final
class MGridClass(nd_grid[L[False]]):
    def __init__(self) -> None: ...

@final
class OGridClass(nd_grid[L[True]]):
    def __init__(self) -> None: ...

class AxisConcatenator(Generic[_AxisT_co, _MatrixT_co, _NDMinT_co, _Trans1DT_co]):
    __slots__ = "axis", "matrix", "ndmin", "trans1d"

    axis: _AxisT_co
    matrix: _MatrixT_co
    trans1d: _Trans1DT_co
    ndmin: _NDMinT_co

    #
    def __init__(
        self,
        /,
        axis: _AxisT_co = ...,
        matrix: _MatrixT_co = ...,
        ndmin: _NDMinT_co = ...,
        trans1d: _Trans1DT_co = ...,
    ) -> None: ...

    # TODO(jorenham): annotate this
    def __getitem__(self, key: Incomplete, /) -> Incomplete: ...
    def __len__(self, /) -> L[0]: ...

    #
    @staticmethod
    @overload
    def concatenate(*a: _ToArray1_nd[_ScalarT], axis: SupportsIndex | None = 0, out: None = None) -> Array[_ScalarT]: ...
    @staticmethod
    @overload
    def concatenate(*a: ArrayLike, axis: SupportsIndex | None = 0, out: _ArrayT) -> _ArrayT: ...
    @staticmethod
    @overload
    def concatenate(*a: ArrayLike, axis: SupportsIndex | None = 0, out: None = None) -> Array: ...

    #
    @staticmethod
    @overload
    def makemat(data: _ToArray1_nd[_ScalarT], dtype: None = None, copy: bool = True) -> Matrix[_ScalarT]: ...
    @staticmethod
    @overload
    def makemat(data: ArrayLike, dtype: _DTypeLike[_ScalarT], copy: bool = True) -> Matrix[_ScalarT]: ...
    @staticmethod
    @overload
    def makemat(data: ArrayLike, dtype: DTypeLike | None = None, copy: bool = True) -> Matrix: ...

@final
class RClass(AxisConcatenator[L[0], L[False], L[1], L[-1]]):
    def __init__(self, /) -> None: ...

@final
class CClass(AxisConcatenator[L[-1], L[False], L[2], L[0]]):
    def __init__(self, /) -> None: ...

class IndexExpression(Generic[_BoolT_co]):
    maketuple: _BoolT_co
    def __init__(self, /, maketuple: _BoolT_co) -> None: ...
    #
    @overload
    def __getitem__(self, item: _TupleT, /) -> _TupleT: ...  # type: ignore[overload-overlap]
    @overload
    def __getitem__(self: IndexExpression[L[False]], item: _T, /) -> _T: ...
    @overload
    def __getitem__(self: IndexExpression[L[True]], item: _T, /) -> tuple[_T]: ...
    @overload
    def __getitem__(self, item: _T, /) -> _T | tuple[_T]: ...

@overload
def ix_(*args: _HasDType[_DTypeT] | Sequence_nd[_HasDType[_DTypeT]]) -> tuple[np.ndarray[tuple[int, ...], _DTypeT], ...]: ...
@overload
def ix_(*args: str | Sequence_nd[str]) -> tuple[Array[np.str_], ...]: ...
@overload
def ix_(*args: bytes | Sequence_nd[bytes]) -> tuple[Array[np.bytes_], ...]: ...
@overload
def ix_(*args: bool | Sequence_nd[bool]) -> tuple[Array[np.bool], ...]: ...
@overload
def ix_(*args: Is[int] | Sequence_nd[Is[int]]) -> tuple[Array[np.intp], ...]: ...
@overload
def ix_(*args: Is[float] | Sequence_nd[Is[float]]) -> tuple[Array[np.float64], ...]: ...
@overload
def ix_(*args: Is[complex] | Sequence_nd[Is[complex]]) -> tuple[Array[np.complex128], ...]: ...
@overload
def ix_(*args: int | Sequence_nd[int]) -> tuple[Array[np.intp | np.bool], ...]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload
def ix_(*args: float | Sequence_nd[float]) -> tuple[Array[np.float64 | np.intp | np.bool], ...]: ...  # type: ignore[overload-cannot-match]
@overload
def ix_(*args: complex | Sequence_nd[complex]) -> tuple[Array[np.complex128 | np.float64 | np.intp | np.bool], ...]: ...  # type: ignore[overload-cannot-match]

#
def fill_diagonal(a: Array, val: Any, wrap: bool = ...) -> None: ...
def diag_indices(n: int, ndim: int = ...) -> tuple[Array[np.int_], ...]: ...
def diag_indices_from(arr: ArrayLike) -> tuple[Array[np.int_], ...]: ...

###

mgrid: Final[MGridClass] = ...
ogrid: Final[OGridClass] = ...

r_: Final[RClass] = ...
c_: Final[CClass] = ...

index_exp: Final[IndexExpression[L[True]]] = ...
s_: Final[IndexExpression[L[False]]] = ...
