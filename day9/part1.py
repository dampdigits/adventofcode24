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

            s = input()
            compact = []
            space = id = 0

            for c in s:
                if space:
                    x = '.'
                else:
                    x = str(id)
                    id += 1

                compact.extend([x]*int(c))
                space ^= 1
            # print(''.join(compact))
            # print()

            l = compact.index('.')
            r = len(compact)-1
            while r > l and compact[r]=='.':
                r -= 1

            while l < r:
                compact[l] = compact[r]
                compact[r] = '.'

                while l < r and compact[l]!='.':
                    l += 1

                while r > l and compact[r]=='.':
                    r -= 1
            # print(compact)
            # print()

            checksum = 0
            for i, c in enumerate(compact):
                if c == '.': break
                checksum += i*int(c)
                # print(i,'*',c, i*int(c))
            print(checksum)


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

