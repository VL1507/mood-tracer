from fastapi import APIRouter, Depends
from app.service.user import UserService
from app.dependecy import get_user_service

router = APIRouter()


@router.post("/user")
async def create_user(
    email: str, password: str, user_service: UserService = Depends(get_user_service)
):
    user_id = await user_service.create_user(email=email, password=password)
    return {"user_id": user_id}
