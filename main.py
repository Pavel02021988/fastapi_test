from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables, delete_tables
from views import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("БД создана!!!")
    yield
    await delete_tables()
    print("БД удалена!!!")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)

