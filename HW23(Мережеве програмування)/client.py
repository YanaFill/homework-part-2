import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    try:
        while True:
            message = input("Введіть повідомлення (або 'exit' для завершення): ")
            client_socket.sendall(message.encode())
            if message.lower() == 'exit':
                break
            data = client_socket.recv(1024).decode()
            print(f"Відповідь від сервера: {data}")
    except ConnectionAbortedError:
        print("З'єднання з сервером було перервано")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
