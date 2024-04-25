from pydantic import BaseModel, field_validator


class CreateAttemptSchema(BaseModel):
    """ Create Attempt Schema. """
    game_id: int
    guess: str

    @field_validator('game_id')
    def check_game_id_is_valid(cls, value):
        if value is not None and value < 1:
            raise ValueError('Game ID must be greater than 0')
        return value

    @field_validator('guess')
    def check_guess_is_valid(cls, value):
        if value is not None and len(value) < 1:
            raise ValueError('Guess must not be empty')
        return value


class AttemptSchema(CreateAttemptSchema):
    """ Attempt Schema. """
    id: int
    number_of_attempts: int
    feedback: str

    class Config:
        from_attributes = True
