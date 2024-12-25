def fib(num):
    num = num - 2
    if num == -2:
        array = [0]
    elif num == -1:
        array = [0, 1]
    else:
        array = [0, 1, 1]
    fib_num_1 = fib_num_2 = 1
    while num > 0:
        fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2
        array.append(fib_num_2)
        num -= 1
    return array

if __name__ == "__main__":
    print(fib(8))