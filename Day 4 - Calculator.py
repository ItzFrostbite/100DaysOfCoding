print("Welcome To The Calculater Made By ItzFrostbite")
print("Enter Equasion To Get Started")

type = input("Enter +,-,*,/,%: ")

num1 = float(input("Enter First Number: "))

num2 = float(input("Enter Second Number: "))

if type == "+":
    print("The Answer Is:", num1 + num2)

elif type == "-":
    print("The Answer Is:", num1 - num2)

elif type == "*":
    print("The Answer Is:", num1 * num2)

elif type == "/":
    print("The Answer Is:", num1 / num2)

elif type == "%":
    print("The Answer Is:", num1 % num2)

bye = input("Press Enter To Exit ")
