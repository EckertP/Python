import random

def random_int(min=None, max=None):
    if not min or not max:
        return print("Min or Max is not Definied!")

    try:
        int(min)
        int(max)
    except Exception as Error:
        return print(Error)

    if min > max:
        return print("Min is bigger than Max!")
    if min == max:
        return print("Min is same as Max")

    random_number = 0
    try:
        random_number - random.randint(min, max)
    except Exception as Error:
        return print(Error)

    return random_number