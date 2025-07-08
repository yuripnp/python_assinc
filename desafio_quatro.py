"crie um programa que envie uma mensagem para três usuarios de forma simultanea respeitando a prioridade de cada usuario"

import asyncio

usuarios = [
    {"nome": "Ana", "prioridade": "VIP", "notificacoes_ativadas": True},
    {"nome": "Pedro", "prioridade": "COMUN", "notificacoes_ativadas": True},
    {"nome": "Joao", "prioridade": "VIP", "notificacoes_ativadas": False}
]
async def enviar_notificacao(usuario):
    if not usuario["notificacoes_ativadas"]:
        print(f"Usuario {usuario['nome']} não tem notificações ativadas")
        return
    if usuario["prioridade"] == "VIP":
        print(f"Enviando notificação para {usuario['nome']} com prioridade VIP")
        await asyncio.sleep(1)
    print(f"Notificação enviada para usuario normal {usuario['nome']}")

async def main():
    print(f"Enviando as notificações...")
    tarefas = [asyncio.create_task(enviar_notificacao(usuario)) for usuario in usuarios]
    await asyncio.gather(*tarefas)

asyncio.run(main())


