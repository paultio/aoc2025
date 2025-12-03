
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

def biggest_number_with_index(line: str, index: int) -> tuple[int, int]:
    numbers = [int(num) for num in list(line)]
    max_num = -1
    max_idx = -1
    for idx, num in enumerate(numbers[index:], start=index):
        if num > max_num:
            max_num = num
            max_idx = idx
    return max_num, max_idx

def n_biggest_numbers(line: str, n: int) -> int:
    
    print(f"Line: {line}")
    numbers = [int(num) for num in list(line)]
    max_nums = [0] * n
    max_indexes = [-1] * n

    # Take list, find out how many number we have to choose
    # Leave space for the next numbers to be chosen
    # From the remaining numbers, choose the biggest one
    # After choosing biggest, split the list, so that we only have the numbers after the last chosen number
    # Repeat n times

    numbers_chosen = 0
    max_numbers = []
    l = numbers
    for i in range(n):
        spacing = n - 1 - numbers_chosen
        l_to_choose_from = l[:-spacing] if spacing > 0 else l
        max_num, max_idx = biggest_number_with_index(l_to_choose_from, 0)
        max_numbers.append(max_num)
        l = l[max_idx + 1:]
        numbers_chosen += 1

    result = int(''.join(str(num) for num in max_numbers))
    # print(f"N Biggest Numbers: {result}")
    return result
