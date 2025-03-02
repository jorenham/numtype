from typing import Final, Literal as L
from typing_extensions import TypeVar

import numpy as np
from _numtype import Array, Array_1d

from ._polybase import ABCPolyBase
from ._polytypes import (
    _FuncBinOp,
    _FuncCompanion,
    _FuncDer,
    _FuncFit,
    _FuncFromRoots,
    _FuncGauss,
    _FuncInteg,
    _FuncLine,
    _FuncPoly2Ortho,
    _FuncPow,
    _FuncRoots,
    _FuncUnOp,
    _FuncVal,
    _FuncVal2D,
    _FuncVal3D,
    _FuncValFromRoots,
    _FuncVander,
    _FuncVander2D,
    _FuncVander3D,
    _FuncWeight,
)
from .polyutils import trimcoef as hermetrim

__all__ = [
    "HermiteE",
    "herme2poly",
    "hermeadd",
    "hermecompanion",
    "hermeder",
    "hermediv",
    "hermedomain",
    "hermefit",
    "hermefromroots",
    "hermegauss",
    "hermegrid2d",
    "hermegrid3d",
    "hermeint",
    "hermeline",
    "hermemul",
    "hermemulx",
    "hermeone",
    "hermepow",
    "hermeroots",
    "hermesub",
    "hermetrim",
    "hermeval",
    "hermeval2d",
    "hermeval3d",
    "hermevander",
    "hermevander2d",
    "hermevander3d",
    "hermeweight",
    "hermex",
    "hermezero",
    "poly2herme",
]

_ND = TypeVar("_ND", bound=tuple[int, ...])

###

hermedomain: Final[Array_1d[np.float64]] = ...
hermezero: Final[Array_1d[np.int_]] = ...
hermeone: Final[Array_1d[np.int_]] = ...
hermex: Final[Array_1d[np.int_]] = ...

poly2herme: Final[_FuncPoly2Ortho[L["poly2herme"]]] = ...
herme2poly: Final[_FuncUnOp[L["herme2poly"]]] = ...
hermeline: Final[_FuncLine[L["hermeline"]]] = ...
hermefromroots: Final[_FuncFromRoots[L["hermefromroots"]]] = ...
hermeadd: Final[_FuncBinOp[L["hermeadd"]]] = ...
hermesub: Final[_FuncBinOp[L["hermesub"]]] = ...
hermemulx: Final[_FuncUnOp[L["hermemulx"]]] = ...
hermemul: Final[_FuncBinOp[L["hermemul"]]] = ...
hermediv: Final[_FuncBinOp[L["hermediv"]]] = ...
hermepow: Final[_FuncPow[L["hermepow"]]] = ...
hermeder: Final[_FuncDer[L["hermeder"]]] = ...
hermeint: Final[_FuncInteg[L["hermeint"]]] = ...
hermeval: Final[_FuncVal[L["hermeval"]]] = ...
hermeval2d: Final[_FuncVal2D[L["hermeval2d"]]] = ...
hermeval3d: Final[_FuncVal3D[L["hermeval3d"]]] = ...
hermevalfromroots: Final[_FuncValFromRoots[L["hermevalfromroots"]]] = ...
hermegrid2d: Final[_FuncVal2D[L["hermegrid2d"]]] = ...
hermegrid3d: Final[_FuncVal3D[L["hermegrid3d"]]] = ...
hermevander: Final[_FuncVander[L["hermevander"]]] = ...
hermevander2d: Final[_FuncVander2D[L["hermevander2d"]]] = ...
hermevander3d: Final[_FuncVander3D[L["hermevander3d"]]] = ...
hermefit: Final[_FuncFit[L["hermefit"]]] = ...
hermecompanion: Final[_FuncCompanion[L["hermecompanion"]]] = ...
hermeroots: Final[_FuncRoots[L["hermeroots"]]] = ...
hermegauss: Final[_FuncGauss[L["hermegauss"]]] = ...
hermeweight: Final[_FuncWeight[L["hermeweight"]]] = ...

def _normed_hermite_e_n(x: Array[np.float64, _ND], n: int | np.intp) -> Array[np.float64, _ND]: ...

class HermiteE(ABCPolyBase[L["He"]]): ...
