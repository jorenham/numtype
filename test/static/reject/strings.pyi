import numpy as np
import numpy.typing as npt

AR_U: npt.NDArray[np.str_]
AR_S: npt.NDArray[np.bytes_]

np.strings.equal(AR_U, AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.not_equal(AR_U, AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.greater_equal(AR_U, AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.greater(AR_U, AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.less_equal(AR_U, AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.less(AR_U, AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.encode(AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.strings.decode(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.strings.join(AR_U, b"_")  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]

np.strings.ljust(AR_U, 5, fillchar=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.ljust(AR_S, 5, fillchar="a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rjust(AR_U, 5, fillchar=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rjust(AR_S, 5, fillchar="a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.lstrip(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.lstrip(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.strip(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.strip(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rstrip(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rstrip(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.partition(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.partition(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rpartition(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rpartition(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.count(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.count(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.endswith(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.endswith(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.startswith(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.startswith(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.find(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.find(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rfind(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rfind(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.index(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.index(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rindex(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.rindex(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.strings.isdecimal(AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.strings.isnumeric(AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.strings.replace(AR_U, b"_", b"-", 10)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.strings.replace(AR_S, "_", "-", 1)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
