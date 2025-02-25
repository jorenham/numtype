from collections.abc import Iterable, Sequence
from typing import Any, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import (
    Array,
    Array_1d,
    CoComplex_0d,
    CoComplex_1d,
    CoFloating_0d,
    CoFloating_1d,
    ToComplex_0d,
    ToComplex_1d,
    ToObject_0d,
    ToObject_1d,
    _ToArray1_1d,
)
from numpy._typing import _FloatLike_co

from ._polytypes import _InexactObject_nd, _ToNumeric_0d, _Tuple2

__all__ = ["as_series", "format_float", "getdomain", "mapdomain", "mapparms", "trimcoef", "trimseq"]

###

_T_seq = TypeVar("_T_seq", bound=_InexactObject_nd | Sequence[_ToNumeric_0d])

###

#
def trimseq(seq: _T_seq) -> _T_seq: ...

#
@overload
def as_series(alist: Array[np.floating | np.integer], trim: bool = True) -> list[Array_1d[np.floating]]: ...
@overload
def as_series(alist: Array[np.complexfloating], trim: bool = True) -> list[Array_1d[np.complexfloating]]: ...
@overload
def as_series(alist: Array[np.object_], trim: bool = True) -> list[Array_1d[np.object_]]: ...
@overload
def as_series(alist: Iterable[CoFloating_1d | CoFloating_0d], trim: bool = True) -> list[Array_1d[np.floating]]: ...
@overload
def as_series(alist: Iterable[ToComplex_1d | ToComplex_0d], trim: bool = True) -> list[Array_1d[np.complexfloating]]: ...
@overload
def as_series(alist: Iterable[ToObject_1d | ToObject_0d], trim: bool = True) -> list[Array_1d[np.object_]]: ...

#
@overload
def trimcoef(c: CoFloating_1d | CoFloating_0d, tol: _FloatLike_co = 0) -> Array_1d[np.floating]: ...
@overload
def trimcoef(c: ToComplex_1d | ToComplex_0d, tol: _FloatLike_co = 0) -> Array_1d[np.complexfloating]: ...
@overload
def trimcoef(c: ToObject_1d | ToObject_0d, tol: _FloatLike_co = 0) -> Array_1d[np.object_]: ...

#
@overload
def getdomain(x: CoFloating_1d | CoFloating_0d) -> Array_1d[np.float64]: ...
@overload
def getdomain(x: ToComplex_1d | ToComplex_0d) -> Array_1d[np.complex128]: ...
@overload
def getdomain(x: ToObject_1d | ToObject_0d) -> Array_1d[np.object_]: ...

#
@overload
def mapparms(old: Sequence[float], new: Sequence[float]) -> _Tuple2[float]: ...
@overload
def mapparms(old: Sequence[complex], new: Sequence[complex]) -> _Tuple2[complex]: ...
@overload
def mapparms(old: _ToArray1_1d[np.floating | np.integer], new: CoFloating_1d) -> _Tuple2[np.floating]: ...
@overload
def mapparms(old: CoFloating_1d, new: _ToArray1_1d[np.floating | np.integer]) -> _Tuple2[np.floating]: ...
@overload
def mapparms(old: _ToArray1_1d[np.complexfloating], new: CoComplex_1d) -> _Tuple2[np.complexfloating]: ...
@overload
def mapparms(old: CoComplex_1d, new: _ToArray1_1d[np.complexfloating]) -> _Tuple2[np.complexfloating]: ...
@overload
def mapparms(old: ToObject_1d | CoComplex_1d, new: ToObject_1d | CoComplex_1d) -> _Tuple2[Any]: ...

#
@overload
def mapdomain(x: CoFloating_0d, old: CoFloating_1d, new: CoFloating_1d) -> np.floating: ...
@overload
def mapdomain(x: ToComplex_0d, old: CoComplex_1d, new: CoComplex_1d) -> np.complexfloating: ...
@overload
def mapdomain(x: CoComplex_0d, old: ToComplex_1d, new: CoComplex_1d) -> np.complexfloating: ...
@overload
def mapdomain(x: CoComplex_0d, old: CoComplex_1d, new: ToComplex_1d) -> np.complexfloating: ...
@overload
def mapdomain(x: CoFloating_1d, old: CoFloating_1d, new: CoFloating_1d) -> Array_1d[np.floating]: ...
@overload
def mapdomain(x: ToComplex_1d, old: CoComplex_1d, new: CoComplex_1d) -> Array_1d[np.complexfloating]: ...
@overload
def mapdomain(x: CoComplex_1d, old: ToComplex_1d, new: CoComplex_1d) -> Array_1d[np.complexfloating]: ...
@overload
def mapdomain(x: CoComplex_1d, old: CoComplex_1d, new: ToComplex_1d) -> Array_1d[np.complexfloating]: ...
@overload
def mapdomain(x: ToObject_0d, old: CoComplex_1d | ToObject_1d, new: CoComplex_1d | ToObject_1d) -> Any: ...
@overload
def mapdomain(x: CoComplex_0d | ToObject_0d, old: ToObject_1d, new: CoComplex_1d | ToObject_1d) -> Any: ...
@overload
def mapdomain(x: CoComplex_0d | ToObject_0d, old: CoComplex_1d | ToObject_1d, new: ToObject_1d) -> Any: ...
@overload
def mapdomain(x: ToObject_1d, old: CoComplex_1d | ToObject_1d, new: CoComplex_1d | ToObject_1d) -> Array_1d[np.object_]: ...
@overload
def mapdomain(x: CoComplex_1d | ToObject_1d, old: ToObject_1d, new: CoComplex_1d | ToObject_1d) -> Array_1d[np.object_]: ...
@overload
def mapdomain(x: CoComplex_1d | ToObject_1d, old: CoComplex_1d | ToObject_1d, new: ToObject_1d) -> Array_1d[np.object_]: ...

#
def format_float(x: _FloatLike_co, parens: bool = False) -> str: ...
