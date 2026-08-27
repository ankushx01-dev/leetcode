class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def lowerBound(nums,target):
            low=0
            high=n-1
            lb=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    lb=mid
                    high=mid-1
                else:
                    low=mid+1
            return lb
        def upperBound(nums,target):
            low=0
            high=n-1
            ub=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>target:
                    ub=mid
                    high=mid-1
                else:
                    low=mid+1
            return ub
        first =lowerBound(nums,target)
        if first == n or nums[first] != target:
            return [-1,-1]
        last = upperBound(nums,target)-1
        return [first ,last]