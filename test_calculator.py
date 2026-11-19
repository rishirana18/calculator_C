from calculator import add, subtract, divide, multiply, CircleArea

def test_add():
    assert add(2,3)==5

def test_divide():
    assert divide(6,2)==3

def test_subtract():
    assert subtract(2,3)==-1

def test_multiply():
    assert multiply(2,3)==6

def test_multiply_zero():
    #arrange 
    a,b=5,0
    #act
    result=multiply(a,b)
    #assert
    assert result==0

def test_circleArea():
    assert CircleArea(-4) == "Error"
