class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1  # Pointer for the next unique element
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # If current element is not a duplicate
                nums[write_index] = nums[i]  # Move unique element to the correct position
                write_index += 1
        
        return write_index  # Number of unique elements
