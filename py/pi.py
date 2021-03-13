from math import sin, pi

def ngon_area(n):
    return 0.5 * n * sin(2*pi/n)

def main(argv):
    p = int(argv[1])
    if len(argv) < 3:
        q = p
    else:
        q = int(argv[2])
    for i in range(p, q + 1):
        print(f"n: {i} pi: {ngon_area(i)}")
    return 0

import sys
sys.exit(main(sys.argv))
