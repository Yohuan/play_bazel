#!/bin/bash
set -e

mkdir ./lib/proto
python -m grpc_tools.protoc \
    -I../protos\
    --python_out=./lib/proto\
    --grpc_python_out=./lib/proto\
    ../protos/greeting.proto
