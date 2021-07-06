# Overview

This is a toy project to make me familiar with [Bazel](https://bazel.build/).

# C++

## 1. Build Executable

```bash
bazel build //cpp/src:hello_world
```

Execute the binary

```bash
./bazel-bin/cpp/src/hello_world
./bazel-bin/cpp/src/hello_world yohuan
```

## 2. Clean the Build Result

```bash
bazel clean
```

## 3.  Build & Run Executable

```bash
bazel run //cpp/src:hello_world
bazel run //cpp/src:hello_world -- yohuan
```

## 4. Build & Run Test

```bash
bazel test //cpp/src/lib:test_greeting
bazel run //cpp/src/lib:test_greeting
```

# Python

## 1. Build Executable

```bash
bazel build //python:hello_world
```

Execute the binary

```bash
./bazel-bin/python/hello_world
./bazel-bin/python/hello_world yohuan
```

## 2. Clean the Build Result

```bash
bazel clean
```

## 3.  Build & Run Executable

```bash
bazel run //python:hello_world
bazel run //python:hello_world -- yohuan
```

## 4. Build & Run Test

```bash
bazel test //python/lib:test_greeting
bazel run //python/lib:test_greeting
```

## 5. Integrate with Docker

Build image and run as a container

```bash
bazel run //python:docker_hello_world
```

# Web Server

Use python to create a simple web server by [Flask](https://flask.palletsprojects.com/en/2.0.x/).

## 1. Build and Run Web Server

```bash
bazel run //python:app
```

Test the web server

```bash
curl localhost:3000/greeting
Hello world
```

## 2. Integrate with Docker

```bash
bazel run //python:docker_app
```

Test the web server if it is running on 10.17.210.40

```bash
curl 10.17.210.40:3000/greeting
Hello world
```
# Misc

## 1. Build all targets in the workspace

```bash
bazel build //...
```

## 2. Run all tests in the workspace

```bash
bazel test //...
```
