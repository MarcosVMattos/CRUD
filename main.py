from fastapi import FastAPI  # apaguei httpexception e outras coisas que eu n usava

from storage import tarefas
from schemas import Tarefa, AtualizarTarefa
from services import criar_tarefa, buscar_tarefa, atualizar_tarefa, deletar_tarefa

app = FastAPI()

@app.get("/")
def raiz():
    return {"message": "API criada com sucesso"}

@app.post("/tarefas", status_code=201)
def criar(tarefa: Tarefa):
    return criar_tarefa(tarefa)

@app.get("/tarefas", status_code=200)
def listar_tarefas():
    return tarefas

@app.get("/tarefas/{id}", status_code=200)
def ver_tarefa_id(id: int):
    return buscar_tarefa(id)
    
@app.patch("/tarefas/{id}", status_code=200)
def atualizar(id: int, nova_tarefa: AtualizarTarefa):
   return atualizar_tarefa(id, nova_tarefa)

@app.delete("/tarefas/{id}", status_code=204)
def deletar(id: int):
    return deletar_tarefa(id)