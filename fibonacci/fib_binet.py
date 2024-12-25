import math

def fib(num):
    a = ((1+math.sqrt(5))/2) ** num
    b = ((1-math.sqrt(5))/2) ** num
    print(round((a - b) / (math.sqrt(5))))

if __name__ == "__main__":
    fib(32)