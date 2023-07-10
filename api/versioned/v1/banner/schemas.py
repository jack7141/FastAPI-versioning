from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Banner(BaseModel):
    id: str
    display_start: datetime
    display_end: datetime
    banner_name: str
    banner_description: Optional[str]
    background_color: str
    text_color: str
    redirection_path: str
    created_at: datetime
    updated_at: datetime

