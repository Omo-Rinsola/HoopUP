from fastapi import FastAPI
from .routers import videos

app = FastAPI()


app.include_router(videos.router)

@app.get("/")
async def root():
    return{"message": "welcome to HoopUP!!"}


