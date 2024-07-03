from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

user_list = [
            User(id=1,name="Coco",surname="Alvadez",url="https://www.youtube.com",age=34),
            User(id=2,name="Taton",surname="Rossa",url="https://www.tatonelcrack.com",age=18),
            User(id=3,name="Maria",surname="Masardi",url="https://www.mariamasar.com",age=28),]

@app.get("/usersjson")
async def usersjson():
    return [{"id": 1,"name": "Coco", "surname": "Alvadez", "url": "https://www.youtube.com", "age": 34},
            {"id": 2,"name": "Taton", "surname": "Rossa", "url": "https://www.tatonelcrack.com", "age": 18},
            {"id": 3,"name": "Maria", "surname": "Masardi", "url": "https://www.mariamasar.com", "age": 28},
            ]
    
@app.get("/users")
async def user():
    return user_list

# path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
# query
@app.get("/userquery")
async def user(id: int):
    return search_user(id)



def search_user(id):
    user = filter(lambda user_of_list: user_of_list.id == id, user_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}