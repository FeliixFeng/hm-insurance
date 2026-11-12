from decimal import Decimal
from pydantic import BaseModel

from app.common.schemas import BaseSchema


class ProductResponse(BaseSchema):
    """保险产品响应结果"""

    id: int
    name: str
    clause_name: str
    category: str
    insurer: str
    image_url: str
    description: str
    min_premium: Decimal | None
    max_premium: Decimal | None
    target_group: str | None
    highlights: list[str]
    status: str