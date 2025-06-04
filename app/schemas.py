from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class VisitanteBase(BaseModel):
    nome: str = Field(..., example="João Silva")
    documento: str = Field(..., example="123.456.789-00")
    telefone: Optional[str] = Field(None, example="(99) 99999-9999")

class VisitanteCreate(VisitanteBase):
    pass

class VisitanteUpdate(VisitanteBase):
    pass

class Visitante(VisitanteBase):
    id: int

    class Config:
        from_attributes = True 

class CondominioBase(BaseModel):
    nome: str = Field(..., example="Condomínio Residencial Sol")
    endereco: str = Field(..., example="Rua das Flores, 123 - Centro")

class CondominioCreate(CondominioBase):
    pass

class Condominio(CondominioBase):
    id: int
    unidades: List["Unidade"] = [] #

    class Config:
        from_attributes = True

class UnidadeBase(BaseModel):
    numero: str = Field(..., example="101")
    bloco: Optional[str] = Field(None, example="A")
    condominio_id: int = Field(..., example=1)

class UnidadeCreate(UnidadeBase):
    pass

class Unidade(UnidadeBase):
    id: int
    condominio: Optional[CondominioBase] = None 
    movimentacoes: List["Movimentacao"] = [] 

    class Config:
        from_attributes = True

class MovimentacaoBase(BaseModel):
    visitante_id: int = Field(..., example=1)
    unidade_id: int = Field(..., example=1)
    observacoes: Optional[str] = Field(None, example="Entrega de encomenda")

class MovimentacaoCreate(MovimentacaoBase):
    pass

class MovimentacaoUpdate(BaseModel):
    data_hora_saida: Optional[datetime] = Field(None, example=datetime.now())
    observacoes: Optional[str] = Field(None, example="Visitante saiu com sucesso.")
    ativa: Optional[bool] = Field(None, example=False)

class Movimentacao(MovimentacaoBase):
    id: int
    data_hora_entrada: datetime
    data_hora_saida: Optional[datetime] = None
    ativa: bool
    visitante: Optional[Visitante] = None 
    unidade: Optional[Unidade] = None 

    class Config:
        from_attributes = True

Unidade.model_rebuild()
Condominio.model_rebuild()
Movimentacao.model_rebuild()