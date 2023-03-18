def test():
    print("test")
    return("test")


def send_video_array(socket, array, clientAddress):
    socket.connect(clientAddress)
    socket.sendall(array)
    return

def receive_video_array(socket, carAddress):
    s