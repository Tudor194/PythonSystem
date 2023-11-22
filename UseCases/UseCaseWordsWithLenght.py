from ProjectComponents.ImportLib import *

class UseCaseWordsWithLenght():
    '''
    This TestStep show me the words with data length
    '''
    def Execute(self):
        x = Basics.PrintWordsWithLength(red = "RED", car = "Ford")
        print(x)

        y = Basics.PrintWordsWithLengthWithoutKey(car = "VW")
        print(y)

UseCaseWordsWithLenght = UseCaseWordsWithLenght()

UseCaseWordsWithLenght.Execute()