#Strassen Method of Matrix Multiplication
def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    m = n // 2
    a = [row[:m] for row in A[:m]]
    b = [row[m:] for row in A[:m]]
    c = [row[:m] for row in A[m:]]
    d = [row[m:] for row in A[m:]]

    e = [row[:m] for row in B[:m]]
    f = [row[m:] for row in B[:m]]
    g = [row[:m] for row in B[m:]]
    h = [row[m:] for row in B[m:]]

    p1 = strassen(a, sub(f, h))
    p2 = strassen(add(a, b), h)
    p3 = strassen(add(c, d), e)
    p4 = strassen(d, sub(g, e))
    p5 = strassen(add(a, d), add(e, h))
    p6 = strassen(sub(b, d), add(g, h))
    p7 = strassen(sub(a, c), add(e, f))

    c11 = add(sub(add(p5, p4), p2), p6)
    c12 = add(p1, p2)
    c21 = add(p3, p4)
    c22 = sub(sub(add(p5, p1), p3), p7)

    result = []
    for i in range(m):
        result.append(c11[i] + c12[i])
    for i in range(m):
        result.append(c21[i] + c22[i])
    return result

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[1, 0, 0, 1],
     [0, 1, 1, 0],
     [1, 0, 1, 0],
     [0, 1, 0, 1]]

res = strassen(A, B)
for row in res:
    print(row)