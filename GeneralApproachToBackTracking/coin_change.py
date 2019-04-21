"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""

'''
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1


Example 2:
Input: coins = [2], amount = 3
Output: -1
'''



class Solution:

    def coinChange(self, coins, amount):
        cache = dict()
        self.backtrack(cache, coins, amount)
        return -1 if cache[amount] == float("inf") else cache[amount]

    def backtrack(self, cache, coins, amount):

        if amount in cache:
            return cache[amount]

        if amount == 0:
            cache[amount] = 0
            return 0


        cache[amount] = float("inf")
        for i in range(len(coins)):

            new_amount = amount - coins[i]
            if new_amount >= 0:
                curr = self.backtrack(cache, coins, new_amount) + 1
                cache[amount] = min(cache[amount], curr)

        return cache[amount]




if __name__ == "__main__":

   three = Solution().coinChange([1, 2, 5], 11)
   print(three, three == 3)

   neg_one = Solution().coinChange([2], 3)
   print(neg_one, neg_one == -1)


   neg_one = Solution().coinChange([2], 0)
   print(neg_one, neg_one == 0)
