import sys

def main():
    try:
        sys.stdin = open('test2.txt','r')
        # sys.stdout = open('output.txt','w')
        # sys.stderr = open('error.txt','w')
        input = sys.stdin.readline
        # print = sys.stdout.write

        R = 5
        grid = []
        for r in range(R):
            row = input()
            grid.append(row)
        C = len(grid[0])

        def calcArea(r,c):
            nonlocal area

            visited.add((r,c))
            area += 1

            for dir in dirs:
                x, y = dirs[dir]
                nr, nc = r+x, c+y
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==grid[r][c] and (nr,nc) not in visited:
                        calcArea(nr,nc)

        def calcPeri(r,c,checkDir,moveDir):
            # print(grid[r][c],r,c,checkDir,moveDir)
            if (r,c,checkDir) in visited: return
            visited.add((r,c,checkDir))

            nonlocal peri
            cr, cc = dirs[checkDir]
            nr, nc = r+cr, c+cc

            # Count 1 side if found cell in checkDir
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==grid[r][c]:
                # print('found in CheckDir')
                peri += 1
                moveDir = checkDir

                if checkDir == 'up':
                    checkDir = 'left'
                elif checkDir == 'left':
                    checkDir = 'down'
                elif checkDir == 'right':
                    checkDir = 'up'
                else:
                    checkDir = 'right'
                # print('new dirs',checkDir, moveDir)
                calcPeri(nr, nc, checkDir, moveDir)
            else:
                mr, mc = dirs[moveDir]
                nr, nc = r+mr, c+mc

                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==grid[r][c]:
                    # print('moving to',nr,nc,checkDir,moveDir)
                    calcPeri(nr, nc, checkDir, moveDir)
                else:
                    # Count 1 side if cant move in moveDir
                    peri += 1
                    checkDir = moveDir

                    if moveDir == 'right':
                        moveDir = 'down'
                    elif moveDir == 'up':
                        moveDir = 'right'
                    elif moveDir == 'down':
                        moveDir = 'left'
                    else:
                        moveDir = 'up'
                    # print('yeah so')
                    calcPeri(r,c,checkDir,moveDir)

        visited = set()
        res = area = peri = 0
        dirs = {'up':[-1,0], 'right':[0,1], 'down':[1,0], 'left':[0,-1]}

        for r in range(R):
            for c in range(C):
                if grid[r][c].isalpha() and (r,c) not in visited:
                    area = peri = 0
                    calcArea(r,c)
                    calcPeri(r,c, 'up', 'right')
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

