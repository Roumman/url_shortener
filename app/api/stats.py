from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.pagination import get_paginated_urls
from app.schemas.pagination import PaginatedURLs
from app.database.db import get_db

router = APIRouter()

@router.get("/stats")
async def get_all_urls(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    """
    Эндпоинт для получения статистики о сокращенных ссылках с пагинацией.
    Возвращает список коротких URL и полных URL на каждой странице.
    """
    return get_paginated_urls(page, per_page, db)
