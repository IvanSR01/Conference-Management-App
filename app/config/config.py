from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()


class Settings:
    """
    Класс для хранения настроек приложения.
    Все параметры читаются из переменных окружения.
    """

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")


# Создаем единый экземпляр настроек
settings = Settings()

import os
from dotenv import load_dotenv

load_dotenv()

