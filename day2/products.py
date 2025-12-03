
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    # return data.split(',')
    return [line.strip() for line in data.split(',')]

def get_min_max(line: str) -> tuple[int, int]:
    parts = line.split('-')
    return int(parts[0]), int(parts[1])

def is_repeating(value: int) -> bool:
    sequence = str(value)
    length = len(sequence)
    if length % 2 != 0:
        return False
    mid = length // 2
    return sequence[:mid] == sequence[mid:]

def factors(n: int) -> list[int]:
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def has_repeating_pattern(value: int) -> bool:
    sequence = str(value)
    length = len(sequence)
    found = False
    for search_window in factors(length):
        for start in range(length - 2 * search_window + 1):
            found = True
            if sequence[start:start + search_window] == sequence[start + search_window:start + 2 * search_window]:
                continue
            else:
                found = False
                break
        if found:
            break

    return found
