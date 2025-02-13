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

@app.post("/text_generation")
async def text_generation(feedback: str):
    try:
        # Geração de texto com Gemini
        prompt = f"Gere um texto para aprimorar os serviços da clínica com base neste feedback: {feedback}"
        response = text_model.generate_text(prompt)
        texto_gerado = response.result

        return {"texto_gerado": texto_gerado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))