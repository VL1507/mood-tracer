from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class Token(BaseModel):
    access_token: str
    token_type: str


# Эндпоинт для авторизации
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Здесь проверяем логин/пароль (обычно против базы данных)
    if form_data.username != "test" or form_data.password != "test":
        raise HTTPException(status_code=400, detail="Неверные данные")

    # В реальном приложении здесь генерируется JWT токен
    # return {"access_token": "fake_token", "token_type": "bearer"}
    return Token(access_token="fake_token", token_type="bearer")
