import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import beanie
import motor
import motor.motor_asyncio

from backend.models.models import Priority, Status, Task
from backend.api import api_router

logger = logging.getLogger(__name__)


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

    await beanie.init_beanie(database=client.todoapp, document_models=[Task, Priority, Status])


app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def connect():
    await init_db()

