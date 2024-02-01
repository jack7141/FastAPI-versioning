from typing import Any

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from api.versioned.v1.banner.schemas import Banner
from common.database import get_db
from common.events import event_manager
from api.versioned.v1.banner.observers import *

router = APIRouter()

def list():
    user_data = {"username": "test", "email": "email"}
    event_manager.publish("user_signup", user_data)
    return "list"

def create(
        banner: Banner, db: Session = Depends(get_db)
) -> Any:
    db_banner = Banner(db, banner)
    if db_banner:
        return db_banner
    else:
        raise HTTPException(status_code=400, detail="Error in creating banner")

