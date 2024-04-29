import time
import random


def eratosthenes(n):
    primes = []
    non_primes = set()
    for i in range(2, n + 1):
        if i not in non_primes:
            primes.append(i)
            non_primes.update(range(i * i, n + 1, i))
    return primes


def count_primes_in_list(numbers, primes):
    count = 0
    for num in numbers:
        if num in primes:
            count += 1
    return count


if __name__ == "__main__":
    n = 1000000
    numbers = [random.randint(2, 9999) for _ in range(n)]

    start_time = time.time()

    primes = set(eratosthenes(max(numbers)))
    prime_count = count_primes_in_list(numbers, primes)

    end_time = time.time()

    print(f"Кількість простих чисел у списку: {prime_count}")
    print(f"Час виконання: {end_time - start_time} секунд")

