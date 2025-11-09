import pytest

async def test_weak_password(client):
    payload = {"login": "weak1", "password": "weakpass"}
    r = await client.post("/api/register", json=payload)
    assert r.status_code == 422
    assert "Пароль" in r.json().get("detail")
