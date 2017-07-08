from random import randint


def qsort(arr):
    l = len(arr)
    if l < 2:
        return arr
    else:
        pivot_index = randint(0, l - 1)
        pivot = arr[pivot_index]
        leftarr, rightarr = [], []
        for i in range(l):
            if i == pivot_index:
                pass
            elif arr[i] < pivot:
                leftarr.append(arr[i])
            else:
                rightarr.append(arr[i])
        return qsort(leftarr) + [pivot] + qsort(rightarr)


def main():
    a = [randint(1, 50) for _ in range(5)]
    print(a)
    print(qsort(a))


if __name__ == '__main__':
    main()
