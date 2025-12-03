from day1.safe import *

def main1_1():
    data = read_input('day1/input.txt')
    curr = 50
    zero_count = 0
    for line in data:
        curr = do_calculation(curr, line)
        if curr == 0:
            zero_count += 1
        print(curr)
    print(f"Number of times zero was reached: {zero_count}")

def main1_2():
    data = read_input('day1/input.txt')
    curr = 50
    zero_cross_count = 0
    print("Input\tAdjust\tCurr\tZero Cross")
    for line in data:
        inp = curr
        crossings, curr = count_zero_crossings(curr, line)
        zero_cross_count += crossings

        print(inp, "\t", line, "\t", curr, "\t", zero_cross_count)
    print(f"Number of times zero was crossed: {zero_cross_count}")

if __name__ == "__main__":
    main1_2()