"crie um programa que faça duas funções simultaneas, usando o asyncio.gather()"
import asyncio

async def funcao_dowload():
    print("iniciando download")
    await asyncio.sleep(2)
    print("download concluido")

async def funcao_dados():
    print("iniciando analise de dados")
    await asyncio.sleep(2)
    print("analise concluida")

async def main():
    await asyncio.gather(funcao_dowload(), funcao_dados())

asyncio.run(main())