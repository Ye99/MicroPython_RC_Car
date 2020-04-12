import readchar
import socket
UDP_IP_ADDRESS = "10.0.0.31"
UDP_PORT = 6789
forward_command = b"f"
backward_command = b"b"
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    print("Please enter command (f, b, l, r, s): ")
    c = readchar.readchar()
    print("Command is {0}.".format(c))
    clientSock.sendto(bytes(c, 'utf-8'), (UDP_IP_ADDRESS, UDP_PORT))
    print("Commend {0} sent. \n ============================".format(c))




