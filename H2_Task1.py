"""hometask"""
# pylint: disable=invalid-name
X = int(input())
Y = int(input())
F = int(input())
N = int(input())
print([
    [i, j, k]
    for i in range(X + 1)
    for j in range(Y + 1)
    for k in range(F + 1)
    if ((i + j + k) != N)
    ])
