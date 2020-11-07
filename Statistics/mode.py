from collections import Counter


def mode1(data1):
    try:
        num_values = len(data1)
        count = Counter(data1)
        get_mode = dict(count)
        mode = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        if len(mode) == num_values:
            get_mode = "No mode found"
        else:
            get_mode = mode[0]
        return get_mode
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
