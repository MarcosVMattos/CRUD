from fastapi import FastAPI

from schemas import Tarefa, TarefaId, AtualizarTarefa
from services import criar_tarefa, listar_tarefas, buscar_tarefa, atualizar_tarefa, deletar_tarefa

app = FastAPI()

@app.get("/")
def raiz():
    return {"message": "API criada com sucesso"}

@app.post("/tarefas", status_code=201, response_model=TarefaId)
def criar(tarefa: Tarefa):
    return criar_tarefa(tarefa)

@app.get("/tarefas", status_code=200, response_model=list[TarefaId])
def listar():
    return listar_tarefas()

@app.get("/tarefas/{tarefa_id}", status_code=200, response_model=TarefaId)
def buscar(tarefa_id: int):
    return buscar_tarefa(tarefa_id)
    
@app.patch("/tarefas/{tarefa_id}", status_code=200, response_model=TarefaId)
def atualizar(tarefa_id: int, nova_tarefa: AtualizarTarefa):
   return atualizar_tarefa(tarefa_id, nova_tarefa)

@app.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar(tarefa_id: int):
    return deletar_tarefa(tarefa_id)
