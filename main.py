from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB, JogosDB
from schemas import ProdutoCreate, ProdutoResponse, JogosCreate, JogosResponse

Base.metadata.create_all(bind=engine) # cria as tabelas, se ainda não existirem
app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins=['*'],
     # em produção, restringir para o domínio real do front-end
     allow_methods=['*'],
     allow_headers=['*'],
)

@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()

@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()    
    db.refresh(novo_produto)
    return novo_produto


# GET /produtos/{id} -> retorna um único produto pelo id

@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto


# DELETE /produtos/{id} -> remove um produto do banco de dados
@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit()

# PUT /produtos/{id} -> atualiza um produto existente no banco
@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db:    Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')

    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade
    db.commit()
    db.refresh(produto)
    return


###JOGOS


@app.get('/jogos', response_model=list[JogosResponse])
def listar_jogos(db: Session = Depends(get_db)):
    return db.query(JogosDB).all()

@app.post('/jogos', response_model=JogosResponse, status_code=201)
def criar_jogo(jogos: JogosCreate, db: Session = Depends(get_db)):
    novo_jogo = JogosDB(**jogos.dict())
    db.add(novo_jogo)
    db.commit()    
    db.refresh(novo_jogo)
    return novo_jogo

# GET /jogos/{id} -> retorna um único produto pelo id

@app.get('/jogos/{jogo_id}', response_model=JogosResponse)
def obter_jogo(jogo_id: int, db: Session = Depends(get_db)):
    jogo = db.query(JogosDB).filter(JogosDB.id == jogo_id).first()
    if jogo is None:
        raise HTTPException(status_code=404, detail='Jogo não encontrado')
    return jogo

# DELETE /jogos/{id} -> remove um produto do banco de dados
@app.delete('/jogos/{jogo_id}', status_code=204)
def remover_jogo(jogo_id: int, db: Session = Depends(get_db)):
    jogo = db.query(JogosDB).filter(JogosDB.id == jogo_id).first()
    if jogo is None:
        raise HTTPException(status_code=404, detail='Jogo não encontrado')
    db.delete(jogo)
    db.commit()
    
# PUT /jogos/{id} -> atualiza um produto existente no banco
@app.put('/jogos/{jogo_id}', response_model=JogosResponse)
def atualizar_jogo(jogo_id: int, dados: JogosCreate, db:    Session = Depends(get_db)):
    jogo = db.query(JogosDB).filter(JogosDB.id == jogo_id).first()
    if jogo is None:
        raise HTTPException(status_code=404, detail='Jogo não encontrado')

    jogo.titulo = dados.titulo
    jogo.genero = dados.genero
    jogo.preco = dados.preco
    jogo.ano_lancamento = dados.ano_lancamento
    jogo.produtora = dados.produtora
    db.commit()
    db.refresh(jogo)
    return
