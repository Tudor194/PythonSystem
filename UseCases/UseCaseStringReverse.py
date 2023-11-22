from ProjectComponents.ImportLib import *

class UseCaseStringReverse():
    '''
    This TestStep show me the reverse strings
    '''
    def Execute(self):
        str1 = 'Hello'
        str1 = Basics.ReverseString(str1)
        print(str1)

UseCaseStringReverse = UseCaseStringReverse()

UseCaseStringReverse.Execute()