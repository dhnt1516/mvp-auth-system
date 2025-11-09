import pytest

async def test_register_duplicate(client):
    payload = {"login": "dupuser", "password": "Aa1!aaaa"}
    r1 = await client.post("/api/register", json=payload)
    assert r1.status_code == 201

    r2 = await client.post("/api/register", json=payload)
    assert r2.status_code == 409
