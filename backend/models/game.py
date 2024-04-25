from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, ForeignKey, UUID, DateTime
from sqlalchemy.orm import relationship

from models.database import Base


class Game(Base):
    """ Game model. """
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)  # Game id.
    unique_id = Column(UUID(as_uuid=True), unique=True, default=lambda x: str(uuid4()))  # Unique id.
    difficulty_id = Column(Integer, ForeignKey("difficulties.id"))  # Difficulty is required.
    status = Column(String, default="in_progress")  # Status can be in_progress, won, or lost.
    is_multiplayer = Column(String, default="false")  # Multiplayer can be true or false.
    secret_code = Column(String)  # Secret code.
    hints = Column(String) # Hints.
    mastermind_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Mastermind is not required.
    codebreaker_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Codebreaker is not required.
    created_at = Column(DateTime, default=datetime.utcnow)  # Created at.
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Updated at.

    # Relationships.
    difficulty = relationship(
        "Difficulty",
        back_populates="games")  # Relationship with Difficulty.
    attempts = relationship(
        "Attempt",
        back_populates="game")  # Relationship with Attempt.
    mastermind = relationship(
        "User",
        foreign_keys=[mastermind_id],
        back_populates="mastermind_games")  # Relationship with User.
    codebreaker = relationship(
        "User",
        foreign_keys=[codebreaker_id],
        back_populates="codebreaker_games")  # Relationship with User.
