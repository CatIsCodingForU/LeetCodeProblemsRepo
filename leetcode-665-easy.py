def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    counter = 0
    raising = False
    maximum = nums[0]
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1] or nums[i+1] < maximum:
            raising = True
            maximum = nums[i+1]
            continue
        else:
            if raising:
                nums[i + 1] = nums[i]
            else:
                nums[i] = nums[i+1]
            raising = False
            counter += 1
        if counter > 1:
            return False
        else:
            continue
    print(nums)
    return True

print(checkPossibility([-1,4,2,3]))
