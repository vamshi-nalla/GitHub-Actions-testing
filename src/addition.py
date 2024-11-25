# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def sub(a,b):
    return a-b

def test_sub():
    assert sub(2,1) == 1
    assert sub(10,5) == 5 


def division(a,b):
    if a>0:
        return a//b
    else:
        return False
    
def test_division():
    assert division(10,5) == 2
    assert division(-10,5) == False