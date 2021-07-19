from concurrent import futures
import logging

import grpc

from protos import greeting_pb2
from protos import greeting_pb2_grpc

_NUM_WORKERS = 10
_HOST = "0.0.0.0"
_PORT = "5566"


class Greeter(greeting_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeting_pb2.HelloResp(message=f"Hello, {request.name}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=_NUM_WORKERS))
    greeting_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    address = f"{_HOST}:{_PORT}"
    server.add_insecure_port(address)
    server.start()
    print(f"Listen on {address}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
