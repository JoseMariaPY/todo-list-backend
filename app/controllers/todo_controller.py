# backend/app/controllers/todo_controller.py
import logging
from typing import List, Optional
from app.models.todo_model import TodoItem
from app.config import todos_collection
from bson import ObjectId
from fastapi import HTTPException

logger = logging.getLogger(__name__)

async def get_all_todos() -> List[TodoItem]:
    todos = []
    async for todo in todos_collection.find():
        # Convertimos a dict y usamos el _id de MongoDB como id
        todo_dict = dict(todo)
        todo_dict["_id"] = str(todo_dict["_id"])  # Convertir ObjectId a str
        todos.append(TodoItem(**todo_dict))
    return todos

async def get_todo(todo_id: str) -> Optional[TodoItem]:
    try:
        logger.info('get_todo controller by id:', todo_id)
        todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo["_id"] = str(todo["_id"])  # Convertir ObjectId a str para la respuesta
        return TodoItem(**todo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def create_todo(todo: TodoItem) -> TodoItem:
    new_todo = todo.dict(exclude_unset=True)  # No incluir id
    result = await todos_collection.insert_one(new_todo)
    new_todo["_id"] = str(result.inserted_id)  # Asignar el _id generado a la respuesta
    return TodoItem(**new_todo)

async def update_todo(todo_id: str, updated_todo: TodoItem) -> Optional[TodoItem]:
    updated_data = updated_todo.dict(exclude_unset=True)  # Excluir los campos que no se han actualizado
    result = await todos_collection.update_one(
        {"_id": ObjectId(todo_id)}, {"$set": updated_data}
    )
    if result.modified_count == 1:
        todo = await get_todo(todo_id)
        return todo
    return None

async def delete_todo(todo_id: str) -> bool:
    result = await todos_collection.delete_one({"_id": ObjectId(todo_id)})
    return result.deleted_count == 1
