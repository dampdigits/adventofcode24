import sys
# import math
# import heapq
# from collections import Counter
# from collections import defaultdict


def main():
    try:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin = open("input.txt", "r")
            # sys.stdout = open("output.txt", "w")
            sys.stderr = open("error.txt", "w")

        R = 140
        res = 0
        grid = []
        dirs = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1), (0,1),
            (1,-1), (1,0), (1,1)
        ]

        for _ in range(R):
            grid.append(list(input()))

        def countMAS(r, c):
            count = 0

            for x, y in dirs:
                found = True
                nr, nc = r, c

                for ch in 'MAS':
                    nr += x
                    nc += y
                    if not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == ch):
                        found = False
                        break
                if found:
                    count += 1

            return count

        C = len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'X':
                    res += countMAS(r, c)

        print(res)

    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin.close()
            # sys.stdout.close()
            sys.stderr.close()


if __name__ == "__main__": main()


