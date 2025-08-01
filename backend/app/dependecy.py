from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.accessor import get_db_session
from app.repository.user import UserRepository
from app.service.user import UserService


async def get_user_repository(
    db_session: AsyncSession = Depends(get_db_session),
) -> UserRepository:
    return UserRepository(db_session=db_session)


async def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repository=user_repository)
