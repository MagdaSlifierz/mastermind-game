import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers.base_router import router


def init_applications():
    sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
    application = FastAPI()
    socket_application = socketio.ASGIApp(sio, other_asgi_app=application)

    origins = [
        "http://localhost:3000",
    ]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)
    return socket_application


app = init_applications()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
