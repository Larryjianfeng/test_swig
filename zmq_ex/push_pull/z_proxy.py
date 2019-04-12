import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:%d" % 5555)

socket_sink = context.socket(zmq.PULL)
socket_sink.bind("tcp://127.0.0.1:%d" % 5557)

socket_client_in = context.socket(zmq.PULL)
socket_client_in.bind("tcp://127.0.0.1:%d" % 5559)

socket_client_out = context.socket(zmq.PUB)
socket_client_out.bind("tcp://127.0.0.1:%d" % 5561)


while True:
    msg = socket_client_in.recv()
    print('PROXY recv', msg)
    socket.send(msg)

    print('PROXY pub', msg)
    reply = socket_sink.recv()
    print('PROYX recv from server', reply)
    # socket_client.send(reply)
    # print('iteration finished')
