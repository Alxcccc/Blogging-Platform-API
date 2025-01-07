from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    category: str
    tags:  list
    createdAt: Optional[str] = datetime.now()
    updateAt: Optional[str] = datetime.now()
    