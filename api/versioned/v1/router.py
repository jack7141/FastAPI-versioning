from fastapi import APIRouter
from .user.router import router as user_router
from .banner.router import router as banner_router

router = APIRouter()
router.include_router(user_router, prefix="/users")
router.include_router(banner_router, prefix="/banner")