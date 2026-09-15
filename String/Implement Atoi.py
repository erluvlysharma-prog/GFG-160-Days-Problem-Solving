class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Step 1: Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Read digits
        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit

            # Step 4: Check overflow
            if num > 2147483647:
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648

            i += 1

        return sign * num