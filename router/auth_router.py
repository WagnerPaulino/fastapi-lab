from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from config.database_config import get_db
from dao.user_dao import UserDao
from dto.user_dto import UserDtoIn, UserDtoOut
from service.auth_service import get_current_user

authRouter = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

userDao = UserDao()


@authRouter.post('/register')
async def sign_on(user: UserDtoIn, session=Depends(get_db)):
    return userDao.create(user, session)


@authRouter.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username}


@authRouter.get("/users/me", response_model=UserDtoOut)
async def read_users_me(current_user: UserDtoIn = Depends(get_current_user)):
    return current_user
