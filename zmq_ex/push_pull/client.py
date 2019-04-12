import zmq


context = zmq.Context()
publisher = context.socket(zmq.PUSH)
publisher.connect("tcp://localhost:5564")

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5566")
while True:
    line = input("input: \n")
    line = line.encode()
    publisher.send(line)
    mes = receiver.recv_multipart()
    print([i.decode() for i in mes])

receiver.close()
publisher.close()
context.term()
