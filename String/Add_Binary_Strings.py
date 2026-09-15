class Solution:
    def addBinary(self, s1, s2):
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            digit1 = int(s1[i]) if i >= 0 else 0
            digit2 = int(s2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry

            result = str(total % 2) + result
            carry = total // 2

            i -= 1
            j -= 1

        return result.lstrip('0') or '0'