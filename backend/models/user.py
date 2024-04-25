from uuid import uuid4

from sqlalchemy import Column, Integer, String, Text, UUID, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class User(Base):
    """ User model. """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # User id.
    unique_id = Column(UUID(as_uuid=True), unique=True, default=lambda x: str(uuid4()))  # Unique id.
    username = Column(Text, unique=True, index=True)  # Username is unique.

    # Relationships.
    mastermind_games = relationship(
        "Game",
        back_populates="mastermind",
        foreign_keys="[Game.mastermind_id]", )  # Relationship with Game.
    codebreaker_games = relationship(
        "Game",
        back_populates="codebreaker",
        foreign_keys="[Game.codebreaker_id]", )  # Relationship with Game.
