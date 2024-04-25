from pydantic import BaseModel, field_validator


class CreateGameSchema(BaseModel):
    """ Create Game Schema. """
    difficulty_id: int
    status: str = "in_progress"
    is_multiplayer: bool = False

    @field_validator('difficulty_id')
    def check_difficulty_id_is_valid(cls, value):
        if value is not None and value < 1:
            raise ValueError('Difficulty ID must be greater than 0')
        return value

    @field_validator('status')
    def check_status_is_valid(cls, value):
        if value is not None and len(value) < 1 and value not in ['in_progress', 'won', 'lost']:
            raise ValueError('Status must be in_progress, won, or lost')
        return value


class GameSchema(CreateGameSchema):
    """ Game Schema. """
    id: int

    class Config:
        from_attributes = True
