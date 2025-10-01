from fastapi import FastAPI
from .database import Base, engine
from .routers import chatbot, clients

# Cria tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Chatbot API")

# Inclui os módulos de rotas
app.include_router(chatbot.router)
app.include_router(clients.router)

@app.get("/")
def root():
    return {"message": "Chatbot API está rodando!"}
