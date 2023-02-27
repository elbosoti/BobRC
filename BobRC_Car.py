import socket,threading,time,sys,cv2
server_ip = ('10.14.1.5',12000)



def main():
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #clientSock.settimeout(1)
    message = b'testing'

    clientSock.sendto(message, server_ip)
    



if __name__ == "__main__":
    main()