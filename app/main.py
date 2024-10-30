from fastapi import FastAPI
import logging
from app.views import todo_view

logging.basicConfig(level=logging.INFO)  # Cambia el nivel si necesitas más detalles
logger = logging.getLogger(__name__)

# Crear instancia de FastAPI
app = FastAPI()
logger.info('Iniciando')

# Registrar el enrutador de tareas
app.include_router(todo_view.router)
