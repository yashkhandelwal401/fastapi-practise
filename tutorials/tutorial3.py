from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Hello world from FastAPI VENV"}

#Users Route
@app.get("/about")
def about():
    return{"message":"This is about page"}

#Users Route
@app.get("/users")
def users():
    return{
        "users": ["Mohit","Rohit","Amit"]  
    }
