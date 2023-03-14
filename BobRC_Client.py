import socket,threading,time,sys, pygame
server_ip = ('0.0.0.0',12000)
car_ip = ('0.0.0.0',12001)

ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ClientSock.bind(server_ip)
def main():
    pygame.init()
    pygame.display.set_caption("RC Car")
    gamewindow = pygame.display.set_mode((1000,1000))
    forward, backward, speed = 0,0,0
    while True:
        time.sleep(0.0003)
        data = ClientSock.recvfrom(1024000)
        image = pygame.image.fromstring(data[0], (320,240), "RGB")
        gamewindow.blit(image, (0,0))
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                forward = 100
            elif event.key == pygame.K_s:
                backward = 100
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                forward = 0
            elif event.key == pygame.K_s:
                backward = 0
        speed = forward - backward
        print(speed)

    return




if __name__ == "__main__":
    main()