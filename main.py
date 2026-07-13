from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

from routers.tasks import router

app = FastAPI()
app.include_router(router=router)

DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API rodando"}
