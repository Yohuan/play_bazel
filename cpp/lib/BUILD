load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")

cc_library(
    name = "libgreeting",
    srcs = ["greeting.cpp"],
    hdrs = ["greeting.h"],
    visibility = ["//cpp:__pkg__"],
)

cc_test(
    name = "test_greeting",
    size = "small",
    srcs = ["test_greeting.cpp"],
    deps = [
        ":libgreeting",
        "@com_google_googletest//:gtest_main",
    ],
)
