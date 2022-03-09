from ctypes import Union
from tokenize import Double


def addTwoNums(num1: int, num2: int) -> int:
    return num1 + num2

def multiplyTwoNums(num1: int, num2: int) -> int:
    return num1 * num2

def divideTwoNums(numerator: int, denominator: int):
    if denominator == 0:
        return None
    else:
        return numerator / denominator