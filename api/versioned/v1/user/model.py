from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ImgSrc(BaseModel):
    sm: Optional[str]
    md: Optional[str]
    lg: Optional[str]
    xl: Optional[str]


class Banner(BaseModel):
    type: Optional[str]
    url: Optional[str]
    title: Optional[str]
    subtitle: Optional[str]
    img_src: Optional[ImgSrc]
    text_color: Optional[str]
    start_at: Optional[datetime]
    expires_at: Optional[datetime]
    order: Optional[int]
    is_published: Optional[bool]

    @classmethod
    def from_entity(cls, entity):
        return cls(**entity.to_dict())
