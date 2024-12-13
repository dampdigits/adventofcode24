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

            def isValid(target, A, i, val):
                if i == len(A):
                    return target == val

                if val==0:
                    res = isValid(target, A, i+1, A[i-1]+A[i])
                else:
                    res = isValid(target, A, i+1, val+A[i])
                if res: return True

                if val==0:
                    res = isValid(target, A, i+1, A[i-1]*A[i])
                else:
                    res = isValid(target, A, i+1, val*A[i])
                if res: return True

                if val==0:
                    res = isValid(target, A, i+1, (A[i-1]*(10**len(str(A[i]))))+A[i])
                else:
                    res = isValid(target, A, i+1, (val*(10**len(str(A[i]))))+A[i])
                return res

            T = 850
            res = 0

            for _ in range(T):
                target, nums = input().split(': ')
                target = int(target)
                A = list(map(int, nums.split()))
                if isValid(target, A, 1, 0):
                    res += target

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

