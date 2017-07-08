def count(arr):
    if not arr:
        return 0
    else:
        arr.pop()
        return 1 + count(arr)


if __name__ == '__main__':
    print(count([1, 2, 3, 4]))
