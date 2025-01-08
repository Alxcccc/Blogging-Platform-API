from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    category: str
    tags: list[str]
    createdAt: Optional[str] = datetime.now()
    updateAt: Optional[str] = datetime.now()
