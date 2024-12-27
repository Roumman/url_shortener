from fastapi import APIRouter
from app.schemas.url_schema import URLRequest
from app.crud.url_crud import create_short_url

router = APIRouter()

@router.post("/shorten")
async def shorten_url(request: URLRequest):
    """
    Эндпоинт для создания короткой ссылки.
    Принимает полный URL, возвращает короткую ссылку.
    """
    return create_short_url(request.url)
