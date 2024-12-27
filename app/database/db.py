from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.url_model import Base

# Путь к базе данных с именем url_shortener.db
DATABASE_URL = "sqlite:///./url_shortener.db"

# Создание движка для подключения к базе данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Сессия для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Функция для инициализации базы данных.
    Создает таблицы, если они еще не существуют.
    """
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    Получение сессии базы данных.
    Используется для выполнения запросов к базе данных.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
