from fastapi import APIRouter
from .view import read_users

router = APIRouter()

router.get("/")(read_users)