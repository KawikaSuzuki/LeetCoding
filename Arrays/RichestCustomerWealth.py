class Solution:
    """
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
    Explanation:
    1st customer has wealth = 1 + 2 + 3 = 6
    2nd customer has wealth = 3 + 2 + 1 = 6
    Both customers are considered the richest with a wealth of 6 each, so return 6.
    """
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        #track the customer with the most wealth
        maxWealthSoFar = 0
        
        #go through a for each loop looking at each customer than their wealth in each bank
        for customer in accounts:
            currentCustomerWealth = 0
            for bank in customer:
                #we can add all the money from the banks to the current customer 
                currentCustomerWealth += bank
            
            #we than compare the max wealth so far with the current customer and if the current customer is higher replace
            maxWealthSoFar = max(maxWealthSoFar, currentCustomerWealth)
        
        print(maxWealthSoFar)
        return maxWealthSoFar
    

solution = Solution()
    
solution.maximumWealth([[1,2,1],[2,2,1]])