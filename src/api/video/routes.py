from fastapi import APIRouter, Depends

from .service import VideoService

router = APIRouter(prefix="/video", tags=["Video"])


@router.post("/")
async def create_video(service: VideoService = Depends()):
    service.generate_video()
    return "OK"
