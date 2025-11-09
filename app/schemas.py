from pydantic import BaseModel, constr

LoginStr = constr(min_length=3, max_length=32, regex=r'^[A-Za-z0-9._-]+$')

class RegisterRequest(BaseModel):
    login: LoginStr
    password: constr(min_length=8)
