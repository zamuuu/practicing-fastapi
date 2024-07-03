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

@app.get("/users")
async def users():
    return user_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
# Query
@app.get("/user")
async def user(id: int):
    return search_user(id)


# POST method in my API
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "Ya existe este usuario."}
    else:
        return user_list.append(user)
    

def search_user(id):
    user = filter(lambda user_of_list: user_of_list.id == id, user_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}