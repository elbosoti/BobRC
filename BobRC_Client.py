import socket
from PIL import Image
import BobRC
import cv2


server_ip = ('0.0.0.0',12000)
car_ip = ('0.0.0.0',12001)

# ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) UDP Route
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP Route
ClientSock.bind(server_ip)


def receivearray():
    ClientSock.listen(1)
    conn, addr = ClientSock.accept()
    data = conn.recv
    imgdata = eval(data.decode())
    cv2.imshow("test", imgdata)



if __name__ == "__main__":
    receivearray()
