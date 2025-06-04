def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

calculator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

a = float(input("Enter first number: "))
sign = input("Enter + to add, - to sub, * to mul and / to div: ")
b = float(input("Enter second number: "))

if sign in calculator:
    c = calculator[sign](a, b)
    print(f"Result: {c}")
else:
    print("Invalid input")
    exit()

cont = input("Press 'y' to continue with this value or 'n' to stop: ").lower()

while cont == 'y':
    print("\n" * 3)
    print(f"Current value: {c}")
    sign = input("Enter + to add, - to sub, * to mul and / to div: ")
    b = float(input("Enter next number: "))

    if sign in calculator:
        c = calculator[sign](c, b)
        print(f"Result: {c}")
    else:
        print("Invalid input")
    
    cont = input("Press 'y' to continue or 'n' to stop: ").lower()

print("Calculator session ended.")
