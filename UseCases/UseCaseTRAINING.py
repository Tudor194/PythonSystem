from ProjectComponents.ImportLib import *

class UseCaseTRAINING():
    '''
    TRAINING
    '''
    def Execute(self):
        print(1+2)
        a = 5
        b = 4
        a, b = Basics.SwapValues(a, b)
        print(a)
        print(b)
        x = TRAINING.MAXIMIZE(a, b)
        print(x)
        print(c_ON)
        print(c_VALID)

        z = 54
        Basics.CheckIsEven("sdjndsk")
        print(Basics.CheckIsEven((z)))
        Basics.PrintListOfAllImproperDividers("t")
        print(Basics.PrintListOfAllImproperDividers(z))
        Basics.PrintImproperDividers(z)
        Basics.PrintImproperDividers("rt")
        Basics.PrintAllDividers(z)
        Basics.PrintAllDividers("iu")
        print(Basics.CheckIsOdd(z))
        Basics.CheckIsOdd("hj")
        print(Basics.CheckIsEvenBitwise(z))
        Basics.CheckIsEvenBitwise("Hello")
        print(Basics.CheckIsPrime(z))
        Basics.CheckIsPrime("hey")
        Basics.CheckNumberOfVowels(z)
        print(Basics.CheckNumberOfVowels("abcdefghij"))
        Basics.PrintDictOfVowels(3)
        Basics.PrintDictOfVowels("iop")
        Basics.PrintWordsWithLengthWithoutKey(a = "sd", v = 3) #
        Basics.PrintWordsWithLengthWithoutKey(a = "sd", v = "ui")
        Basics.PrintListOfVowels(56)
        Basics.PrintListOfVowels("iugyuuyf")
        print(Basics.CheckIsDivider(54, 2))
        Basics.CheckIsDivider("a", "b")
        Basics.CheckIsDivider(54, "j")

        l1 = 4
        l2 = 8
        x = 5
        print(Basics.CheckIsIntoInterval(x, l1, l2, "[]"))
        print(Basics.CheckIsIntoInterval(x, l1, l2-7, 3))
        Basics.CheckIsIntoInterval(x, l1, l2 - 7, 3)
        print(Basics.CheckIsIntoInterval(x, "a", l2 - 7, 3))
        Basics.CheckIsIntoInterval(x, "a", l2 - 7, 3)
        print(Basics.CheckIsIntoInterval(x, l2, l1, "()"))

        u = 456
        print(Basics.MirrorNumber(u))
        Basics.MirrorNumber("u")

        print(Basics.CheckIsPalindrome(11211))
        print(Basics.CheckIsPalindrome(89))
        Basics.CheckIsPalindrome("09")
        Basics.CheckIsPalindrome([2, 3])

        the_list = ['a2', '2', 3, [2, 3, '4', 'as']]
        x = [2, 3, '4', 'as']
        print(Basics.CheckIsInTheList(x, the_list))

        a = 2
        b = [2, 'sd']
        a, b = Basics.SwapValues(a, b)
        print(a)
        print(b)

        x = 7
        print(Basics.ReturnTheIndexFromTheList(x, [8, 'hu', '7', 7, 8]))
        print(Basics.ReturnAllIndexesFromTheList(x, [8, 'hu', 7, 7, 8]))

        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 2,
            'x': 3,
            'y': 'abcd'
        }
        print(Basics.CheckValueIsInTheDict(x, the_dict))

        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 2,
            'abcd': 3,
            'abcd': 4,
        }
        print(Basics.CheckKeyIsInTheDict(x, the_dict))
        print(Basics.ReturnIndexOfKeyInDict(x, the_dict))
        print(Basics.ReturnIndexOfKeyInDictWithStr(x, the_dict))
        print(Basics.ReturnIndexOfKeyInDictWithForStatement(x, the_dict))

        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 2,
            'x': 3,
            'y': 'abcd',
            'abcd': 9,
            'abcd': 10
        }
        print(Basics.ReturnIndexOfKeyInDictWithList(x, the_dict))
        print(Basics.ReturnIndexOfKeyInDict(x, the_dict))

        x = 'abcd'
        the_dict = {
            1: 1.3,
            'as': 'abcd',
            'x': 'abcd',
            'y': 4,
        }
        print(Basics.ReturnAllKeysIndexInDict(x, the_dict))

        a = 3456
        print(Basics.ReturnNumberOfDigits(a))

        my_list = [5, 2, 7, 9, 1]
        print(Basics.SortListAscending(my_list))
        print(Basics.SortListDescending(my_list))

        my_string = "zxsaubvrAEB"
        print(Basics.SortStringLexicographic(my_string))
        print(Basics.SortStringReverseLexicographic(my_string))

        my_dict = {
            "11": 1.3,
            "x": 9,
            "b": 7,
            "e": 4,
        }
        print(Basics.SortDictValuesAscending(my_dict))
        print(Basics.SortDictValuesDescending(my_dict))
        print(Basics.SortDictKeysAscending(my_dict))
        print(Basics.SortDictKeysDescending(my_dict))

        my_tuple = (5, 9, 2, 1, 7)
        print(Basics.SortTupleAscending(my_tuple))
        print(Basics.SortTupleDescending(my_tuple))

        my_tuple = ('a', 'c', 'b')
        print(Basics.SortTupleAscending(my_tuple))

        my_set = {1, 4, 2, 6, 3}
        print(Basics.SortSetAscending(my_set))
        Basics.SortSetDescending(my_set)

        my_list = [1, 2, 4, 6, 7, 8, 10]
        print(Basics.CheckIfListIsSortedAscending(my_list))

        my_list = [9, 7, 6, 2, 1, 0]
        print(Basics.CheckIfListIsSortedDescending(my_list))

        my_list = ['a', 'bc']
        print(Basics.CheckIfListIsSortedAscending(my_list))

        my_dict = {
            "a": "a",
            "c": "c",
            "d": "d"
        }
        print(Basics.CheckIfDictValuesAreSortedAscending(my_dict))
        print(Basics.CheckIfDictKeysAreAscending(my_dict))

        my_dict = {
            "a": "d",
            "c": "c",
            "d": "a"
        }
        print(Basics.CheckIfDictValuesAreSortedDescending(my_dict))

        my_dict = {
            9: '9',
            8: '8'
        }
        print(Basics.CheckIfDictKeysAreDescending(my_dict))

        my_tuple = (1, 2, 3)
        print(Basics.CheckIfTupleIsAscending(my_tuple))

        my_tuple = (3, 2, 1)
        print(Basics.CheckIfTupleIsDescending(my_tuple))

        my_set = {1, 2, 3, 4}
        print(Basics.CheckIfSetIsAscending(my_set))

        #my_set = {4, 3, 2, 1}
        #print(Basics.CheckIfSetIsDescending(my_set))

        my_string = "abcd"
        print(Basics.CheckIfStringIsLexicographic(my_string))

        my_string = "cba"
        print(Basics.CheckIfStringIsReverseLexicographic(my_string))

        my_string = "ASDFui"
        print(Basics.ReturnAllCharsWithLowerCase(my_string))
        print(Basics.ReturnAllCharsWithUpperCase(my_string))

        print(Basics.ReturnDataTypeLength(my_dict))

        print(Basics.CheckIfStringIsNonNumerical("34s"))
        print(Basics.CheckIfStringIsNonNumerical("aes"))
        print(Basics.CheckIfStringHasNumbers("asd"))
        print(Basics.CheckIfStringHasNumbers("asd7"))

        x = 2235114
        print(Basics.SortDigitsAscending(x))
        print(Basics.SortDigitsDescending(x))
        print(Basics.SortDigitsAscendingWithRepeat1(x))
        print(Basics.SortDigitsDescendingWithRepeat1(x))

        my_string = "Hello"
        print(Basics.SortLexicographicStringWithRepeat1(my_string))
        print(Basics.SortReverseLexicographicStringWithRepeat1(my_string))

        my_list = [1, 2, 4, 3, 7, 6, 5, 5]
        print(Basics.SortListAscending(my_list))
        print(Basics.SortListAscendindWithRepeat1(my_list))
        print(Basics.SortListDescendindWithRepeat1(my_list))

        my_dict = {
            'a': 1,
            'b': 2,
            'c': 3,
            'a': 4,
            'b': 5
        }
        print(Basics.SortAscendingDictKeysWitHRepeat1(my_dict))
        print(Basics.SortDescendingDictKeysWitHRepeat1(my_dict))

        my_dict = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 1,
            'e': 2
        }
        print(Basics.SortAscendingDictValuesWitHRepeat1(my_dict))
        print(Basics.SortDescendingDictValuesWitHRepeat1(my_dict))

        my_tuple = (3, 2, 4, 1, 2, 3, 5)
        print(Basics.SortTupleAscending(my_tuple))
        print(Basics.SortAscendingTupleWithRepeat1(my_tuple))
        print(Basics.SortDescendingTupleWithRepeat1(my_tuple))

        my_dict = {
            "11": 1,
            "xx": 99,
            "bb": 7,
            "11": 1,
            "ee": 4
        }
        print(Basics.SortDictValuesAscending(my_dict))

        x = 12345
        print(Basics.ReturnNumberPermutation(x, 9, 1, 0))

        my_string = "abcde"
        print(Basics.ReturnStringPermutation(my_string, 2, 0, 1))

        my_list = [1, 2, 3, 4, 5]
        print(Basics.ReturnListPermutation(my_list, 2, 1, 0))

        my_list = [2, 3, 4, 5, 10, 40, 69]
        print(Algorithms.ReturnBinarySearchPositionRecursive(my_list, 0, len(my_list) - 1, 10))
        print(Algorithms.ReturnBinarySearchPositionIterative(my_list, 10))
        print(Algorithms.ReturnAllBinarySearchPositions(my_list, 10))

        x = 67
        print(Base2Operations.ConvertB10ToB2(x))
        print(Base2Operations.ConvertB10ToB16(x))

        x = 100101101
        print(Base2Operations.ConvertB2ToB10(x))

UseCaseTRAINING = UseCaseTRAINING()

UseCaseTRAINING.Execute()