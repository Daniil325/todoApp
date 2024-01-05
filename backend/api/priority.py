from fastapi import APIRouter

from backend.models import Priority
from backend.schema.schemas import PriorityRead, PriorityCreate

router = APIRouter()


@router.get('/', response_model=list[PriorityRead])
async def get_priorities():
    return await Priority.find_all().to_list()


@router.post('/', response_model=PriorityRead)
async def post_priority(priority_create: PriorityCreate):
    priority = Priority(**priority_create.model_dump(mode='json'))
    await priority.insert()
    return priority
