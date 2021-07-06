load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@io_bazel_rules_docker//contrib:test.bzl", "container_test")

container_image(
    name = "basic_alpine",
    base = "@alpine_linux_amd64//image",
    cmd = ["Hello World!"],
    entrypoint = ["echo"],
)

container_test(
    name = "test_basic_alpine_bazel",
    configs = ["//docker/test_configs:basic_alpine.yml"],
    image = ":basic_alpine",
)
