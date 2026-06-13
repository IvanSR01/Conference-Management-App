from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import Base
from app.database import engine

from app.routers.participants import router as participant_router

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Conference Management System",
    version="1.0.0"
)

# Подключаем статику
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# Подключаем роутер участников
app.include_router(participant_router)