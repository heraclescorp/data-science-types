from typing import Union, Optional

from ._core import _ShapeType, ndarray, float64, int64, _Float, _Num

def permutation(size: int) -> ndarray[int64]: ...
def seed(s: int) -> None: ...
def shuffle(x: ndarray) -> None: ...
def uniform(size: _ShapeType) -> ndarray: ...
def randn(*args: int) -> ndarray[float64]: ...

class RandomState:
    def __init__(self, seed: int = ...): ...
    def permutation(self, size: int) -> ndarray[int64]: ...
    def shuffle(self, x: ndarray) -> None: ...
    def uniform(self, size: _ShapeType) -> ndarray: ...
    def normal(
        self,
        loc: Union[float, ndarray[_Num]] = ...,
        scale: Union[float, ndarray[_Num]] = ...,
        size: Optional[_ShapeType] = ...,
    ) -> ndarray[_Num]: ...
    def multivariate_normal(
        self, mean: ndarray[_Num] = ..., cov: ndarray[_Num] = ..., size: Optional[_ShapeType] = ...
    ) -> ndarray[_Num]: ...
