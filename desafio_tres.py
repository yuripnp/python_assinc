"crie um programa que calcule um fatorial de um numero"

import asyncio
from concurrent.futures import ThreadPoolExecutor
from math import factorial

# Função síncrona para calcular o fatorial
def calcular_fatorial(n):
    return n, factorial(n)

# Função assíncrona para rodar o cálculo em thread separada
async def calcular_fatorial_async(executor, n):
    loop = asyncio.get_running_loop() #pega o loop de execução
    return await loop.run_in_executor(executor, calcular_fatorial, n) #executa a função calcular_fatorial em uma thread separada

async def main():
    numeros = [7, 3, 5, 10, 2]  # Cinco números diferentes
    resultados = []
    with ThreadPoolExecutor() as executor: #cria um pool de threads
        # Dispara todos os cálculos em paralelo
        tarefas = [calcular_fatorial_async(executor, n) for n in numeros]
        for coro in asyncio.as_completed(tarefas):
            resultado = await coro
            resultados.append(resultado)
    # Ordena os resultados pelo número
    resultados.sort(key=lambda x: x[0])
    for n, fat in resultados:
        print(f"Fatorial de {n} = {fat}")

if __name__ == "__main__":
    asyncio.run(main())