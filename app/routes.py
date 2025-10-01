from fastapi import APIRouter
from pydantic import BaseModel
from .chatbot import processar_mensagem

router = APIRouter()

class Mensagem(BaseModel):
    remetente: str
    nome: str
    texto: str

@router.post("/mensagem")
def receber_mensagem(mensagem: Mensagem):
    resposta = processar_mensagem(mensagem.remetente, mensagem.nome, mensagem.texto)
    return {"resposta": resposta}
