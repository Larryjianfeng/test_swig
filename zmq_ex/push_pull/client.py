import zmq


context = zmq.Context()
socket_in = context.socket(zmq.PUSH)
socket_in.connect("tcp://127.0.0.1:%d" % 5559)

socket_out = context.socket(zmq.SUB)
socket_out.setsockopt(zmq.SUBSCRIBE, b'1')

with open('1.txt', 'wb') as f:
    for i in range(100):
        socket_in.send('你好周杰伦'.encode())
        #res = socket_out.recv()
        #f.write(res + b'\n')
