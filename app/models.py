from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Visitante(Base):
    __tablename__ = "visitantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    documento = Column(String, unique=True, index=True)
    telefone = Column(String, nullable=True)
    movimentacoes = relationship("Movimentacao", back_populates="visitante")
    
class Condominio(Base):
    __tablename__ = "condominios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    endereco = Column(String)

    unidades = relationship("Unidade", back_populates="condominio")

class Unidade(Base):
   __tablename__ = "unidades"
   id = Column(Integer, primary_key=True, index=True)
   numero = Column(String, index=True)
   bloco = Column(String, nullable=True)
   condominio_id = Column(Integer, ForeignKey("condominios.id"))

   condominio = relationship("Condominio", back_populates="unidades")
   movimentacoes = relationship("Movimentacao", back_populates="unidade")
    
class Movimentacao(Base):
    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True, index=True)
    visitante_id = Column(Integer, ForeignKey("visitantes.id"))
    unidade_id = Column(Integer, ForeignKey("unidades.id"))
    data_hora_entrada = Column(DateTime, default=datetime.now)
    data_hora_saida = Column(DateTime, nullable=True)
    observacoes = Column(String, nullable=True)
    ativa = Column(Boolean, default=True) # Indica se a movimentação está em aberto (entrada sem saída)

    visitante = relationship("Visitante", back_populates="movimentacoes")
    unidade = relationship("Unidade", back_populates="movimentacoes")