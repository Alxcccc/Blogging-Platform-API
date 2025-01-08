import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes import post

app = FastAPI()

# Routers
app.include_router(post.router)

@app.get("/", status_code=302, include_in_schema=False)
async def root():
    return RedirectResponse("/docs")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)