numbers = []
while True:
    try:
        data = input().split()
        numbers.extend([int(date) for date in data])
    except EOFError:
        break

max_no = max(numbers)
print(f"Total numbers: {len(numbers)}.")
print(f"The greatest number: {max_no} ({numbers.count(max_no)} time(s)).")
