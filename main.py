from fastapi import FastAPI
from config.database_config import engine, Base
from router.auth_router import authRouter
from router.books_router import booksRouter
from router.author_router import authorsRouter
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Collections")
app.include_router(booksRouter)
app.include_router(authorsRouter)
app.include_router(authRouter)
