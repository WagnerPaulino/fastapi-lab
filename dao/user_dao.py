from domain.models import User
from sqlalchemy.orm import Session
from dto.user_dto import UserDtoIn


class UserDao:
    def findAll(self, db: Session):
        return db.query(User).all()

    def findOne(self, user_id: int, db: Session):
        return db.query(User).filter(User.id == user_id).first()

    def findOneByUsername(self, username: str, db: Session):
        return db.query(User).filter(User.username == username).first()

    def create(self, user: UserDtoIn, db: Session):
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user: UserDtoIn, db: Session):
        db.query(User).filter(User.id == user_id).update(user.dict(), synchronize_session=False)
        db.commit()
        return user

    def delete(self, user_id: int, db: Session):
        db.query(User).filter(User.id == user_id).delete()
        db.commit()
