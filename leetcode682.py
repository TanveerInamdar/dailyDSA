class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        total = 0
        for i in range(len(operations)):

            if operations[i] == "+":
                adder = int(stk[-1]) + int(stk[-2])
                stk.append(adder)
                total += adder
            elif operations[i] == "D":
                doubler = 2 * int(stk[-1])
                total += doubler
                stk.append(doubler)
            elif operations[i] == "C":
                x = stk.pop()
                total -= int(x)
            else:
                stk.append(operations[i])
                total += int(operations[i])
        return total
