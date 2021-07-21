load("@rules_python//python:defs.bzl", "py_binary")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@rules_proto_grpc//python:defs.bzl", "python_grpc_compile", "python_grpc_library")

python_grpc_compile(
    name = "greeter_python_grpc",
    protos = ["//protos:greeter_grpc_proto"],
)

python_grpc_library(
    name = "greeter_grpc",
    protos = ["//protos:greeter_grpc_proto"],
)

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    deps = [
        "//python/lib:libgreeting",
        # "@external_dependency//python/lib:libgreeting"
    ],
)

py_binary(
    name = "flask_server",
    srcs = ["flask_server.py"],
    deps = [
        "//python/pip:flask",
    ],
)

py_binary(
    name = "greeter_grpc_server",
    srcs = ["greeting_server.py"],
    main = "greeting_server.py",
    deps = [
        ":greeter_grpc",
        "//python/pip:grpc",
    ],
)

py_binary(
    name = "greeter_grpc_client",
    srcs = ["greeting_client.py"],
    main = "greeting_client.py",
    deps = [
        ":greeter_grpc",
        "//python/pip:grpc",
    ],
)

py3_image(
    name = "docker_hello_world",
    srcs = ["hello_world.py"],
    deps = ["//python/lib:libgreeting"],
    main = "hello_world.py",
)

py3_image(
    name = "docker_flask_server",
    srcs = ["flask_server.py"],
    layers = [
        "//python/pip:flask",
    ],
    main = "flask_server.py",
)
