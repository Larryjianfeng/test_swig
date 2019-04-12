import zmq
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.SUB)

#socket.RCVTIMEO = 1000
socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.connect("tcp://127.0.0.1:%d" % 5555)

socket_out = context.socket(zmq.PUSH)
socket_out.connect("tcp://127.0.0.1:%d" % 5557)

while True:
    msg = socket.recv()
    print('SERVER recv, ', msg)
    socket_out.send(msg)
    # print('SERVER send')
