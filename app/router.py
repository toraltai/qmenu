from fastapi import APIRouter
from .users.urls import userRouter
from .companies.urls import companyRouter


api_router = APIRouter()


api_router.include_router(userRouter, prefix='/user', tags=['User API'])
api_router.include_router(companyRouter, prefix='/com', tags=['Company API'])