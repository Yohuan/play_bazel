FROM ubuntu:18.04

RUN apt-get update && apt-get install -y npm python3 python3-venv
RUN npm install -g @bazel/bazelisk

WORKDIR /python_env
RUN python3 -m venv myenv && . myenv/bin/activate

WORKDIR /src
COPY . /src

RUN bazel build //python:app

ENTRYPOINT ["bazel", "run", "//python:app"]

EXPOSE 3000
