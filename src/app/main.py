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
    Album(1, "The Jimi Hendrix Experience", "Jimi Hendrix", "Hey Joe", "https://m.media-amazon.com/images/I/810UEpS8ctL._AC_UY218_.jpg", "https://www.youtube.com/watch?v=rXwMrBb2x1Q"),
    Album(2, "Hit the Road Jack", "Ray Charles", "Hit the Road Jack", "https://images-na.ssl-images-amazon.com/images/I/51yihgHF-5L._SY300_SX300_QL70_FMwebp_.jpg", "https://www.youtube.com/watch?v=uSiHqxgE2d0"),
    Album(3, "Nimrod", "Green Day", "Good Riddance (Time Of Your Life)", "https://m.media-amazon.com/images/I/71dBwWTWgKL._SX425_.jpg", "https://www.youtube.com/watch?v=CnQ8N1KacJc"),
    Album(4, "Time at JnJ", "Xu Labels", "I'll Miss Y'all", "http://www.xuguanzhou.io/theme/images/project/goals.png", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    Album(5, "Making Mirrors", "Gotye", "Goodbye Stranger", "https://m.media-amazon.com/images/I/91vXYllHodL._SX425_.jpg", "https://www.youtube.com/watch?v=8UVNT4wvIGY"),
    Album(6, "Breakfast in America", "Supertramp", "Breakfast in America", "https://upload.wikimedia.org/wikipedia/en/c/c4/Supertramp_-_Breakfast_in_America.jpg", "https://www.youtube.com/watch?v=u8pVZ5hTGJQ"),
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
