import sys
sys.path.insert(0, '..')
from src.some_functions import multiplyTwoNums

def test() -> None:
    assert multiplyTwoNums(3, 5) == 15