load("@pip_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "flask",
    visibility = ["//python:__pkg__"],
    deps = [
        requirement("Flask"),
        requirement("Jinja2"),
        requirement("MarkupSafe"),
        requirement("Werkzeug"),
        requirement("click"),
        requirement("itsdangerous"),
    ],
)

py_library(
    name = "grpc",
    visibility = ["//python:__pkg__"],
    deps = [
        requirement("grpcio"),
        requirement("six"),
    ],
)
