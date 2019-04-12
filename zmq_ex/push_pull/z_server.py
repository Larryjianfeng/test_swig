import zmq
import sys


server_id = sys.argv[1]
def main():
    """ main method """

    # Prepare our context and publisher
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5563")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"B")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"A")

    receiver = context.socket(zmq.PUSH)
    receiver.connect("tcp://localhost:5565")

    while True:
        # Read envelope with address
        [address, _id, contents] = subscriber.recv_multipart()
        # print("%s, %s , %s" % (address, contents.decode(), server_id))
        receiver.send_multipart([_id, contents])

    # We never get here but clean up anyhow
    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
