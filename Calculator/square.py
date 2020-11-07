def square(a):
    try:
        return float(a)**2
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")