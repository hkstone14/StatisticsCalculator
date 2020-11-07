def squareroot(a):
    try:
        return a ** (1/2)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")