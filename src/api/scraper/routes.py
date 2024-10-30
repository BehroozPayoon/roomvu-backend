from fastapi import APIRouter, Depends

from .service import ScraperService

router = APIRouter(prefix="/scrapper", tags=["Scraper"])


@router.get("/")
async def scrape_page(service: ScraperService = Depends()):
    response = await service.scrape_science_news()
    return response
