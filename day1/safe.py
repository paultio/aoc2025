

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def do_calculation(current_value: int, adjustment: str) -> int:
    ans = 0
    if adjustment.startswith('L'):
        ans = current_value - int(adjustment[1:])
    elif adjustment.startswith('R'):
        ans = current_value + int(adjustment[1:])
    else:
        print("Invalid adjustment" + adjustment)

    return ans % 100

def count_zero_crossings(current_value: int, adjustment: str) -> tuple[int, int]:
    adjust = 0
    modifier = 1
    zero_cross_count = 0
    if adjustment.startswith('L'):
        adjust = int(adjustment[1:])
        modifier = -1
    elif adjustment.startswith('R'):
        adjust = int(adjustment[1:])
        modifier = 1

    for i in range(adjust):
        current_value += modifier
        current_value %= 100
        if current_value == 0:
            zero_cross_count += 1

    return zero_cross_count, current_value
