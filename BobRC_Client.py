import socket
from PIL import Image
import BobRC
import cv2, numpy


server_ip = ('0.0.0.0',12000)
car_ip = ('0.0.0.0',12001)

# ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) UDP Route
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP Route
ClientSock.bind(server_ip)


def receivearray():
    ClientSock.listen(1)
    conn, addr = ClientSock.accept()
    img = bytearray()
    np_tile = [numpy.empty((90,80,3),dtype=numpy.uint8)]*8
    pervious_index = 0
    while True:
        package = conn.recv(65536)
        index = int.from_bytes(package[:1],'big')
        if index < 8:
            if pervious_index != index:#new tile
                webp_tile = numpy.frombuffer(img, dtype=numpy.uint8)
                try:
                    np_tile[pervious_index] = cv2.imdecode(webp_tile,cv2.IMREAD_COLOR)#webp to np
                    if pervious_index > index:#only show pic if all tiles are send 
                        img_t  =numpy.concatenate((np_tile[0:4]),axis=1)#reassemble image together horizontally
                        img_d  =numpy.concatenate((np_tile[4:8]),axis=1)#reassemble image together vertically
                        img_al =numpy.concatenate((img_t,img_d)) #list of numpy arrays into single numpy array
                        img_al =cv2.resize(img_al,(640,360))#upscale the image to get a better view
                        cv2.imshow('videostream Open-ATS',img_al) #first arg is the name of the window; dont displays the picture
                        cv2.waitKey(1)#displays the picture, waits 1ms
                except:print('failed');pass;
                img = bytearray()#reset img for next tile
            pervious_index = index
            img = img + package[1:]


    imgdata = eval(data.decode())
    cv2.imshow("test", imgdata)



if __name__ == "__main__":
    receivearray()
