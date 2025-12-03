from day2.products import *

def main2_1():
    input_data = read_input("day2/input.txt")
    print(f"Input Data: {input_data}")
    sum_values = 0
    for line in input_data:
        min_val, max_val = get_min_max(line)
        for value in range(min_val, max_val + 1):
            if is_repeating(value):
                print(f"Line: {line}, Repeating Value: {value}")
                sum_values += value
    print(f"Sum of Repeating Values: {sum_values}")

if __name__ == "__main__":
    main2_1()
