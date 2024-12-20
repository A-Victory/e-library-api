from fastapi import FastAPI
from app.routes import user, book, borrow

app = FastAPI(title="E-Library API System")

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(book.router, prefix="/books", tags=["Books"])
app.include_router(borrow.router, prefix="/borrow", tags=["Borrow"])