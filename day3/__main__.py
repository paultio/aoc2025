from day3.battery import *

def main3_1():
    data = read_input('day3/input.txt')
    # Process data for part 1
    total_joltage = 0
    for line in data:
        max_jolt = biggest_numbers(line)
        print(f"Max Jolt: {max_jolt}\n")
        total_joltage += max_jolt
    print("Total Joltage:", total_joltage)


def main3_2():
    data = read_input('day3/input.txt')
    # Process data for part 2
    total_joltage = 0
    for line in data:
        n_max_jolt = n_biggest_numbers(line, 12)
        print(f"N Max Jolt: {n_max_jolt}\n")
        total_joltage += n_max_jolt
    print("Total N Joltage:", total_joltage)


if __name__ == "__main__":
    main3_2()


234234234234278