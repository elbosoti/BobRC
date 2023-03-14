import RPi.GPIO as GPIO
from time import sleep
import socket, pygame.camera
clientAddress = ("10.14.1.50", 12000)
address = ("0.0.0.0", 12001)
GPIO.setmode(GPIO.BOARD) # Set pin mode to Board across entire program
CarSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Global Socket variable
CarSock.bind(address)
print("server port bound")



def send_video():
    pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    while True:
        sleep(0.0003)
        image = cam.get_image()
        CarSock.sendto(image, clientAddress)


def receive_controls():
    while True:
        message = CarSock.recvfrom(1024)[0].decode()
        if (message[0] == "C"):
            controls = message.split()
            print("going", controls[1], controls[2])
            
    return

def main():
    send_video()
    
if __name__ == "__main__":
    main()