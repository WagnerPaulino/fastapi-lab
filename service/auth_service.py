from fastapi import Depends, HTTPException, status

from config.auth_config import oauth2_scheme
from config.database_config import get_db
from dao.user_dao import UserDao

userDao = UserDao()


async def get_current_user(token: str = Depends(oauth2_scheme), session=Depends(get_db)):
    print(token)
    user = userDao.findOneByUsername(token, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
