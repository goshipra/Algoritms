#!/usr/bin/env python3
# Sqrt.py
# Author : Shipra

class Solution(object):
    def mySqrt(self, x):
        """
        Given a non-negative integer x, compute and return the square root of x.
        Since the return type is an integer, the decimal digits are truncated,
        and only the integer part of the result is returned.
        Note: You are not allowed to use any built-in exponent function or
        operator, such as pow(x, 0.5) or x ** 0.5.

       """
        start = 0
        end = x

        while start + 1 < end:
            mid = start + (end - start) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid

        if end * end == x:
            return end

        return start



target = 4
obj = Solution()
print(obj.mySqrt(target))
