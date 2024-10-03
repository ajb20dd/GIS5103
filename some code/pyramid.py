n = int(input())

def pyramid(n):
    for i in range(1, n + 1):
        str_brick = '*'
        str_space = ' '
        print((str_space * (n - i)) + (str_brick * (2 * i - 1)) + (str_space * (n - i)))

pyramid(n)
