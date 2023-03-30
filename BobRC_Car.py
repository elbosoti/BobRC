import socket
import time
import threading
import BobRC
from picamera2 import Picamera2
import cv2, numpy
import struct
# import RPi.GPIO as GPIO


client_address = ("10.14.1.50", 12000)
address = ("0.0.0.0", 12000)
car_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Global Socket variable
car_sock.bind(address)

def send_video():
    picam2 = Picamera2()
    video_config = picam2.create_preview_configuration({"size": (320, 180), "format":"BGR888"})
    picam2.configure(video_config)
    picam2.start()
    time.sleep(1)
    while True:
        img_array = picam2.capture_array()
        img_list = img_array.reshape(2, 90, 4, 80, 3).swapaxes(1,2)

        for i, img_row in enumerate(img_list):
            for j, img_tile in enumerate(img_row):
                img_split_jpg = cv2.imencode('.webp', img_tile, [int(cv2.IMWRITE_WEBP_QUALITY),90])[1]
                car_sock.sendto(struct.pack("B", 4*i +j) + img_split_jpg.tobytes(), client_address)

def receive_controls():
    rc_car = BobRC.CarSpeed()
    rc_car.set_pins(3, 5, 7, 11, 13, 15)
    while True:
        data, addr = car_sock.recvfrom(65536)
        rc_car.from_bytes(data)
        rc_car.update_motors()
        

if (__name__ == "__main__"):
    controls = threading.Thread(target=receive_controls)
    video = threading.Thread(target=send_video)
    controls.start()
    # video.start()
    