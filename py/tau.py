from math import sqrt

# \frac{tau^2}{24} = \sum_{n=1}^{\infty}\frac{1}{n^2}

def main(n1, n0 = 0, sum0 = 0):
    sum1 = sum0
    i = n0
    while i != n1:
        i += 1
        sum1 += 24*i**(-2)
        print(i, sum1, sqrt(sum1))

# 64110 39.478043250702136 6.283155516991612
