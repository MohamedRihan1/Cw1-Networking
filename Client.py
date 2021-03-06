# Creating client
import threading
import socket
username = input('Enter a Username >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()), 59000))

# Creating function to receive client requests
def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "username?":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break

# creating function to send the message by client
def client_send():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('utf-8'))

# Enabling thread
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()