from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.timer import timingMiddleWare

from app.routes.issues import router as issues_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_middleware(timingMiddleWare)

app.include_router(issues_router)
