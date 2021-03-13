#what is the nth triangle number?
def triangle(n):
    result = 0
    while n >= 1:
        result += n
        n -= 1
    return result

print(triangle(255))
