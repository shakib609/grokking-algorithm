def max_element(arr):
    length = len(arr)
    if length == 0:
        return None
    elif length == 1:
        return arr[0]
    else:
        mx = arr[0] if arr[0] > arr[1] else arr[1]
        return max_element([mx] + arr[2:])


if __name__ == '__main__':
    print(max_element([1, 5, 9, 1, 3]))
