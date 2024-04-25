import socketio
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from models.database import get_db
from schemas.attempt_schema import AttemptSchema, CreateAttemptSchema
from schemas.game_schema import CreateGameSchema, GameSchema
from schemas.hints_schema import HintSchema

from services.game_service import GameService

router = APIRouter()


def get_game_service(db: Session = Depends(get_db)) -> GameService:
    """ Get game service. """
    return GameService(db)


@router.post("/games", status_code=status.HTTP_201_CREATED, response_model=GameSchema)
def create_game(game: CreateGameSchema, game_service: GameService = Depends(get_game_service)):
    """ Create a game. """
    return game_service.save_game(game)


@router.get("/games", status_code=status.HTTP_200_OK, response_model=list[GameSchema])
def get_all_games(game_service: GameService = Depends(get_game_service)) -> list[GameSchema]:
    """ Get all games. """
    return game_service.find_all_games()


@router.get("/games/{game_id}", status_code=status.HTTP_200_OK, response_model=GameSchema)
def get_game(game_id: int, game_service: GameService = Depends(get_game_service)):
    """ Get a game by id. """
    game = game_service.find_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    return game


@router.get("/games/{game_id}/hints", status_code=status.HTTP_200_OK, response_model=HintSchema)
def get_game_hints(game_id: int, game_service: GameService = Depends(get_game_service)):
    """ Get hints by game id. """
    game = game_service.find_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    return game_service.get_game_hints(game_id)


@router.post("/games/{game_id}/attempts", status_code=status.HTTP_201_CREATED, response_model=AttemptSchema)
def create_attempt_to_game(game_id: int, attempt: CreateAttemptSchema,
                           game_service: GameService = Depends(get_game_service)):
    """ Create an attempt to a game. """
    game = game_service.find_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")
    return game_service.save_attempt_to_game(game_id, attempt)


@router.get("/games/{game_id}/attempts", status_code=status.HTTP_200_OK, response_model=list[AttemptSchema])
def get_all_attempts_by_game_id(game_id: int, game_service: GameService = Depends(get_game_service)):
    """ Get all attempts by game id. """
    return game_service.find_all_attempts_by_game_id(game_id)


sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')


@sio.event
async def connect(sid, environ):
    print("connect ", sid)


# Event handler for messages on the 'chat' event
@sio.event
async def chat(sid, data):
    print("message ", data)
    await sio.emit('reply', data, room=sid)


# Event handler for disconnections
@sio.event
async def disconnect(sid):
    print("disconnect ", sid)
