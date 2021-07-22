# Overview

This is a toy project to make me familiar with [Bazel](https://bazel.build/).

Before everything, we need to [install Bazel](https://docs.bazel.build/versions/main/install.html) of version **4.1.0**.

# C++

## 1. Build an Executable

```bash
bazel build //cpp:hello_world
```

Execute the built binary

```bash
./bazel-bin/cpp/hello_world
./bazel-bin/cpp/hello_world yohuan
```

## 2. Clean the Built Result

```bash
bazel clean
```

## 3.  Build & Run an Executable

```bash
bazel run //cpp:hello_world
bazel run //cpp:hello_world -- yohuan
```

## 4. Build & Run a Test

```bash
bazel test //cpp/lib:test_greeting
bazel run //cpp/lib:test_greeting
```

# Python

## 1. Build an Executable

```bash
bazel build //python:hello_world
```

Execute the built binary

```bash
./bazel-bin/python/hello_world
./bazel-bin/python/hello_world yohuan
```

## 2. Clean the Built Result

```bash
bazel clean
```

## 3.  Build & Run an Executable

```bash
bazel run //python:hello_world
bazel run //python:hello_world -- yohuan
```

## 4. Build & Run a Test

```bash
bazel test //python/lib:test_greeting
bazel run //python/lib:test_greeting
```

## 5. Integrate with Docker

Build an image and run as a container

```bash
bazel run //python:docker_hello_world
```

# Web Server

Use python to create a simple web server with [Flask](https://flask.palletsprojects.com/en/2.0.x/).

## 1. Build and Run a Web Server

```bash
bazel run //python:flask_server
```

Test the web server

```bash
curl localhost:3000/greeting
Hello world
```

## 2. Integrate with Docker

```bash
bazel run //python:docker_flask_server
```

Test the web server if it is running on 10.17.210.40

```bash
curl 10.17.210.40:3000/greeting
Hello world
```
# Misc

## 1. Build All Targets in the Workspace

```bash
bazel build //...
```

## 2. Run All Tests in the Workspace

```bash
bazel test //...
```
