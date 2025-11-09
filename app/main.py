from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from app.schemas import RegisterRequest
from app.security import validate_password, hash_password
from app.crud import get_user_by_login, create_user
from app.config import settings
from app.logger import logger
import asyncio

app = FastAPI(title="MVP Auth", docs_url="/docs")

@app.on_event("startup")
async def startup():
    # initialize DB (dev convenience) - production: run alembic migrations
    from app.db import init_db
    await init_db()
    logger.info("Startup complete")

@app.post("/api/register", status_code=201)
async def register(payload: RegisterRequest):
    # Validate password policy
    ok, msg = validate_password(payload.password)
    if not ok:
        logger.info(f"Weak password attempt for login={payload.login}")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=msg)

    # Prevent logging the raw password
    existing = await get_user_by_login(payload.login)
    if existing:
        logger.info(f"Duplicate login attempt: {payload.login}")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="login already exists")

    pwd_hash = hash_password(payload.password)
    try:
        await create_user(payload.login, pwd_hash)
    except Exception:
        # if IntegrityError from unique constraint
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="login already exists")
    return JSONResponse(status_code=201, content={"message": "user создан"})
