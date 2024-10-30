import json

from fastapi import Depends
from redis.asyncio import Redis
import httpx
from bs4 import BeautifulSoup

from src.core.mocks import get_redis_session


class ScraperService:

    def __init__(self, redis_session: Redis = Depends(get_redis_session)) -> None:
        self.redis_session = redis_session

    async def scrape_science_news(self):
        cached_result = await self._load_from_cache()
        if cached_result:
            return cached_result

        url = "https://www.sciencenews.org/"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            trending_stories = soup.find(
                'section', class_='trending-stories__wrapper___-7tOu')
            items = trending_stories.find_all('li', limit=10)

            result = []
            for item in items:
                category = item.find(
                    'a', class_='carousel__eyebrow___VMI-N').text.strip()
                title = item.find(
                    'h3', class_='carousel__title___1uDeB').text.strip()
                author = item.find('span', class_='author').text.strip()
                image_url = item.find('img')['src']

                result.append({
                    "news_category": category,
                    "news_title": title,
                    "author": author,
                    "image_url": image_url
                })
            await self._save_to_cache(result)
            return result

    async def _load_from_cache(self):
        json_data = await self.redis_session.get("Trending")
        if json_data:
            print("HERE!!")
            return json.loads(json_data)
        return None

    async def _save_to_cache(self, data):
        json_data = json.dumps(data)
        await self.redis_session.set("Trending", json_data, ex=3600)
