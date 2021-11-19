""" Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504 """

import math


def solution(r):
    area = math.pi * r**2
    return area

def test_solution():
    radius = 1.1
    result = solution(radius)
    assert result == 3.8013271108436504

    radius = 1
    result = solution(radius)
    assert result == 3.141592653589793

    print("Tests ran successfully.")

test_solution()
