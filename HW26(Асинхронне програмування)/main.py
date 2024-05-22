import time
from time import perf_counter

def take_order(order_id):
    print(f"Taking order {order_id}...")
    time.sleep(2)  # Прийом замовлення займає 2 хвилини
    print(f"Order {order_id} taken!")

def make_coffee(order_id):
    print(f"Making coffee for order {order_id}...")
    time.sleep(3)  # Приготування кави займає 3 хвилини
    print(f"Coffee for order {order_id} is ready!")

def make_sandwich(order_id):
    print(f"Making sandwich for order {order_id}...")
    time.sleep(4)  # Приготування сендвіча займає 4 хвилини
    print(f"Sandwich for order {order_id} is ready!")

def serve_order(order_id):
    print(f"Serving order {order_id}...")
    time.sleep(1)  # Подача замовлення займає 1 хвилину
    print(f"Order {order_id} served!")

def process_order(order_id):
    take_order(order_id)
    make_coffee(order_id)
    make_sandwich(order_id)
    serve_order(order_id)

start_time = perf_counter()
def main():
    orders = [1, 2, 3]
    for order_id in orders:
        process_order(order_id)
    print("All orders have been processed!")

# Запускаємо синхронний процес обслуговування клієнтів
main()

end_time = perf_counter()

print(f"Time for work: {end_time - start_time: 0.4f} sec")
