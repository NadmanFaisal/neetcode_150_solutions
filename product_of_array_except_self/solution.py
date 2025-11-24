def productExceptSelf(nums: list[int]) -> list[int]:
    output = [0] * len(nums)
    prefix = [0] * len(nums)
    postfix = [0] * len(nums)

    i = len(nums) - 1
    j = 0
    while(j <= i):
        if (j == 0):
            prefix[j] = 1 * nums[j]
        else:
            prefix[j] = prefix[j - 1] * nums[j]
        j = j + 1

    while(i >= 0):
        if (i == (len(nums) - 1)):
            postfix[i] = nums[i] * 1
        else:
            postfix[i] = nums[i] * postfix[i + 1]
        i = i - 1

    l = len(nums)
    for k in range(len(nums)):
        if k > 0:
            prefix_prod = prefix[k - 1]
        else:
            prefix_prod = 1

        if k < l - 1:
            postfix_prod = postfix[k + 1]
        else:
            postfix_prod = 1

        output[k] = prefix_prod * postfix_prod 
    
    return output

nums = [1,2,4,6]
print(productExceptSelf(nums))

