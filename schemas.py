# schemas.py
from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float    
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
     
class Config:
    from_attributes = True

class JogosBase(BaseModel):
    titulo: str
    genero: str    
    ano_lancamento: int
    preco: float    
    produtora: str

class JogosCreate(JogosBase):
    pass

class JogosResponse(JogosBase):
    id: int
     
class Config:
    from_attributes = True