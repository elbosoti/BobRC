import RPi.GPIO as GPIO
from time import sleep
import socket

address = ("10.14.1.11", 12001)
GPIO.setmode(GPIO.BOARD) # Set pin mode to Board across entire program
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Global Socket variable
sock.bind(address)
print("server port bound")


def cartest():
    print("Test")
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    pwm=GPIO.PWM(7, 100)
    pwm.start(0)
    GPIO.output(3, True)
    GPIO.output(5, False)
    pwm.ChangeDutyCycle(50)
    GPIO.output(7, True)
    sleep(5)
    GPIO.output(7, False)
    pwm.ChangeDutyCycle(100)
    GPIO.output(3, False)
    GPIO.output(5, True)
    GPIO.output(7, True)
    sleep(3)
    GPIO.output(7, False)
    pwm.stop()
    GPIO.cleanup()

def clientRC():
    return

def receive_controls():
    while True:
        message = sock.recvfrom(1024)[0].decode()
        if (message[0] == "C"):
            controls = message.split()
            print("going", controls[1], controls[2])
            
    return

def main():
    receive_controls()
    
if __name__ == "__main__":
    main()