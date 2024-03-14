try:
    num = float(input("Unesite broj: "))
    if num < 0 or num > 1.0:
        raise ValueError("Uneseni broj mora biti izmedju 0.0 i 1.0")
    if num < 0.6:
        print('F')
    elif num < 0.7:
        print('D')
    elif num < 0.8:
        print('C')
    elif num < 0.9:
        print('B')
    else:
        print('A')
except ValueError as error:
    print(error)