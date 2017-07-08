import random


def find_largest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        largest_index = find_largest(arr)
        new_arr.append(arr.pop(largest_index))
    return new_arr


def main():
    arr = [random.randint(0, 15) for _ in range(10)]
    print(arr)
    print(selection_sort(arr))


if __name__ == '__main__':
    main()
