from re import match

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(match(r"^[+-]?(\d+|\d+\.\d*|\d*\.\d+)([eE][+-]?(\d+))?$", s))
