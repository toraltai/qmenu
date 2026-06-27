from fastapi import APIRouter
from .service import *
from .repository import TortoiseRepository
from typing import List


companyRouter = APIRouter()


repo = TortoiseRepository()
service = CompanyService(repo)


@companyRouter.get('/all')
async def test():
    return await service.list_of_company()


@companyRouter.post('/', response_model=GetCompany)
async def add_company(company: CreateCompany): #type: ignore
    return await service.create_company(company)