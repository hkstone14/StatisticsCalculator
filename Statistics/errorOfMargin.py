from Calculator.division import division
from Calculator.sqaureroot import squareroot
from Calculator.multiplication import multiplication


def errorOfMargin(data):
    try:
        n = len(data)
        p = 0.5
        z = 1.96
        temp1 = multiplication(p, (1 - p))
        temp2 = round(division(n, temp1), 3)
        temp3 = squareroot(temp2)
        moe = multiplication(z, temp3)
        return round(multiplication(moe, 100), 3)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
