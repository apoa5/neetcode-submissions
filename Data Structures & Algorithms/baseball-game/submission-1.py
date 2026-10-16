class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "+":
                prevsum = record[-1] + record[-2]
                record.append(prevsum)
            elif op == "D":
                product = record[-1] * 2
                record.append(product)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)