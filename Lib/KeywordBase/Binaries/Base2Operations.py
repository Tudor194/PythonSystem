import math
from Lib.KeywordBase.Config.Constants import *
from Lib.KeywordBase.Basics.Basics import Basics
from Lib.KeywordBase.Logics.Algorithms import Algorithms


class Base2Operations():
    def ConvertB10ToB2(self, x):
        """
        :param x: 67
        :return: 1000011
        """
        try:
            result = ""
            while x > 0:
                result += str(x % 2)
                x = x // 2
            return result[::-1]
        except TypeError:
            print("Error: Incorrect data type!")

    def ConvertB2ToB10(self, x):
        """
        :param x:
        :return:
        """
        try:
            pass
        except TypeError:
            print("Error: Incorrect data type!")

    def ConvertB10ToB16(self, x):
        """
        :param x: 67
        :return: 34
        """
        try:
            conversion_dict = {
                0:'0',
                1:'1',
                2:'2',
                3:'3',
                4:'4',
                5:'5',
                6:'6',
                7:'7',
                8:'8',
                9:'9',
                10:'A',
                11:'B',
                12:'C',
                13:'D',
                14:'E',
                15:'F'
            }
            result = ""
            while x > 0:
                reminder = x % 16
                result += conversion_dict[reminder]
                x = x // 16
            return result
        except TypeError:
            print("Error: Incorrect data type!")