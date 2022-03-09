import sys
sys.path.insert(0, '..')
from src.some_functions import addTwoNums

def test_add_two_nums() -> None:
    assert addTwoNums(3, 5) == 8

if __name__=="__main__":
    print(sys.path)