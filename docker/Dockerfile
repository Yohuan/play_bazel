FROM ubuntu:18.04

RUN apt-get update && apt-get install -y npm python3
RUN npm install -g @bazel/bazelisk

WORKDIR /src
COPY . /src

RUN bazel build
