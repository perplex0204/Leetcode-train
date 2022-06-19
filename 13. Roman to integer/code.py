# 羅馬數字由七個符號 I V X L C D M組成

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead,
# the number four is written as IV. Because the one is before the five we subtract
# it making four. The same principle applies to the number nine, which is written
# as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# 大意是在說4、9不是IIII、VIIII而是(5-1)、(10-1)，用IV、IX來表示

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# class Solution:
#     def romanToInt(self, s: str) -> int:

class Solution:
    def romanToInt(self, s):
        answer = 0
        buffer_letter = []
        buffer_number = []
        reverse_s = s[::-1]
        for i in reverse_s:
            buffer_letter.append(i)
        for index, data in enumerate(buffer_letter):
            if data == 'I':
                buffer_number.append(1)
            elif data == 'V':
                try:
                    if buffer_letter[index+1] == 'I':
                        buffer_number.append(4)
                        buffer_letter.pop(index+1)
                    else:
                        buffer_number.append(5)
                except:
                    buffer_number.append(5)
            elif data == 'X':
                try:
                    if buffer_letter[index+1] == 'I':
                        buffer_number.append(9)
                        buffer_letter.pop(index+1)
                    else:
                        buffer_number.append(10)
                except:
                    buffer_number.append(10)
            elif data == 'L':
                try:
                    if buffer_letter[index+1] == 'X':
                        buffer_number.append(40)
                        buffer_letter.pop(index+1)
                    else:
                        buffer_number.append(50)
                except:
                    buffer_number.append(50)
            elif data == 'C':
                try:
                    if buffer_letter[index+1] == 'X':
                        buffer_number.append(90)
                        buffer_letter.pop(index+1)
                    else:
                        buffer_number.append(100)
                except:
                    buffer_number.append(100)
            elif data == 'D':
                try:
                    if buffer_letter[index+1] == 'C':
                        buffer_number.append(400)
                        buffer_letter.pop(index+1)
                    else:
                        buffer_number.append(500)
                except:
                    buffer_number.append(500)
            elif data == 'M':
                try:
                    if buffer_letter[index+1] == 'C':
                        buffer_number.append(900)
                        buffer_letter.pop(index+1)
                    else:
                        buffer_number.append(1000)
                except:
                    buffer_number.append(1000)

        for i in buffer_number:
            answer = answer + i

        return answer

# 使用s.replace的解法
# string.replace(old, new, count)
# 記得要存回去變數


class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        # 也可以把全部的.replace打在一起
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
