import asyncio
from time import perf_counter


async def take_order(order_id):
    print(f"Taking order {order_id}...")
    await asyncio.sleep(2)
    print(f"Order {order_id} taken!")


async def make_coffee(order_id):
    print(f"Making coffee for order {order_id}...")
    await asyncio.sleep(3)
    print(f"Coffee for order {order_id} is ready!")


async def make_sandwich(order_id):
    print(f"Making sandwich for order {order_id}...")
    await asyncio.sleep(4)
    print(f"Sandwich for order {order_id} is ready!")


async def serve_order(order_id):
    print(f"Serving order {order_id}...")
    await asyncio.sleep(1)
    print(f"Order {order_id} served!")


async def process_order(order_id):
    await take_order(order_id)
    await make_coffee(order_id)
    await make_sandwich(order_id)
    await serve_order(order_id)

start_time = perf_counter()


async def main():
    orders = [1, 2, 3]
    tasks = [process_order(order_id) for order_id in orders]
    await asyncio.gather(*tasks)
    print("All orders have been processed!")

asyncio.run(main())

end_time = perf_counter()

print(f"Time for work: {end_time - start_time: 0.4f} sec")