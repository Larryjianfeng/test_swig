import zmq
import jieba

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket_out = context.socket(zmq.PUSH)

socket.setsockopt(zmq.SUBSCRIBE, ''.encode())

socket.connect("tcp://127.0.0.1:%d" % 5555)
socket_out.connect("tcp://127.0.0.1:%d" % 5557)

while True:
    msg = socket.recv()
    socket_out.send(' '.join(jieba.cut(msg)).encode())
