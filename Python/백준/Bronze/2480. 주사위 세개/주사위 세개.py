nums = list(map(int, input().split()))
nums.sort()
if(nums[0] == nums[1] and nums[1] == nums[2]):
    print(10000 + nums[0] * 1000)
elif(nums[0] == nums[1]):
    print(1000 + nums[0] * 100)
elif(nums[1] == nums[2]):
    print(1000 + nums[1] * 100)
else:
    print(nums[2] * 100)
