"""
crie um programa que
1 - verifique se o pagamento foi aprovado
2 - se o pagamento foi aprovado, verifique se tem estoque disponivel
3 - somente se ouver estoque disponivel, envie mensagem de envio com sucesso
4 - se não tiver estoque disponivel ou não tiver pagamento aprovado, envie mensagem de falha
"""

import asyncio

# massa de dados
pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def processar_pagamento(pedido):
    await asyncio.sleep(1)
    if pedido['pagamento_aprovado']:
        print(f"Pagamento aprovado para {pedido['id']}")
        return True
    else:
        print(f"Pagamento recusado para pedido {pedido['id']}")
        return False

async def processa_estoque(pedido):
    await asyncio.sleep(1)
    if pedido['estoque_disponivel']:
        print(f"Pedido disponivel em estoque {pedido['id']}")
        return True
    else:
        print(f"Produto indisponivel do pedido {pedido['id']}")
        return False
    

    

async def processar_pedido(pedido):
    print(f"Processando pedido {pedido['id']}")
    pagamento = await processar_pagamento(pedido)
    if  not  pagamento:
        return
    estoque =  await processa_estoque(pedido)
    if not estoque:
        return
    print(f"processo terminado do pedido {pedido['id']}")


async def main():
    processos = [asyncio.create_task(processar_pedido(pedido)) for pedido in pedidos]
    await asyncio.gather(*processos)

asyncio.run(main())

        

