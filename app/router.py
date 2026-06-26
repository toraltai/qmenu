from fastapi import APIRouter
from .users.urls import userRouter


api_router = APIRouter()


api_router.include_router(userRouter, prefix='/user', tags=['User API'])