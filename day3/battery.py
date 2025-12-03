
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def biggest_numbers(line: str) -> int:
    print(f"Line: {line}")
    numbers = [int(num) for num in list(line)]
    max_num = 0
    max_idx = -1
    for idx, num in enumerate(numbers):
        if idx == len(numbers) - 1:
            break
        if num > max_num:
            max_num = num
            max_idx = idx

    # print(f"Index: {max_idx}, Number: {max_num}")

    second_max = -1
    for idx, num in enumerate(numbers[max_idx + 1:], start=max_idx + 1):
        # print(f"Idx: {idx}, Num: {num}")

        if num > second_max:
            second_max = num
    # print(f"Second Max: {second_max}")

    # print(f"{max_num}{second_max}")
    return int(f"{max_num}{second_max}")
