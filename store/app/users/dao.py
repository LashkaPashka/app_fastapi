from app.users.models import Users
from app.dao.basedao import BaseDAO
from sqlalchemy import insert
from app.database import async_session_maker


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def add_user(cls, **data):
        query = insert(cls.model).values(**data).returning(cls.model.id)
        async with async_session_maker() as session:
            await session.execute(query)
            await session.commit()
