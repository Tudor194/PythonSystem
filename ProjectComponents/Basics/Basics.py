from Lib.KeywordBase.Basics.Basics import Basics
from Lib.KeywordBase.Config.Constants import *

class Basics(Basics):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def PrintWordsWithLengthWithoutKey(self, **kwargs):
        '''key, value -> len(value)'''
        try:
            for key, value in kwargs.items():
                print(key, value)
                print("Word for value:", value, ", Length: ", len(value))
                print()
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckNumberOfVowels(self, charset_string):
        '''vowels of a word -> 5'''
        try:
            vowels = set("aeiouAEIOU")
            cnt = 0
            for _char in charset_string:
                if _char in vowels:
                    cnt += 1

            return cnt
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckNumberOfConsonants(self, charset_string):
        '''vowels of a word -> 8'''
        try:
            vowels = set("aeiouAEIOU")
            cnt = 0
            for _char in charset_string:
                if _char not in vowels and _char.isalpha():
                    cnt += 1

            return cnt
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsEvenBitwise(self, x):
        '''x % 2 == 0'''
        try:
            result = c_TRUE
            if x & 1:
                result &= c_FALSE
                #print(x, "is not even!")
                return result
            else:
                #print(x, "is even!")
                return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsOddBitwise(self, x):
        '''x % 2 == 1'''
        try:
            result = c_TRUE
            if x & 1 == 0:
                result &= c_FALSE
                # print(x, "is not odd!")
                return result
            else:
                # print(x, "is odd!")
                return result
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnIndexOfKeyInDictWithList(self, x, the_dict):
        '''
                Example:
                x = 'abcd'
                the_dict = {
                    1: 1.3,
                    'as': 2,
                    'abcd': 3,
                    'abcd': 4,
                }
                -> [2]
                '''
        try:
            list_dict = list(the_dict.items())
            results = [i for i, key in enumerate(list_dict) if key[0] == x]
            return results
        except TypeError:
            print("Error: Incorrect data type!")
    def ReturnIndexOfKeyInDictWithStr(self, x, the_dict):
        '''
        Example:
        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 2,
            'abcd': 3,
            'abcd': 4,
        }
        -> 2
        '''
        try:
            return str(list(the_dict.keys()).index(x))
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnIndexOfKeyInDictWithForStatement(self, x, the_dict):
        '''
        Example:
        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 2,
            'abcd': 3,
            'abcd': 4,
        }
        -> 2
        '''
        try:
            index = None
            for i, key in enumerate(the_dict.keys()):
                if key == x:
                    index = i
                    return format(index)
        except TypeError:
            print("Error: Incorrect data type!")
    def SortListDescendindWithRepeat1(self, my_list):
        """
        :param my_list: [1, 2, 4, 3, 7, 6, 5, 5]
        :return: [7, 6, 5, 4, 3, 2, 1]
        """
        try:
            converted_list_to_set = set(my_list)
            my_list = list(converted_list_to_set)
            my_list.sort(reverse = c_ACTIVE)
            return  my_list
        except TypeError:
            print("Error: Incorrect data type!")

    def SortAscendingDictKeysWitHRepeat1(self, my_dict):
        """
        :param my_dict:
        {
            'a': 1,
            'b': 2,
            'c': 3,
            'a': 4,
            'b': 5
        }
        :return: {'a': 4, 'b': 5, 'c': 3}
        """
        try:
            converted_dict_to_list = list(my_dict.items())
            converted_dict_to_list = list(set(converted_dict_to_list))
            converted_dict_to_list = sorted(converted_dict_to_list, key=lambda x: x[0])
            my_dict = dict(converted_dict_to_list)
            return my_dict
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDescendingDictKeysWitHRepeat1(self, my_dict):
        """
        :param my_dict:
        {
            'a': 1,
            'b': 2,
            'c': 3,
            'a': 4,
            'b': 5
        }
        :return: {'c': 3, 'b': 5, 'a': 4}
        """
        try:
            converted_dict_to_list = list(my_dict.items())
            converted_dict_to_list = list(set(converted_dict_to_list))
            converted_dict_to_list = sorted(converted_dict_to_list, key=lambda x: x[0], reverse = c_ACTIVE)
            my_dict = dict(converted_dict_to_list)
            return my_dict
        except TypeError:
            print("Error: Incorrect data type!")
    def SortAscendingDictValuesWitHRepeat1(self, my_dict):
        """
        :param my_dict:
        {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 1,
            'e': 2
        }
        :return: {'a': 1, 'd': 1, 'e': 2, 'b': 2, 'c': 3}
        """
        try:
            converted_dict_to_list = list(my_dict.items())
            converted_dict_to_list = list(set(converted_dict_to_list))
            converted_dict_to_list = sorted(converted_dict_to_list, key=lambda x: x[1])
            my_dict = dict(converted_dict_to_list)
            return my_dict
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDescendingDictValuesWitHRepeat1(self, my_dict):
        """
        :param my_dict:
        {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 1,
            'e': 2
        }
        :return: {'c': 3, 'e': 2, 'b': 2, 'a': 1, 'd': 1}
        """
        try:
            converted_dict_to_list = list(my_dict.items())
            converted_dict_to_list = list(set(converted_dict_to_list))
            converted_dict_to_list = sorted(converted_dict_to_list, key=lambda x: x[1], reverse = c_ACTIVE)
            my_dict = dict(converted_dict_to_list)
            return my_dict
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnListPermutationWithSlicing(self, my_list, number_of_repetitions = 0, left = 0, right = 0):
        """
        :param my_list: [1, 2, 3, 4, 5]
        :param number_of_repetitions: 2
        :param left: 0
        :param right: 1
        :return: [4, 5, 1, 2, 3]
        """
        try:
            if left == c_ON and right == c_OFF:
                p1 = my_list[:number_of_repetitions]
                p2 = my_list[number_of_repetitions:]
                my_list = p2 + p1
                return my_list
            elif left == c_OFF and right == c_ON:
                p1 = my_list[-number_of_repetitions:]
                p2 = my_list[:-number_of_repetitions]
                my_list = p1 + p2
                return my_list
            elif left == c_ON and right == c_ON:
                print("Error: Only one side!")
            elif left == c_OFF and right == c_OFF:
                print("Error: One side must be 1!")
            else:
                print("Error: Invalid parameters!")
        except TypeError:
            print("Error: Incorrect data type!")

Basics = Basics()