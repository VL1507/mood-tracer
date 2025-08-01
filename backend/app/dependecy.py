from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.accessor import get_db_session
from app.repository.User import UserRepository


async def get_user_repository(
    db_session: AsyncSession = Depends(get_db_session),
) -> UserRepository:
    return UserRepository(db_session=db_session)
