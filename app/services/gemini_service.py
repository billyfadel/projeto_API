from app.google.gemini import GeminiClient
from app.models.feedback import Feedback

class GeminiService:
    def __init__(self, api_key: str):
        self.client = GeminiClient(api_key=aAIzaSyAfSlMBINrNi1Ut5_fb5PcHMSZ2T0Gih4s)

    async def analisar_sentimento(self, feedback: Feedback) -> str:
        # Implementação da análise de sentimento com Gemini
        # Retorna "positivo", "neutro" ou "negativo"
        pass

    async def gerar_texto(self, feedback: Feedback) -> str:
        # Implementação da geração de texto com Gemini
        pass

    # Implementação da Análise de Sentimento e Geração de Texto com Google Gemini
async def analisar_sentimento(self, feedback: Feedback) -> str:
    response = self.client.analyze_sentiment(feedback.texto)
    sentiment = response.sentiment.category
    if sentiment == "POSITIVE":
        return "positivo"
    elif sentiment == "NEGATIVE":
        return "negativo"
    else:
        return "neutro"

# Implementar o método gerar_texto

async def gerar_texto(self, feedback: Feedback) -> str:
    prompt = f"""
    Com base no feedback do paciente a seguir, gere sugestões para aprimoramento dos serviços de saúde:

    Feedback: {feedback.texto}

    Modelo de Pesquisa de Satisfação do Cliente para Serviços de Saúde:

    Aplicabilidade: Avaliar a qualidade dos serviços médicos e demais atendimentos oferecidos pela clínica (secretaria, marcação de consulta, retorno de consultas e exames, etc.).

    Métricas: CSAT (Customer Satisfaction Score), NPS (Net Promoter Score), (Net Effort Score).

    KPIs: Taxa de satisfação, Feedbacks Positivos vs. Negativos, Taxa de Esforço do Cliente, Identificação de Pontos de Fricção, Tempo Médio de Resolução, Taxa de Problemas Resolvidos, Avaliação da Experiência do Cliente.

    Modelo de Pesquisa:

    Pergunta CSAT - Em uma escala de 1 a 7, qual é sua satisfação com o atendimento médico que recebeu?

    Pergunta NPS - Em uma escala de 0 a 10, o quanto você recomendaria esta clínica a um amigo ou familiar?

    Pergunta NES¹ - Compartilhe qualquer preocupação ou sugestão que você tenha sobre nossos serviços.

    Pergunta NES²: Você encontrou algum desafio significativo durante seu processo de interação conosco?

    Pergunta NES³: Que sugestões você tem para tornar nosso serviço mais fácil de usar?
    """
    response = self.client.generate_text(prompt=prompt)
    return response.text
    pass