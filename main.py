from fastapi import FastAPI
from routes import post

app = FastAPI()

# Routers
app.include_router(post.router)

@app.get("/")
def root():
    return {"mesagge": "Hello World"}