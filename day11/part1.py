import sys

def main():
    try:
        sys.stdin = open('input.txt','r')
        # sys.stdout = open('output.txt','w')
        # sys.stderr = open('error.txt','w')
        input = sys.stdin.readline
        print = sys.stdout.write

        A = list(map(int, input().split()))
        for i in range(25):
            print(str(i)+'\n')
            nA = []
            for a in A:
                if a == 0:
                    nA.append(1)
                else:
                    l = len(str(a))
                    if l&1==0:
                        div = 10**(l >> 1)
                        first = a // div
                        last = a % div
                        nA.append(first)
                        nA.append(last)
                    else:
                        nA.append(a*2024)
            A = nA

        print(str(len(A))+'\n')

    except Exception as e:
        sys.stderr.write(f'Error: {str(e)}\n')
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        sys.stdin.close()
        # sys.stdout.close()
        # sys.stderr.close()

if __name__ == '__main__': main()

