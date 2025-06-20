from typing import List, Optional

# from fastapi.responses import JSONResponse

from fastapi import Response
from fastapi import Path

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models import Curso

app = FastAPI()

cursos = {
    1: {"titulo": "Programação para Leigos", "aulas": 112, "horas": 58},
    2: {"titulo": "Algoritmos e Lógica de Programação", "aulas": 87, "horas": 67},
    3: {"titulo": "Python Completo", "aulas": 134, "horas": 72},
    4: {"titulo": "Desenvolvimento Web com Django", "aulas": 98, "horas": 64},
    5: {"titulo": "JavaScript Moderno", "aulas": 110, "horas": 70},
    6: {"titulo": "Banco de Dados com SQL", "aulas": 75, "horas": 50},
    7: {"titulo": "Machine Learning para Iniciantes", "aulas": 120, "horas": 80},
    8: {"titulo": "FastAPI na Prática", "aulas": 95, "horas": 60},
    9: {"titulo": "React do Zero ao Avançado", "aulas": 150, "horas": 90},
    10: {"titulo": "Estrutura de Dados e Algoritmos em Python", "aulas": 140, "horas": 85}
}

@app.get('/cursos')
async def get_cursos():
  return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(..., title="ID do curso", description='Deve ser entre 1 e 2', gt=0, lt=3)):
  try:
    curso = cursos[curso_id]
    return curso
  except KeyError:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!")

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
  next_id: int = len(cursos) + 1  
  cursos[next_id] = curso
  del curso.id
  return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
  if curso_id in cursos:
    cursos[curso_id] = curso
    del curso.id

    return cursos
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe com o id {curso_id}'
    )

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
  if curso_id in cursos:
    del cursos[curso_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe com o id {curso_id}'
    )

@app.get('/calculadora')
async def calcular(a: int, b: int, c: Optional[int] = None):
  soma = a+ b + c

  return {"resultado": soma}

if __name__ == "__main__":
  import uvicorn

  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)