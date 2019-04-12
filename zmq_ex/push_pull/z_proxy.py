import threading
import zmq
import random

num_parts = 3


def gen_id():
    return str(random.randint(0, 100000)).encode()


class ProxyIn(threading.Thread):
    # Note: proxyIn get message from client. send it to server.
    def __init__(self):
        super().__init__()

    def run(self):
        context = zmq.Context()
        publisher = context.socket(zmq.PUB)
        publisher.bind("tcp://*:5563")

        C_receiver = context.socket(zmq.PULL)
        C_receiver.bind("tcp://*:5564")

        while True:
            msg = C_receiver.recv()
            _id = gen_id()
            publisher.send_multipart([b"A", _id, msg])

        publisher.close()
        C_receiver.close()
        context.term()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ProxyOut(threading.Thread):
    # NOTE: proxyout get message from server, merge it
    #       then send back to client.
    def __init__(self):
        super().__init__()

    def run(self):
        context = zmq.Context()

        S_receiver = context.socket(zmq.PULL)
        S_receiver.bind("tcp://*:5565")

        sender = context.socket(zmq.PUSH)
        sender.bind("tcp://*:5566")

        print('proxy out')
        res = {}
        while True:
            _id, contents, server_id = S_receiver.recv_multipart()
            print('S_receiver received')
            if _id not in res:
                res[_id] = []
            res[_id].append((server_id, contents))
            if len(res[_id]) == 3:
                mes = sorted(res[_id], key=lambda x: x[0])
                sender.send_multipart([_[1] for _ in mes])
                del res[_id]

        S_receiver.close()
        sender.close()
        context.term()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def main():
    si = ProxyIn()
    si.start()

    so = ProxyOut()
    so.start()

if __name__ == "__main__":
    main()
