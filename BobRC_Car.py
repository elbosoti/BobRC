import socket
import time
import io
import BobRC
from picamera2 import Picamera2
import cv2, numpy



client_address = ("10.14.1.50", 12000)
address = ("0.0.0.0", 12001)
#GPIO.setmode(GPIO.BOARD) # Set pin mode to Board across entire program
car_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Global Socket variable
# car_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Global Socket variable
# car_sock.bind(address)
print("server port bound")



def send_array():
    tilex=4#count tiles in x
    tiley=2#count tiles in y
    picam2 = Picamera2()
    
    video_config = picam2.create_preview_configuration({"size": (320, 180)})
    picam2.configure(video_config)
    picam2.start()
    buffer = io.BytesIO()
    time.sleep(1)
    # car_sock.connect(client_address)
    while True:
        arraydata = picam2.capture_array()
        img = cv2.resize(arraydata, (320, 180))
        img=img.reshape(tiley, int(img.shape[0]/tiley), tilex, int(img.shape[1]/tilex), 4).swapaxes(1,2)
        for id_img_row, img_row in enumerate(img):
            for id_img_tile, img_tile in enumerate(img_row):
                webp_image = (cv2.imencode('.webp',img_tile,[int(cv2.IMWRITE_WEBP_QUALITY),90])[1])
                udp_packages = numpy.array_split(webp_image,len(webp_image)/500+1) #split into 500 byte chunks
                for package in udp_packages:
                    car_sock.sendto((id_img_tile+id_img_row*4).to_bytes(1,'big')+package.tobytes(), client_address)

def send_video():
    picam2 = Picamera2()
    video_config = picam2.create_preview_configuration({"size": (320, 180)})
    picam2.configure(video_config)
    picam2.start()
    time.sleep(1)
    while True:
        img_array = picam2.capture_array()
        img_str = img_array.flatten().tostring()
        print(len(img_str))
        for i in range(10):
            msg_len = int(len(img_str) / 10)

            car_sock.sendto(img_str[msg_len * i : msg_len * (i + 1)], client_address)
        time.sleep(1)
        

if (__name__ == "__main__"):
    send_video()
    