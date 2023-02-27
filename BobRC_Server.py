import socket,threading,time,sys
server_ip = ('0.0.0.0',12000)
car_ip = ('0.0.0.0',12001)



def main():
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind(server_ip)
    #serverSock.sendto(b'', server_ip)
    message, client = serverSock.recvfrom(1024)
    print(message)



if __name__ == "__main__":
    main()