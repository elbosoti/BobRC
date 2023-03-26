import cv2, numpy
import struct

def process_package(package):
    try:
        index = struct.unpack("B",package[:1])[0]
        img = cv2.imdecode( numpy.frombuffer(package[1:], dtype=numpy.uint8), cv2.IMREAD_COLOR)
        return index, img
    except Exception as e:
        print("Error processing package", e)
        return -1, None
    
class CarSpeed:
    def __init__(self):
        self.speed = 0
        self.direction = 0
    
    def key_press(self, key):
        if key == 'w':
            self.speed = 1
        elif key == 's':
            self.speed = -1
        elif key == 'a':
            self.direction = -1
        elif key == 'd':
            self.direction = 1
        elif key == ' ':
            self.speed = 0
            self.direction = 0
        else:
            return False
        return True
    
    def key_depress(self, key):
        if key == 'w' or key == 's':
            self.speed = 0
        elif key == 'a' or key == 'd':
            self.direction = 0
        else:
            return False
        return True
    
    def to_bytes(self):
        return struct.pack("b", self.speed, self.direction)
    
    def from_bytes(self, data):
        speed, direction = struct.unpack("b", data)
        rc_car = CarSpeed()
        rc_car.speed = self.speed
        rc_car.direction = self.direction
        return rc_car