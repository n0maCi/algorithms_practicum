import time
numbers = [5, 10, 20, 30, 40]

def fib(num):
    num = num - 2
    fib_num_1 = fib_num_2 = 1
    while num > 0:
        fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2
        num -= 1
    return fib_num_2

if __name__ == "__main__":
    for number in numbers:
        date_stamp_1 = time.time() * 1000
        fibonacci = fib(number)
        date_stamp_2 = time.time() * 1000
        print(f'Число: {number}, Результат: {fibonacci}, Время: {date_stamp_2 - date_stamp_1}')