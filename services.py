from fastapi import HTTPException

from storage import cont_id, tarefas
from schemas import Tarefa, TarefaId, AtualizarTarefa

def criar_tarefa(tarefa: Tarefa):
    global cont_id
    cont_id += 1
    tarefa_id = TarefaId(id=cont_id, title=tarefa.title, description=tarefa.description)
    tarefas.append(tarefa_id)
    return tarefa_id

def buscar_tarefa(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            return tarefa
    raise HTTPException(
        status_code=404,
        detail= "Tarefa não encontrada"
    )

def atualizar_tarefa(tarefa_id: int, nova_tarefa: AtualizarTarefa):
    tarefa = buscar_tarefa(tarefa_id)
    if nova_tarefa.title is not None:
        if nova_tarefa.title.strip() != "":
            tarefa.title = nova_tarefa.title
    if nova_tarefa.description is not None:
        tarefa.description = nova_tarefa.description
    return nova_tarefa

def deletar_tarefa(tarefa_id: int):
    tarefa = buscar_tarefa(tarefa_id)
    tarefas.remove(tarefa)
    return