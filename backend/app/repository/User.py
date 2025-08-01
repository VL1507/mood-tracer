from app.infrastructure.database.models import User

from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class UserRepository:
    db_session: AsyncSession

    async def create_user(self, email: str, password_hash: str) -> User:
        async with self.db_session as session:
            user = User(email=email, password_hash=password_hash)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
