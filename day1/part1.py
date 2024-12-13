import sys
# import math
import heapq
# from collections import Counter
# from collections import defaultdict


def main():
    try:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")
            sys.stderr = open("error.txt", "w")

        A = []
        B = []

        for _ in range(1000):
            a, b = map(int, input().split())
            heapq.heappush(A, a)
            heapq.heappush(B, b)

        res = 0
        for _ in range(1000):
            res += abs(heapq.heappop(A) - heapq.heappop(B))

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

