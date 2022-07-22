def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]
    current_max = nums[0]
    leng = len(nums)
    for i in range(1, leng):
        current_max = max(nums[i], nums[i] + current_max)
        res = max(res, current_max)
    return res