from fastapi import APIRouter

from backend.models import Task
from backend.schema.schemas import TaskCreate, TaskRead

router = APIRouter()


@router.get('/', response_model=list[TaskRead])
async def get_statuses():
    return await Task.find_all().to_list()


@router.post('/', response_model=TaskRead)
async def post_status(task_create: TaskCreate):
    task = Task(**task_create.model_dump(mode='json'))
    await task.insert()
    return task
