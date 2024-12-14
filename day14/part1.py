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

        # dirs = ['up':(-1,0), 'right':(0,1), 'down':(-1,0), 'left':(0,-1)]

        R, C = 103, 101
        T = 500
        robots = []

        for t in range(T):
            c, r, y, x = map(int, input().split())
            robots.append([c,r,y,x])
            # N = int(input())
            # N, K = map(int, input().split())
            # A = list(map(int, input().split()))

        pos = []
        for i in range(len(robots)):
            c, r, y, x = robots[i]
            r += x*100
            c += y*100
            r %= R
            c %= C
            pos.append([r,c])

        quads = [0]*4
        hR, hC = R >> 1, C >> 1
        for r, c in pos:
            if 0 <= r < hR:
                if 0 <= c < hC:
                    print('quad1',r,c)
                    quads[0] += 1
                elif hC < c:
                    print('quad2',r,c)
                    quads[1] += 1
            elif hR < r:
                if 0 <= c < hC:
                    print('quad3',r,c)
                    quads[2] += 1
                elif hC < c:
                    print('quad4',r,c)
                    quads[3] += 1

        print(quads)
        res = 1
        for q in quads:
            res *= q
        print(res)

            ################## Djikstra's Algo ##################

            # adj = defaultdict(dict)
            #
            # for a, b, w in edges:
            #     adj[a][b] = w
            #     adj[b][a] = w
            #
            # minheap = [(0, 0)]
            # shortest = {}
            #
            # while minheap:
            #     w, node = heapq.heappop(minheap)
            #     if node in shortest:
            #         continue
            #     shortest[node] = w
            #
            #     for nei, wt in adj[node].items():
            #         if nei not in shortest:
            #             heapq.heappush(minheap, (wt + w, nei))
            #
            # print(shortest)


    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        sys.stdin.close()
        # sys.stdout.close()
        # sys.stderr.close()


if __name__ == "__main__": main()

