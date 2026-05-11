from fastapi import FastAPI, HTTPException

from storage import tarefas, cont_id
from schemas import Tarefa, TarefaId, AtualizarTarefa

app = FastAPI()

@app.get("/")
def teste():
    return "API criada com sucesso"

@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    global cont_id
    cont_id += 1
    tarefa_id = TarefaId(id=cont_id, title=tarefa.title, description=tarefa.description)
    tarefas.append(tarefa_id)
    return tarefa_id

def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
    raise HTTPException(
        status_code=404,
        detail= "Tarefa não encontrada"
    )

@app.get("/tarefas", status_code=200)
def ver_tarefas():
    return tarefas

@app.get("/tarefas/{id}", status_code=200)
def ver_tarefa_id(id: int):
    return buscar_tarefa(id)

        
@app.patch("/tarefas/{id}", status_code=200)
def atualizar_tarefa(id: int, nova_tarefa: AtualizarTarefa):
    tarefa = buscar_tarefa(id)
    if nova_tarefa.title is not None:
        if nova_tarefa.title.strip() != "":
            tarefa.title = nova_tarefa.title
    if nova_tarefa.description is not None:
        tarefa.description = nova_tarefa.description
    return nova_tarefa

@app.delete("/tarefas/{id}", status_code=204)
def deletar_tarefa(id: int):
    tarefa = buscar_tarefa(id)
    tarefas.remove(tarefa)
    return {"message": f"deleted successfully"}
