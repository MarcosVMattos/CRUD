from fastapi import FastAPI
from routers.tarefas import router

app = FastAPI()
app.include_router(router=router)

@app.get("/")
def raiz():
    return {"message": "API rodando"}
