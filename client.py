import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(('127.0.0.1', 65432))
    print("Connected to server")

    message = "Hello from client"
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024)
    print("Response from server:", response.decode())
except Exception as e:
    print(f"Client error: {e}")
finally:
    client_socket.close()
    print("Client disconnected.")