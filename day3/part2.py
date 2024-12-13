import sys
# import math
# import heapq
# from collections import Counter
# from collections import defaultdict


def main():
    try:
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
        sys.stderr = open("error.txt", "w")

        res = 0
        enabled = True

        for _ in range(6):
            s = input()
            n = len(s)
            i = 0

            while i < n - 8:
                if s[i]=='d' and s[i+1]=='o' and s[i+2]=='(' and s[i+3]==')':
                    enabled = True
                    i += 4
                elif s[i]=='d' and s[i+1]=='o' and s[i+2]=='n' and s[i+3]=="'" and s[i+4]=='t' and s[i+5]=='(' and s[i+6]==')':
                    enabled = False
                    i += 7
                elif enabled and s[i]=='m' and s[i+1]=='u' and s[i+2]=='l' and s[i+3]=='(':
                    i += 4
                    j = i

                    while j<n and s[j].isdigit():
                        j += 1

                    n1 = int(s[i:j])
                    if j>=n or s[j]!=',' or n1==0 or n1>=1000:
                        i = j
                        continue

                    j += 1
                    k = j
                    while k<n and s[k].isdigit():
                        k += 1

                    n2 = int(s[j:k])
                    if k>=n or s[k]!=')' or n2==0 or n2>=1000:
                        i = k
                        continue

                    res += n1 * n2
                    i = k+1
                else:
                    i += 1

        print(res)

    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        sys.stdin.close()
        sys.stdout.close()
        sys.stderr.close()


if __name__ == "__main__": main()

