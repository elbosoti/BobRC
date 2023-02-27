import socket,threading,time,sys,cv2
server_ip = ('10.14.1.5',5001)
client_ip = ('0.0.0.0',5000)



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_ip)
    message, client = sock.recvfrom(1024)
    print(message)

def streamvideo():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
    cap.set(cv2.CAP_PROP_FPS, 30)


if __name__ == "__main__":
    main()