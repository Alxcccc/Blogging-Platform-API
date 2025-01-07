from pydantic import BaseModel
from typing import Optional

class UpdatePost(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags:  Optional[list] = None
    createdAt: Optional[str] = None
    updateAt: str
    