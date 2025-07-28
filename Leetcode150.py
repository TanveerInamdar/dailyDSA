class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                x = stk[-1] + stk[-2]
                stk.pop()
                stk.pop()
                stk.append(x)

            elif tokens[i] == "-":
                x = stk[-2] - stk[-1]
                stk.pop()
                stk.pop()
                stk.append(x)

            elif tokens[i] == "*":
                x = stk[-1] * stk[-2]
                stk.pop()
                stk.pop()
                stk.append(x)
            elif tokens[i] == "/":
                x = int(stk[-2] / stk[-1])

                stk.pop()
                stk.pop()
                stk.append(x)
            else:
                x = int(tokens[i])
                stk.append(x)
        return stk[-1]
