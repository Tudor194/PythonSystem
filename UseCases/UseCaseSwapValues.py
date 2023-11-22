from ProjectComponents.ImportLib import *

class UseCaseSwapValues():
    '''
    This TestStep show me a <-> b
    '''
    def Execute(self):
        a = 5
        b = 4
        a, b = Basics.SwapValues(a, b)
        print(a)
        print(b)

        str1 = 'Hello'
        str2 = 'Aloha'
        x, y = Basics.SwapValues(str1, str2)
        print(x, y)

        l1 = [1, 0]
        l2 = [0, 0, 1]
        l3, l4 = Basics.SwapValues(l1, l2)
        print(l3, l4)

UseCaseSwapValues = UseCaseSwapValues()

UseCaseSwapValues.Execute()