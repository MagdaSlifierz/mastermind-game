from datetime import datetime
from uuid import uuid4

from sqlalchemy import Integer, Column, Text, ForeignKey, DateTime, UUID
from sqlalchemy.orm import relationship

from models.database import Base


class Attempt(Base):
    """ Attempt model. """
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)  # Attempt id.
    unique_id = Column(UUID(as_uuid=True), unique=True, default=lambda x: str(uuid4()))  # Unique id.
    game_id = Column(Integer, ForeignKey("games.id"))  # Game is required.
    number_of_attempts = Column(Integer, nullable=False)  # Number of attempts is required.
    guess = Column(Text, nullable=False)  # Guess is required.
    feedback = Column(Text, nullable=False)  # Feedback is required.
    created_at = Column(DateTime, default=datetime.utcnow)  # Created at.
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Updated at.

    # Relationships.
    game = relationship("Game", back_populates="attempts")  # Game is required.
