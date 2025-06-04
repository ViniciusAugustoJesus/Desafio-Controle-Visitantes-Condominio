from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/controle-acesso",
    tags=["Controle de Acesso"],
    responses={404: {"description": "Movimentação não encontrada"}},
)

@router.post("/entrada", response_model=schemas.Movimentacao, status_code=status.HTTP_201_CREATED)
def liberar_entrada_visitante(movimentacao: schemas.MovimentacaoCreate, db: Session = Depends(get_db)):
    db_visitante = crud.get_visitante(db, movimentacao.visitante_id)
    if not db_visitante:
        raise HTTPException(status_code=404, detail="Visitante não encontrado")

    db_unidade = crud.get_unidade(db, movimentacao.unidade_id)
    if not db_unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")

    db_movimentacao = crud.create_movimentacao_entrada(db=db, movimentacao=movimentacao)
    if db_movimentacao is None:
        raise HTTPException(status_code=400, detail="Já existe uma entrada ativa para este visitante nesta unidade.")
    return db_movimentacao

@router.put("/saida/{movimentacao_id}", response_model=schemas.Movimentacao)
def realizar_baixa_saida_visitante(movimentacao_id: int, db: Session = Depends(get_db)):
    db_movimentacao = crud.update_movimentacao_saida(db, movimentacao_id)
    if db_movimentacao is None:
        raise HTTPException(status_code=404, detail="Movimentação não encontrada ou já finalizada.")
    return db_movimentacao

@router.get("/unidades/{unidade_id}/movimentacoes", response_model=List[schemas.Movimentacao])
def listar_movimentacoes_por_unidade(unidade_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_unidade = crud.get_unidade(db, unidade_id)
    if not db_unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")
    movimentacoes = crud.get_movimentacoes_por_unidade(db, unidade_id=unidade_id, skip=skip, limit=limit)
    return movimentacoes