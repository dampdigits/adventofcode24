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

        R = 130
        grid = []
        start = None

        for r in range(R):
            row = list(input())
            grid.append(row)

            if start == None:
                for c, ch in enumerate(row):
                    if ch == '^':
                        start = (r, c)

        def getsStuck(curr_r, curr_c):
            obstacles = set()
            stuck = False
            curr_dir = 'up'

            while 0 < curr_r < R-1 and 0 < curr_c < C-1:
                nr = curr_r + dirs[curr_dir][0]
                nc = curr_c + dirs[curr_dir][1]

                while grid[nr][nc] == '#':
                    if (curr_r, curr_c, curr_dir) in obstacles:
                        stuck = True
                        break

                    obstacles.add((curr_r, curr_c, curr_dir))
                    if curr_dir == 'up':
                        curr_dir = 'right'
                    elif curr_dir == 'right':
                        curr_dir = 'down'
                    elif curr_dir == 'down':
                        curr_dir = 'left'
                    else:
                        curr_dir = 'up'
                    nr = curr_r + dirs[curr_dir][0]
                    nc = curr_c + dirs[curr_dir][1]

                curr_r = nr
                curr_c = nc

            return stuck

        C = len(grid[0])
        res = 0
        dirs = {'up':(-1,0), 'left':(0,-1), 'down':(1,0), 'right':(0,1)}
        curr_dir = 'up'
        curr_r, curr_c = start

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    grid[r][c] = '#'
                    # print('putting 0 at',r,c)
                    if getsStuck(curr_r, curr_c):
                        print('stuck due to ', r, c)
                        res += 1
                    grid[r][c] = '.'

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

