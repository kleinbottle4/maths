def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

def p(n):
    return f(3) / (f(n) * f(3-n)) * (0.23)**(n) * (0.77)**(3-n)

print(sum([n*p(n) for n in range(3+1)]))
