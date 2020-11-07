from collections import Counter

def mode1(data1):

    try:
        n = len(data1)
        data = Counter(data1)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

        if len(mode) == n:
            pass
        else:
            get_mode = map(str, mode)

        print(get_mode)
        return  get_mode

    except ValueError:
        print("ERROR: Check your input value")
