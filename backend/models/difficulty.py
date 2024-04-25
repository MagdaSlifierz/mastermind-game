from sqlalchemy import Column, Integer, Boolean
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from models.database import Base


class Difficulty(Base):
    """ Difficulty model. """
    __tablename__ = "difficulties"

    id = Column(Integer, primary_key=True, index=True)  # Difficulty id.
    name = Column(Text, unique=True, nullable=False, index=True)  # Difficulty name is unique.
    label = Column(Text, unique=True, nullable=False, index=True)  # Difficulty label is unique.
    max_attempts = Column(Integer, nullable=False)  # Maximum attempts is required.
    code_length = Column(Integer, nullable=False)  # Code length is required.
    minimum_number = Column(Integer, nullable=False)  # Minimum number is required.
    maximum_number = Column(Integer, nullable=False)  # Maximum number is required.
    is_duplicate_allowed = Column(Boolean)  # Duplicate allowed can be true or false.

    # Relationships.
    games = relationship("Game", back_populates="difficulty")  # Difficulty has many games.
