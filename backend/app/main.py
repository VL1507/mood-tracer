from fastapi import FastAPI

from app.settings import settings
from app.handlers import api_router

def on_startup():
    print("JWT_SECRET_KEY:", settings.JWT)
    print("JWT_SECRET_KEY:", settings.JWT.SECRET_KEY)


app = FastAPI(on_startup=[on_startup])

app.include_router(api_router)


