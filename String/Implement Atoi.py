'''Given a string s, convert it into a 32-bit signed integer (similar to the atoi() function) without using any built-in conversion functions.
The conversion follows these rules:

Ignore Leading Whitespaces: Skip all leading whitespace characters.
Check Sign: If the next character is either '+' or '-', take it as the sign of the number. If no sign is present, assume the number is positive.
Read Digits: Read the digits and ignore any leading zeros. Stop reading when a non-digit character is encountered or the end of the string is reached. If no digits are found, return 0.
Handle Overflow: If the number exceeds the range of a 32-bit signed integer:
Return 2³¹ − 1 (i.e., 2147483647) if it is greater than the maximum value.
Return −2³¹ (i.e., -2147483648) if it is smaller than the minimum value.
Return the final integer value.'''


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