import logging

import grpc

from protos import greeting_pb2
from protos import greeting_pb2_grpc

_HOST = "localhost"
_PORT = "5566"


def run():
    with grpc.insecure_channel(f"{_HOST}:{_PORT}") as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeting_pb2.HelloReq(name="world"))
    print("Received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
