from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UpdatePost(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags:  Optional[list[str]] = None
    updateAt: Optional[str] = datetime.now()