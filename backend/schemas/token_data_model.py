from typing import Optional

from pydantic import BaseModel


class TokenDataModel(BaseModel):
    username: Optional[str] = None
