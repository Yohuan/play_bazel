load("@rules_python//python:defs.bzl", "py_binary")
load("@pip_deps//:requirements.bzl", "requirement")

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    deps = [
        "//python/lib:libgreeting",
        # "@external_depedency//python/lib:libgreeting"
    ],
)

py_binary(
    name = "app",
    srcs = ["app.py"],
    deps = [
        requirement("flask"),
    ],
)
