from typing import Optional

from pydantic import BaseModel, Field

class Tarefa(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None

class TarefaId(Tarefa):
    id: int

class AtualizarTarefa(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None