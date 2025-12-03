from day1.safe import *

def main():
    data = read_input('day1/test.txt')
    curr = 50
    zero_count = 0
    for line in data:
        curr = do_calculation(curr, line)
        if curr == 0:
            zero_count += 1
        print(curr)
    print(f"Number of times zero was reached: {zero_count}")




if __name__ == "__main__":
    main()