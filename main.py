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

@app.get("/tarefas/{tarefa_id}", status_code=200)
def ver_tarefa_id(tarefa_id: int):
    return buscar_tarefa(tarefa_id)
    
@app.patch("/tarefas/{tarefa_id}", status_code=200)
def atualizar(tarefa_id: int, nova_tarefa: AtualizarTarefa):
   return atualizar_tarefa(tarefa_id, nova_tarefa)

@app.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar(tarefa_id: int):
    return deletar_tarefa(tarefa_id)