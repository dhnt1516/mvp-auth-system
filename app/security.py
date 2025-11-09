import re
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto",
                           argon2__time_cost=settings.ARGON2_TIME_COST,
                           argon2__memory_cost=settings.ARGON2_MEMORY_COST,
                           argon2__parallelism=settings.ARGON2_PARALLELISM)

PWD_POLICY = {
    "length": 8,
    "upper": r"[A-Z]",
    "lower": r"[a-z]",
    "digit": r"\d",
    "special": r"[!@#$%^&*(),.?\":{}|<>_\-\\\[\];'/~`+=]"
}

def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < PWD_POLICY["length"]:
        return False, f"Пароль должен быть минимум {PWD_POLICY['length']} символов"
    if not re.search(PWD_POLICY["upper"], password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву"
    if not re.search(PWD_POLICY["lower"], password):
        return False, "Пароль должен содержать хотя бы одну строчную букву"
    if not re.search(PWD_POLICY["digit"], password):
        return False, "Пароль должен содержать хотя бы одну цифру"
    if not re.search(PWD_POLICY["special"], password):
        return False, "Пароль должен содержать хотя бы один специальный символ"
    return True, "ok"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
