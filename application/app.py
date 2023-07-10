from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.endpoints.room import router as room_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(room_router, prefix="/rooms", tags=["rooms"])

    return app