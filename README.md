# todo-list-backend


todo-list-backend/
├── app/
│   ├── controllers/
│   │   └── todo_controller.py
│   ├── models/
│   │   └── todo_model.py
│   ├── views/
│   │   └── todo_view.py
│   ├── main.py
│   ├── config.py
│   └── __init__.py
├── Dockerfile
└── requirements.txt


Estructura de la API:
---------------------------------------
* GET /todos: Obtiene todas las tareas.
* POST /todos: Crea una nueva tarea.
* PUT /todos/{todo_id}: Actualiza una tarea específica.
* DELETE /todos/{todo_id}: Elimina una tarea específica.