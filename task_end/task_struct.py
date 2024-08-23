from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    label: str
    description: Optional[str]
    status: bool


