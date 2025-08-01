from fastapi import APIRouter
from . import ping

test_router = APIRouter()

test_router.include_router(ping.router)
