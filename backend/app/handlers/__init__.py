from fastapi import APIRouter
from . import auth
from . import test
from . import user

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(test.test_router)
api_router.include_router(user.router)