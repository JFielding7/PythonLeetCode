class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        quotient_pos = (dividend < 0) == (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient_digits = []
        dividend_str = str(dividend)
        curr_dividend = 0

        for digit in dividend_str:
            curr_dividend = int(f"{curr_dividend}{digit}")
            factor = 0
            divisor_mult = divisor

            while divisor_mult <= curr_dividend:
                factor += 1
                divisor_mult += divisor

            quotient_digits.append(str(factor))
            curr_dividend -= divisor_mult - divisor

        quotient_magnitude = int("".join(quotient_digits))
        quotient = quotient_magnitude if quotient_pos else -quotient_magnitude
        return quotient if quotient < (1 << 31) else (1 << 31) - 1