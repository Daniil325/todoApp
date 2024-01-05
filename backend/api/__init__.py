from fastapi import APIRouter
from .task import router as tasks_router
from .priority import router as priority_router
from .status import router as status_router

api_router = APIRouter()
api_router.include_router(tasks_router, tags=["task"], prefix="/task")
api_router.include_router(priority_router, tags=["priority"], prefix="/priority")
api_router.include_router(status_router, tags=["status"], prefix="/status")
