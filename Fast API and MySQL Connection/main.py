from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class ToDoBase(BaseModel):
    id: int
    task_body: str
    due_day: int
    due_month: str
    due_year: int
    user_id: int

class UserBase(BaseModel):
    id: int
    name: str
    age: int
    gender: str



db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: ToDoBase, db: db_dependency):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    return {"detail": "Todo added successfully"}

@app.get( "/todos/", status_code=status.HTTP_200_OK)
async def get_todos(db: db_dependency):
    return db.query(models.Todo).all()

@app.put("/todos/{todo_id}", response_model=ToDoBase,status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, todo_request: ToDoBase, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if db_todo.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found')
    update_data = todo_request.model_dump(exclude_unset=True)

    db_todo.update(update_data, synchronize_session=False)
    db.commit()

    return db_todo.first()


@app.delete("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(todo_id: int, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id)

    if db_todo.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found')

    db_todo.delete(synchronize_session=False)
    db.commit()

    return {"detail": "Todo deleted successfully"}

@app.get("/users/", status_code=status.HTTP_200_OK, tags=["User"])
async def get_users(db: db_dependency):
    return db.query(models.User).all()

@app.post("/users/", status_code=status.HTTP_201_CREATED, tags=["User"])
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    return{"detail": "User added successfully"}