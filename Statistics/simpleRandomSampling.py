import random


def simpleRandomSampling(data):
    try:
        sampled_list = random.sample(data, 15)
        print("Sample data :", sampled_list)
        return len(sampled_list)
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")