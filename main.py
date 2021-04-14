from fastapi import FastAPI, Depends
from config.database_config import engine, Base
from router.auth_router import authRouter
from router.books_router import booksRouter
from router.author_router import authorsRouter
from service import auth_service

Base.metadata.create_all(bind=engine)

# routes
PROTECTED = [Depends(auth_service.get_current_user)]
app = FastAPI(title="Book Collections")
app.include_router(booksRouter, dependencies=PROTECTED)
app.include_router(authorsRouter, dependencies=PROTECTED)
app.include_router(authRouter)
