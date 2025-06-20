# Projeto FastAPI - Seção 04

Este projeto demonstra o uso do FastAPI com SQLAlchemy assíncrono, organização de módulos e conexão com banco de dados PostgreSQL.

## Estrutura

- `main.py`: Arquivo principal da aplicação FastAPI.
- `criar_tabelas.py`: Script para criação das tabelas no banco de dados.
- `core/`: Configurações, conexão com banco e dependências.
- `models/`: Modelos ORM das tabelas do banco.
- `schemas/`: Schemas Pydantic para validação de dados.
- `requirements.txt`: Dependências do projeto.

## Como rodar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

2. Configure o banco de dados PostgreSQL conforme a string em `core/configs.py`.

3. Crie as tabelas:
   ```sh
   python criar_tabelas.py
   ```

4. Inicie o servidor FastAPI:
   ```sh
   uvicorn main:app --reload
   ```

Acesse a documentação automática em [http://localhost:8000/docs](http://localhost:8000/docs).

---

> Projeto de estudos baseado no
