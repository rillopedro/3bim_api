
from sqlalchemy import Column, Integer, String, Float
from database import Base

class ProdutoDB(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    
class JogosDB(Base):
    __tablename__ = 'jogos'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    ano_lancamento = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    produtora = Column(String(100), nullable=False)
