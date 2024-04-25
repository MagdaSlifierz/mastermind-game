from pydantic import BaseModel, field_validator


class CreateUserSchema(BaseModel):
    """ Create User Schema. """
    username: str

    @field_validator('username')
    def check_username_is_valid(cls, value):
        if value is not None and len(value) < 1:
            raise ValueError('Username must not be empty')
        return value


class UserSchema(CreateUserSchema):
    """ User Schema. """
    username: str

    class Config:
        from_atrributes = True
