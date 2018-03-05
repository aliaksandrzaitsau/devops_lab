

from collections import OrderedDict

words = OrderedDict()
a = int(input())
for _ in range(a):
	key = input()
	words[key] = words.get(key, 0) + 1
print (len(words))
print (*[str(words[key]) for key in words], sep = " ")
