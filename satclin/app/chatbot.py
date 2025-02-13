from fastapi import FastAPI, HTTPException
from google.generativeai import text_model
import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


app = FastAPI()

# Configuração da API do Gemini
text_model.configure(api_key="AIzaSyAfSlMBINrNi1Ut5_fb5PcHMSZ2T0Gih4s")

@app.post("/chatbot")
async def chatbot(feedback: str):
    try:
        # Análise de sentimento com Gemini
        prompt = f"Analise o sentimento deste feedback: {feedback}"
        response = text_model.generate_text(prompt)
        sentimento = response.result

        # Lógica de resposta do chatbot (exemplo)
        if "positivo" in sentimento.lower():
            resposta = "É uma grande satisfação saber que sua experiência foi positiva."
        elif "negativo" in sentimento.lower():
            resposta = "Nos entristece saber que sua experiência não foi positiva."
        else:
            resposta = "Agradecemos seu feedback!"

        return {"resposta": resposta, "sentimento": sentimento}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))