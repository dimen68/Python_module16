# Задача "Начало пути"
# Запуск сервера - uvicorn module_16_1:app --reload --port=8161
# http://127.0.0.1:8161/
# http://127.0.0.1:8161/docs
# http://127.0.0.1:8161/redoc


from fastapi import FastAPI
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def read_root() -> dict:
    return {"message": "Главная страница"}

# Фиксированный параметр
@app.get("/user/admin")
async def read_admin() -> dict:
    return {"user": "Вы вошли как администратор"}

# Динамический параметр в маршруте
@app.get("/user/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"user": f"Вы вошли как пользователь № {user_id}"}

# Пример использования Query Parameters
@app.get("/user/")
async def read_user_info(username: str, age: int) -> dict:
    return {"user": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}