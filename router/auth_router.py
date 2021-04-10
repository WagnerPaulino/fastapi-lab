from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from config.auth_config import oauth2_scheme
from config.database_config import get_db
from dao.user_dao import UserDao
from dto.user_dto import UserDtoIn, UserDtoOut

authRouter = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

userDao = UserDao()


@authRouter.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username}


async def get_current_user(token: str = Depends(oauth2_scheme), session=Depends(get_db)):
    user = userDao.findOneByUsername(token, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@authRouter.get("/users/me", response_model=UserDtoOut)
async def read_users_me(current_user: UserDtoIn = Depends(get_current_user)):
    return current_user
