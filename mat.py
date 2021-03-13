# A:
# 1 2
# 3 4
# = [[1, 2], [3, 4]]

# mathematical indexing of matrices starts from 1 rather than 0

# no safety nets

def prinmat(M):
    [[print(i) for i in row] for row in M]

def scamul(k, M):
    return [[k*val for val in row] for row in M]

def matmul(A, B):
    r = collen(A)
    c = rowlen(B)
    AB = []
    for _r in range(r):
        AB.append([])
        for _c in range(c):
            AB[_r].append(dot(A[_r], col(B, _c + 1)))
    return AB

# number of rows == length of a column
def collen(A):
    return len(A)

def rowlen(A):
    return len(A[0])

def col(B, j):
    rtn = []
    for row in B:
        rtn.append(row[j - 1])
    return rtn

def dot(a, b):
    rtn = 0
    i = len(a)
    while i != 0:
        rtn += a[i-1] * b[i-1]
        i -= 1
    return rtn

def exmat(m, _i, _j):
    # exclude row _i and col _j
    i = _i - 1
    j = _j - 1
    rtn = []
    for x, row in enumerate(m):
        if x != i:
            tmp_row = []
            for y, val in enumerate(row):
                if y != j:
                    tmp_row.append(val)
            rtn.append(tmp_row)
    return rtn

def det(m):
    # enter rectangular matrices at your own risk!
    if len(m) == 1:
        return m[0][0]
    else:
        return sum( [ (1-2*(i % 2)) * row[0] * det(exmat(m, i+1, 1))
                    for i, row in enumerate(m) ] )

def inv(m):
    c = []
    for i, row in enumerate(m):
        nrow = []
        for j, val in enumerate(row):
            nrow.append(cofact(m, i + 1, j + 1))
        c.append(nrow)
    ct = transpose(c)
    d = det(m)
    return scamul(1/d, ct)

def cofact(m, _i, _j):
    sign = 1 - 2 * ((_i + _j) % 2)
    e = exmat(m, _i, _j)
    return sign * det(e)

def transpose(m):
    rl = rowlen(m)
    cl = collen(m)
    rtn = []
    i = 0
    j = 0
    for j in range(rl):
        n = []
        for i in range(cl):
            n.append(m[i][j])
        rtn.append(n)
    return rtn
