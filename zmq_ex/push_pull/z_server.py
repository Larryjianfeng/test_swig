import zmq
import sys
import jieba

server_id = sys.argv[1].encode()

# this is the model part. can be imported outside
def trans(contents):
    return ' '.join(jieba.cut(contents)).encode()


def main():

    # initial subcriber part and receiver part
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5563")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"B")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"A")

    receiver = context.socket(zmq.PUSH)
    receiver.connect("tcp://localhost:5565")

    while True:
        # Receive from proxy
        [address, _id, contents] = subscriber.recv_multipart()
        print('server received')
        # process data
        contents = trans(contents)
        # send out data
        receiver.send_multipart([_id, contents, server_id])
        print('server send')

    # destroy context
    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
