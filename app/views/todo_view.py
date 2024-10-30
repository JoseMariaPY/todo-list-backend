# backend/app/views/todo_view.py
import logging
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.todo_model import TodoItem
from app.controllers import todo_controller

router = APIRouter()

@router.get("/todos", response_model=List[TodoItem])
async def get_todos():
    return await todo_controller.get_all_todos()

@router.get("/todos/{todo_id}", response_model=TodoItem)
async def get_todo(todo_id: str):
    logging.info('get_todo view by id:', todo_id)
    todo = await todo_controller.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos", response_model=TodoItem)
async def create_todo(todo: TodoItem):
    return await todo_controller.create_todo(todo)

@router.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: str, todo: TodoItem):
    updated_todo = await todo_controller.update_todo(todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    success = await todo_controller.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
