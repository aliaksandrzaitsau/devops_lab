"""homework"""
from collections import OrderedDict
WORDS = OrderedDict()
A = int(input())
for _ in range(A):
    key = input()
    WORDS[key] = WORDS.get(key, 0) + 1
print(len(WORDS))
print(*[str(WORDS[key]) for key in WORDS], sep="")
