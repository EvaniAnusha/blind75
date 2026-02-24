class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # initialize xor var with 0
        # when perfoming ex-or operation, xor with 0 gives xor, xor with 1 gives toggle bit 
        xor = 0
        n = len(nums)
        # compute the total xor for numbers from 0 to n (inclusive)
        for i in range(0, n+1, 1):
            xor = xor ^ i
        # when ex-or operation is done b/n numbers from array and total xor
        # the duplicate numbers will nullify, leaving the resulting xor with the missing number 
        for i in range(n):
            xor = xor ^ nums[i]
        # return the resultant missing Number
        return xor
        
