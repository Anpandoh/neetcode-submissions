class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #O(n) w/ division
        #multiply all then divide by amount of curr element

        #O(n^2) w/o division
        #brute force, multiply the rest

        #O(n) w/o division
        #save array of every value below and after the curr element (post and prefix arrays)
        prefix = []
        postfix = []
        prevNum = 1
        for num in nums:
            newNum = num*prevNum
            prefix.append(newNum)
            prevNum = newNum

        prevNum = 1
        for i in range(len(nums) - 1, -1, -1):
            newNum = nums[i]*prevNum
            postfix.insert(0, newNum)
            prevNum = newNum
        
        print(prefix)
        print(postfix)
        res = []
        for i in range(len(nums)):
            if i == 0:
                pre = 1
            else:
                pre = prefix[i-1]
            if i + 1 >= len(nums):
                pos = 1
            else:
                pos = postfix[i+1]

            res.append(pre * pos)
        
        return res



        