def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, value in enumerate(nums):
            abt = target - nums[i]
            
            if abt in seen:
                return [i, seen[abt]]
            
            seen[value] = i
