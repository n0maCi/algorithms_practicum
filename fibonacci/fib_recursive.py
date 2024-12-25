import time
numbers = [1, 10, 14, 20, 24]

def fib(num):
    if num <= 0 or num > 24:
        return 0
    elif num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)

if __name__ == "__main__":
    for number in numbers:
        date_stamp_1 = time.time() * 1000
        fibonacci = fib(number)
        date_stamp_2 = time.time() * 1000
        print(f'Число: {number}, Результат: {fibonacci}, Время: {date_stamp_2 - date_stamp_1}')