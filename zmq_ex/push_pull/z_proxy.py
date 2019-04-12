import threading
import zmq
import random


def gen_id():
    return str(random.randint(0, 100000)).encode()


def main():
    # Prepare our context and publisher
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5563")

    C_receiver = context.socket(zmq.PULL)
    C_receiver.bind("tcp://*:5564")

    S_receiver = context.socket(zmq.PULL)
    S_receiver.bind("tcp://*:5565")

    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5566")

    while True:
        # Write two messages, each with an envelope and content
        msg = C_receiver.recv()
        _id = gen_id()
        publisher.send_multipart([b"A", _id, msg])
        res = S_receiver.recv_multipart()

    # We never get here but clean up anyhow
    publisher.close()
    context.term()

if __name__ == "__main__":
    main()
