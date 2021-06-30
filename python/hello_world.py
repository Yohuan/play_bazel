import sys

from python.lib import greeting

# from external_depedency.python.lib import greeting


if __name__ == "__main__":
    who = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greeting.greet(who))
