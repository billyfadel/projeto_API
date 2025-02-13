from fastapi import APIRouter, Depends
from app.models.feedback import Feedback
from app.services.gemini_service import GeminiService

router = APIRouter(prefix="/feedback")

async def get_gemini_service():
    # Configurar a API KEY do Google Gemini
    api_key = "AIzaSyAfSlMBINrNi1Ut5_fb5PcHMSZ2T0Gih4s"
    return GeminiService(api_key)

@router.post("/", response_model=str)
async def analisar_feedback(
    feedback: Feedback, gemini_service: GeminiService = Depends(get_gemini_service)
):
    polaridade = await gemini_service.analisar_sentimento(feedback)

    if polaridade == "positivo":
        return (
            "É uma grande satisfação saber que sua experiência foi positiva! "
            "Gostaria de sugerir algo a mais para melhorarmos cada vez mais o nosso serviço? "
            "Agradecemos a sua participação. Tenha um dia agradável!"
        )
    elif polaridade == "negativo":
        return (
            "Nos entristece saber que sua experiência não foi positiva. "
            "Sua reclamação será registrada, de forma anônima, e tomaremos as providências. "
            "Agradecemos a sua participação. Tenha um bom dia!"
        )
    else:
        return (
            "Agradecemos seu feedback! "
            "Estamos sempre buscando melhorar nossos serviços. "
            "Tenha um bom dia!"
        )

@router.post("/aprimoramento", response_model=str)
async def gerar_aprimoramento(
    feedback: Feedback, gemini_service: GeminiService = Depends(get_gemini_service)
):
    return await gemini_service.gerar_texto(feedback)