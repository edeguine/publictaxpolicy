import random as rd
import math

def main():
    u0 = rd.uniform(0, 1)
    collected = 0
    print u0
    un = u0

    i = 0

    if(u0 != 1):
        while(True):
            un = un * abs(math.cos(un))
            collected += un
            i += 1
            if( i == 1000 * 1000):
                print i, collected

main()
