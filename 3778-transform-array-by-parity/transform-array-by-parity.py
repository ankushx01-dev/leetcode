class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        zero=0
        for num in nums:
            if num%2==0:
                zero+=1
        return [0]*zero + [1]*(len(nums)-zero)