from typing import Any

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from api.versioned.v1.banner.schemas import Banner
from common.database import get_db

router = APIRouter()

def list():
    return "list"

def create(banner: Banner, db: Session = Depends(get_db)) -> Any:
    db_banner = Banner(db, banner)
    if db_banner:
        return db_banner
    else:
        raise HTTPException(status_code=400, detail="Error in creating banner")

