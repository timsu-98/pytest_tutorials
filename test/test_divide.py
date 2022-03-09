import sys
sys.path.insert(0, '..')
from src.some_functions import divideTwoNums

def test() -> None:
    assert divideTwoNums(1, 0) == None
    assert divideTwoNums(1, 2) == 0.5

