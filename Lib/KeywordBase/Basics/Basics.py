from Lib.KeywordBase.Config.Constants import *

class Basics():
    '''Common'''
    def SwapValues(self, var1, var2):
        '''Numbers or anything'''
        try:
            aux = var1
            var1 = var2
            var2 = aux
            return var1, var2
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsInTheList(self, x, the_list):
        '''
        Example:
        the_list = ['a2', '2', 3, [2, 3, '4', 'as']]
        x = [2, 3, '4', 'as']
        -> 1
        '''
        try:
            result = c_TRUE
            result &= x in the_list
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnTheIndexFromTheList(self, x, the_list):
        '''
        Return the first index:
        Example: x = 7, the_list = [8, 'hu', 7, 7, 8] -> 2
        '''
        try:
            try:
                return the_list.index(x)
            except ValueError:
                return 0
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnAllIndexesFromTheList(self, x, the_list):
        '''
        Example: x = 7, the_list = [8, 'hu', 7, 7, 8] -> [2, 3]
        Example: x = 7, the_list = [8, 'hu', 4, 5, 8] -> []
        '''
        try:
            return [i for i, y in enumerate(the_list) if y == x]
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckValueIsInTheDict(self, x, the_dict):
        '''
        Example:
        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 2,
            'x': 3,
            'y': 'abcd'
        }
        '''
        try:
            result = c_TRUE
            if x in the_dict.values():
                result &= c_TRUE
                return result
            else:
                result &= c_FALSE
                return  result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckKeyIsInTheDict(self, x, the_dict):
        '''
        Example:
        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 2,
            'abcd': 3,
        }
        '''
        try:
            result = c_TRUE
            if x in the_dict.keys():
                result &= c_TRUE
                return result
            else:
                result &= c_FALSE
                return  result
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnIndexOfValueInDict(self, x, the_dict):
        '''
        Example:

        '''
        pass

        '''
        try:
            try:
                return next(i for i, v in enumerate(the_dict.values()) if v == x)
            except StopIteration:
                return 0
        except TypeError:
            print("Error: Incorrect data type!")
        '''

    def ReturnIndexOfKeyInDict(self, x, the_dict):
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
            if x in the_dict:
                return list(the_dict).index(x)
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnAllKeysIndexInDict(self, x, the_dict):
        '''
        Example:
        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 'abcd',
            'x': 'abcd',
            'y': 4,
        }
        -> ['as', 'x']
        '''
        try:
            def find_key(value, dictionary):
                try:
                    for k, v in dictionary.items():
                        if v == value:
                            yield k
                except TypeError:
                    print("Error: Incorrect data type!")
            positions = list(find_key(x, the_dict))
            return positions
        except TypeError:
            print("Error: Incorrect data type!")

    def SortListAscending(self, my_list):
        '''
        Example: my_list = [5, 2, 7, 9, 1] -> [1, 2, 5, 7, 9]
        '''
        try:
            my_list.sort()
            return my_list
        except TypeError:
            print("Error: Incorrect data type!")

    def SortListDescending(self, my_list):
        '''
        Example: my_list = [5, 2, 7, 9, 1] -> [9, 7, 5, 2, 1]
        '''
        try:
            my_list.sort(reverse = c_ACTIVE)
            return my_list
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDictValuesAscending(self, my_dict):
        '''
        my_dict = {
            "1": 1.3,
            "x": 9,
            "b": 7,
            "e": 4,
        }
        -> {'1': 1.3, 'e': 4, 'b': 7, 'x': 9}
        '''
        try:
            return dict(sorted(my_dict.items(), key = lambda x: x[1]))
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDictValuesDescending(self, my_dict):
        '''
        my_dict = {
            "1": 1.3,
            "x": 9,
            "b": 7,
            "e": 4,
        }
        -> {'x': 9, 'b': 7, 'e': 4, '1': 1.3}
        '''
        try:
            return dict(sorted(my_dict.items(), key = lambda x: x[1], reverse = c_ACTIVE))
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDictKeysAscending(self, my_dict):
        '''
        my_dict = {
            "1": 1.3,
            "x": 9,
            "b": 7,
            "e": 4,
        }
        -> {'1': 1.3, 'b': 7, 'e': 4, 'x': 9}
        '''
        try:
            return dict(sorted(my_dict.items(), key = lambda x: x[0]))
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDictKeysDescending(self, my_dict):
        '''
        my_dict = {
            "1": 1.3,
            "x": 9,
            "b": 7,
            "e": 4,
        }
        -> {'x': 9, 'e': 4, 'b': 7, '1': 1.3}
        '''
        try:
            return dict(sorted(my_dict.items(), key = lambda x: x[0], reverse = c_ACTIVE))
        except TypeError:
            print("Error: Incorrect data type!")

    def SortTupleAscending(self, my_tuple):
        """
        :param my_tuple: (5, 9, 2, 1, 7)
        :return: (1, 2, 5, 7, 9)
        """
        try:
            _tuple = sorted(my_tuple)
            #print(_tuple)
            return tuple(_tuple)
        except TypeError:
            print("Error: Incorrect data type!")

    def SortTupleDescending(self, my_tuple):
        """
        :param my_tuple: (5, 9, 2, 1, 7)
        :return: (9, 7, 5, 2, 1)
        """
        try:
            _tuple = sorted(my_tuple, reverse = c_ACTIVE)
            #print(_tuple)
            return tuple(_tuple)
        except TypeError:
            print("Error: Incorrect data type!")

    def SortSetAscending(self, my_set):
        """
        :param my_set: {1, 4, 2, 6, 3}
        :return: {1, 2, 3, 4, 6}
        """
        try:
            _set = sorted(my_set)
            #print(_set)
            return set(_set)
        except TypeError:
            print("Error: Incorrect data type!")

    def SortSetDescending(self, my_set):
        """
        :param my_set: {1, 4, 2, 6, 3}
        :return: [6, 4, 3, 2, 1] OR {1, 2, 3, 4, 6}
        """
        try:
            _set = sorted(my_set, reverse = c_ACTIVE)
            print(_set)
            #return set(_set)
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfListIsSortedAscending(self, my_list):
        """
        :param my_list: [1, 2, 4, 6, 7, 8, 10]
        :return: True
        """
        try:
            result = c_TRUE
            if my_list != sorted(my_list):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfListIsSortedDescending(self, my_list):
        """
        :param my_list: [9, 6, 7, 2, 1, 0]
        :return: True
        """
        try:
            result = c_TRUE
            if my_list != sorted(my_list, reverse = c_ACTIVE):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfDictValuesAreSortedAscending(self, my_dict):
        """
        :param my_dict:
        my_dict = {
            "a": "a",
            "c": "c",
            "d": "d"
        }
        :return: True
        """
        try:
            result = c_TRUE
            if list(my_dict.values()) != sorted(my_dict.values()):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfDictValuesAreSortedDescending(self, my_dict):
        """
        :param my_dict:
        my_dict = {
            "a": "d",
            "c": "c",
            "d": "a"
        }
        :return: True
        """
        try:
            result = c_TRUE
            if list(my_dict.values()) != sorted(my_dict.values(), reverse = c_TRUE):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfDictKeysAreAscending(self, my_dict):
        """
        :param my_dict:
        my_dict = {
            "a": "a",
            "c": "c",
            "d": "d"
        }
        :return: True
        """
        try:
            result = c_TRUE
            if list(my_dict.keys()) != sorted(my_dict.keys()):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfDictKeysAreDescending(self, my_dict):
        """
        :param my_dict:
        my_dict = {
            9: '9',
            8: '8'
        }
        :return: True
        """
        try:
            result = c_TRUE
            if list(my_dict.keys()) != sorted(my_dict.keys(), reverse = c_TRUE):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfTupleIsAscending(self, my_tuple):
        """
        :param my_tuple: (1, 2, 3)
        :return: True
        """
        try:
            result = c_TRUE
            if sorted(my_tuple) != list(my_tuple):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfTupleIsDescending(self, my_tuple):
        """
        :param my_tuple: (1, 2, 3)
        :return: True
        """
        try:
            result = c_TRUE
            if sorted(my_tuple, reverse = c_ACTIVE) != list(my_tuple):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfSetIsAscending(self, my_set):
        """
        :param my_set: {1, 2, 3, 4}
        :return: True
        """
        try:
            result = c_TRUE
            if sorted(my_set) != list(my_set):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfSetIsDescending(self, my_set):
        """
        :param my_set: {4, 3, 2, 1}
        :return: True
        """
        '''
        try:
            result = c_TRUE
            #print(sorted(my_set, reverse = c_ACTIVE))
            print(list(my_set))
            if sorted(my_set, reverse = c_ACTIVE) != list(my_set):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")
        '''
        pass

    def ReturnDataTypeLength(self, x):
        """
        :param x: tuple, dict, string, list, set (without numbers)
        :return: int number
        """
        try:
            return len(x)
        except TypeError:
            print("Error: Incorrect data type!")

    def SortListAscendindWithRepeat1(self, my_list):
        """
        :param my_list: [1, 2, 4, 3, 7, 6, 5, 5]
        :return: [1, 2, 3, 4, 5, 6, 7]
        """
        try:
            converted_list_to_set = set(my_list)
            my_list = list(converted_list_to_set)
            my_list.sort()
            return  my_list
        except TypeError:
            print("Error: Incorrect data type!")

    def SortAscendingTupleWithRepeat1(self, my_tuple):
        """
        :param my_tuple: (3, 2, 4, 1, 2, 3, 5)
        :return: (1, 2, 3, 4, 5)
        """
        try:
            converted_tuple_to_list = list(my_tuple)
            converted_tuple_to_list = list(set(my_tuple))
            converted_tuple_to_list.sort()
            my_tuple = tuple(converted_tuple_to_list)
            return my_tuple
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDescendingTupleWithRepeat1(self, my_tuple):
        """
        :param my_tuple: (3, 2, 4, 1, 2, 3, 5)
        :return: (5, 4, 3, 2, 1)
        """
        try:
            converted_tuple_to_list = list(my_tuple)
            converted_tuple_to_list = list(set(my_tuple))
            converted_tuple_to_list.sort(reverse = c_ACTIVE)
            my_tuple = tuple(converted_tuple_to_list)
            return my_tuple
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnListPermutation(self, my_list, number_of_repetitions = 0, left = 0, right = 0):
        """
        :param my_list: [1, 2, 3, 4, 5]
        :param number_of_repetitions: 2
        :param left: 0
        :param right: 1
        :return: [4, 5, 1, 2, 3]
        """
        try:
            if left == c_ON and right == c_OFF:
                p = []
                for i in range(len(my_list)):
                    j = (i + number_of_repetitions) % len(my_list)
                    p.append(my_list[j])
                return p
            elif left == c_OFF and right == c_ON:
                p = []
                for i in range(len(my_list)):
                    j = (i - number_of_repetitions) % len(my_list)
                    p.append(my_list[j])
                return p
            elif left == c_ON and right == c_ON:
                print("Error: Only one side!")
            elif left == c_OFF and right == c_OFF:
                print("Error: One side must be 1!")
            else:
                print("Error: Invalid parameters!")
        except TypeError:
            print("Error: Incorrect data type!")

    '''Strings'''
    def ReverseString(self, string1):
        '''Example: Hello -> olleH'''
        try:
            reverse_string1 = string1[::-1]

            return reverse_string1
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintWordsWithLength(self, **kwargs):
        '''key, value -> len(key), len(value)'''
        try:
            for key, value in kwargs.items():
                print(key, value)
                print("Word for key: ", key, ", Length: ", len(key))
                print("Word for value:", value, ", Length: ", len(value))
                print()
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintListOfVowels(self, charset_string):
        '''vowels of a word -> ['o', 'e', 'o', 'a', 'o']'''
        try:
            vowels = set("aeiouAEIOU")
            vowels_list = []
            for _char in charset_string:
                if _char in vowels:
                    vowels_list.append(_char)

            print(vowels_list)
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintStringOfVowels(self, charset_string):
        '''vowels of a word -> oeoao'''
        try:
            vowels = set("aeiouAEIOU")
            vowels_string = ""
            for _char in charset_string:
                if _char in vowels:
                    vowels_string += _char

            print(vowels_string)
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintDictOfVowels(self, charset_string):
        '''vowels of a word -> dict_keys(['o', 'e', 'a'])'''
        try:
            vowels = set("aeiouAEIOU")
            vowels_dict = {}
            for _char in charset_string:
                if _char in vowels:
                    vowels_dict[_char] = 1

            print(vowels_dict.keys())
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintListOfConsonants(self, charset_string):
        '''vowels of a word -> ['v', 'w', 'l', 's', 'f', 'w', 'r', 'd']'''
        try:
            vowels = set("aeiouAEIOU")
            consonants_list = []
            for _char in charset_string:
                if _char not in vowels and _char.isalpha():
                    consonants_list.append(_char)

            print(consonants_list)
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintStringOfConsonants(self, charset_string):
        '''vowels of a word -> vwlsfwrd'''
        try:
            vowels = set("aeiouAEIOU")
            consonants_string = ""
            for _char in charset_string:
                if _char not in vowels and _char.isalpha():
                    consonants_string += _char

            print(consonants_string)
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintDictOfConsonants(self, charset_string):
        '''vowels of a word -> dict_keys(['v', 'w', 'l', 's', 'f', 'r', 'd'])'''
        try:
            vowels = set("aeiouAEIOU")
            consonants_dict = {}
            for _char in charset_string:
                if _char not in vowels and _char.isalpha():
                    consonants_dict[_char] = 1

            print(consonants_dict.keys())
        except TypeError:
            print("Error: Incorrect data type!")

    def SortStringLexicographic(self, my_string):
        '''
        Example: my_string = "zxsaubvrAEB" -> "ABEabrsuvxz"
        '''
        try:
            _string = sorted(my_string)
            #print(_string)
            _new_string = "".join(_string)
            return _new_string
        except TypeError:
            print("Error: Incorrect data type!")

    def SortStringReverseLexicographic(self, my_string):
        '''
        Example: my_string = "zxsaubvrAEB" -> "zxvusrbaEBA"
        '''
        try:
            _string = sorted(my_string, reverse = c_ACTIVE)
            #print(_string)
            _new_string = "".join(_string)
            return _new_string
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfStringIsLexicographic(self, my_string):
        """
        :param my_string: "abcd"
        :return: True
        """
        try:
            result = c_TRUE
            if sorted(my_string) != list(my_string):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfStringIsReverseLexicographic(self, my_string):
        """
        :param my_string: "abcd"
        :return: True
        """
        try:
            result = c_TRUE
            if sorted(my_string, reverse = c_ACTIVE) != list(my_string):
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnAllCharsWithLowerCase(self, my_string):
        """
        :param my_string: "AAASbnK"
        :return: "aaasbnk"
        """
        try:
            return my_string.lower()
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnAllCharsWithUpperCase(self, my_string):
        """
        :param my_string: "ab"
        :return: "AB"
        """
        try:
            return my_string.upper()
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfStringIsNonNumerical(self, my_string):
        """
        :param my_string: "asd"
        :return: True
        """
        try:
            if my_string.isalpha():
                result = c_TRUE
            else:
                result = c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfStringHasNumbers(self, my_string):
        """
        :param my_string: "asd3"
        :return: True
        """
        try:
            if my_string.isalpha():
                result = c_FALSE
            else:
                result = c_TRUE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def SortLexicographicStringWithRepeat1(self, my_string):
        """
        :param my_string: "Hello"
        :return: Helo
        """
        try:
            converted_string_to_list = list(my_string)
            converted_string_to_list = list(set(converted_string_to_list))
            converted_string_to_list.sort()
            my_string = "".join(converted_string_to_list)
            return my_string
        except TypeError:
            print("Error: Incorrect data type!")

    def SortReverseLexicographicStringWithRepeat1(self, my_string):
        """
        :param my_string: "Hello"
        :return: oleH
        """
        try:
            converted_string_to_list = list(my_string)
            converted_string_to_list = list(set(converted_string_to_list))
            converted_string_to_list.sort(reverse = c_ACTIVE)
            my_string = "".join(converted_string_to_list)
            return my_string
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnStringPermutation(self, my_string, number_of_repetitions = 0, left = 0, right = 0):
        """
        :param my_string: "abcde"
        :param number_of_repetitions: 2
        :param left: 1
        :param right: 0
        :return: cdeab
        """
        try:
            if left == c_ON and right == c_OFF:
                p1 = my_string[:number_of_repetitions]
                p2 = my_string[number_of_repetitions:]
                my_string = p2 + p1
                return my_string
            elif left == c_OFF and right == c_ON:
                p1 = my_string[-number_of_repetitions:]
                p2 = my_string[:-number_of_repetitions]
                my_string = p1 + p2
                return my_string
            elif left == c_ON and right == c_ON:
                print("Error: Only one side!")
            elif left == c_OFF and right == c_OFF:
                print("Error: One side must be 1!")
            else:
                print("Error: Invalid parameters!")
        except TypeError:
            print("Error: Incorrect data type!")

    '''Numbers'''
    def CheckIsPrime(self, x):
        '''x = 11 -> True'''
        try:
            ok = result = c_TRUE
            if x == 1:
                #print(x, " is not a prime number!")
                result &= c_FALSE
            elif x > 1:
                for i in range(2, x):
                    if x % i == 0:
                        ok = c_FALSE
                        result &= c_FALSE
                        break
                if ok:
                    #print(x, "is a prime number!")
                    result &= c_TRUE
                else:
                    #print(x, " is not a prime number!")
                    result &= c_FALSE

            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsEven(self, x):
        '''x % 2 == 0'''
        try:
            result = c_TRUE
            if x % 2 == 1:
                result &= c_FALSE
                #print(x, "is not even!")
                return result
            else:
                #print(x, "is even!")
                return result
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsOdd(self, x):
        '''x % 2 == 1'''
        try:
            result = c_TRUE
            if x % 2 == 0:
                result &= c_FALSE
                # print(x, "is not odd!")
                return result
            else:
                # print(x, "is odd!")
                return result
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnNumberOfDigits(self, x):
        '''
        Example:
        x = 5678 -> 4
        '''
        try:
            cnt = 0
            while x > 0:
                cnt += 1
                x = x // 10
            return cnt
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintAllDividers(self, x):
        '''
        x = 68 ->
        1
        2
        4
        17
        34
        68
        '''
        try:
            for i in range(1, x + 1):
                if x % i == 0:
                    print(i)
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintListOfAllDividers(self, x):
        '''x = 68 -> [1, 2, 4, 17, 34, 68]'''
        try:
            dividers_list = []
            for i in range(1, x + 1):
                if x % i == 0:
                    dividers_list.append(i)

            #print(dividers_list)
            return dividers_list
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsDivider(self, x, divider):
        '''67, 5 -> False'''
        try:
            result = c_TRUE
            if x % divider != 0:
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintImproperDividers(self, x):
        '''
        x = 12 ->
        2
        3
        4
        6
        '''
        try:
            limit = (x + 1) / 2
            int_limit = int(limit)
            for i in range(2, int_limit + 1):
                if x % i == 0:
                    print(i)
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintListOfAllImproperDividers(self, x):
        '''x = 12 -> [2, 3, 4, 6]'''
        try:
            improper_dividers_list = []
            limit = (x + 1) / 2
            int_limit = int(limit)
            for i in range(2, int_limit + 1):
                if x % i == 0:
                    improper_dividers_list.append(i)

            #print(improper_dividers_list)
            return improper_dividers_list
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsIntoInterval(self, x, a, b, brackets):
        '''x = 12, a = 4, b = 18, brackets = "[]" -> True'''
        try:
            if a > b:
                a, b = self.SwapValues(a, b)

            result = c_TRUE
            if brackets == "[]":
                if x >= a and x <= b:
                    result &= c_TRUE
                else:
                    result &= c_FALSE
            elif brackets == "()":
                if x > a and x < b:
                    result &= c_TRUE
                else:
                    result &= c_FALSE
            elif brackets != "[]" and brackets != "()":
                result &= c_FALSE
                print("Error: Incorrect data type!")

            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def MirrorNumber(self, x):
        '''456 -> 654'''
        try:
            mirror = 0
            while x != 0:
                mirror = mirror * 10 + x % 10
                x = x // 10

            return mirror
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIsPalindrome(self, x):
        '''121 -> True'''
        try:
            result = c_TRUE
            if x != self.MirrorNumber(x):
                result &= c_FALSE

            return result
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDigitsAscending(self, x):
        """
        :param x: 53241
        :return: 12345
        """
        try:
            converted_number_to_string = str(x)
            converted_to_list = list(converted_number_to_string)
            converted_to_list.sort()
            converted_number_to_string = "".join(converted_to_list)
            x = int(converted_number_to_string)
            return x
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDigitsDescending(self, x):
        """
        :param x: 53241
        :return: 54321
        """
        try:
            converted_number_to_string = str(x)
            converted_to_list = list(converted_number_to_string)
            converted_to_list.sort(reverse=c_ACTIVE)
            converted_number_to_string = "".join(converted_to_list)
            x = int(converted_number_to_string)
            return x
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDigitsAscendingWithRepeat1(self, x):
        """
        :param x: 2235114
        :return: 12345
        """
        try:
            converted_number_to_string = str(x)
            converted_to_list = list(converted_number_to_string)
            converted_to_list = list(set(converted_to_list))
            converted_to_list.sort()
            converted_number_to_string = "".join(converted_to_list)
            x = int(converted_number_to_string)
            return x
        except TypeError:
            print("Error: Incorrect data type!")

    def SortDigitsDescendingWithRepeat1(self, x):
        """
        :param x: 2235114
        :return: 54321
        """
        try:
            converted_number_to_string = str(x)
            converted_to_list = list(converted_number_to_string)
            converted_to_list = list(set(converted_to_list))
            converted_to_list.sort(reverse = c_ACTIVE)
            converted_number_to_string = "".join(converted_to_list)
            x = int(converted_number_to_string)
            return x
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnNumberPermutation(self, x, number_of_repetitions = 0, left = 0, right = 0):
        """
        :param x: 12345
        :param number_of_repetitions: 2
        :param left: 0
        :param right: 1
        :return: 45123
        """
        try:
            if left == c_ON and right == c_OFF:
                converted_number_to_string = str(x)
                p1 = converted_number_to_string[:number_of_repetitions]
                p2 = converted_number_to_string[number_of_repetitions:]
                converted_number_to_string = p2 + p1
                x = int(converted_number_to_string)
                return x
            elif left == c_OFF and right == c_ON:
                converted_number_to_string = str(x)
                p1 = converted_number_to_string[-number_of_repetitions:]
                p2 = converted_number_to_string[:-number_of_repetitions]
                converted_number_to_string = p1 + p2
                x = int(converted_number_to_string)
                return x
            elif left == c_ON and right == c_ON:
                print("Error: Only one side!")
            elif left == c_OFF and right == c_OFF:
                print("Error: One side must be 1!")
            else:
                print("Error: Invalid parameters!")
        except TypeError:
            print("Error: Incorrect data type!")

#Basics = Basics()