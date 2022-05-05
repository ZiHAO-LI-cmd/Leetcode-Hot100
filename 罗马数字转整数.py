class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        n = len(s)
        for i, char in enumerate(s):
            value = SYMBOL_VALUES[char]
            if i < n - 1 and value < SYMBOL_VALUES[s[i+1]]:
                res = res - value
            else:
                res = res + value

        return res
