import socket
import threading

SERVER = "192.168.1.14"
PORT = 9090
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = "!DISCONNECT"
ANSWER_MESSAGE = "!ANSWER"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def recieve_msg():
    while True:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            if msg == ANSWER_MESSAGE:
                msg = input()
                send_msg(msg)
            elif msg == DISCONNECT_MESSAGE:
                break
            else:
                print(msg)


thread_talk = threading.Thread(target=recieve_msg, args=())
thread_talk.start()
