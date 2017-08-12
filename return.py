def factorial (number):
    factorials  =1
    for i in range(1,number+1):
        factorials *=i
    #print("Factorial:",factorials)
    return

text = int(input("Please enter a number:"))
factorial(text)