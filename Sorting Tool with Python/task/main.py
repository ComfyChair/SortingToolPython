import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-dataType",
                    default="word",
                    choices=["word","line","long"])

def parse_numbers():
    numbers = []
    while True:
        try:
            data = input().split()
            numbers.extend([int(date) for date in data])
        except EOFError:
            break
    print(f"Total numbers: {len(numbers)}.")
    max_no = max(numbers)
    count_max = numbers.count(max_no)
    percent = math.floor(count_max / len(numbers) * 100)
    print(f"The greatest number: {max_no} ({count_max} time(s), {percent}%).")

def parse_words():
    words = []
    while True:
        try:
            data = input().split()
            words.extend([date for date in data])
        except EOFError:
            break
    print(f"Total words: {len(words)}.")
    words.sort(key=lambda x: len(x), reverse=True)
    longest = words[0]
    count = words.count(longest)
    percent = math.floor(count / len(words) * 100)
    print(f"The longest word: {longest} ({count} time(s), {percent:.0f}%).")


def parse_lines():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    print(f"Total lines: {len(lines)}.")
    lines.sort(key=lambda x: len(x), reverse=True)
    longest = lines[0]
    count = lines.count(longest)
    percent = math.floor(count / len(lines) * 100)
    print(f"The longest line:\n{longest}\n({count} time(s), {percent:.0f}%).")


match (data_type := parser.parse_args().dataType):
    case "word": parse_words()
    case "line": parse_lines()
    case "long": parse_numbers()

