from fastapi import APIRouter
from .view import create, list

router = APIRouter()

router.get("")(list)
router.post("")(create)