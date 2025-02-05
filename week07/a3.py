# We're not going to worry about invalid input for this...
num = int(input("Enter a number: "))
i = 1
while i <= num: 
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0: 
        print("Buzz")
    else:
        print(i)
    i += 1