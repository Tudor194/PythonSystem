from Lib.KeywordBase.Config.Constants import *
#from Lib.KeywordBase.Basics.Basics import Basics
from ProjectComponents.Basics.Basics import Basics

class TRAINING():
    def Fibonacci(self, n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def func(self):
        str1 = 'Hello'
        str1 = Basics.ReverseString(str1)
        print(str1)
        print("Algo!!!!!!")