# Aqui você pode plugar CRM, banco de dados ou integrações externas
# Exemplo: salvar logs de conversas no MongoDB

def salvar_interacao(usuario: str, mensagem: str, resposta: str):
    print(f"[LOG] {usuario}: {mensagem} -> BOT: {resposta}")
    # Aqui poderia ser um insert no banco
    # db.insert({"usuario": usuario, "mensagem": mensagem, "resposta": resposta})
