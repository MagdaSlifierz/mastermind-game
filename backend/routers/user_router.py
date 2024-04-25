from fastapi import Depends, APIRouter, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi import status

from models.database import get_db
from schemas.user_schema import CreateUserSchema, UserSchema
from services.user_service import UserService

router = APIRouter()


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    """ Get user service. """
    return UserService(db)


@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUserSchema, response: Response, user_service: UserService = Depends(get_user_service)):
    """ Create a user. """
    user_id = user_service.save_user(user)
    response.headers['Location'] = f"/users/{user_id}"
    return Response(status_code=status.HTTP_201_CREATED, headers={"Location": f"/users/{user_id}"})


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=UserSchema)
def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    """ Get a user by id. """
    user = user_service.find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
