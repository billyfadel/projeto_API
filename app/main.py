import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

from app.api.v1.feedback import router as feedback_router

app = FastAPI(
    title="SatClin API",
    description="API para análise de sentimento e geração de texto com Google Gemini.",
    version="1.0.0",
)
# Inclui os endpoints do feedback
app.include_router(feedback_router, prefix="/api/v1/feedback")

@app.get("/")
async def SatClin():
    return {"SatClin": "Esta ON"}
# Importação dos endpoints
from app.api.v1.feedback import router as feedback_router

app.include_router(feedback_router, prefix="/api/v1")
