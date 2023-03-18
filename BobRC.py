from PIL import Image


def test():
    print("test")
    return("test")


def send_video_array(socket, image, clientAddress):
    data = image.tobytes()
    
    socket.sendto(data, clientAddress)
    return

def receive_video_array(socket, carAddress):
    s