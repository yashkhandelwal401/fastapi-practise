from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Allowed Origins(Front-end URL)
origins = [
    " http://localhost:4200/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, #allowed FE
    allow_credentials = True,
    allow_methods = ["*"] , #GET,PUT,POST,DELETE
    allow_headers=["*"]
)
