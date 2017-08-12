def hello():
    print("Hello World")


hello()

#function for factorial

def factorial(number):
    factorials =1
    for i in range(1,number +1):
        factorials *=i
    print("Factorial",factorials)

text = int(input("Please enter a number:"))

factorial(text)