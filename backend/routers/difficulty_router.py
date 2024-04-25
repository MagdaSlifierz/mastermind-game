from fastapi import Depends, APIRouter, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi import status

from models.database import get_db
from schemas.difficulty_schema import DifficultySchema

from services.difficulty_service import DifficultyService

router = APIRouter()


def get_difficulty_service(db: Session = Depends(get_db)) -> DifficultyService:
    """ Get difficulty service. """
    return DifficultyService(db)


@router.get("/difficulties", status_code=status.HTTP_200_OK, response_model=list[DifficultySchema])
def get_all_difficulties(difficulty_service: DifficultyService = Depends(get_difficulty_service)) -> list[
    DifficultySchema]:
    """ Get all difficulties. """
    return difficulty_service.find_all_difficulties()


@router.get("/difficulties/{difficulty_id}", status_code=status.HTTP_200_OK, response_model=DifficultySchema)
def get_difficulty_by_id(difficulty_id: int,
                         difficulty_service: DifficultyService = Depends(get_difficulty_service)) -> DifficultySchema:
    """ Get a difficulty by id. """
    difficulty = difficulty_service.find_difficulty_by_id(difficulty_id)
    if difficulty is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Difficulty not found")
    return difficulty
