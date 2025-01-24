from collections.abc import Callable, Sequence
from typing import (
    Any,
    Final,
    Literal as L,
    NoReturn,
    SupportsAbs,
    SupportsIndex,
    TypeAlias,
    TypeGuard,
    TypeVar,
    overload,
)
from typing_extensions import Unpack

import numpy as np
from numpy import (
    False_,
    True_,
    _OrderCF,
    _OrderKACF,
    # re-exports
    bitwise_not,
    broadcast,
    complexfloating,
    dtype,
    flatiter,
    float64,
    floating,
    from_dlpack,
    # other
    generic,
    inf,
    int_,
    intp,
    little_endian,
    matmul,
    nan,
    ndarray,
    nditer,
    newaxis,
    object_,
    signedinteger,
    timedelta64,
    ufunc,
    unsignedinteger,
    vecdot,
)
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
    _ArrayLikeUInt_co,
    _ArrayLikeUnknown,
    _DTypeLike,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc,
    _SupportsDType,
)

from .multiarray import (
    # other
    _Array,
    _ConstructorEmpty,
    _KwargsEmpty,
    # re-exports
    arange,
    array,
    asanyarray,
    asarray,
    ascontiguousarray,
    asfortranarray,
    can_cast,
    concatenate,
    copyto,
    dot,
    empty,
    empty_like,
    frombuffer,
    fromfile,
    fromiter,
    fromstring,
    inner,
    lexsort,
    may_share_memory,
    min_scalar_type,
    nested_iters,
    promote_types,
    putmask,
    result_type,
    shares_memory,
    vdot,
    where,
    zeros,
)

__all__ = [
    "False_",
    "True_",
    "allclose",
    "arange",
    "argwhere",
    "array",
    "array_equal",
    "array_equiv",
    "asanyarray",
    "asarray",
    "ascontiguousarray",
    "asfortranarray",
    "astype",
    "base_repr",
    "binary_repr",
    "bitwise_not",
    "broadcast",
    "can_cast",
    "concatenate",
    "convolve",
    "copyto",
    "correlate",
    "count_nonzero",
    "cross",
    "dot",
    "dtype",
    "empty",
    "empty_like",
    "flatiter",
    "flatnonzero",
    "from_dlpack",
    "frombuffer",
    "fromfile",
    "fromfunction",
    "fromiter",
    "fromstring",
    "full",
    "full_like",
    "identity",
    "indices",
    "inf",
    "inner",
    "isclose",
    "isfortran",
    "isscalar",
    "lexsort",
    "little_endian",
    "matmul",
    "may_share_memory",
    "min_scalar_type",
    "moveaxis",
    "nan",
    "ndarray",
    "nditer",
    "nested_iters",
    "newaxis",
    "ones",
    "ones_like",
    "outer",
    "promote_types",
    "putmask",
    "result_type",
    "roll",
    "rollaxis",
    "shares_memory",
    "tensordot",
    "ufunc",
    "vdot",
    "vecdot",
    "where",
    "zeros",
    "zeros_like",
]

_T = TypeVar("_T")
_SCT = TypeVar("_SCT", bound=generic)
_DType = TypeVar("_DType", bound=np.dtype[Any])
_ArrayType = TypeVar("_ArrayType", bound=np.ndarray[Any, Any])
_SizeType = TypeVar("_SizeType", bound=int)
_ShapeType = TypeVar("_ShapeType", bound=tuple[int, ...])

_CorrelateMode: TypeAlias = L["valid", "same", "full"]

