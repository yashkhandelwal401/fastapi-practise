from fastapi import FastAPI,HTTPException,Depends,Header
from jose import jwt
from datetime import datetime , timedelta 

app = FastAPI()

SECRET_KEY = "mysecret"

ALGORITHM = "HS256"

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({
        "exp":explore
    })
    token = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

    return token

#Login API(Token Generate)
@app.post("/login")
def login(username:str , password:str):
    if username != "admin" or password != "1234"
    raise HTTPException(
        status_code=401,
        detail="Invalid Username and password"
    )
    token = create_token({
    "sub":username
    })
    return{
        "access_token": token
    }

#Token Varify

