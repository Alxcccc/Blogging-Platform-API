from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UpdatePost(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None
    updateAt: Optional[str] = datetime.now()
