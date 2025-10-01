def chatbot_response(message: str) -> str:
    """Simples lógica do chatbot"""
    if "oi" in message.lower() or "olá" in message.lower():
        return "Olá! Como posso te ajudar hoje?"
    elif "cadastro" in message.lower():
        return "Beleza! Me diga seu nome, email e telefone."
    elif "tchau" in message.lower():
        return "Até mais! Foi bom conversar com você."
    else:
        return "Desculpe, não entendi. Pode repetir?"
