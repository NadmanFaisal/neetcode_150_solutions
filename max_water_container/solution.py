def maxArea(heights: list[int]) -> int:
    lP = 0
    rP = len(heights) - 1
    
    leftHeight = heights[lP]
    rightHeight = heights[rP]

    maxArea = 0

    while lP < rP:
        area = (rP - lP ) * min(heights[lP], heights[rP])
        if area > maxArea:
            maxArea = area

        if heights[lP] < heights[rP]:
            lP += 1
        else:
            rP -= 1
    return maxArea


input_list = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
print(maxArea(input_list))
