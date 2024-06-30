import random

class Countdown:
    
    def __init__(self, start):
        if start < 1:
            raise ValueError("Start must be greater than or equal to 1")
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current

def fibonacci_generator(limit):
    
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def random_number_generator(start, end, count):
   
    if start >= end:
        raise ValueError("Start must be less than end")
    for _ in range(count):
        yield random.randint(start, end)

def main():
    print("Countdown from 5:")
    try:
        for number in Countdown(5):
            print(number, end=" ")
    except ValueError as e:
        print(e)
    print("\n")

    print("Fibonacci numbers up to 100:")
    for number in fibonacci_generator(100):
        print(number, end=" ")
    print("\n")

    print("Random numbers between 1 and 10 (5 numbers):")
    try:
        for number in random_number_generator(1, 10, 5):
            print(number, end=" ")
    except ValueError as e:
        print(e)
    print()

if __name__ == "__main__":
    main()
