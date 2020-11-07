from Statistics.errorOfMargin import errorOfMargin
from Calculator.division import division
from Calculator.multiplication import multiplication
from Calculator.square import square


def UnknownPopulationStd_Dev(data):
    z = 1.96
    zBy2 = 0.475
    EOM = errorOfMargin(data)
    EOMDivby2 = division(2, EOM)
    p = 0.5
    q = 1 - p
    temp1 = multiplication(p, q)
    temp2 = division(EOMDivby2, zBy2)
    temp3 = square(temp2)
    temp4 = round(multiplication(temp1, temp3), 3)
    return temp4
