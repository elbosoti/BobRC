import socket
import BobRC
import cv2, numpy

import pygame

server_ip = ('0.0.0.0',12000)
car_ip = ('10.14.1.11',12000)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP Route
client_sock.bind(server_ip)

def receive_video():
    pygame.init()
    screen = pygame.display.set_mode((640, 360))
    pygame.display.set_caption("BobRC")
    img_tiles = [numpy.empty((90, 80, 3),dtype=numpy.uint8)]*8
    rc_car = BobRC.CarSpeed()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                rc_car.key_press(event.key)
            elif event.type == pygame.KEYUP:
                rc_car.key_depress(event.key)
        client_sock.sendto(rc_car.to_bytes(), car_ip)
        package, addr = client_sock.recvfrom(65536)
        #index = struct.unpack("B",package[:1])[0]
        index, img = BobRC.process_package(package)
        if index != -1:
            img_tiles[index] = img
            if index == 7:
                img_x1 = numpy.concatenate((img_tiles[0:4]),axis=1)
                img_x2 = numpy.concatenate((img_tiles[4:8]),axis=1)
                img = cv2.resize(numpy.concatenate((img_x1,img_x2)), (640,360))
                img = img.swapaxes(0,1)
                surf = pygame.surfarray.make_surface(img)
                screen.blit(surf, (0,0))
                pygame.display.update()



if __name__ == "__main__":
    receive_video()
