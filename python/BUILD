load("@rules_python//python:defs.bzl", "py_binary")
load("@pip_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

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

py3_image(
    name = "docker_hello_world",
    srcs = ["hello_world.py"],
    deps = ["//python/lib:libgreeting"],
    main = "hello_world.py",
)

py3_image(
    name = "docker_app",
    srcs = ["app.py"],
    layers = [
        requirement("flask"),
    ],
    main = "app.py",
)
