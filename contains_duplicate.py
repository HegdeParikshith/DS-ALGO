def containsDuplicate( nums) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if(nums[i] == nums[i+1]):
            return True
    return False

print(containsDuplicate([1,2,1,1]))