import sys
from collections import Counter

def main():
    try:
        sys.stdin = open('input.txt','r')
        input = sys.stdin.readline

        inp = list(map(int, input().split()))
        freq = Counter(inp)

        for t in range(75):
            nfreq = Counter()

            for a,f in freq.items():
                if a == 0:
                    nfreq[1] += f
                else:
                    s = str(a)
                    l = len(s)
                    if l&1==0:
                        l >>= 1
                        first = s[:l]
                        last = s[l:]
                        nfreq[int(first)] += f
                        nfreq[int(last)] += f
                    else:
                        nfreq[a*2024] += f
            freq = nfreq

        print(sum(freq.values()))

    except Exception as e:
        sys.stderr.write(f'Error: {str(e)}\n')
        import traceback
        traceback.print_exc(file=sys.stderr)

    finally:
        sys.stdin.close()
        # sys.stdout.close()
        # sys.stderr.close()

if __name__ == '__main__': main()

