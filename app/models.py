from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    login: str = Field(index=True, max_length=32, unique=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
