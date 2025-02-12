from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from enum import Enum

class NomeGrupo(str, Enum):
    operacoes = "Operações matemáticas simples enum"
    teste = "Teste"

description = f"""
    API desenvolvida durante a aula 2 (bloco c), contendo endpoints de exemplo e soma"

    - /teste: retorna uma mensagem de sucesso
    - /soma/numero1/numero2: recebe dois números e retorna a soma
"""

app = FastAPI(
    title="API do ",
    description=description,
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Samantha Adiely Alecrim",
        "url": "http://github.com/Adiely/",
        "email": "samanthaalecrim.biotec@gmail.com",
    },
     license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/teste", 
         summary="Retorna mensagem de teste", 
         description="Retorna uma mensagem de exemplo para testar e verificar se deu certo",
         tags=[NomeGrupo.teste])

def hello_world():
    return {"mensagem": "Deu certo"}

API_TOKEN = 123

# Criando um endpoint para receber dois números e retornar a soma
# Formato 1
# Passando o número 1 e 2 na URL
@app.post("/soma/{numero1}/{numero2}/{api_token}", tags=[NomeGrupo.operacoes])
def soma(numero1: int, numero2: int, api_token: int):
    
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="API Token inválido")
    
    if numero1 < 0 or numero2 < 0:
        raise HTTPException(status_code=400, detail="Não é permitido números negativos")
    
    total = numero1 + numero2
    
    if total < 0:
        raise HTTPException(status_code=400, detail="Resultado negativo")
    
    return {"resultado": total, "warning": "Esta versão será descontinuada em 30 dias"}

# Formato 2: passando o número 1 e 2 no corpo da requisição
@app.post("/soma/v2", tags=[NomeGrupo.operacoes])
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

# Formato 3: passando o número 1 e 2 no corpo da requisição

class Numeros(BaseModel):
 numero1: int
 numero2: int
 numero3: int = 0

class Resultado(BaseModel):
    resultado: int

@app.post("/soma/v3", response_model=Resultado, tags=[NomeGrupo.operacoes], status_code=status.HTTP_200_OK)
def soma_formato3(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2 + numeros.numero3
    return {"resultado": total}

def checar_creditos(id_usuario: int):
    return False

@app.post("/divisao/{numero1}/{numero2}", tags=[NomeGrupo.operacoes])
def divisao(numero1: int, numero2: int):
    
    if numero2 == 0:
        raise HTTPException(status_code=400, detail="Não é permitido divisão por zero")
        
    total = numero1 / numero2
    
    return {"resultado": total}

class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"

@app.post("/operacao", tags=[NomeGrupo.operacoes])
def operacao(numero: Numeros, tipo: TipoOperacao):
    
    if tipo == TipoOperacao.soma:
        total = numero.numero1 + numero.numero2
    
    elif tipo == TipoOperacao.subtracao:
        total = numero.numero1 - numero.numero2
    
    elif tipo == TipoOperacao.multiplicacao:
        total = numero.numero1 * numero.numero2
    
    elif tipo == TipoOperacao.divisao:
        total = numero.numero1 / numero.numero2
    
    return {"resultado": total}