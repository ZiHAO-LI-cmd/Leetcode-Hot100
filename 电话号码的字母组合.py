class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        nums = []
        res = []
        for i in range(len(digits)):
            nums.append(int(digits[i]))
        s = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        tmp = []
        for num in nums:
            tmp.append(s[num])
        if len(digits) == 1:
            return tmp[0]
        elif len(digits) == 2:
            for first in tmp[0]:
                for second in tmp[1]:
                    res.append(first + second)
        elif len(digits) == 3:
            for first in tmp[0]:
                for second in tmp[1]:
                    for third in tmp[2]:
                        res.append(first + second + third)
        else:
            for first in tmp[0]:
                for second in tmp[1]:
                    for third in tmp[2]:
                        for forth in tmp[3]:
                            res.append(first + second + third + forth)
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        s = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        queue = ['']
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop()
                for c in s[int(digit)]:
                    queue.insert(0, tmp + c)

        return queue
