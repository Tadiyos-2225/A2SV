class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        num_list=[]
        for x in range(1,n+1):
                if x % 3 == 0 and x % 5 == 0:
                    result="FizzBuzz"
                    num_list.append(result)
                elif x % 3 == 0:
                    result="Fizz"
                    num_list.append(result)
                elif x % 5 == 0:
                    result="Buzz"
                    num_list.append(result)
                else:
                    num_list.append(str(x))   
        return num_list
            
            
            