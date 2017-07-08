def binary_search(arr, el, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    mid = (low + high) // 2
    if low > high:
        return None
    elif arr[mid] > el:
        return binary_search(arr, el, low, mid-1)
    elif arr[mid] < el:
        return binary_search(arr, el, mid+1, high)
    else:
        return mid


def main():
    print(binary_search([x for x in range(0, 150, 6)], 25))


if __name__ == '__main__':
    main()
