from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)
from model import Todo

app = FastAPI()

allowed = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed,
    allow_credentials=True,
    allow_methods=allowed,
    allow_headers=allowed,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/todo")
async def get_todo():
    response = fetch_all_todos()
    return response


@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'There is no TODO item with this title: {title}')


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong / Bad Request')


@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f'There is no TODO item with this title: {title}')


@app.delete("/api/todo{title}", response_model=Todo)
def delete_todo(title):
    response = remove_todo(title)
    if response:
        return f'TODO item with title "{title}" removed'
    raise HTTPException(404, f'There is no TODO item with this title: {title}')


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')

    # Or use terminal command: uvicorn main:app --reload
