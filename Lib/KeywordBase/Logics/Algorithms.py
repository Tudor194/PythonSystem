import math
from Lib.KeywordBase.Config.Constants import *
from Lib.KeywordBase.Basics.Basics import Basics

class Algorithms():
    """Fibonacci Series"""

    def PrintFibonacciLessThanN(self, n):
        '''
        Fibonacci Series < n
        Example: n = 56 -> 0 1 1 2 3 5 8 13 21 34 55
        '''
        try:
            a, b = 1, 1
            while a < n:
                print(a, end=' ')
                a, b = b, a+b
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnNTHFibonacciNumber(self, n):
        """
        :param n: 13
        :return: 233
        """
        try:
            my_list = [1, 1]
            for i in range(2, n):
                temp = my_list[i - 1] + my_list[i - 2]
                my_list.append(temp)
            return my_list[n - 1]
        except TypeError:
            print("Error: Incorrect data type!")

    def PrintFirstNFibonacciNumbers(self, n):
        """
        :param n: 13
        :return:
        """
        try:
            a, b, cnt = 1, 1, 0
            while cnt < n:
                print(a, end=' ')
                a, b = b, a + b
                cnt += 1
        except TypeError:
            print("Error: Incorrect data type!")

    def CheckIfNumberIsFibonacci(self, x):
        """
        :param x: 13
        :return: True
        """
        try:
            result = c_TRUE
            a = 5 * x * x + 4
            b = 5 * x * x - 4
            if math.sqrt(a) == int(math.sqrt(a)) or math.sqrt(b) == int(math.sqrt(b)):
                result &= c_TRUE
            else:
                result &= c_FALSE
            return result
        except TypeError:
            print("Error: Incorrect data type!")

    """Binary Search"""
    def ReturnBinarySearchPositionRecursive(self, my_list, left, right, x):
        """
        :param my_list: [2, 3, 4, 5, 10, 40, 69]
        :param left: 0
        :param right: len(my_list)
        :param x: 10
        :return: 4
        """
        try:
            if right >= left:
                middle = (left + right) // 2
                if my_list[middle] == x:
                    return middle
                elif my_list[middle] > x:
                    return self.ReturnBinarySearchPositionRecursive(my_list, left, middle - 1, x)
                else:
                    return self.ReturnBinarySearchPositionRecursive(my_list, middle + 1, right, x)
            else:
                return "Error: The input doesn't match with your request!"
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnBinarySearchPositionIterative(self, my_list, x):
        """
        :param my_list: [2, 3, 4, 5, 10, 40, 69]
        :param left: 0
        :param right: len(my_list)
        :param x: 10
        :return: 4
        """
        try:
            left = 0
            right = len(my_list) - 1
            while left <= right:
                middle = (left + right) // 2
                if my_list[middle] == x:
                    return middle
                elif my_list[middle] < x:
                    left = middle + 1
                elif my_list[middle] > x:
                    right = middle - 1
                else:
                    return "Error: The input doesn't match with your request!"
        except TypeError:
            print("Error: Incorrect data type!")

    def ReturnAllBinarySearchPositions(self, my_list, x):
        """
        :param my_list: [2, 3, 4, 5, 10, 40, 69]
        :param left: 0
        :param right: len(my_list)
        :param x: 10
        :return: (4, [3, 5, 4])
        """
        try:
            left = 0
            right = len(my_list) - 1
            middle = (left + right) // 2
            visits = []
            while left <= right:
                visits.append(middle)
                if my_list[middle] == x:
                    return (middle, visits)
                elif my_list[middle] < x:
                    left = middle + 1
                elif my_list[middle] > x:
                    right = middle - 1
                else:
                    return ("Error: The input doesn't match with your request!", visits)
                middle = (left + right) // 2
        except TypeError:
            print("Error: Incorrect data type!")