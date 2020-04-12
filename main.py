import machine
import time

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


def foward() -> None:
    start()
    left_forward()
    right_forward()


def left_backward() -> None:
    in1.on()
    in2.off()

def right_backward() -> None:
    in3.off()
    in4.on()


def backwoard() -> None:
    start()
    left_backward()
    right_backward()


def turn_left() -> None:
    start()
    left_forward()
    right_backward()


def turn_right() -> None:
    start()
    right_forward()
    left_backward()


def stop() -> None:
    en_right.off()
    en_left.off()


def start() -> None:
    en_right.on()
    en_left.on()

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


