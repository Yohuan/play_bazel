load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    deps = [
        "//python/lib:libgreeting",
        # "@external_depedency//python/lib:libgreeting"
    ],
)
