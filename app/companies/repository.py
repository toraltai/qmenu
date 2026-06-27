from ..models.companies import *


class TortoiseRepository:
    async def list_of_company(self):
        return await GetCompany.from_queryset(Company.all())
    

    async def create_company(self, obj = CreateCompany):
        obj = await Company.create(**obj.dict(exclude_unset=True))
        return await GetCompany.from_tortoise_orm(obj)