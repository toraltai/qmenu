from ..models.users import *


class TortoiseRepository:
    async def test(self):
        return {"hello":"world"}
    
    async def create(self, user: CreateUser): #type: ignore
        user_obj = User(name=user.name)
        user_obj.set_password(user.password_hash)

        await user_obj.save()

        return await GetUser.from_tortoise_orm(user_obj)