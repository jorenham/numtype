# ruff: noqa: PYI010
import numpy as np
import numpy.typing as npt

f8: np.float64
AR_f8: npt.NDArray[np.float64]
AR_M: npt.NDArray[np.datetime64]
AR_b: npt.NDArray[np.bool]

ctypes_obj = AR_f8.ctypes

###

ctypes_obj.get_data()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
ctypes_obj.get_shape()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
ctypes_obj.get_strides()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
ctypes_obj.get_as_parameter()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

# NOTE: mypy stops analysis after something returns `NoReturn`; wrapping them in functions works around this

def test_argpartition() -> None:
    f8.argpartition(0)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_diagonal() -> None:
    f8.diagonal()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_trace() -> None:
    f8.trace()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_dot() -> None:
    f8.dot(1)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_nonzero() -> None:
    f8.nonzero()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_partition() -> None:
    f8.partition(0)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_setfield() -> None:
    f8.setfield(2, np.float64)  # type: ignore[misc, arg-type]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_sort() -> None:
    f8.sort()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

AR_b.__index__()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

AR_f8[1.5]  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
AR_f8["field_a"]  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
AR_f8[["field_a", "field_b"]]  # type: ignore[index]  # pyright: ignore[reportCallIssue,reportArgumentType]
