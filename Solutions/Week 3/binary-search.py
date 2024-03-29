class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        i = 0
        j = len(nums)-1
        while i<=j:
            mid = i+(j-i)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                j = mid-1
            else:
                i = mid+1
        return -1