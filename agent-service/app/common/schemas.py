from typing import TypeVar, Generic, List

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


T = TypeVar("T")

class PageResults(BaseModel, Generic[T]):
    items: List[T]
    page: int
    page_size: int
    total: int