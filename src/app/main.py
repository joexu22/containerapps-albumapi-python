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
    def __init__(self, id, title, artist, song, image_url, link):
         self.id = id
         self.title = title
         self.artist = artist
         self.song = song
         self.image_url = image_url
         self.link = link

albums = [
    Album(1, "Nimrod", "Green Day", "Good Riddance (Time Of Your Life)", "https://m.media-amazon.com/images/I/71dBwWTWgKL._SX425_.jpg", "https://www.youtube.com/watch?v=CnQ8N1KacJc"),
    Album(2, "Breakfast in America", "Supertramp", "Goodbye Stranger", "https://m.media-amazon.com/images/I/51Xs5nXws8L._UX358_FMwebp_QL85_.jpg", "https://www.youtube.com/watch?v=u8pVZ5hTGJQ"),
    Album(3, "Time at JnJ", "Xu Labels", "I'll Miss Y'all", "https://image.shutterstock.com/image-vector/chinese-calligraphy-translation-xu-a-260nw-1773157127.jpg", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    Album(4, "No Strings Attached", "NSYNC", "Bye Bye Bye", "https://m.media-amazon.com/images/I/812H+OFXlCL._SX425_.jpg", "https://www.youtube.com/watch?v=Eo-KmOd3i7s"),
    Album(5, "Hit the Road Jack", "Ray Charles", "Hit the Road Jack", "https://images-na.ssl-images-amazon.com/images/I/51yihgHF-5L._SY300_SX300_QL70_FMwebp_.jpg", "https://www.youtube.com/watch?v=uSiHqxgE2d0"),
    Album(6, "Making Mirrors", "Gotye", "Somebody That I Used to Know", "https://m.media-amazon.com/images/I/91vXYllHodL._SX425_.jpg", "https://www.youtube.com/watch?v=8UVNT4wvIGY"),    
    Album(7, "Feeling Strangely Fine", "Semisonic", "Closing Time", "https://images-na.ssl-images-amazon.com/images/I/61nyQCkciLL._SX300_SY300_QL70_FMwebp_.jpg", "https://www.youtube.com/watch?v=xGytDsqkQY8"),
]

@app.get("/")
def read_root():
    return {"Azure Container Apps Python Sample API"}

@app.get("/albums")
def get_albums():
    return albums

@app.get("/hello")
def get_hello():
    return {"Hey CoreInfra Team"}

@app.get("/goodbye")
def get_goodbye():
    return {"Goodbye CoreInfra Team"}
