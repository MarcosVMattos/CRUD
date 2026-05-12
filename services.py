from storage import cont_id, tarefas
from schemas import Tarefa, TarefaId, AtualizarTarefa

def criar_tarefa(tarefa: Tarefa):
    global cont_id
    cont_id += 1
    tarefa_id = TarefaId(id=cont_id, title=tarefa.title, description=tarefa.description)
    tarefas.append(tarefa_id)
    return tarefa_id
