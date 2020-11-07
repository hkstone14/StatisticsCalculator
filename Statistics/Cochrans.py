from Statistics.errorOfMargin import errorOfMargin
from Calculator.square import square
from Calculator.multiplication import multiplication
from Calculator.division import division


def cochran(data):
    try:
        e = errorOfMargin(data)
        p = 0.5
        z = 1.96
        q = 1 - p
        temp1 = square(z)
        temp2 = multiplication(p, q)
        temp3 = multiplication(temp1, temp2)
        temp4 = square(e)
        cochrans = division(temp4, temp3)
        final_cochran = round(multiplication(cochrans, 100), 4)
        return final_cochran
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
