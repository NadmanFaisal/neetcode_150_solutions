def productExceptSelf(nums: list[int]) -> list[int]:
    output = []
    for i in range(len(nums)):
        current_product = 1
        for j in range(0, len(nums)):
            if j != i:
                current_product *= nums[j]
        output.append(current_product)
    return output

nums = [1,2,4,6]
print(productExceptSelf(nums))

