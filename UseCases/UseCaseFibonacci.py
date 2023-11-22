from ProjectComponents.ImportLib import *

class UseCaseFibonacci():
    def Execute(self):
        x = Algorithms.PrintFibonacciLessThanN(56)
        print(x)
        print(Algorithms.ReturnNTHFibonacciNumber(10))
        Algorithms.PrintFirstNFibonacciNumbers(5)
        print(Algorithms.CheckIfNumberIsFibonacci(13))

UseCaseFibonacci = UseCaseFibonacci()

UseCaseFibonacci.Execute()