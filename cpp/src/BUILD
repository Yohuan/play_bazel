load("@rules_cc//cc:defs.bzl", "cc_binary")

cc_binary(
    name = "hello_world",
    srcs = ["hello_world.cpp"],
    deps = [
        "//cpp/src/lib:libgreeting",
        # "@external_depedency//cpp/src/lib:libgreeting",
    ],
)
