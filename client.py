import socket
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client_socket.bind((SERVER_IP, SERVER_PORT)) #bind server ip and server port

def reverse_chiper(msg):
    translated = " "
    i = len(msg) - 1
    while i >= 0:
        translated = translated + msg[i]
        i = i - 1
    return translated


connected = True
while connected:
    msg, serverAddress = client_socket.recvfrom(1024)
    if (msg):
        print("Message is decoding...")
        time.sleep(2)
        msg = reverse_chiper(msg.decode()) #it decodes the message
        print(f"message from server: {msg}")
        print(f"server ip: {serverAddress[0]} ")
        print(f"server port adress: {serverAddress[1]} ")
        connected = False