@overload
def zeros_like(
    a: _ArrayType,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: L[True] = ...,
    shape: None = ...,
    *,
    device: None | L["cpu"] = ...,
) -> _ArrayType: ...
@overload
def zeros_like(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[_SCT]: ...
@overload
def zeros_like(
    a: object,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[Any]: ...
@overload
def zeros_like(
    a: Any,
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[_SCT]: ...
@overload
def zeros_like(
    a: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[Any]: ...

ones: Final[_ConstructorEmpty]

@overload
def ones_like(
    a: _ArrayType,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: L[True] = ...,
    shape: None = ...,
    *,
    device: None | L["cpu"] = ...,
) -> _ArrayType: ...
@overload
def ones_like(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[_SCT]: ...
@overload
def ones_like(
    a: object,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[Any]: ...
@overload
def ones_like(
    a: Any,
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[_SCT]: ...
@overload
def ones_like(
    a: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[Any]: ...

# TODO: Add overloads for bool, int, float, complex, str, bytes, and memoryview
# 1-D shape
@overload
def full(
    shape: _SizeType,
    fill_value: _SCT,
    dtype: None = ...,
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> _Array[tuple[_SizeType], _SCT]: ...
@overload
def full(
    shape: _SizeType,
    fill_value: Any,
    dtype: _DType | _SupportsDType[_DType],
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> np.ndarray[tuple[_SizeType], _DType]: ...
@overload
def full(
    shape: _SizeType,
    fill_value: Any,
    dtype: type[_SCT],
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> _Array[tuple[_SizeType], _SCT]: ...
@overload
def full(
    shape: _SizeType,
    fill_value: Any,
    dtype: None | DTypeLike = ...,
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> _Array[tuple[_SizeType], Any]: ...

# known shape
@overload
def full(
    shape: _ShapeType,
    fill_value: _SCT,
    dtype: None = ...,
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> _Array[_ShapeType, _SCT]: ...
@overload
def full(
    shape: _ShapeType,
    fill_value: Any,
    dtype: _DType | _SupportsDType[_DType],
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> np.ndarray[_ShapeType, _DType]: ...
@overload
def full(
    shape: _ShapeType,
    fill_value: Any,
    dtype: type[_SCT],
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> _Array[_ShapeType, _SCT]: ...
@overload
def full(
    shape: _ShapeType,
    fill_value: Any,
    dtype: None | DTypeLike = ...,
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> _Array[_ShapeType, Any]: ...

# unknown shape
@overload
def full(
    shape: _ShapeLike,
    fill_value: _SCT,
    dtype: None = ...,
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> NDArray[_SCT]: ...
@overload
def full(
    shape: _ShapeLike,
    fill_value: Any,
    dtype: _DType | _SupportsDType[_DType],
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> np.ndarray[Any, _DType]: ...
@overload
def full(
    shape: _ShapeLike,
    fill_value: Any,
    dtype: type[_SCT],
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> NDArray[_SCT]: ...
@overload
def full(
    shape: _ShapeLike,
    fill_value: Any,
    dtype: None | DTypeLike = ...,
    order: _OrderCF = ...,
    **kwargs: Unpack[_KwargsEmpty],
) -> NDArray[Any]: ...
@overload
def full_like(
    a: _ArrayType,
    fill_value: Any,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: L[True] = ...,
    shape: None = ...,
    *,
    device: None | L["cpu"] = ...,
) -> _ArrayType: ...
@overload
def full_like(
    a: _ArrayLike[_SCT],
    fill_value: Any,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[_SCT]: ...
@overload
def full_like(
    a: object,
    fill_value: Any,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[Any]: ...
@overload
def full_like(
    a: Any,
    fill_value: Any,
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[_SCT]: ...
@overload
def full_like(
    a: Any,
    fill_value: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: None | _ShapeLike = ...,
    *,
    device: None | L["cpu"] = ...,
) -> NDArray[Any]: ...
@overload
def count_nonzero(
    a: ArrayLike,
    axis: None = ...,
    *,
    keepdims: L[False] = ...,
) -> int: ...
@overload
def count_nonzero(
    a: ArrayLike,
    axis: _ShapeLike = ...,
    *,
    keepdims: bool = ...,
) -> Any: ...  # TODO: np.intp or ndarray[np.intp]
def isfortran(a: NDArray[Any] | generic) -> bool: ...
def argwhere(a: ArrayLike) -> NDArray[intp]: ...
def flatnonzero(a: ArrayLike) -> NDArray[intp]: ...
@overload
def correlate(
    a: _ArrayLikeUnknown,
    v: _ArrayLikeUnknown,
    mode: _CorrelateMode = ...,
) -> NDArray[Any]: ...
@overload
def correlate(
    a: _ArrayLikeBool_co,
    v: _ArrayLikeBool_co,
    mode: _CorrelateMode = ...,
) -> NDArray[np.bool]: ...
@overload
def correlate(
    a: _ArrayLikeUInt_co,
    v: _ArrayLikeUInt_co,
    mode: _CorrelateMode = ...,
) -> NDArray[unsignedinteger[Any]]: ...
@overload
def correlate(
    a: _ArrayLikeInt_co,
    v: _ArrayLikeInt_co,
    mode: _CorrelateMode = ...,
) -> NDArray[signedinteger[Any]]: ...
@overload
def correlate(
    a: _ArrayLikeFloat_co,
    v: _ArrayLikeFloat_co,
    mode: _CorrelateMode = ...,
) -> NDArray[floating[Any]]: ...
@overload
def correlate(
    a: _ArrayLikeComplex_co,
    v: _ArrayLikeComplex_co,
    mode: _CorrelateMode = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
@overload
def correlate(
    a: _ArrayLikeTD64_co,
    v: _ArrayLikeTD64_co,
    mode: _CorrelateMode = ...,
) -> NDArray[timedelta64]: ...
@overload
def correlate(
    a: _ArrayLikeObject_co,
    v: _ArrayLikeObject_co,
    mode: _CorrelateMode = ...,
) -> NDArray[object_]: ...
@overload
def convolve(
    a: _ArrayLikeUnknown,
    v: _ArrayLikeUnknown,
    mode: _CorrelateMode = ...,
) -> NDArray[Any]: ...
@overload
def convolve(
    a: _ArrayLikeBool_co,
    v: _ArrayLikeBool_co,
    mode: _CorrelateMode = ...,
) -> NDArray[np.bool]: ...
@overload
def convolve(
    a: _ArrayLikeUInt_co,
    v: _ArrayLikeUInt_co,
    mode: _CorrelateMode = ...,
) -> NDArray[unsignedinteger[Any]]: ...
@overload
def convolve(
    a: _ArrayLikeInt_co,
    v: _ArrayLikeInt_co,
    mode: _CorrelateMode = ...,
) -> NDArray[signedinteger[Any]]: ...
@overload
def convolve(
    a: _ArrayLikeFloat_co,
    v: _ArrayLikeFloat_co,
    mode: _CorrelateMode = ...,
) -> NDArray[floating[Any]]: ...
@overload
def convolve(
    a: _ArrayLikeComplex_co,
    v: _ArrayLikeComplex_co,
    mode: _CorrelateMode = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
@overload
def convolve(
    a: _ArrayLikeTD64_co,
    v: _ArrayLikeTD64_co,
    mode: _CorrelateMode = ...,
) -> NDArray[timedelta64]: ...
@overload
def convolve(
    a: _ArrayLikeObject_co,
    v: _ArrayLikeObject_co,
    mode: _CorrelateMode = ...,
) -> NDArray[object_]: ...
@overload
def outer(
    a: _ArrayLikeUnknown,
    b: _ArrayLikeUnknown,
    out: None = ...,
) -> NDArray[Any]: ...
@overload
def outer(
    a: _ArrayLikeBool_co,
    b: _ArrayLikeBool_co,
    out: None = ...,
) -> NDArray[np.bool]: ...
@overload
def outer(
    a: _ArrayLikeUInt_co,
    b: _ArrayLikeUInt_co,
    out: None = ...,
) -> NDArray[unsignedinteger[Any]]: ...
@overload
def outer(
    a: _ArrayLikeInt_co,
    b: _ArrayLikeInt_co,
    out: None = ...,
) -> NDArray[signedinteger[Any]]: ...
@overload
def outer(
    a: _ArrayLikeFloat_co,
    b: _ArrayLikeFloat_co,
    out: None = ...,
) -> NDArray[floating[Any]]: ...
@overload
def outer(
    a: _ArrayLikeComplex_co,
    b: _ArrayLikeComplex_co,
    out: None = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
@overload
def outer(
    a: _ArrayLikeTD64_co,
    b: _ArrayLikeTD64_co,
    out: None = ...,
) -> NDArray[timedelta64]: ...
@overload
def outer(
    a: _ArrayLikeObject_co,
    b: _ArrayLikeObject_co,
    out: None = ...,
) -> NDArray[object_]: ...
@overload
def outer(
    a: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    b: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    out: _ArrayType,
) -> _ArrayType: ...
@overload
def tensordot(
    a: _ArrayLikeUnknown,
    b: _ArrayLikeUnknown,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[Any]: ...
@overload
def tensordot(
    a: _ArrayLikeBool_co,
    b: _ArrayLikeBool_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.bool]: ...
@overload
def tensordot(
    a: _ArrayLikeUInt_co,
    b: _ArrayLikeUInt_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[unsignedinteger[Any]]: ...
@overload
def tensordot(
    a: _ArrayLikeInt_co,
    b: _ArrayLikeInt_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[signedinteger[Any]]: ...
@overload
def tensordot(
    a: _ArrayLikeFloat_co,
    b: _ArrayLikeFloat_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[floating[Any]]: ...
@overload
def tensordot(
    a: _ArrayLikeComplex_co,
    b: _ArrayLikeComplex_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
@overload
def tensordot(
    a: _ArrayLikeTD64_co,
    b: _ArrayLikeTD64_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[timedelta64]: ...
@overload
def tensordot(
    a: _ArrayLikeObject_co,
    b: _ArrayLikeObject_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[object_]: ...
@overload
def roll(
    a: _ArrayLike[_SCT],
    shift: _ShapeLike,
    axis: None | _ShapeLike = ...,
) -> NDArray[_SCT]: ...
@overload
def roll(
    a: ArrayLike,
    shift: _ShapeLike,
    axis: None | _ShapeLike = ...,
) -> NDArray[Any]: ...
def rollaxis(
    a: NDArray[_SCT],
    axis: int,
    start: int = ...,
) -> NDArray[_SCT]: ...
def moveaxis(
    a: NDArray[_SCT],
    source: _ShapeLike,
    destination: _ShapeLike,
) -> NDArray[_SCT]: ...
@overload
def cross(
    x1: _ArrayLikeUnknown,
    x2: _ArrayLikeUnknown,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: None | int = ...,
) -> NDArray[Any]: ...
@overload
def cross(
    x1: _ArrayLikeBool_co,
    x2: _ArrayLikeBool_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: None | int = ...,
) -> NoReturn: ...
@overload
def cross(
    x1: _ArrayLikeUInt_co,
    x2: _ArrayLikeUInt_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: None | int = ...,
) -> NDArray[unsignedinteger[Any]]: ...
@overload
def cross(
    x1: _ArrayLikeInt_co,
    x2: _ArrayLikeInt_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: None | int = ...,
) -> NDArray[signedinteger[Any]]: ...
@overload
def cross(
    x1: _ArrayLikeFloat_co,
    x2: _ArrayLikeFloat_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: None | int = ...,
) -> NDArray[floating[Any]]: ...
@overload
def cross(
    x1: _ArrayLikeComplex_co,
    x2: _ArrayLikeComplex_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: None | int = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
@overload
def cross(
    x1: _ArrayLikeObject_co,
    x2: _ArrayLikeObject_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: None | int = ...,
) -> NDArray[object_]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: type[int] = ...,
    sparse: L[False] = ...,
) -> NDArray[int_]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: type[int] = ...,
    sparse: L[True] = ...,
) -> tuple[NDArray[int_], ...]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: _DTypeLike[_SCT],
    sparse: L[False] = ...,
) -> NDArray[_SCT]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: _DTypeLike[_SCT],
    sparse: L[True],
) -> tuple[NDArray[_SCT], ...]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: DTypeLike,
    sparse: L[False] = ...,
) -> NDArray[Any]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: DTypeLike,
    sparse: L[True],
) -> tuple[NDArray[Any], ...]: ...
def fromfunction(
    function: Callable[..., _T],
    shape: Sequence[int],
    *,
    dtype: DTypeLike = ...,
    like: _SupportsArrayFunc = ...,
    **kwargs: Any,
) -> _T: ...
def isscalar(element: object) -> TypeGuard[generic | bool | int | float | complex | str | bytes | memoryview]: ...
def binary_repr(num: SupportsIndex, width: None | int = ...) -> str: ...
def base_repr(
    number: SupportsAbs[float],
    base: float = ...,
    padding: SupportsIndex = ...,
) -> str: ...
@overload
def identity(
    n: int,
    dtype: None = ...,
    *,
    like: _SupportsArrayFunc = ...,
) -> NDArray[float64]: ...
@overload
def identity(
    n: int,
    dtype: _DTypeLike[_SCT],
    *,
    like: _SupportsArrayFunc = ...,
) -> NDArray[_SCT]: ...
@overload
def identity(
    n: int,
    dtype: DTypeLike,
    *,
    like: _SupportsArrayFunc = ...,
) -> NDArray[Any]: ...
def allclose(
    a: ArrayLike,
    b: ArrayLike,
    rtol: ArrayLike = ...,
    atol: ArrayLike = ...,
    equal_nan: bool = ...,
) -> bool: ...
@overload
def isclose(
    a: _ScalarLike_co,
    b: _ScalarLike_co,
    rtol: ArrayLike = ...,
    atol: ArrayLike = ...,
    equal_nan: bool = ...,
) -> np.bool: ...
@overload
def isclose(
    a: ArrayLike,
    b: ArrayLike,
    rtol: ArrayLike = ...,
    atol: ArrayLike = ...,
    equal_nan: bool = ...,
) -> NDArray[np.bool]: ...
def array_equal(a1: ArrayLike, a2: ArrayLike, equal_nan: bool = ...) -> bool: ...
def array_equiv(a1: ArrayLike, a2: ArrayLike) -> bool: ...
@overload
def astype(
    x: ndarray[_ShapeType, dtype[Any]],
    dtype: _DTypeLike[_SCT],
    copy: bool = ...,
    device: None | L["cpu"] = ...,
) -> ndarray[_ShapeType, dtype[_SCT]]: ...
@overload
def astype(
    x: ndarray[_ShapeType, dtype[Any]],
    dtype: DTypeLike,
    copy: bool = ...,
    device: None | L["cpu"] = ...,
) -> ndarray[_ShapeType, dtype[Any]]: ...
