import sys
# from math
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict


def main():
    try:
        sys.stdin = open("input.txt", "r")
        # sys.stdout = open("output.txt", "w")
        # sys.stderr = open("error.txt", "w")
        input = sys.stdin.readline
        # print = sys.stdout.write

        dirs = {'up':(-1,0), 'right':(0,1), 'down':(1,0), 'left':(0,-1)}

        R = 50
        grid = []
        bot = None

        for r in range(R):
            s = input()

            row = []
            for c,ch in enumerate(s):
                if ch not in ('#','O','.','@'): continue
                if ch == '@':
                    bot = [r,c]
                row.append(ch)

            grid.append(row)

        C = len(grid[0])
        input()

        # for r in range(R):
        #     for c in range(C):
        #         print(grid[r][c],end='')
        #     print()

        for _ in range(20):
            moves = input()
            for move in moves:
                if move not in ('<','>','^','v'):
                    continue

                # print(f'\nMove {move}:')
                if move == '<':
                    dir = 'left'
                elif move == '>':
                    dir = 'right'
                elif move == '^':
                    dir = 'up'
                else:
                    dir = 'down'

                r,c = bot
                nr, nc = r+dirs[dir][0], c+dirs[dir][1]

                while (0 < nr < R-1) and (0 < nc < C-1) and (grid[nr][nc] == 'O'):
                    nr, nc = nr+dirs[dir][0], nc+dirs[dir][1]

                if grid[nr][nc] != '#':
                    grid[nr][nc] = 'O'
                    nr, nc = r+dirs[dir][0], c+dirs[dir][1]
                    grid[nr][nc] = '@'
                    bot = [nr,nc]
                    grid[r][c] = '.'

                # for r in range(R):
                #     for c in range(C):
                #         print(grid[r][c],end='')
                #     print()

        res = 0
        for r in range(R):
            for c in range(C):
                # print(grid[r][c],end='')
                if grid[r][c] == 'O':
                    res += (100*r) + c
            # print()
        print(res)


    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        sys.stdin.close()
        # sys.stdout.close()
        # sys.stderr.close()


if __name__ == "__main__": main()

