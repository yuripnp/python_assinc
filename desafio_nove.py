import asyncio

async def produtor(futuro):
    print("Produtor: iniciando processamento...")
    await asyncio.sleep(2)  # Simula trabalho demorado
    resultado = "Dado processado!"
    futuro.set_result(resultado)  # Preenche o Future
    print("Produtor: resultado definido no Future.")

async def consumidor(futuro):
    print("Consumidor: aguardando resultado do produtor...")
    resultado = await futuro  # Espera até o Future ser preenchido
    print(f"Consumidor: recebeu resultado -> {resultado}")

async def main():
    loop = asyncio.get_running_loop()
    futuro = loop.create_future()  # Cria um Future vazio

    # Inicia produtor e consumidor simultaneamente
    await asyncio.gather(
        produtor(futuro),
        consumidor(futuro)
    )

if __name__ == "__main__":
    asyncio.run(main())