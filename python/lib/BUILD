load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "libgreeting",
    srcs = ["greeting.py"],
    visibility = ["//python:__pkg__"],
)

py_test(
    name = "test_greeting",
    srcs = ["test_greeting.py"],
    deps = [
        ":libgreeting",
    ],
)
