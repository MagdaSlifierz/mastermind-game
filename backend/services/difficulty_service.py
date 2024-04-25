from sqlalchemy.orm import Session

from schemas.difficulty_schema import DifficultySchema
from models.difficulty import Difficulty


class DifficultyService:
    """ Difficulty service. """

    def __init__(self, db: Session):
        self.db = db

    def find_all_difficulties(self) -> list[DifficultySchema]:
        """ Find all difficulties. """
        return self.db.query(Difficulty).all()

    def find_difficulty_by_id(self, difficulty_id: int) -> DifficultySchema:
        """ Find a difficulty by id. """
        return self.db.query(Difficulty).filter(Difficulty.id == difficulty_id).first()
