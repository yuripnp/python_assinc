import asyncio
import random

async def sensor_temperatura():
    while True:
        await asyncio.sleep(2)
        temp = random.randint(20, 30)
        print(f"[{2}s] Temperatura: {temp}°C")

async def sensor_pressao():
    while True:
        await asyncio.sleep(5)
        press = random.randint(50, 70)
        print(f"[{2}s] Temperatura: {press}%")

async def sensor_qualidade_ar():
    while True:
        await asyncio.sleep(1)
        qualidade = random.choice(["Boa", "Ruim", "Mediana"])
        print(f"[{2}s] Temperatura: {qualidade}°C")

async def main():
    await asyncio.gather(sensor_temperatura(), sensor_pressao(), sensor_qualidade_ar())

asyncio.run(main())
