def countdown(n):
    print(n)
    if n > 1:
        countdown(n - 1)


if __name__ == '__main__':
    countdown(5)
