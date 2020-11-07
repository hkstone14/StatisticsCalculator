def median1(data):
    try:
        n = len(data)
        final_result = []
        for i in data:
            final_result.append(float(i["Value1"]))
        final_result.sort()
        if n % 2 == 0:
            median1 = final_result[n // 2]
            median2 = final_result[n // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = final_result[n // 2]
        return median
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
