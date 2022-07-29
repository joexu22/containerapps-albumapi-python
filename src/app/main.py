from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="GET",
    allow_headers=["*"]
)

class Album():
    def __init__(self, id, title, artist, price, image_url, link):
         self.id = id
         self.title = title
         self.artist = artist
         self.price = price
         self.image_url = image_url
         self.link = link

albums = [ 
    Album(1, "Feeling Strangely Fine", "Semisonic", "Closing Time", "https://images-na.ssl-images-amazon.com/images/I/61nyQCkciLL._SX300_SY300_QL70_FMwebp_.jpg", "https://www.youtube.com/watch?v=xGytDsqkQY8"),
    Album(2, "Nimrod", "Green Day", "Green Day - Good Riddance (Time Of Your Life)", "https://m.media-amazon.com/images/I/71dBwWTWgKL._SX425_.jpg", "https://www.youtube.com/watch?v=CnQ8N1KacJc"),
]

@app.get("/")
def read_root():
    return {"Azure Container Apps Python Sample API"}

@app.get("/albums")
def get_albums():
    return albums

@app.get("/hello")
def get_test():
    return {"Hey CoreInfra Team"}

@app.get("/goodbye")
def get_goodbye():
    return {"Goodbye CoreInfra Team"}
