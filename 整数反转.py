class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            y = '-' + x[1::][::-1]
        else:
            y = x[::-1]
        y = int(y)
        if y < -1*2**31 or y > 2**31-1:
            return 0
        return y