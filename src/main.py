import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from auth.router import router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=13500)
