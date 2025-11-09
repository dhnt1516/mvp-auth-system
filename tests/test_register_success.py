import pytest

async def test_register_success(client):
    payload = {"login": "user1", "password": "Aa1!aaaa"}
    r = await client.post("/api/register", json=payload)
    assert r.status_code == 201
    assert r.json().get("message") == "user создан"
