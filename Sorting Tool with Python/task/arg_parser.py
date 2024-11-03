import argparse


class ArgParser(argparse.ArgumentParser):
    unrecognized_args = set()
    def __init__(self):
        super().__init__()
        self.add_argument("-dataType",
                          choices=["word", "line", "long"],
                          default="word")
        self.add_argument("-sortingType",
                          choices=["natural", "byCount"],
                          default="natural")

    def error(self, message):
        first, second = message.split(":", maxsplit=1)
        if message.endswith("expected one argument"):
            # Original message: "argument -argType: expected one argument"
            arg = first.split("-")[1].rstrip("Type")
            print(f"No {arg} type defined!")
            # exit immediately to avoid printing additional "unrecognized" error for this orphan keyword
            exit(0)
        elif message.startswith("unrecognized arguments"):
            # Original message: "unrecognized arguments: arg1 .. argN"
            for arg in second.split():
                if arg.startswith("-"):
                    print(f'"{arg}" is not a valid parameter. It will be skipped.')
