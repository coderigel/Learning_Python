factorial = 1

while True:
    number = int(input("Please enter a non-negative number:"))
    if (number <= 0):
        print("Please, NON-negative :/")
    else:
        for i in range(1,number +1):
            factorial *= i

#factorial = factorial *i -------> factorial *= i

        print("factorial:",factorial)
        break