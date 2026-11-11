from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging, get_logger
import uvicorn


# 日志配置
configure_logging(settings.logging.level)
logger = get_logger(__name__)


# 初始化FastAPI
app = FastAPI(
    title=settings.app.name,
    debug=settings.app.debug,
)

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
