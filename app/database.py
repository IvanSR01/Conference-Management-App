from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.config import settings

# Формируем строку подключения к PostgreSQL
DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

# Создаем объект подключения к БД
engine = create_engine(DATABASE_URL)

# Фабрика сессий SQLAlchemy
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Базовый класс для всех моделей
Base = declarative_base()

# Генератор сессий БД
def get_db():
    """
    Создает сессию БД и закрывает её после завершения запроса.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()