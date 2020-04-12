import machine
import time
import socket

UDP_IP = "10.0.0.31"
UDP_PORT = 6789
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# right side
en_right = machine.Pin(5, machine.Pin.OUT)
in1 = machine.Pin(14, machine.Pin.OUT)
in2 = machine.Pin(12, machine.Pin.OUT)

# left side
en_left = machine.Pin(4, machine.Pin.OUT)
in3 = machine.Pin(13, machine.Pin.OUT)
in4 = machine.Pin(15, machine.Pin.OUT)

def left_forward() -> None:
    in1.off()
    in2.on()


def right_forward() -> None:
    in3.on()
    in4.off()


def forward() -> None:
    stop()
    left_forward()
    right_forward()
    start()


def left_backward() -> None:
    in1.on()
    in2.off()

def right_backward() -> None:
    in3.off()
    in4.on()


def backwoard() -> None:
    stop()
    left_backward()
    right_backward()
    start()


def turn_left() -> None:
    stop()
    left_forward()
    right_backward()
    start()


def turn_right() -> None:
    stop()
    right_forward()
    left_backward()
    start()


def stop() -> None:
    en_right.off()
    en_left.off()
    time.sleep_ms(100)


def start() -> None:
    en_right.on()
    en_left.on()

while True:
    time.sleep_ms(2)
    data, addr = sock.recvfrom(1024)
    key = data.decode()
    print(key)
    if key == "f":
        print("forward")
        forward()
    if key == "b":
        print("backward")
        backwoard()


"""
stop()
time.sleep(1)
foward()
time.sleep(3)
backwoard()
time.sleep(3)
turn_right()
time.sleep(3)
turn_left()
time.sleep(3)
stop()
"""



