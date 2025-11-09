import asyncio
import pytest
from httpx import AsyncClient
from app.main import app
import os

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
