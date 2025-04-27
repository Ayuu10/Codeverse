class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        for c in num:
            while k and s and s[-1] > c:
                s.pop()
                k -= 1
            s.append(c)
        
        s = s[:len(s) - k]
        return ''.join(s).lstrip('0') or '0'
