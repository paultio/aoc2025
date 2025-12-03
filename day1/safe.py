

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