import asyncio

async def tarefa(nome, tempo):
    print(f"Iniciando {nome} (tempo: {tempo}s)")
    await asyncio.sleep(tempo)
    print(f"Finalizando {nome}")

async def main():
    tarefas = [
        tarefa("Tarefa 1", 3),
        tarefa("Tarefa 2", 1),
        tarefa("Tarefa 3", 2),
    ]
    await asyncio.gather(*tarefas)
    print("Todas as tarefas foram concluídas.")

if __name__ == "__main__":
    asyncio.run(main())