from pydantic import BaseModel


class HintSchema(BaseModel):
    """ Hint schema. """
    hints: str  # Hints.

    class Config:
        from_atrributes = True
