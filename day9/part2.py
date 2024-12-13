import sys
from collections import defaultdict


def main():
    try:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")
            sys.stderr = open("error.txt", "w")

            s = input()
            size = space = id = 0
            spaces = []
            ids = []

            for c in s:
                c = int(c)
                if space:
                    if c:
                        spaces.append([size,c])
                else:
                    if c:
                        ids.append([size,c,id])
                    id += 1

                size += c
                space ^= 1

            for i in range(len(ids)-1,-1,-1):
                for j in range(len(spaces)):
                    if spaces[j][0] < ids[i][0] and ids[i][1] <= spaces[j][1]:
                        if ids[i][2] == '6':
                            print('changing',ids[i])
                        ids[i][0] = spaces[j][0]
                        spaces[j][0] += ids[i][1]
                        spaces[j][1] -= ids[i][1]
                        if ids[i][2] == '6':
                            print('to',ids[i])
                        break

            space = []
            for a,b in spaces:
                if b:
                    space.append([a,b])

            space.sort()
            ids.sort()

            # print(spaces)
            # print(ids)

            i = j = k = 0
            s = []

            while i < len(ids) and j < len(space):
                if k == ids[i][0]:
                    s.extend([ids[i][2]] * ids[i][1])
                    k += ids[i][1]
                    i += 1
                elif k == space[j][0]:
                    s.extend(['.'] * space[j][1])
                    k += space[j][1]
                    j += 1
                else:
                    p = min(ids[i][0], space[j][0])
                    s.extend(['.'] * (p - k))
                    k = p

            while i < len(ids):
                s.extend([ids[i][2]] * ids[i][1])
                i += 1

            while j < len(space):
                s.extend(['.'] * space[j][1])
                j += 1

            # print(''.join(s))
            res = 0
            for i, c in enumerate(s):
                if c == '.': continue
                res += i*c

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

