from .repository import *


class CompanyService:
    def __init__(self, repo: TortoiseRepository):
        self.repo = repo

    async def test(self):
        return await self.repo.test()
    
    async def list_of_company(self):
        return await self.repo.list_of_company()