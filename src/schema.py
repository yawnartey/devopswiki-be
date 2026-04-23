from pydantic import BaseModel
from typing import List, Optional

class ResourceOut(BaseModel):
    id:          int
    title:       str
    url:         str
    description: Optional[str]
    source:      Optional[str]
    type:        Optional[str]
    tags:        Optional[List[str]]

    class Config:
        from_attributes = True

class ResourceCreate(BaseModel):
    title:       str
    url:         str
    description: Optional[str]
    source:      Optional[str]
    type:        Optional[str]
    tags:        Optional[List[str]]