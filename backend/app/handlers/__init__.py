from fastapi import APIRouter
from . import auth
from . import test

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(test.test_router)
