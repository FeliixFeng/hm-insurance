from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.exceptions import ApplicationError
from app.core.logging import configure_logging, get_logger
import uvicorn

from app.modules.chat_thread.exceptions import ChatThreadNotFoundError

# 日志配置
configure_logging(settings.logging.level)
logger = get_logger(__name__)


# 初始话生命周期钩子
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("项目启动中， 正在初始化。。。")
    from app.infra.database import check_database, close_database
    try:
        await check_database()

        yield
    finally:
        await close_database()


# 初始化FastAPI
app = FastAPI(
    title=settings.app.name,
    debug=settings.app.debug,
    lifespan=lifespan,
)

@app.exception_handler(ApplicationError)
async def handle_application_error(
    request: Request,
    exc: ApplicationError, # 捕获到的异常（这里用自定义异常基类捕获，所有业务异常都会匹配到）
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code, # 异常中自带status
        content={
            "code": exc.code,        # 异常中自带code
            "message": exc.message,  # 异常中自带message
        },
    )



from app.modules.product.router import router as product_router
from app.modules.chat_thread.router import router as chat_thread_router
app.include_router(product_router)
app.include_router(chat_thread_router)

@app.get("/healthy", summary="健康检测接口")
async def healthy() -> dict[str, str]:
    logger.info("健康检测接口正常调用。")
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=False
    )
