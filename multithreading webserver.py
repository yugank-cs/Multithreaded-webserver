import socket
import threading

# Define the server parameters
HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Port to listen on
BUFFER_SIZE = 1024  # Size of the buffer for receiving data

# Function to handle client requests
def handle_client(client_socket, address):
    print(f"Connection from {address} has been established.")

    # Receive data from the client
    request = client_socket.recv(BUFFER_SIZE).decode()
    print(f"Received request from {address}:")
    print(request)

    # Example response
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\nHello, World!"
    client_socket.send(response.encode())

    # Close the connection
    client_socket.close()
    print(f"Connection from {address} has been closed.")

# Main function to start the server
def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server is listening on {HOST}:{PORT}")

    try:
        while True:
            # Accept incoming connection
            client_socket, address = server_socket.accept()

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
        server_socket.close()

if __name__ == "__main__":
    main()
