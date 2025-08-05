from dataclasses import dataclass
from app.repository.user import UserRepository


@dataclass
class UserService:
    user_repository: UserRepository

    async def create_user(self, email: str, password: str):
        password_hash = password  # FIXME: Hash the password

        user = await self.user_repository.create_user(
            email=email, password_hash=password_hash
        )
        return user.id
