#!/usr/bin/env python3
# RemoveDuplicates.py
# Author : Shipra

class Solution(object):
    def removeDuplicates(self, nums):
        """
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
        Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
        """

        count = 1
        j = 1
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                i = i+1
            else:
                nums[j] = nums[i+1]
                count +=1
                j = j+1
                i = i+1

        return count


nums = [1,2,2,3,3,4]
obj = Solution()
print(obj.removeDuplicates(nums))
