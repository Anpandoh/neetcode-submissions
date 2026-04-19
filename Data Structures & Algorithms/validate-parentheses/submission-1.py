class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []
        forwardParenthesis = {'{', '[', '('}
        for char in s:
            if char in forwardParenthesis:
                stack.append(char)
            else:
                if not stack:
                    return False
                matching = stack.pop(-1)
                if char == '}' and matching != '{':
                    return False
                if char == ']' and matching != '[':
                    return False
                if char == ')' and matching != '(':
                    return False
        
        if stack:
            return False
        
        return True

