from pydantic import BaseModel, Field
from typing import Optional

class TodoItem(BaseModel):
    id: str = Field(None, alias="_id")
    title: str
    description: str
    completed: bool = False
