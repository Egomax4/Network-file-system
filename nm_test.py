import socket
import struct
import threading

# Constants for commands
CMD_READ = 1
CMD_WRITE = 2

# Function to register a storage server
def register_storage_server(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        connection_type = 'S'
        s.send(connection_type.encode())
        # Example storage server details (modify as needed)
        ss_details = struct.pack('!4sI', socket.inet_aton(ip), port)
        s.send(ss_details)
        print("Storage Server registered.")

# Function to simulate a client request
def client_request(ip, port, command, file_name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        connection_type = 'C'
        s.send(connection_type.encode())
        
        # Prepare message based on command
        if command == CMD_READ:
            msg = struct.pack('!I50s', CMD_READ, file_name.encode())
        elif command == CMD_WRITE:
            msg = struct.pack('!I50s', CMD_WRITE, file_name.encode())
        
        s.send(msg)
        
        # Receive response
        response = s.recv(1024)
        print(f"Response: {response.decode()}")

# Start the naming server in a separate thread (if needed)
def start_naming_server():
    # This function should connect to the actual naming server.
    pass  # Implement server connection logic here

# Example usage
if __name__ == "__main__":
    # Start the naming server (if needed)
    # threading.Thread(target=start_naming_server).start()

    # Register a storage server (example IP and port)
    register_storage_server('127.0.0.1', 5000)

    # Simulate client requests
    client_request('127.0.0.1', 5000, CMD_READ, 'test_file.txt')
    client_request('127.0.0.1', 5000, CMD_WRITE, 'test_file.txt')
