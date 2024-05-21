import threading
import time


def server_status():
    while True:
        print("[Server Status]: Running")
        time.sleep(2)

t = threading. Thread(target=server_status)

t.daemon = True

t.start()


def run_server():

    for _ in range(10):
        print("[Server]: Processing data...")
        time. sleep(1)

run_server()
print("Server_shutdown.")