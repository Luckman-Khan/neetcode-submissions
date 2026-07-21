class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')','[':']','{':'}'}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if not stack:
                    return False
                val = stack.pop()
                if mapping[val] != ch:
                    return False
        return len(stack) == 0
