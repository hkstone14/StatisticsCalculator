def subtraction(a, b):
    try:
        return b - a
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")