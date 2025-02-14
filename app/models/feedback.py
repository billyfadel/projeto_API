from pydantic import BaseModel

class Feedback(BaseModel):
    texto: str