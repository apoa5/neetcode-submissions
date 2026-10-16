class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack and stack[-1] == matching[c]:
                    stack.pop()
                else:
                    return False
        return not stack
             

