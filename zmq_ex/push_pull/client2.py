import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:%d" % 5559)


with open('2.txt', 'wb') as f:
    for i in range(100):
        socket.send('那年夏天'.encode())
        res = socket.recv()
        f.write(res + b'\n')
