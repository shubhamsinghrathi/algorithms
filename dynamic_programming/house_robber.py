'''
Problem Statement:
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each 
of them is that adjacent houses have security system connected and it will automatically contact the 
police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the 
maximum amount of money you can rob tonight without alerting the police.

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Solution Approach:-
Here, we are using recursion. So, if the robber choose house "n"th to rob then he can rob n'th and max loot from houses from "n-2",
but, if the robber choose "n-1"th then he can take loot from n'th house hence ans will be max loot till n-1'th house
Here, to make the calculation faster we are using memoization
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.catch = {}
        return self.result(nums, len(nums)-1)
    
    def result(self, nums, n):
        try:
            return self.catch[n]
        except:
            if n<0:
                self.catch[n] = 0
                return self.catch[n]
            self.catch[n] = max( (self.result(nums, n-2) + nums[n]), self.result(nums, n-1) )
            return self.catch[n]