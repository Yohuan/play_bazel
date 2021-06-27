import sys


def get_greet(who: str) -> str:
    return f"Hello {who}"


if __name__ == "__main__":
    who = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(get_greet(who))
