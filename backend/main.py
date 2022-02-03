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

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'There is no TODO item with this title: {title}')


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong / Bad Request')


@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f'There is no TODO item with this title: {title}')


@app.delete("/api/todo{title}", response_model=Todo)
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return f'TODO item with title "{title}" removed'
    raise HTTPException(404, f'There is no TODO item with this title: {title}')


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')

    # Or use terminal command: uvicorn main:app --reload
