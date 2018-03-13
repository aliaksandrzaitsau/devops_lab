"""homework"""
# pylint: disable=invalid-name
LIST = 'qwertyuiopasdfghjklzxcvbnm'
print("enter any letter:")
A = str(input())
B = LIST.find(A)
if A == "m":
    print("q")
else:
    print(LIST[B+1])
