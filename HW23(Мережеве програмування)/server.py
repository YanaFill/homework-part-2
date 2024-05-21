import socket
from datetime import datetime
import time

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Сервер запущено. Очікування підключення...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Підключення від {addr}")

        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data or data.lower() == 'exit':
                    print("Клієнт завершив з'єднання")
                    break
                print(f"Отримано: {data}")
                print(f"Час отримання: {datetime.now()}")
                time.sleep(5)
                sent = client_socket.send(data.encode())
                if sent == len(data):
                    print("Відповідь успішно відправлена")
        except ConnectionResetError:
            print("З'єднання було перервано клієнтом")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
