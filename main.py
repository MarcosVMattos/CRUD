from fastapi import FastAPI

from database import Base, engine
from models import Task
from routers.tasks import router


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=router)

@app.get("/")
def root():
    return {"message": "API rodando"}
