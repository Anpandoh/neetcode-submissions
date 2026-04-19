class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        intStack = []

        for token in tokens:
            if token in ['*','+','-','/']:
                secondNum = intStack.pop(-1)
                firstNum = intStack.pop(-1)
                res = 0
                match(token):
                    case('*'):
                        res = firstNum * secondNum
                    case('+'):
                        res = firstNum + secondNum
                    case('-'):
                        res = firstNum - secondNum
                    case('/'):
                        res = int(float(firstNum / secondNum))
                intStack.append(res)
            else:
                intStack.append(int(token))


        return intStack.pop(0)

        