from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from enum import Enum
from app import chatbot, text_generation # Importa os módulos com as rotas da API

async def app(scope, receive, send):
    ...

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

app = FastAPI(
    title="API SATCLIN ",
    description=description,
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Billy Fádel, Edson Laranjeiras e Samantha Alecrim",
        "url": "http://github.com/Adiely/",
        "email": "samanthaalecrim.biotec@gmail.com",
    },
     license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
# Inclui as rotas dos módulos na API
app.include_router(chatbot.app)
app.include_router(text_generation.app)

# Rota raiz (opcional)
@app.get("/")
async def root():
    return {"message": "Bem-vindo ao SatClin!"}