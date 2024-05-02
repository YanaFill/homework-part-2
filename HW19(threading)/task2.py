import random
import time

def generate_random_list(n):
  random_list = []
  for _ in range(n):
    random_list.append(random.randint(-20, 20))
  return random_list

def calculate_sum_and_product(random_list):
  sum = 0
  product = 1
  for num in random_list:
    sum += num
    product *= num
  return sum, product

if __name__ == "__main__":
  n = int(input("Введіть розмір списку: "))

  start_time = time.time()
  random_list = generate_random_list(n)
  end_time = time.time()
  generate_time = end_time - start_time
  start_time = time.time()
  sum, product = calculate_sum_and_product(random_list)
  end_time = time.time()
  calculate_time = end_time - start_time
  print(f"Список: {random_list}")
  print(f"Сума: {sum}")
  print(f"Добуток: {product}")
  print(f"Час генерування списку: {generate_time:.2f} секунд")
  print(f"Час обчислення суми та добутку: {calculate_time:.2f} секунд")



