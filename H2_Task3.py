"""homework"""
print("check your first number:")
X = (int(input()))
print("check your second number:")
Y = (int(input()))
def self_numbers(left, right):
    """write here"""
    def self_dividing(n):
        """something"""
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
print(self_numbers(X, Y))
