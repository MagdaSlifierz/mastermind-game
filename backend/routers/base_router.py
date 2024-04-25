from fastapi import APIRouter

from routers import user_router, game_router, difficulty_router

router = APIRouter()
router.include_router(difficulty_router.router)
router.include_router(game_router.router)
router.include_router(user_router.router)
