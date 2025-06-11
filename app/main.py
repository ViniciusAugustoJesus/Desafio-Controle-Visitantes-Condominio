from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models, crud
from .routers import visitantes, condominios, controle_acesso

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Controle de Entrada e Saída de Visitantes em Condomínios",
    description="API RESTful para gerenciar o fluxo de entrada e saída de visitantes em condomínios.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(visitantes.router)
app.include_router(condominios.router)
app.include_router(controle_acesso.router)

@app.on_event("startup")
def on_startup():
    db = next(get_db())
    crud.create_initial_data(db)
    db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Controle de Visitantes!"}