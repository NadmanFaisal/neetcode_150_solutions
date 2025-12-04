import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        operation_stack = []
        answer = 0

        for token in tokens:
            if token == "+":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(num_1 + num_2)
            elif token == "-":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(num_1 - num_2)
            elif token == "*":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(num_1 * num_2)
            elif token == "/":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(int(num_1 / num_2))
            else:
                num_stack.append(int(token))

        print("Len: ", len(num_stack))

        print("Num stack: ", num_stack)
        return num_stack[-1]


if __name__ == "__main__":
    sol = Solution()
    s = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(s))
