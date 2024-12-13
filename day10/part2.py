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

            R = 52
            grid = []
            zeros = []
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]

            for r in range(R):
                s = input()
                row = []
                for c, ch in enumerate(s):
                    row.append(int(ch))
                    if ch == '0':
                        zeros.append((r,c))
                grid.append(row)

            # print(zeros)
            # for row in grid:
            #     print(row)

            def trail(r,c):
                # nonlocal visited
                # visited.add((r,c))

                if cache[r][c] != None:
                    return cache[r][c]

                if grid[r][c] == 9:
                    # print((r,c))
                    return 1

                res = 0
                for x,y in dirs:
                    nr, nc = r+x, c+y
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]-grid[r][c]==1:
                        res += trail(nr,nc)

                cache[r][c] = res
                return res

            C = len(grid[0])
            res = 0
            cache = [[None]*C for _ in range(R)]
            # visited = set()

            for r,c in zeros:
                # visited = set()
                ans = trail(r,c)
                # print(ans)
                # print()
                res += ans
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

