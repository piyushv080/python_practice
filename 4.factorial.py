#function of factorial number

num = int(input("Enter factorial which you wnat factorial number: \n"))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(num))

