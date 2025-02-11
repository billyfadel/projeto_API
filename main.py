from fastapi import FastAPI

app = FastAPI()

@app.get("/teste")
def hello_world():
 return {"mensagem": " Deu certo!"}

# Formato 1
# Passando o número 1 e 2 na URL
@app.post("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int=0):
 
 total = numero1 + numero2

 return {"resultado": total}

# Formato 2
# #Passando o número 1 e 2 no corpo da requisição
@app.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
 total = numero1 + numero2
 return {"resultado": total}

# Formato 3
# Passando o número 1 e 2 no corpo da requisição
from pydantic import BaseModel
class Numeros(BaseModel):
 numero1: int
 numero2: int

@app.post("/soma_formato3")
def soma_formato3(numeros: Numeros):
 total = numeros.numero1 + numeros.numero2
 return {"resultado": total}