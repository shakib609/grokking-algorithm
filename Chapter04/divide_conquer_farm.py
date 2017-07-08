def divide_farm(a, b):
    a, b = sorted([a, b])
    if b % a == 0:
        print(a)
        return
    else:
        temp = b // a
        divide_farm(temp * a, b % a)


if __name__ == '__main__':
    divide_farm(1680, 640)
