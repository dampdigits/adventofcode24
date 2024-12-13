import sys
# import math
# import heapq
# from collections import Counter
# from collections import defaultdict


def main():
    try:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")
            sys.stderr = open("error.txt", "w")

        res = 0
        for t in range(1000):
            A = list(map(int, input().split()))

            if A[0] == A[1]: continue
            elif A[0] < A[1]:
                x = 1
            else:
                x = -1

            isSafe = True
            for i in range(len(A)-1):
                if not (1 <= (A[i+1] - A[i]) * x <= 3):
                    isSafe = False
                    break

            if isSafe: res+= 1

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


