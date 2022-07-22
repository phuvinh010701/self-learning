def bin_search(self, nums, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bin_search(nums, left, mid - 1, target)
        else:
            return self.bin_search(nums, mid + 1, right, target)
    else:
        return -1
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return self.bin_search(nums, 0, len(nums) - 1, target)