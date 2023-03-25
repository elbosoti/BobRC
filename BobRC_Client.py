import socket
from PIL import Image
import BobRC
import cv2, numpy
import struct


server_ip = ('0.0.0.0',12000)
car_ip = ('0.0.0.0',12001)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP Route
client_sock.bind(server_ip)


def receive_video():
    last_index = 0
    img_tiles = [numpy.empty((90, 80, 3),dtype=numpy.uint8)]*8
    img = bytearray()
    while True:
        package, addr = client_sock.recvfrom(65536)
        index = struct.unpack("B",package[:1])[0]
        if index != last_index:
            try:
                img_tiles[last_index] = cv2.imdecode( numpy.frombuffer(img, dtype=numpy.uint8), cv2.IMREAD_COLOR)
                if index < last_index:
                    img_x1 = numpy.concatenate((img_tiles[0:4]),axis=1)
                    img_x2 = numpy.concatenate((img_tiles[4:8]),axis=1)
                    img = numpy.concatenate((img_x1,img_x2))
                    cv2.imshow('frame',  img)
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            except Exception as e: print(e)
            img = bytearray()
        img = img + package[1:]
        last_index = index


        

if __name__ == "__main__":
    receive_video2()
