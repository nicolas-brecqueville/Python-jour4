def calcul(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2

num1 = int(input("Rentrez un nombre : "))
operator = input("Rentrez un operateur : ")
num2 = int(input("Rentrez un nombre : "))

print(calcul(num1, operator, num2))
