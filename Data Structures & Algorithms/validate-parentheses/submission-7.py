class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {')':'(',']':'[','}':'{'}
        for ch in s:

            if ch in ('(','{','['):
                stack.append(ch)
            elif ch in (')','}',']') and stack:
                c = stack.pop()

                if mapping[ch] != c:
                    return False
            elif ch and not stack:
                return False
        if stack:
            return False
        return True


        