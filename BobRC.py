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
        #self.motor1a = 0
        #self.motor1b = 0
        #self.enable1 = 0
        #self.motor2a = 0
        #self.motor2b = 0
        #self.enable2 = 0
    
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
        return struct.pack("2b", self.speed, self.direction)
    
    def from_bytes(self, data):
        self.speed, self.direction = struct.unpack("2b", data)

    def set_pins(self, motor1a, motor1b, enable1, motor2a, motor2b, enable2):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        self.motor1a = motor1a
        self.motor1b = motor1b
        self.enable1 = enable1
        self.motor2a = motor2a
        self.motor2b = motor2b
        self.enable2 = enable2
        GPIO.setup(motor1a, GPIO.OUT)
        GPIO.setup(motor1b, GPIO.OUT)
        GPIO.setup(enable1, GPIO.OUT)
        GPIO.setup(motor2a, GPIO.OUT)
        GPIO.setup(motor2b, GPIO.OUT)
        GPIO.setup(enable2, GPIO.OUT)
    
    def update_motors(self):
        import RPi.GPIO as GPIO
        if self.speed < 0:
            GPIO.output(self.enable1, 1)
            GPIO.output(self.motor1a, 0)
            GPIO.output(self.motor1b, 1)
        elif self.speed > 0:
            GPIO.output(self.enable1, 1)
            GPIO.output(self.motor1a, 1)
            GPIO.output(self.motor1b, 0)
        else:
            GPIO.output(self.enable1, 0)
            GPIO.output(self.motor1a, 0)
            GPIO.output(self.motor1b, 0)
        
        if self.direction < 0:
            GPIO.output(self.enable2, 1)
            GPIO.output(self.motor2a, 0)
            GPIO.output(self.motor2b, 1)
        elif self.direction > 0:
            GPIO.output(self.enable2, 1)
            GPIO.output(self.motor2a, 1)
            GPIO.output(self.motor2b, 0)
        else:
            GPIO.output(self.enable2, 0)
            GPIO.output(self.motor2a, 0)
            GPIO.output(self.motor2b, 0)