from fastapi import APIRouter
from .service import *
from .repository import TortoiseRepository

companyRouter = APIRouter()


repo = TortoiseRepository()
service = CompanyService(repo)


@companyRouter.get('/')
async def test():
    return await service.test()