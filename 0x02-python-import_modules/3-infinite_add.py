#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_t = 0

    for i in range(len(sys.argv)-1):
        sum_t += int(sys.argv[i + 1])
    print(f"{sum_t}")
