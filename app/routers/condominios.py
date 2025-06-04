from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/condominios",
    tags=["Condomínios e Unidades"],
    responses={404: {"description": "Condomínio não encontrado"}},
)


@router.post(
    "/", response_model=schemas.Condominio, status_code=status.HTTP_201_CREATED
)
def create_condominio(
    condominio: schemas.CondominioCreate, db: Session = Depends(get_db)
):
    return crud.create_condominio(db=db, condominio=condominio)


@router.get("/", response_model=List[schemas.Condominio])
def read_condominios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    condominios = crud.get_condominios(db, skip=skip, limit=limit)
    return condominios


@router.get("/{condominio_id}", response_model=schemas.Condominio)
def read_condominio(condominio_id: int, db: Session = Depends(get_db)):
    db_condominio = crud.get_condominio(db, condominio_id=condominio_id)
    if db_condominio is None:
        raise HTTPException(status_code=404, detail="Condomínio não encontrado")
    return db_condominio


@router.get("/{condominio_id}/unidades", response_model=List[schemas.Unidade])
def read_unidades_por_condominio(
    condominio_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    unidades = crud.get_unidades_por_condominio(
        db, condominio_id=condominio_id, skip=skip, limit=limit
    )
    if not unidades:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma unidade encontrada para este condomínio ou condomínio inexistente",
        )
    return unidades


@router.post(
    "/{condominio_id}/unidades/",
    response_model=schemas.Unidade,
    status_code=status.HTTP_201_CREATED,
)
def create_unidade_para_condominio(
    condominio_id: int, unidade: schemas.UnidadeCreate, db: Session = Depends(get_db)
):
    if unidade.condominio_id != condominio_id:
        raise HTTPException(
            status_code=400,
            detail="ID do condomínio na URL e no corpo da requisição não correspondem.",
        )
    db_condominio = crud.get_condominio(db, condominio_id=condominio_id)
    if db_condominio is None:
        raise HTTPException(status_code=404, detail="Condomínio não encontrado")
    return crud.create_unidade(db=db, unidade=unidade)


@router.get("/relacao/unidades", response_model=List[schemas.Condominio])
def get_condominios_com_unidades(db: Session = Depends(get_db)):

    condominios_com_unidades = db.query(models.Condominio).all()

    for condominio in condominios_com_unidades:
        condominio.unidades
    return condominios_com_unidades
