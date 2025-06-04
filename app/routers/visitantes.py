from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/visitantes",
    tags=["Visitantes"],
    responses={404: {"description": "Visitante não encontrado"}},
)

@router.post("/", response_model=schemas.Visitante, status_code=status.HTTP_201_CREATED)
def create_visitante(visitante: schemas.VisitanteCreate, db: Session = Depends(get_db)):
    db_visitante = crud.get_visitante_by_documento(db, documento=visitante.documento)
    if db_visitante:
        raise HTTPException(status_code=400, detail="Visitante com este documento já cadastrado")
    return crud.create_visitante(db=db, visitante=visitante)

@router.get("/", response_model=List[schemas.Visitante])
def read_visitantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    visitantes = crud.get_visitantes(db, skip=skip, limit=limit)
    return visitantes

@router.get("/{visitante_id}", response_model=schemas.Visitante)
def read_visitante(visitante_id: int, db: Session = Depends(get_db)):
    db_visitante = crud.get_visitante(db, visitante_id=visitante_id)
    if db_visitante is None:
        raise HTTPException(status_code=404, detail="Visitante não encontrado")
    return db_visitante

@router.put("/{visitante_id}", response_model=schemas.Visitante)
def update_visitante(visitante_id: int, visitante: schemas.VisitanteUpdate, db: Session = Depends(get_db)):
    db_visitante = crud.update_visitante(db, visitante_id, visitante)
    if db_visitante is None:
        raise HTTPException(status_code=404, detail="Visitante não encontrado")
    return db_visitante

@router.delete("/{visitante_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_visitante(visitante_id: int, db: Session = Depends(get_db)):
    success = crud.delete_visitante(db, visitante_id)
    if not success:
        raise HTTPException(status_code=404, detail="Visitante não encontrado")
    return {"message": "Visitante deletado com sucesso"}