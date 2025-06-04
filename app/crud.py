from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from datetime import datetime

def get_visitante(db: Session, visitante_id: int):
    return db.query(models.Visitante).filter(models.Visitante.id == visitante_id).first()

def get_visitante_by_documento(db: Session, documento: str):
    return db.query(models.Visitante).filter(models.Visitante.documento == documento).first()

def get_visitantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Visitante).offset(skip).limit(limit).all()

def create_visitante(db: Session, visitante: schemas.VisitanteCreate):
    db_visitante = models.Visitante(
        nome=visitante.nome,
        documento=visitante.documento,
        telefone=visitante.telefone
    )
    db.add(db_visitante)
    db.commit()
    db.refresh(db_visitante)
    return db_visitante

def update_visitante(db: Session, visitante_id: int, visitante: schemas.VisitanteUpdate):
    db_visitante = db.query(models.Visitante).filter(models.Visitante.id == visitante_id).first()
    if db_visitante:
        for var, value in vars(visitante).items():
            setattr(db_visitante, var, value) if value else None
        db.add(db_visitante)
        db.commit()
        db.refresh(db_visitante)
    return db_visitante

def delete_visitante(db: Session, visitante_id: int):
    db_visitante = db.query(models.Visitante).filter(models.Visitante.id == visitante_id).first()
    if db_visitante:
        db.delete(db_visitante)
        db.commit()
        return True
    return False

def get_condominio(db: Session, condominio_id: int):
    return db.query(models.Condominio).filter(models.Condominio.id == condominio_id).first()

def get_condominios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Condominio).offset(skip).limit(limit).all()

def create_condominio(db: Session, condominio: schemas.CondominioCreate):
    db_condominio = models.Condominio(
        nome=condominio.nome,
        endereco=condominio.endereco
    )
    db.add(db_condominio)
    db.commit()
    db.refresh(db_condominio)
    return db_condominio

def get_unidade(db: Session, unidade_id: int):
    return db.query(models.Unidade).filter(models.Unidade.id == unidade_id).first()

def get_unidades_por_condominio(db: Session, condominio_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Unidade).filter(models.Unidade.condominio_id == condominio_id).offset(skip).limit(limit).all()

def get_todas_unidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unidade).offset(skip).limit(limit).all()

def create_unidade(db: Session, unidade: schemas.UnidadeCreate):
    db_unidade = models.Unidade(
        numero=unidade.numero,
        bloco=unidade.bloco,
        condominio_id=unidade.condominio_id
    )
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade

def get_movimentacao(db: Session, movimentacao_id: int):
    return db.query(models.Movimentacao).filter(models.Movimentacao.id == movimentacao_id).first()

def get_movimentacoes_por_unidade(db: Session, unidade_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Movimentacao).filter(models.Movimentacao.unidade_id == unidade_id).offset(skip).limit(limit).all()

def create_movimentacao_entrada(db: Session, movimentacao: schemas.MovimentacaoCreate):
    
    mov_ativa = db.query(models.Movimentacao).filter(
        models.Movimentacao.visitante_id == movimentacao.visitante_id,
        models.Movimentacao.unidade_id == movimentacao.unidade_id,
        models.Movimentacao.ativa == True
    ).first()
    if mov_ativa:
        return None 

    db_movimentacao = models.Movimentacao(
        visitante_id=movimentacao.visitante_id,
        unidade_id=movimentacao.unidade_id,
        observacoes=movimentacao.observacoes,
        data_hora_entrada=datetime.now(),
        ativa=True
    )
    db.add(db_movimentacao)
    db.commit()
    db.refresh(db_movimentacao)
    return db_movimentacao

def update_movimentacao_saida(db: Session, movimentacao_id: int):
    db_movimentacao = db.query(models.Movimentacao).filter(models.Movimentacao.id == movimentacao_id).first()
    if db_movimentacao and db_movimentacao.ativa:
        db_movimentacao.data_hora_saida = datetime.now()
        db_movimentacao.ativa = False
        db.add(db_movimentacao)
        db.commit()
        db.refresh(db_movimentacao)
        return db_movimentacao
    return None 

def get_condominios_com_unidades(db: Session):
    return db.query(models.Condominio).options(
        relationship.load_only(models.Condominio.id, models.Condominio.nome),
        relationship.contains_eager(models.Condominio.unidades)
    ).join(models.Unidade).all()
    
def create_initial_data(db: Session):
    if not db.query(models.Condominio).first():
        condominio1 = models.Condominio(nome="Condomínio Alpha", endereco="Rua A, 100")
        condominio2 = models.Condominio(nome="Condomínio Beta", endereco="Avenida B, 200")
        db.add_all([condominio1, condominio2])
        db.commit()
        db.refresh(condominio1)
        db.refresh(condominio2)

        unidade1_alpha = models.Unidade(numero="101", bloco="A", condominio_id=condominio1.id)
        unidade2_alpha = models.Unidade(numero="102", bloco="A", condominio_id=condominio1.id)
        unidade1_beta = models.Unidade(numero="201", bloco="B", condominio_id=condominio2.id)
        db.add_all([unidade1_alpha, unidade2_alpha, unidade1_beta])
        db.commit()
        db.refresh(unidade1_alpha)
        db.refresh(unidade2_alpha)
        db.refresh(unidade1_beta)

        visitante1 = models.Visitante(nome="Carlos Souza", documento="111.222.333-44", telefone="98765-4321")
        visitante2 = models.Visitante(nome="Maria Oliveira", documento="555.666.777-88", telefone="12345-6789")
        db.add_all([visitante1, visitante2])
        db.commit()
        db.refresh(visitante1)
        db.refresh(visitante2)