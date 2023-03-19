import socket
import time
import RPi.GPIO as GPIO
import io

import BobRC
from picamera2 import Picamera2, Preview 
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput


clientAddress = ("10.14.1.50", 12000)
address = ("0.0.0.0", 12001)
GPIO.setmode(GPIO.BOARD) # Set pin mode to Board across entire program
# CarSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Global Socket variable
CarSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Global Socket variable
# CarSock.bind(address)
print("server port bound")



def send_video():
    picam2 = Picamera2()
    video_config = picam2.create_preview_configuration({"size": (320, 180)})
    picam2.configure(video_config)
    picam2.start()
    buffer = io.BytesIO()
    time.sleep(1)
    CarSock.connect(clientAddress)
    arraydata = picam2.capture_array()
    arraybinary = str(arraydata).encode()
    print("arraydata", str(arraydata)[0:10])
    #picturedata = picam2.capture_image()
    # picturebinary = picturedata.tobytes()
    #print("sending array: ", len(picturebinary))
    CarSock.sendall(arraybinary)



if (__name__ == "__main__"):
    send_video()
    