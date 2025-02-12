# Задача "Аннотация и валидация":
# Запуск сервера - uvicorn module_16_2:app --reload --port=8162
# http://127.0.0.1:8162/
# http://127.0.0.1:8162/docs
# http://127.0.0.1:8162/redoc
from typing import Annotated

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def read_root() -> dict:
    return {"message": "Главная страница 16_2"}


# Фиксированный параметр
@app.get("/user/admin")
async def read_admin() -> dict:
    return {"user": "Вы вошли как администратор"}


# Динамический параметр в маршруте
@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]) -> dict:
    return {"user": f"Вы вошли как пользователь № {user_id}"}


# Пример использования Query Parameters
@app.get("/user/{username}/{age}")
async def read_user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> dict:
    return {"user": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
