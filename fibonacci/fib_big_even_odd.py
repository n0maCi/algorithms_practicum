def fib_eo(num):
    a = 0
    b = 1
    i = 2
    while i <= num:
        c = (a + b) % 10
        a = b
        b = c
        i += 1
    return "even" if b % 2 == 0 else "odd"

if __name__ == "__main__":
    print(fib_eo(841645))