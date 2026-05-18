from fastapi import APIRouter

from schemas import Tarefa, TarefaId, AtualizarTarefa
from services import criar_tarefa, listar_tarefas, buscar_tarefa, atualizar_tarefa, deletar_tarefa

router = APIRouter()

@router.get("/")
def raiz():
    return {"message": "API criada com sucesso"}

@router.post("/tarefas", status_code=201, response_model=TarefaId)
def criar(tarefa: Tarefa):
    return criar_tarefa(tarefa)

@router.get("/tarefas", status_code=200, response_model=list[TarefaId])
def listar():
    return listar_tarefas()

@router.get("/tarefas/{tarefa_id}", status_code=200, response_model=TarefaId)
def buscar(tarefa_id: int):
    return buscar_tarefa(tarefa_id)
    
@router.patch("/tarefas/{tarefa_id}", status_code=200, response_model=TarefaId)
def atualizar(tarefa_id: int, nova_tarefa: AtualizarTarefa):
   return atualizar_tarefa(tarefa_id, nova_tarefa)

@router.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar(tarefa_id: int):
    return deletar_tarefa(tarefa_id)