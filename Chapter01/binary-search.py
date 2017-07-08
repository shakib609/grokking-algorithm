def binary_search(lst, el):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == el:
            return mid
        elif guess < el:
            low = mid + 1
        else:
            high = mid - 1
    return None


def main():
    l = [x for x in range(0, 100, 2)]
    print(binary_search(l, 55))
    print(binary_search(l, 56))


if __name__ == '__main__':
    main()
