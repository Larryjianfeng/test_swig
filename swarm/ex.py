#!/usr/bin/python
import zmq
import logging

logger = logging.getLogger("template")
# set level: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
server_id = b'1'
logger.addHandler(console_handler)

# this is the model part. can be imported outside
def trans(contents):
    return ' '.join(list(contents.decode())).encode()


def main():

    # initial subcriber part and receiver part
    context = zmq.Context()
    subscriber = context.socket(zmq.PULL)
    subscriber.bind("tcp://*:5563")
    #subscriber.setsockopt(zmq.SUBSCRIBE, b"B")
    #subscriber.setsockopt(zmq.SUBSCRIBE, b"A")

    receiver = context.socket(zmq.PUB)
    receiver.bind("tcp://*:5565")

    while True:
        # Receive from proxy
        [address, _id, contents] = subscriber.recv_multipart()
        print('server received')
        # process data
        contents = trans(contents)
        print(contents)
        logger.info(contents)
        # send out data
        receiver.send_multipart([_id, contents, server_id])
        print('server send')

    # destroy context
    subscriber.close()
    receiver.close()
    context.term()

if __name__ == "__main__":
    main()
