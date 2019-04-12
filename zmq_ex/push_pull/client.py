import zmq


context = zmq.Context()
publisher = context.socket(zmq.PUSH)
publisher.connect("tcp://localhost:5564")

while True:
    line = input("input: \n")
    line = line.encode()
    publisher.send(line)

publisher.close()
context.term()
