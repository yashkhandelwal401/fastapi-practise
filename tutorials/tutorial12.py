from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def User_Not_Found_Exception(request:Request , exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":"User f{exc.name} not found "
        }
    )
@app.get("/user/{name}")
def get_user(name:str):
    if name != "mohit":
        raise UserNotFoundException(name)
    return{
        "name":name
    }

# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="User Not found"
#         )
#     return{
#         "id":1,
#         "name":"Mohit"
#     }