from app.core.exceptions import ApplicationError


class ChatThreadNotFoundError(ApplicationError):
    """会话不存在或不属于当前用户"""
    status_code: int = 400
    code: str = "CHAT_THREAD_NOT_FOUND"
    message: str = "当前会话不存在或者不属于当前用户"