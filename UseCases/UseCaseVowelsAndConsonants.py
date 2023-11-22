from ProjectComponents.ImportLib import *

class UseCaseVowelsAndConsonants():
    '''
    This TestStep show me the words with data length
    '''
    def Execute(self):
        charset_string = "vowels of a word"
        Basics.PrintListOfVowels(charset_string)
        Basics.PrintStringOfVowels(charset_string)
        Basics.PrintDictOfVowels(charset_string)
        print(Basics.CheckNumberOfVowels(charset_string))

        Basics.PrintListOfConsonants(charset_string)
        Basics.PrintStringOfConsonants(charset_string)
        Basics.PrintDictOfConsonants(charset_string)
        print(Basics.CheckNumberOfConsonants(charset_string))

UseCaseVowelsAndConsonants = UseCaseVowelsAndConsonants()

UseCaseVowelsAndConsonants.Execute()