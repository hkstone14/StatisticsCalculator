def addition(a, b):
    try:
        return a + b
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
