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

            R = 50
            grid = []

            for r in range(R):
                row = []
                s = input()
                for c in s:
                    row.append(c)
                grid.append(row)
            C = len(grid[0])

            freq = defaultdict(list)
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == '.':
                        continue
                    freq[grid[r][c]].append((r,c))

            res = set()
            for ch in freq:
                n = len(freq[ch])
                for i in range(n-1):
                    for j in range(i+1,n):
                        if freq[ch][i][0] < freq[ch][j][0]:
                            r1,c1 = freq[ch][i]
                            r2,c2 = freq[ch][j]
                        else:
                            r1,c1 = freq[ch][j]
                            r2,c2 = freq[ch][i]

                        res.add((r1,c1))
                        res.add((r2,c2))

                        rdiff = abs(r1-r2)
                        cdiff = abs(c1-c2)

                        r3 = r1
                        c3 = c1
                        while True:
                            r3 -=rdiff
                            if c1 < c2:
                                c3 -= cdiff
                            else:
                                c3 += cdiff
                            if 0 <= r3 < R and 0 <= c3 < C:
                                res.add((r3,c3))
                                # if grid[r3][c3] == '.':
                                #     grid[r3][c3] = '#'
                            else:
                                break

                        r4 = r2
                        c4 = c2
                        while True:
                            r4 += rdiff
                            if c1 < c2:
                                c4 += cdiff
                            else:
                                c4 -= cdiff
                            if 0 <= r4 < R and 0 <= c4 < C:
                                res.add((r4,c4))
                                # if grid[r4][c4] == '.':
                                #     grid[r4][c4] = '#'
                            else:
                                break

            print(len(res))
            # for r in range(R):
            #     for c in range(C):
            #         print(grid[r][c],end='')
            #     print()

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

