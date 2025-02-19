class Solution:
    """
    Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]

    Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

    Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    """
    def fizzBuzz(self, n: int) -> list[str]:
        newList = []
        for number in range(1, n+1):
            #if the number is divisible by 3 add Fizz to the new list
            if(number % 3 == 0 and number % 5 == 0):
                newList.append("FizzBuzz")
            elif(number % 5 == 0):
                newList.append("Buzz")
            elif(number % 3 == 0):
                newList.append("Fizz")
            else:
                newList.append(str(number))
        print(newList)
        return newList
    
solution = Solution()
solution.fizzBuzz(3)