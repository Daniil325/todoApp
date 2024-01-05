from datetime import datetime

from beanie import Document


class Priority(Document):
    name: str


class Status(Document):
    name: str


class Task(Document):
    name: str
    created_date: datetime
    deadline: datetime
    description: str
    status: Status
    priority: Priority
