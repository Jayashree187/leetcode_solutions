class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract using powers of 2
        while dividend >= divisor:
            value = divisor
            count = 1

            while dividend >= value + value:
                value += value
                count += count

            dividend -= value
            quotient += count

        if negative:
            quotient = -quotient

        return quotient
