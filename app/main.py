from fastapi import FastAPI
from .database.database import engine, Base
from .routers import mpc


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(mpc.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
