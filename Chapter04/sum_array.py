def sum_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + sum_array(arr)


if __name__ == '__main__':
    print(sum_array([x for x in range(11)]))
