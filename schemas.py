from typing import Optional

from pydantic import BaseModel, Field

class Tarefa(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None

class TarefaId(Tarefa):
    id: int

class AtualizarTarefa(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    description: Optional[str] = None
