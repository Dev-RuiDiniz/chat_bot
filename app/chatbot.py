from .utils import delay
from .services import salvar_interacao

def processar_mensagem(remetente: str, nome: str, texto: str) -> str:
    """Processa a mensagem recebida e retorna a resposta do bot"""

    resposta = ""

    # Fluxo de atendimento
    if any(word in texto.lower() for word in ["menu", "oi", "ola", "olá", "bom dia", "boa tarde", "boa noite"]):
        resposta = (f"Olá {nome}! Sou o Henrique, assistente virtual da 3D Art & Print.\n"
                    "Como posso ajudá-lo hoje? Digite uma das opções abaixo:\n\n"
                    "1 - Quais produtos possuem?\n"
                    "2 - Como comprar?\n"
                    "3 - Sobre o envio\n"
                    "4 - Sobre o pagamento\n"
                    "5 - Outras perguntas")

    elif texto == "1":
        resposta = ("Fornecemos adesivos, etiquetas VOID, panfletos, lonas, banners, mídia digital e muito mais.\n\n"
                    "Atendimento 100% online e seguro.\n"
                    "Temos ótimos preços e descontos exclusivos!\n\n"
                    "Nosso site: https://sl1nk.com/nGY4n")

    elif texto == "2":
        resposta = ("Me diga qual produto deseja e a quantidade.\n"
                    "Envie também sua logo ou arte.\n"
                    "Se já tiver a arte pronta, me envie e comente que não deseja alteração.\n\n"
                    "Estou aguardando suas informações...")

    elif texto == "3":
        resposta = ("O envio é feito via transportadora.\n"
                    "O frete é calculado após o pedido.\n"
                    "Pagamento deve ser feito antes da produção.\n\n"
                    "Após o pagamento, realizamos o envio.")

    elif texto == "4":
        resposta = ("Entregas em Taubaté são grátis para pedidos acima de R$99.\n"
                    "Prazo de 7 a 15 dias dependendo da localização.\n\n"
                    "Nosso site: https://sl1nk.com/nGY4n")

    elif texto == "5":
        resposta = "Se tiver outras dúvidas, fale aqui ou visite nosso site: https://sl1nk.com/nGY4n"

    else:
        resposta = "Desculpe, não entendi sua mensagem. Digite 'menu' para ver as opções."

    # Salva no log / banco
    salvar_interacao(remetente, texto, resposta)

    return resposta
