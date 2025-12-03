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



if __name__ == "__main__":
    main3_1()