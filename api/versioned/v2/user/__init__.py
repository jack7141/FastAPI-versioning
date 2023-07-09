# api/versioned/v1/__init__.py

from fastapi import APIRouter

from api.versioned.v1.user.router import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/users")
