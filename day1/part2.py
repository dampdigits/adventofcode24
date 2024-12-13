import sys
# import math
# import heapq
# from collections import Counter
from collections import defaultdict


def main():
    try:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")
            sys.stderr = open("error.txt", "w")

        freqA = defaultdict(int)
        freqB = defaultdict(int)

        for _ in range(1000):
            a, b = map(int, input().split())
            freqA[a] += 1
            freqB[b] += 1

        res = 0
        for num in freqA:
            res += num * freqA[num] * freqB[num]

        # print(freqA)
        # print(freqB)
        print(res)

    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin.close()
            sys.stdout.close()
            sys.stderr.close()


if __name__ == "__main__": main()

