import uvicorn
from fastapi import FastAPI
from app.routers.user_router import user_router

app = FastAPI()
app.include_router(user_router, prefix='/user')


@app.get("/")
async def root():
    return "welcome to our project!!!!!!!!!!!!!"


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
