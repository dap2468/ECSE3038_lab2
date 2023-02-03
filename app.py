from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []

@app.get("/todos")
async def get_all_todos():
    return fake_database

@app.post("/todos")
async def create_new_todo(request: Request):
    todo= await request.json()
    fake_database.append(todo)
    return todo

@app.patch("/todos/{id}")
async def update_todo_by_id(id:int, request: Request):
    todo_update= await request.json()
    for todo in fake_database:
        if id== todo['id']:
            todo.update(todo_update)
            raise HTTPException(status_code=200, detail="OK")
            return todo
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/todos/{id}")
async def delete_todo_by_id(id:int):
    for todo in fake_database:
        if id== todo['id']:
            fake_database.remove(todo)
            raise HTTPException(status_code=200, detail="OK")
            return {"message":"ITEM WAS DELETED "}
    raise HTTPException(status_code=404, detail="Item not found")
    
