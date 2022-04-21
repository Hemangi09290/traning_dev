import os

"handle error in except block"
def exception_handle1():
    try:
        assert 2+2==4
        "here 1+2 =3 will come but to raise exception, written in this way"
        assert 1+2==4
    except:
        "if any error occur in the code, we can handle iin except block"
        print("An assert failed.")
    finally:
        "finally block will always call"
        print("Okay")
    print("Bye")

"not handle error instead raise exception, will throw assertion error"
def exception_handle12():
    try:
        assert 2+2==4
        "here 1+2 =3 will come but to raise exception, written in this way"
        assert 1+2==4
    except:
        "if any error occur in the code, we can handle iin except block"
        print("An assert failed.")
        raise
    finally:
        "finally block will always call"
        print("Okay")
    print("Bye")

"multiple exceptions can also be handle"
def exception_handle13():
    a,b=1,0
    try:
        print(a/b)
        "This won't be printed as in above line ZeroDivisionError will occur"
        print('10'+10)
    except TypeError:
        print("You added values of incompatible types")
    except ZeroDivisionError:
        print("You divided by 0")
          
exception_handle1()
exception_handle12()
exception_handle13()
