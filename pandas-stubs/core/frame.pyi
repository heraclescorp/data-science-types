from pathlib import Path
from typing import Any, Tuple, List, Union, Callable, Dict, Optional, Type, TypeVar, overload
from typing_extensions import Literal
import numpy as _np

from .series import Series
from .index import Index
from .indexing import _iLocIndexer, _LocIndexer

_AxisType = Literal["columns", "index"]

_ListLike = Union[_np.ndarray, Series, List, Dict[str, _np.ndarray]]

_DType = TypeVar('_DType', bound=_np.dtype)

class DataFrame:
    def __init__(
        self,
        data: Optional[Union[_ListLike, DataFrame]] = ...,
        columns: Optional[Union[List[str], Index]] = ...,
        index: Optional[Union[_np.ndarray, Index]] = ...,
    ): ...
    #
    # magic methods
    @overload
    def __getitem__(self, idx: str) -> Series: ...
    @overload
    def __getitem__(self, idx: Union[List[str], Index]) -> DataFrame: ...
    def __len__(self) -> int: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    #
    # properties
    @property
    def columns(self) -> Index[str]: ...
    @columns.setter  # setter needs to be right next to getter; otherwise mypy complains
    def columns(self, cols: Union[List[str], Index[str]]) -> None: ...
    @property
    def iloc(self) -> _iLocIndexer: ...
    @property
    def index(self) -> Index[int]: ...
    @index.setter
    def index(self, idx: Index) -> None: ...
    @property
    def loc(self) -> _LocIndexer: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def size(self) -> int: ...
    # this function is deprecated:
    @property
    def values(self) -> _np.ndarray: ...
    #
    # methods
    def append(
        self, s: Dict[str, Any], ignore_index: bool = ..., sort: bool = ...
    ) -> DataFrame: ...
    def apply(self, f: Callable) -> DataFrame: ...
    def copy(self) -> DataFrame: ...
    def count(self) -> Series: ...
    def drop(self, index: Union[List[str], Index], axis: _AxisType = ...) -> DataFrame: ...
    def head(self, n: int) -> DataFrame: ...
    def mode(self, axis: _AxisType = ...) -> DataFrame: ...
    def nunique(self) -> Series: ...
    def query(self, expr: str) -> DataFrame: ...
    def rename(self, mapper: Callable, axis: _AxisType = ...) -> DataFrame: ...
    def replace(self, a: float, b: float) -> DataFrame: ...
    def reset_index(self, drop: bool) -> DataFrame: ...
    @overload
    def sample(self, frac: float, random_state: int = ..., replace: bool = ...) -> DataFrame: ...
    @overload
    def sample(self, n: int, random_state: int = ..., replace: bool = ...) -> DataFrame: ...
    def set_index(self, index: List[str]) -> DataFrame: ...
    @overload
    def sort_values(
        self, by: List[str], inplace: Literal[True], axis: _AxisType = ..., ascending: bool = ...
    ) -> None: ...
    @overload
    def sort_values(
        self,
        by: List[str],
        inplace: Optional[Literal[False]] = ...,
        axis: _AxisType = ...,
        ascending: bool = ...,
    ) -> DataFrame: ...
    def to_csv(self, filename: Path, index: bool = ...) -> None: ...
    def to_feather(self, filename: Path) -> None: ...
    @overload
    def to_numpy(self) -> _np.ndarray: ...
    @overload
    def to_numpy(self, dtype: Type[_DType]) -> _np.ndarray[_DType]: ...
