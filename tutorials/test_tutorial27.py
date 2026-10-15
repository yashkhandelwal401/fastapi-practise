from fastapi.testclient import TestClient 
from tutorials.tutorial27 import app

client = TestClient(app)

#Test Home API
def test_home():
    response = client.get("/")
    #Status Code check
    assert response.status_code == 200
    #Response data check 
    assert response.json() == {"message":"Hello Mohit"}

#Test ADD API
def test_add():
    response = client.get("/add?a=5&b=4")

    assert response.status_code == 200
    assert response.json() == {"return": 9}