import asyncio


# awaitable object, é qualquer objeto que pode ser esperado por um await. Existem 3 tipos de awaitable object:
# 1. Corrotinas
# 2. Tasks
# 3. Futures

# Corrotinas são funções que podem ser suspensas e retomadas. Elas são definidas com a palavra-chave async.

async def corrotina(numero):
    print(f"Corrotina {numero} iniciada")
    await asyncio.sleep(2)
    print(f"Corrotina {numero} concluida")


def main():
    asyncio.run(corrotina(1))
    asyncio.run(corrotina(2))

asyncio.run(main())
#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------

# Tasks são corrotinas que são executadas de forma assíncrona. Elas são definidas com a função asyncio.create_task().

async def task(numero):
    print(f"Task {numero} iniciada")
    await asyncio.sleep(2)
    print(f"Task {numero} concluida")

async def main():
    tarefa_um = asyncio.create_task(task(1))
    tarefa_dois = asyncio.create_task(task(2))
    await tarefa_um
    await tarefa_dois
  

asyncio.run(main())
#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------

# Futures são objetos que representam o resultado de uma operação assíncrona. Elas são definidas com a função asyncio.Future().

async def future(numero):
    print(f"Future {numero} iniciada")
    await asyncio.sleep(2)
    print(f"Future {numero} concluida")

async def main():
    futuro = asyncio.Future()
    futuro.set_result(10)
    resultado = await futuro
    print(resultado)

asyncio.run(main())
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
async def main():
    await asyncio.gather(future(1), future(2), future(3))