import uvicorn
from app.routers.user_router import user_router
from app.routers.operation_router import operation_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(user_router, prefix='/user')
app.include_router(operation_router, prefix='/operation')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
