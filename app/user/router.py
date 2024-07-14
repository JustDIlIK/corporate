from fastapi import APIRouter, Response

from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.user.auth import get_hashed_password, create_access_token, authenticate_user
from app.user.dao import UsersDAO
from app.user.schemas import SUsersAuth

router = APIRouter(
    prefix=("/auth"),
    tags=["Пользователь"]
)


@router.post("/register")
async def register_user(user_data: SUsersAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExistsException

    password = get_hashed_password(user_data.password)
    user_data.password = password
    await UsersDAO.add_record(email=user_data.email, password=user_data.password)


@router.post("/login")
async def login_user(response: Response, user_data: SUsersAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token)
    return access_token


@router.post("/logout")
async def login_user(response: Response):
     response.delete_cookie("access_token")

