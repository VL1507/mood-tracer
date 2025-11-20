from fastapi import APIRouter
from . import auth
from . import test
from . import user
from . import redirect_to_docs

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(test.test_router)
api_router.include_router(user.router)
api_router.include_router(redirect_to_docs.router)