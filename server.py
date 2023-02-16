import socket
import threading

# set up the server
host = 'localhost'
port = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(2)
print("Waiting for connections...")

# list of clients
clients = []

# thread function to handle a client connection
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    clients.append(client_socket)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # broadcast the data to all connected clients
        for c in clients:
            if c != client_socket:
                c.send(data)
    print(f"Connection closed by {client_address}")
    clients.remove(client_socket)
    client_socket.close()

# main server loop
while True:
    client_socket, client_address = server_socket.accept()
    # create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
