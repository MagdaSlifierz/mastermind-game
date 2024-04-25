from pydantic import BaseModel


class DifficultySchema(BaseModel):
    """ Difficulty Schema. """
    id: int
    name: str
    label: str
    max_attempts: int
    code_length: int
    minimum_number: int
    maximum_number: int
    is_duplicate_allowed: bool

    class Config:
        from_attributes = True
