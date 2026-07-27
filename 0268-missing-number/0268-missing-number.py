class Solution(object):
    def missingNumber(self, nums):
        summ=0
        n=len(nums)

        for i in range(0,n):
            summ=summ+nums[i]
        
        m=n*(n+1)//2
        return m-summ
        