import socket
import time
import io
import BobRC
from picamera2 import Picamera2
import cv2, numpy
import struct



client_address = ("10.14.1.50", 12000)
address = ("0.0.0.0", 12001)
#GPIO.setmode(GPIO.BOARD) # Set pin mode to Board across entire program
car_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Global Socket variable
# car_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Global Socket variable
# car_sock.bind(address)
print("server port bound")


def send_video():
    picam2 = Picamera2()
    video_config = picam2.create_preview_configuration({"size": (320, 180)})
    picam2.configure(video_config)
    picam2.start()
    time.sleep(1)
    while True:
        img_array = picam2.capture_array()
        img_list = img_array.reshape(2, 90, 4, 80, 4).swapaxes(1,2)

        for i, imgrow in enumerate(img_list):
            for j, im_tile in enumerate(imgrow):
                img_split_jpg = cv2.imencode('.webp', im_tile, [int(cv2.IMWRITE_WEBP_QUALITY),90])[1]
                car_sock.sendto(struct.pack("B", 4*i +j) + img_split_jpg.tobytes(), client_address)

        

if (__name__ == "__main__"):
    send_video()
    