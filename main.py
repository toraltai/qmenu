from fastapi import FastAPI
from app.router import api_router
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from config import settings


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=settings.CORS_ORIGINS,  #Проверить
    allow_origins=[
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api/v1')


register_tortoise(
    app,
    db_url=settings.DB_URL,
    modules={"models": settings.APPS_MODEL},
    generate_schemas=True,
    add_exception_handlers=True,
)