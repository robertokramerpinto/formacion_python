import asyncio

async def get_data():
    print("Start data extraction")
    await asyncio.sleep(5)
    print("Data Extracted")
    return [1,2,3,4]

async def print_range(x):
    for n in range(x):
        print(f"Range value: {n}")
        await asyncio.sleep(1)

# Crear una main funcion para gestionar las tasks - coroutines
async def main():
    task_1 = asyncio.create_task(get_data())
    task_2 = asyncio.create_task(print_range(10))

    extracted_data = await task_1
    print(f"Extracted data: {extracted_data}")
    await task_2

asyncio.run(main())