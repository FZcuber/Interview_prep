def twoSum(nums, target):
    dic = {}

    for i, v in enumerate(nums):
        diff = target - v

        if diff in dic:
            return [dic[diff], i]

        dic[v] = i
