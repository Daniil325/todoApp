from fastapi import APIRouter

from backend.models import Status
from backend.schema.schemas import StatusRead, StatusCreate

router = APIRouter()


@router.get('/', response_model=list[StatusRead])
async def get_statuses():
    return await Status.find_all().to_list()


@router.post('/', response_model=StatusRead)
async def post_status(status_create: StatusCreate):
    status = Status(**status_create.model_dump(mode='json'))
    await status.insert()
    return status
