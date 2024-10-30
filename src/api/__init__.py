from fastapi import APIRouter

from .video import router as video_router
from .scraper import router as scraper_router

router = APIRouter()

router.include_router(video_router)
router.include_router(scraper_router)

__all__ = ["router"]
