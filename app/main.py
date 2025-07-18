from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

# from .database import engine
# from . import models
# from .routers import items

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

class SItems(BaseModel):
    name: str
    descr: str
    stars: int


@app.get('/items')
def get_items(
        author: str,
        date_from: date,
        date_to: date,
        view: Optional[int] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
):
    "Optional - не обязательный параметр"
    "Query - Ограничение от 1 до 5 "
    items = [
        {
            'name': 'how',
            'descr': 'aawdawda',
            'stars': 5
        }
    ]
    return f"item: "


class SCategory(BaseModel):
    cat_id: int
    name: str
    description: str


@app.post("/category")
def add_category(category: SCategory):
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)  # hello - name file
    # reload перезапустить сервер если садержимое изменится
