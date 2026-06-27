from fastapi import APIRouter
from .service import *
from .repository import TortoiseRepository
from typing import List


companyRouter = APIRouter()


repo = TortoiseRepository()
service = CompanyService(repo)


@companyRouter.get('/')
async def test():
    return await service.test()


@companyRouter.get('/all', response_model=List[GetCompany])
async def test():
    return await service.list_of_company()