import machine
from micropython import const
_pause_in_stop_ms = const(200)

import time
import socket

UDP_IP = "10.0.0.31"
UDP_PORT = 6789
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Initial command is stop state.
# Use this to add pause if new command is different to current command, in order to reduce gear impact.
_current_command = b"s"

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
    left_backward()
    right_backward()
    start()


def turn_left() -> None:
    left_forward()
    right_backward()
    start()


def turn_right() -> None:
    right_forward()
    left_backward()
    start()


def stop() -> None:
    en_right.off()
    en_left.off()


def start() -> None:
    en_right.on()
    en_left.on()

def execute_command(command) -> None:
    print(command)

    global _current_command
    if (command != _current_command):
        stop()
        time.sleep_ms(_pause_in_stop_ms) # pause to reduce impact to gear
        _current_command = command

    if command == "f":
        print("forward")
        forward()
    elif command == "b":
        print("backward")
        backwoard()
    elif command == "s":
        print("stop")
        stop()


while True:
    data, addr = sock.recvfrom(1024)
    key = data.decode()
    execute_command(key)



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



