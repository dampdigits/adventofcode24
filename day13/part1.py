import sys
# import math
# import heapq
# from collections import Counter
# from collections import defaultdict


def main():
    try:
        sys.stdin = open("input.txt", "r")
        # sys.stdout = open("output.txt", "w")
        # sys.stderr = open("error.txt", "w")

        T = 320
        res = 0

        for t in range(T):
            inp = input()[10:]
            j, k = inp.index('+'), inp.index(',')
            ax = int(inp[j : k])
            ay = int(inp[k+4 :])

            inp = input()[10:]
            j, k = inp.index('+'), inp.index(',')
            bx = int(inp[j : k])
            by = int(inp[k+4 :])

            inp = input()[9:]
            k = inp.index(',')
            prizex = int(inp[:k])
            prizey = int(inp[k+4:])
            input()

            n = ((prizey*ax) - (prizex*ay))//((by*ax) - (bx*ay))
            m = (prizex - (bx*n))//ax

            if (ax*m+bx*n == prizex) and (ay*m+by*n == prizey):
                res += (3*m)+n

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

