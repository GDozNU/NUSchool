import socket

# Create and bind socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))
server_socket.listen(1)
print("Server is listening on port 65432...")

try:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received from client:", data.decode())
        conn.sendall(b"Message received")
except Exception as e:
    print(f"Server error: {e}")
finally:
    conn.close()
    server_socket.close()
    print("Server shutdown.")