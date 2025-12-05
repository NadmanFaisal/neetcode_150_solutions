class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd
            stack.append([t, i])
        return output

if __name__ == "__main__":
    sol = Solution()
    input = [30,38,30,36,35,40,28]
    print(sol.dailyTemperatures())
