from .repository import *


class CompanyService:
    def __init__(self, repo: TortoiseRepository):
        self.repo = repo


    async def list_of_company(self):
        return await self.repo.list_of_company()
    

    async def create_company(self, company: CreateCompany,): #type: ignore
        return await self.repo.create_company(company)