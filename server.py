# Creating server
import threading
import socket
host = socket.gethostbyname(socket.gethostname())
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding server with host and port
server.bind((host, port))
server.listen()
clients = []
usernames = []

# Function to send message to clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Function to handle clients'connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
# Disconnecting unwanted users            
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} has left the chat room!'.encode('utf-8'))
            usernames.remove(username)
            break


# Main function to receive the clients connection
def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
# Adding new client        
        client.send('username?'.encode('utf-8'))
        username = client.recv(1024)
        usernames.append(username)
        clients.append(client)
        print(f'The alias of this client is {username}'.encode('utf-8'))
        broadcast(f'{username} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
# Creating and starting thread        
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Starting server
if __name__ == "__main__":
    receive()