import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("Enter your nickname: ")

ip_address = "127.0.0.1"
port = 8000

conn = client.connect((ip_address, port))

print("Connected to the server")

def receive():
    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            if message == "nickname":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = "{}".format(input(''))
        client.send(message.encode("utf-8"))

receive_thread = Thread(target = receive)
receive_thread.start()

write_thread = Thread(target = write)
write_thread.start()