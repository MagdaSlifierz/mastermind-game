from sqlalchemy.orm import Session

from schemas.user_schema import UserSchema, CreateUserSchema
from models.user import User


class UserService:
    """ User service. """

    def __init__(self, db: Session):
        self.db = db

    def save_user(self, user: CreateUserSchema) -> int:
        """ Save user to database. """
        new_user = User(username=user.username)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user.id

    def find_user_by_id(self, user_id: int) -> UserSchema:
        """ Find user by id. """
        return self.db.query(User).filter(User.id == user_id).first()

    def find_games_by_user_id(self, user_id: int) -> list[UserSchema]:
        """ Find games by user id. """
        return self.db.query(User).filter(User.id == user_id).first().games
