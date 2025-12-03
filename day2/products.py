
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