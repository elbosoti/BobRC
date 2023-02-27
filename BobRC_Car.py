import socket,threading,time,sys,cv2


def main():
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def streamvideo():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
    cap.set(cv2.CAP_PROP_FPS, 30)
