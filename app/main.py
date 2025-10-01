from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Chatbot WhatsApp API", version="1.0.0")

# Inclui rotas
app.include_router(router, prefix="/chatbot", tags=["Chatbot"])

@app.get("/")
def root():
    return {"status": "Chatbot API rodando 🚀"}
