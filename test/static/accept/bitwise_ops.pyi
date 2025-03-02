from typing import Literal as L, TypeAlias
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

FalseType: TypeAlias = L[False]
TrueType: TypeAlias = L[True]

i4: np.int32
u4: np.uint32
i8: np.int64
u8: np.uint64

b: bool
i: int
b_: np.bool[bool]

b0: FalseType
b1: TrueType
b0_: np.bool[FalseType]
b1_: np.bool[TrueType]

AR: npt.NDArray[np.int32]

###

assert_type(i8 << i8, np.int64)
assert_type(i8 >> i8, np.int64)
assert_type(i8 | i8, np.int64)
assert_type(i8 ^ i8, np.int64)
assert_type(i8 & i8, np.int64)

assert_type(i8 << AR, npt.NDArray[np.signedinteger])
assert_type(i8 >> AR, npt.NDArray[np.signedinteger])
assert_type(i8 | AR, npt.NDArray[np.signedinteger])
assert_type(i8 ^ AR, npt.NDArray[np.signedinteger])
assert_type(i8 & AR, npt.NDArray[np.signedinteger])

assert_type(i4 << i4, np.int32)
assert_type(i4 >> i4, np.int32)
assert_type(i4 | i4, np.int32)
assert_type(i4 ^ i4, np.int32)
assert_type(i4 & i4, np.int32)

assert_type(i8 << i4, np.int64)
assert_type(i8 >> i4, np.int64)
assert_type(i8 | i4, np.int64)
assert_type(i8 ^ i4, np.int64)
assert_type(i8 & i4, np.int64)

assert_type(i8 << b_, np.int64)
assert_type(i8 >> b_, np.int64)
assert_type(i8 | b_, np.int64)
assert_type(i8 ^ b_, np.int64)
assert_type(i8 & b_, np.int64)

assert_type(i8 << b, np.int64)
assert_type(i8 >> b, np.int64)
assert_type(i8 | b, np.int64)
assert_type(i8 ^ b, np.int64)
assert_type(i8 & b, np.int64)

assert_type(u8 << u8, np.uint64)
assert_type(u8 >> u8, np.uint64)
assert_type(u8 | u8, np.uint64)
assert_type(u8 ^ u8, np.uint64)
assert_type(u8 & u8, np.uint64)

assert_type(u8 << AR, npt.NDArray[np.signedinteger])
assert_type(u8 >> AR, npt.NDArray[np.signedinteger])
assert_type(u8 | AR, npt.NDArray[np.signedinteger])
assert_type(u8 ^ AR, npt.NDArray[np.signedinteger])
assert_type(u8 & AR, npt.NDArray[np.signedinteger])

assert_type(u4 << u4, np.uint32)
assert_type(u4 >> u4, np.uint32)
assert_type(u4 | u4, np.uint32)
assert_type(u4 ^ u4, np.uint32)
assert_type(u4 & u4, np.uint32)

assert_type(u4 << i4, np.int64)
assert_type(u4 >> i4, np.int64)
assert_type(u4 | i4, np.int64)
assert_type(u4 ^ i4, np.int64)
assert_type(u4 & i4, np.int64)

assert_type(u4 << i, np.uint32)
assert_type(u4 >> i, np.uint32)
assert_type(u4 | i, np.uint32)
assert_type(u4 ^ i, np.uint32)
assert_type(u4 & i, np.uint32)

assert_type(u8 << b_, np.uint64)
assert_type(u8 >> b_, np.uint64)
assert_type(u8 | b_, np.uint64)
assert_type(u8 ^ b_, np.uint64)
assert_type(u8 & b_, np.uint64)

assert_type(u8 << b, np.uint64)
assert_type(u8 >> b, np.uint64)
assert_type(u8 | b, np.uint64)
assert_type(u8 ^ b, np.uint64)
assert_type(u8 & b, np.uint64)

assert_type(b_ << b_, np.int8)
assert_type(b_ >> b_, np.int8)
assert_type(b_ | b_, np.bool)
assert_type(b_ ^ b_, np.bool)
assert_type(b_ & b_, np.bool)

assert_type(b_ << AR, npt.NDArray[np.signedinteger])
assert_type(b_ >> AR, npt.NDArray[np.signedinteger])
assert_type(b_ | AR, npt.NDArray[np.signedinteger])
assert_type(b_ ^ AR, npt.NDArray[np.signedinteger])
assert_type(b_ & AR, npt.NDArray[np.signedinteger])

assert_type(b_ << b, np.int8)
assert_type(b_ >> b, np.int8)
assert_type(b_ | b, np.bool)
assert_type(b_ ^ b, np.bool)
assert_type(b_ & b, np.bool)

assert_type(b_ << i, np.int8 | np.int_)
assert_type(b_ >> i, np.int8 | np.int_)
assert_type(b_ | i, np.bool | np.int_)
assert_type(b_ ^ i, np.bool | np.int_)
assert_type(b_ & i, np.bool | np.int_)

assert_type(~i8, np.int64)
assert_type(~i4, np.int32)
assert_type(~u8, np.uint64)
assert_type(~u4, np.uint32)
assert_type(~b_, np.bool)
assert_type(~b0_, np.bool[TrueType])
assert_type(~b1_, np.bool[FalseType])
assert_type(~AR, npt.NDArray[np.int32])

assert_type(b_ | b0_, np.bool)
assert_type(b0_ | b_, np.bool)
assert_type(b_ | b1_, np.bool[TrueType])
assert_type(b1_ | b_, np.bool[TrueType])

assert_type(b_ ^ b0_, np.bool)
assert_type(b0_ ^ b_, np.bool)
assert_type(b_ ^ b1_, np.bool)
assert_type(b1_ ^ b_, np.bool)

assert_type(b_ & b0_, np.bool[FalseType])
assert_type(b0_ & b_, np.bool[FalseType])
assert_type(b_ & b1_, np.bool)
assert_type(b1_ & b_, np.bool)

assert_type(b0_ | b0_, np.bool[FalseType])
assert_type(b0_ | b1_, np.bool[TrueType])
assert_type(b1_ | b0_, np.bool[TrueType])
assert_type(b1_ | b1_, np.bool[TrueType])

assert_type(b0_ ^ b0_, np.bool[FalseType])
assert_type(b0_ ^ b1_, np.bool[TrueType])
assert_type(b1_ ^ b0_, np.bool[TrueType])
assert_type(b1_ ^ b1_, np.bool[FalseType])

assert_type(b0_ & b0_, np.bool[FalseType])
assert_type(b0_ & b1_, np.bool[FalseType])
assert_type(b1_ & b0_, np.bool[FalseType])
assert_type(b1_ & b1_, np.bool[TrueType])
