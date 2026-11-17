class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Use a stack to keep track of the succession of the scores

        # 1. Empty stack (implemented as a list)
        records = []

        for op in operations:
            
            if op == "+":
                records.append(int(records[-1]) + int(records[-2]))
            elif op == "D":
                records.append(int(records[-1]) * 2)
            elif op == "C":
                records.pop()
            else:
                records.append(op)

        res = 0
        for number in records:
            res += int(number)
        return res