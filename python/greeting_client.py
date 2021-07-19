import logging

import grpc

from protos import greeting_pb2
from protos import greeting_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeting_pb2.HelloReq(name="world"))
    print("Received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
