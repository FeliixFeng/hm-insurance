from fastapi import APIRouter, Depends, Query, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.infra.database import get_session
from app.modules.product.schemas import ProductResponse
from app.modules.product.service import ProductService
from decimal import Decimal
from typing import Annotated

router = APIRouter(prefix="/api/v1/products", tags=["产品管理相关接口"])

def get_product_service(session: AsyncSession = Depends(get_session)):
    service = ProductService(session)
    yield service


@router.get("", response_model=list[ProductResponse])
async def list_products(
    category: str | None = None,
    service: ProductService = Depends(get_product_service),
) -> list[ProductResponse]:
    # 1.获取Service
    # 2.查询并返回产品列表
    return await service.list_products(category)

@router.get("/candidates", response_model=list[ProductResponse])
async def list_candidates(
    categories: list[str] = Query(min_length=1),
    premium_min: Decimal | None = None,
    limit_per_category: int = 5,
    service: ProductService = Depends(get_product_service),
) -> list[ProductResponse]:
    return await service.list_candidates(
        categories=categories,
        premium_min=premium_min,
        limit_per_category=limit_per_category,
    )