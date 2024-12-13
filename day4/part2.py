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

        R = 140
        res = 0
        grid = []

        for _ in range(R):
            grid.append(list(input()))

        C = len(grid[0])
        for r in range(1,R-1):
            for c in range(1,C-1):
                if grid[r][c] == 'A':
                    # x pattern
                    if (
                        (
                            (grid[r-1][c-1]=='M' and grid[r+1][c+1]=='S') or
                            (grid[r-1][c-1]=='S' and grid[r+1][c+1]=='M')
                        ) and
                        (
                            (grid[r-1][c+1]=='M' and grid[r+1][c-1]=='S') or
                            (grid[r-1][c+1]=='S' and grid[r+1][c-1]=='M')
                        )
                    ):
                        res += 1

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


