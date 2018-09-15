class Solution(object):
    def isValid(self, input):
        """
        input: string input
        return: boolean
        """
        # write your solution here
        stack = []

        for ch in input:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif ch == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif ch == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif ch == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
        return len(stack) == 0