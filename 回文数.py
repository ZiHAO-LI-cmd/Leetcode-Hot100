class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = 0
        tmp = x
        while x != 0:
            num = num * 10 + x % 10
            x = x // 10
        if num == tmp:
            return True
        else:
            return False
