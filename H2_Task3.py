"""homework"""
# pylint: disable=invalid-name
print("check your first number:")
X = (int(input()))
print("check your second number:")
Y = (int(input()))


def self_numbers(left, right):
    """write here"""
    def self_dividing(N):
        """something"""
        for A in str(N):
            if A == '0' or N % int(A) > 0:
                return False
        return True
    ans = []
    for N in range(left, right + 1):
        if self_dividing(N):
            ans.append(N)
    return ans


print("self dividing numbers are:")
print(self_numbers(X, Y))
