for i in range(1, 100):
    if i % 2 == 0 and i % 11 == 0:
        print("FizzBuzz")
    elif i % 2 == 0:
        print("Fizz")
    elif i % 11 == 0:
        print("Buzz")
    else:
        print(i)
