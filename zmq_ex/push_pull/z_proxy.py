import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:%d" % 5555)

socket_sink = context.socket(zmq.PULL)
socket_sink.bind("tcp://127.0.0.1:%d" % 5557)

socket_client = context.socket(zmq.REP)
socket_client.bind("tcp://127.0.0.1:%d" % 5559)


while True:
    msg = socket_client.recv()
    print('received ', msg)
    socket.send(msg)
    print('send ', msg)
    reply = socket_sink.recv()
    print('server finished, sending back')
    socket_client.send(reply)
    print('iteration finished')
