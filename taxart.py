# Copyright
# Etienne Deguine

import png
import random as rd
import math
import numpy as np

def colored(n, m):
    res = []
    for i in range(0, m):
        line = []
        for j in range(0, n):
            line.append(rd.randint(0, 255))
        res.append(line)
    return res

def tupler(cols):
    res = []
    i = 0
    for line in cols:
        print i
        res.append(tuple(line))
        i += 1
    return res

def imagewriter(cols):
    print cols
    f = open('taxart.png', 'wb')
    w = png.Writer(1000, 1000)
    print "writing"
    w.write(f, cols)
    print "closing"
    f.close()

def main():
    u0 = rd.uniform(0, 1)
    collected = 0
    print u0
    un = u0
    line = []
    cols = []

    i = 0
    r = 0
    g = 0
    b = 0

    #imagewriter(tupler(colored(3000, 1000)))

    if(u0 != 1):
        for i in range(0, 1000):
            line = []
            for j in range(0, 3000):
                un = un * abs(math.cos(un))
                collected += un
                scaled = un * rd.uniform(0, 10000000000000000)

                if(len(line) == 0):
                    line = [int(scaled) % 255]
                else:
                    line.append(int(scaled) % 255)
            cols.append(line)
        #imagewriter(tupler(cols))
        imagewriter(tupler(colored(3000, 1000)))

main()
