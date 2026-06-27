from ..models.companies import *
from tortoise import connections


class TortoiseRepository:
    async def list_of_company(self):
        # return await Company.all().values('id','title','user_id')
        conn = connections.get("default")
        return await conn.execute_query_dict("select * from company")
    

    async def create_company(self, obj = CreateCompany):
        obj = await Company.create(**obj.dict(exclude_unset=True))
        return await GetCompany.from_tortoise_orm(obj)