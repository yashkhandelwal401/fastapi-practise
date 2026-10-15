from fastapi import FastAPI, HTTPException, Depends
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime , timedelta 
from passlib.context import CryptContext

app = FastAPI()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

#password hashing SETUP
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#OauthSetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy user DB
fake_user_db = {
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}

#Hash Password
def hash_password(password:str):
    return pwd_context.hash(password)

#verify Password
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

    return token

#Login API(OAuth2 Form)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        ) 
    access_token = create_token({"sub":form_data.username})
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

#Token Varify
def verify_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

#protected Route
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return{
        "message":"Secure Data Accessed",
        "user":user
    }

#Protected Route
@app.get("/protected")
def protected_route(user: dict = Depends(verify_token)):
    return{
        "message":"Hello you have access to this protected route",
        "user":user
    }
