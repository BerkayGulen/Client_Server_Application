
import socket
import time

SERVER_IP = "192.168.1.10"
SERVER_PORT = 5005
print("SERVER IS STARTING...")
time.sleep(2)
print(f"UDP target IP:  {SERVER_IP}")
print(f"UDP target port:  {SERVER_PORT}" )
MESSAGE = "schoolNumber:20170613017, fullName:Berkay Gülen, ‘CE306-Section2, ‘LabAssignment#2’"

# this is a simple algorithm to decript a message. It takes a string and reverse it.
def reverse_chiper(msg):
    translated = " "
    i = len(msg) - 1
    while i >= 0:
        translated = translated + msg[i]
        i = i - 1
    return translated


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE = reverse_chiper(MESSAGE)
while True:
    sock.sendto(MESSAGE.encode(), (SERVER_IP, SERVER_PORT))
    choice = input("Message is ready. Do you want to send? [y][n]: ")
    if choice.lower() == "y":
        print(f"[ENCRIPTED MESSAGE]: {MESSAGE} ")
        sock.sendto(MESSAGE.encode(), (SERVER_IP, SERVER_PORT))
        print("Message is send")
