# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# data = response.json()
# print(data[:2])

from fastapi import FastAPI,HTTPException
import requests

app = FastAPI()

#Get ALL data
@app.get("/posts")
def get_posts():
    URL = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(URL)
    return response.json()

#Get Single post 
@app.get("/posts/{post_id}")
def get_posts(post_id:int):
    URL = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(URL)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail = "Page not found")
    return response.json()