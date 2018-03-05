

print ("check your first number:")
x=(int(input()))
print ("check your second number:")
y=(int(input()))

def selfDividingNumbers(left, right):
    def self_dividing(n):

        for a in str(n):
            if a == '0' or n % int(a) > 0:
                return False
        return True
    ans = []
    for n in range(left, right + 1):
        if self_dividing(n):
            ans.append(n)

    return ans
print("self dividing numbers are:")
print(selfDividingNumbers(x,y))

