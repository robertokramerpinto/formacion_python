# Async Hello World
import asyncio

async def hello_async_world():
    print("Hello Async World")
    task = asyncio.create_task(print_value("Calling Coroutine"))
    print("Finished")

async def print_value(x):
    print(f"First print: {x}")
    await asyncio.sleep(5)
    print(f"Second print: {x}")

#asyncio.run(#async function)
asyncio.run(hello_async_world())