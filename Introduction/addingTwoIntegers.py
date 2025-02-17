class Solution(object):
    def sum(self, num1: int, num2: int) -> int:
        finalValue = num1 + num2
        print("The two numbers added together is", finalValue)
        return finalValue

#create an instance of solution
solution = Solution()

#call the sum function similar to how we create a method in main() than create
#an object of the method to run the function

solution.sum(3, 5)