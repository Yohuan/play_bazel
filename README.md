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
