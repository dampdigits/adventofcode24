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
            row = input()
            grid.append(row)

            if start == None:
                for c, ch in enumerate(row):
                    if ch == '^':
                        start = (r, c)

        C = len(grid[0])
        visited = set()
        visited.add(start)

        dirs = {'up':(-1,0), 'left':(0,-1), 'down':(1,0), 'right':(0,1)}
        curr_dir = 'up'
        curr_r, curr_c = start

        while (curr_r not in (0, R-1)) and (curr_c not in (0, C-1)):
            nr = curr_r + dirs[curr_dir][0]
            nc = curr_c + dirs[curr_dir][1]

            if grid[nr][nc] == '#':
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
            visited.add((curr_r, curr_c))

        print(len(visited))

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


