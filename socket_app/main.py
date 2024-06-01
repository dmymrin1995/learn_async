import socket
import selectors
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print("Ничего")

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == server_socket:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f"Запрос на подключение {client_address}")
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f"Получены данные: {data}")
            event_socket.send(data)


# connections = []
# event:

# try:
#     try:
#         connections.append(connection)
#     except BlockingIOError:
#         pass

#     for connect in connections:
#         try:
#             buffer = b""

#             while buffer[-2:] != b"\r\n":
#                 data = connection.recv(2)
#                 if not data:
#                     break
#                 else:
#                     print(f"данные получены {data}")
#                     buffer = buffer + data

#             print(f"все данные {buffer.decode('utf-8')}")
#             connection.sendall(buffer)
#         except BlockingIOError:
#             pass


# finally:
#     server_socket.close()
