# def intToRoman(num: int):
#         dic = {
#             0: '',
#             1: 'I',
#             2: 'II',
#             3: 'III',
#             4: 'IV',
#             5: 'V',
#             6: 'VI',
#             7: 'VII',
#             8: 'VIII',
#             9: 'IX',
#             10: 'X',
#             50: 'L',
#             100: 'C',
#             500: 'D',
#             1000: 'M'
#         }
#         if num <= 10:
#             return dic[num]
#         elif 10 < num < 50:
#             first = num // 10
#             second = num % 10
#             return dic[10] * first + dic[second]
#         elif num == 50:
#             return dic[50]
#         elif 50 < num < 100:
#             first = num // 50
#             tmp = num % 50
#             second = tmp // 10
#             tmp = tmp % 10
#             third = tmp
#             return dic[50] * first + dic[10] * second + dic[third]
#         elif num == 100:
#             return dic[100]
#         elif 100 < num < 500:
#             first = num // 100
#             tmp = num % 100
#             second = tmp // 50
#             tmp = tmp % 50
#             third = tmp // 10
#             tmp = tmp % 10
#             fouth = tmp
#             return dic[100] * first + dic[50] * second + dic[10] * third + dic[fouth]
#         elif num == 500:
#             return dic[500]
#         elif 500 < num < 1000:
#             first = num // 500
#             tmp = num % 500
#             second = tmp // 100
#             tmp = tmp % 100
#             third = tmp // 50
#             tmp = tmp % 50
#             fouth = tmp // 50
#             tmp = tmp % 10
#             fifth = tmp
#             return dic[500] * first + dic[100] * second + dic[50] * third + dic[10] * fouth + dic[fifth]
#         elif num == 1000:
#             return dic[1000]
#         else:
#             first = num // 1000
#             tmp = num % 1000
#             second = tmp // 500
#             tmp = tmp % 500
#             third = tmp // 100
#             tmp = tmp % 100
#             fouth = tmp // 50
#             tmp = tmp % 50
#             fifth = tmp // 10
#             tmp = tmp % 10
#             sixth = tmp
#             return dic[1000] * first + dic[500] * second + dic[100] * third + dic[50] * fouth + dic[10] * fifth + dic[sixth]

# print(intToRoman(900))

class Solution:

    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def intToRoman(self, num: int) -> str:
        roman = list()
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)


class Solution:
    def intToRoman(self, num: int) -> str:
        # 使用哈希表，按照从大到小顺序排列
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                   90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res += hashmap[key] * count
                num %= key
        return res


# 作者：z1m
# 链接：https://leetcode-cn.com/problems/integer-to-roman/solution/tan-xin-ha-xi-biao-tu-jie-by-ml-zimingmeng/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
