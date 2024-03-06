def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    len_nums = len(nums)
    nums.sort()
    max_num = max(nums)
    min_num = min(nums)

    if len(nums) == 3:
        if (nums[0] + nums[1] + nums[2] == 0):
            res.append([nums[0], nums[1], nums[2]])
            return res
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            if max_num != 0 and min_num != 0 and not(nums[i] == 0) and not(nums[j] == 0):
                if nums[i] + nums[j] >= max_num:
                    print('пропустил на значениях', nums[i], nums[j] , 'max')
                    continue
                else:
                    if nums[i] + nums[j] <= min_num:
                        print('пропустил на значениях', nums[i], nums[j], 'min')
                        continue
            for k in range(j + 1, len_nums):
                try:

                    if nums[i] + nums[j] + nums[k] == 0:
                        a = [nums[i], nums[j], nums[k]]
                        a.sort()
                        if a not in res:
                            res.append(a)
                except IndexError:
                    continue
    return res


nums = [3,0,-2,-1,1,2]
print(threeSum(nums=nums))
print("Expected [[-2,-1,3],[-2,0,2],[-1,0,1]]")
