def operand():
    global operator
    global op
    while True:
        try:
            operator = int(input("Which function?\n1. Add\n2. Sub\n3. Multiply\n4. Divide\n5. Exponent\n6. Compound interest\n7. Combinations of things\n:"))
            if operator == 1:
                op = "+"
                break
            if operator == 2:
                op = "-"
                break
            if operator == 3:
                op = "*"
                break
            if operator == 4:
                op = "/"
                break
            if operator == 5:
                op = "**"
                break
            if operator == 6:
                compound_interest()
                break
            if operator == 7:
                combination()
                break
        except ValueError:
            print("Error, not a number")
        else:
            operand()

def compound_interest():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the interest rate: "))
    t = float(input("Enter the time in years: "))

    result = p * ((1 + r / 100) ** t)
    interest = result - p
    print("Compound amount is $%.2f" % result)
    print("Compound interest is $%.2f" % interest)

def combination():
    pass

def math():
    global a
    global b
    while True:
        try:
            a = int(input("enter #: "))
        except ValueError:
            print("Error, not a number")
            continue
        try:
            b = int(input("enter #: "))
        except ValueError:
            print("Error, not a number")
            continue
        else:
            break
    x = eval(str(a) + op + str(b))
    print(x)

def doanother():
    while True:
        try:
            another = input("Do another function? [y/n]")
            if another == "y":
                operand()
                math()
            if another == "n":
                break
        except ValueError:
            print("Invalid Input")
    

operand()
if operator < 6:
    math()
doanother()