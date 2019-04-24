import zmq

ctx = zmq.Context()
soc = ctx.socket(zmq.PUSH)
soc.connect("tcp://localhost:5563")

for _ in range(10):
    soc.send_multipart([b"B", b"asd", b"asdfas"])

soc.close()
ctx.term()
