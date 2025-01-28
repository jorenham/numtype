from typing import Final

import numpy as np

i8: Final[np.int64] = ...
i4: Final[np.int32] = ...
u8: Final[np.uint64] = ...
b_: Final[np.bool] = ...
i: Final[int] = 0

f8 = np.float64()

b_ >> f8  # E: No overload variant
i8 << f8  # E: No overload variant
i | f8  # E: Unsupported operand types
i8 ^ f8  # E: No overload variant
u8 & f8  # E: No overload variant
~f8  # E: Unsupported operand type
# TODO: Certain mixes like i4 << u8 go to float and thus should fail

# mypys' error message for `NoReturn` is unfortunately pretty bad
# TODO: Re-enable this once we add support for numerical precision for `number`s
# a = u8 | 0  # E: Need type annotation
