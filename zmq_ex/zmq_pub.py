import zmq
import time


def pub_example():
    context = zmq.Context()
    service = context.socket(zmq.PUB)
    service.bind("tcp://127.0.0.1:%d" % 5555)
    for i in range(1000):
        service.send((str(i) + '\n').encode())
        print('sending finished')
        time.sleep(1)


def sub_example():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    # this is mandatory, or error. can't understand.
    socket.setsockopt(zmq.SUBSCRIBE, ''.encode())

    socket.connect("tcp://127.0.0.1:%d" % 5555)
    while True:
        string = socket.recv()
        print(string)
