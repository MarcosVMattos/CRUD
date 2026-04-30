# CRUD de tarefas com FastAPI

Uma API para criar, listar, atualizar e deletar tarefas.

## Como rodar o projeto

1. Clone o repositório: 

```bash
git clone https://github.com/MarcosVMattos/CRUD.git
```

2. Entre na pasta do projeto:

```bash
cd CRUD
```

3. Crie o ambiente virtual:

```bash
python -m venv venv
```

4. Ative o ambiente virtual (Windows):

```bash
venv\Scripts\activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

6. Rode o servidor:

```bash
uvicorn main:app --reload
```

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic

## Endpoints

- POST   /tasks      -> Cria uma nova tarefa
- GET    /tasks      -> Lista todas as tarefas
- GET    /tasks/{id} -> Retorna uma tarefa pelo ID
- PUT    /tasks/{id} -> Atualiza uma tarefa pelo ID
- DELETE /tasks/{id} -> Remove uma tarefa pelo ID

## Exemplo de requisição

```json
{
    "title": "Exemplo de título",
    "description": "Exemplo de descrição"
}
```

## Documentação 

A documentação interativa da API está disponível em:

[Acessar documentação](http://127.0.0.1:8000/docs)