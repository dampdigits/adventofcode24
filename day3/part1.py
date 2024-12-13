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

        res = 0

        for _ in range(6):
            s = input()
            i = 0

            while i < len(s)-8:
                if s[i:i+4] == 'mul(':
                    j = i + 4

                    while j < len(s) and s[j].isdigit():
                        j += 1

                    if (i+4 == j) or (j < len(s) and s[j] != ','):
                        i = j
                        continue

                    n1 = int(s[i+4:j])
                    k = j + 1

                    while k < len(s) and s[k].isdigit():
                        k += 1

                    if (j+1 == k) or (k < len(s) and s[k] != ')'):
                        i = k
                        continue

                    n2 = int(s[j+1:k])
                    res += n1 * n2
                    i = k + 1
                else:
                    i += 1

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

