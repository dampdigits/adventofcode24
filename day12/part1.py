import sys

def main():
    try:
        sys.stdin = open('input.txt','r')
        # sys.stdout = open('output.txt','w')
        # sys.stderr = open('error.txt','w')
        input = sys.stdin.readline
        # print = sys.stdout.write

        R = 140
        grid = []
        for r in range(R):
            row = input()
            grid.append(row)
        C = len(grid[0])

        def dfs(r,c):
            nonlocal area
            nonlocal peri

            visited.add((r,c))
            area += 1

            for x,y in dirs:
                nr, nc = r+x, c+y
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==grid[r][c]:
                    if (nr,nc) not in visited:
                        dfs(nr,nc)
                else:
                    peri+=1

        visited = set()
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        res = area = peri = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c].isalpha() and (r,c) not in visited:
                    area = peri = 0
                    dfs(r,c)
                    res += area * peri
                    print(grid[r][c],area,peri,area*peri)
        print(res)

    except Exception as e:
        sys.stderr.write(f'Error: {str(e)}\n')
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        sys.stdin.close()
        # sys.stdout.close()
        # sys.stderr.close()

if __name__ == '__main__': main()

