from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from backend.models import Status, Priority


class StatusBase(BaseModel):
    name: str


class StatusCreate(StatusBase):
    pass


class StatusRead(StatusBase):
    id: PydanticObjectId = Field()


class TaskBase(BaseModel):
    name: str
    created_date: datetime
    deadline: datetime
    description: str
    status: Status
    priority: Priority


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: PydanticObjectId = Field()


class PriorityBase(BaseModel):
    name: str


class PriorityCreate(PriorityBase):
    pass


class PriorityRead(PriorityBase):
    id: PydanticObjectId = Field()
