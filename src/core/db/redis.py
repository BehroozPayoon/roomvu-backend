from typing import Any, AsyncContextManager, AsyncGenerator, Callable

import redis.asyncio as redis

from src.core.settings import get_settings
from src.core.mocks import get_redis_session

AsyncSessionGenerator = AsyncGenerator[redis.Redis, None]


def async_session(
        host: str, password: str, *, wrap: Callable[..., Any] | None = None,
) -> Callable[..., AsyncSessionGenerator] | AsyncContextManager[Any]:
    pool = redis.ConnectionPool(
        host=host, password=password, decode_responses=True)

    async def get_session() -> AsyncSessionGenerator:  # noqa: WPS430, WPS442
        async with redis.Redis(connection_pool=pool) as session:
            yield session

    return get_session if wrap is None else wrap(get_session)


override_session = get_redis_session, async_session(get_settings().redis_host,
                                                    get_settings().redis_password)
context_session = redis.from_url(
    f"redis://:{get_settings().redis_password}@{get_settings().redis_host}")
