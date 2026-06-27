from ..models.companies import *


class TortoiseRepository:
    async def test(self):
        return {"status":"success"}
    

    async def list_of_company(self):
        return await GetCompany.from_queryset(Company.all())