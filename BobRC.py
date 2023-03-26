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