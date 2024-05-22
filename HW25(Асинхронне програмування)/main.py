import asyncio
from time import perf_counter


async def util(limit):
    for i in range(limit + 1):
        print(i)
        await asyncio.sleep(1)



async def main():
    start_time = perf_counter()
    counter1 = asyncio.create_task(util(10))
    counter2 = asyncio.create_task(util(20))

    await counter1
    await counter2
    print(f"Time of work: {perf_counter() - start_time:.2f} sec")


asyncio.run(main())

