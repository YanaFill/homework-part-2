import threading


def process_file(filename: str, key: bool):
    with open(filename + ".txt", 'w') as file:
        str_nums = ""
        list_nums = []
        if key:
            for number in list_numbers:
                if number % 2 == 0:
                    str_nums += f"{number} "
                    list_nums.append(number)
            file.write(str_nums)
            print(f"Кількість парних чисел: {len(list_nums)}")
        else:
            for number in list_numbers:
                if number % 2 == 1:
                    str_nums += f"{number} "
                    list_nums.append(number)
            file.write(str_nums)
            print(f"Кількість непарних чисел: {len(list_nums)}")


user_filename = input("Введіть шлях до файлу: ")
with open(user_filename, "r") as file:
    list_numbers = [int(num) for num in file.read().split(" ")]

    even_thread = threading.Thread(target=process_file, args=("even_numbers", True))
    odd_thread = threading.Thread(target=process_file, args=("odd_numbers", False))
    even_thread.start()
    odd_thread.start()
    even_thread.join()
    odd_thread.join()
