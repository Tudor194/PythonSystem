from ProjectComponents.ImportLib import *

class UseCaseNumbers():
    def Execute(self):
        print(Basics.CheckIsPrime(12))

        x = 14
        y = 15
        print(Basics.CheckIsEven(x))
        print(Basics.CheckIsEvenBitwise(x))
        print(Basics.CheckIsEven(y))
        print(Basics.CheckIsEvenBitwise(y))

        print(Basics.CheckIsOdd(x))
        print(Basics.CheckIsOddBitwise(x))
        print(Basics.CheckIsOdd(y))
        print(Basics.CheckIsOddBitwise(y))

        a = 68
        Basics.PrintAllDividers(a)
        ls = Basics.PrintListOfAllDividers(a)
        print(ls)
        Basics.PrintImproperDividers(12)
        ls_impr = Basics.PrintListOfAllImproperDividers(12)
        print(ls_impr)

        resp = Basics.CheckIsDivider(67, 5)
        print(resp)

UseCaseNumbers = UseCaseNumbers()

UseCaseNumbers.Execute()