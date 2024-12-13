import sys
from collections import defaultdict


def main():
    try:
        if "ONLINE_JUDGE" not in sys.argv:
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")
            sys.stderr = open("error.txt", "w")

        T = 1373
        i = res = 0
        nmap = defaultdict(set)

        while True:
            i += 1
            s = input()
            if s == '': break
            a, b = map(int, s.split('|'))
            nmap[a].add(b)

        for _ in range(T-i):
            A = list(map(int, input().split(',')))
            n = len(A)
            correct = True

            for j in range(n-1):
                for k in range(j+1, n):
                    if A[k] not in nmap[A[j]]:
                        correct = False
                        break
                if not correct: break

            if correct:
                print('Correct')
                res += A[n>>1]
            else:
                print('Incorrect')

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

