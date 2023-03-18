import socket
import time
import RPi.GPIO as GPIO

from picamera2 import Picamera2, Preview 
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput


clientAddress = ("10.14.1.50", 12000)
address = ("0.0.0.0", 12001)
GPIO.setmode(GPIO.BOARD) # Set pin mode to Board across entire program
CarSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Global Socket variable
# CarSock.bind(address)
print("server port bound")



def send_video():
    picam2 = Picamera2()
    video_config = picam2.create_preview_configuration({"size": (640, 360)})
    picam2.configure(video_config)
    encoder = H264Encoder(1000000)
    while(True):
        CarSock.connect(clientAddress)
        stream = sock.makefile("wb")
        picam2.start_recording(encoder, FileOutput(stream))
        time.sleep(20)
        picam2.stop_recording()

def receive_controls():
    while True:
        message = CarSock.recvfrom(1024)[0].decode()
        if (message[0] == "C"):
            controls = message.split()
            print("going", controls[1], controls[2])
            
    return



if (__name__ == "__main__"):
    send_video()
