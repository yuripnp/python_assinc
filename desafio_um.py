"criando um temporizador assincron"
"""
A função asyncio.gather() no Python é usada quando você deseja executar várias 
corrotinas (coroutines) simultaneamente e aguardar que todas sejam concluídas. 
Ela é uma das principais ferramentas para concorrência em programas assíncronos usando o módulo asyncio.
"""
import asyncio

async def temporizador(tempo):
    print(f"Temporizador iniciado por {tempo} segundos")
    await asyncio.sleep(tempo)
    print(f"Temporizador concluido em {tempo} segundos")


async def main():
    await asyncio.gather(temporizador(1), temporizador(2), temporizador(3))

asyncio.run(main())
