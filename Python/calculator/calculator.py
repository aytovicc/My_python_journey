from art import logo
print(logo)
import math

# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Substract 
def substract(n1, n2):
    return n1 - n2

# Divide 
def divide(n1, n2):
    return n1 / n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

def exponent(n1, n2):
    return n1 ** n2

def logaritmic(n1, n2):
    return math.log(n2, n1)
#################
operations = {
"+" : add,
"-" : substract,
"/" : divide,
"*" : multiply,
"**" : exponent,
"log" : logaritmic,
}
#################
last_answer = []


number1 = float(input("What's the number?\n"))
print("..................")
for keys in operations.keys():
     print(keys)
print("..................")
operator = input("Pick an operation to continue.\n")
for symbol in operations.keys():
    if operator == symbol:
        number2 = float(input("What's the number?\n"))
        answer = operations[symbol](number1,number2)
        last_answer = answer
print(f"{number1} {operator} {number2} = {answer}")


resume = ""
again = input("Do you want to keep going? yes or no?\n").lower()
resume += again

the_end = False


if resume == "yes":
    while not the_end:
        print("..................")
        for keys in operations.keys():
            print(keys)
        print("..................")
        new_operator = input("Pick an operation to continue.\n")
        new_number = float(input("What's the number?\n"))
        for symbol in operations.keys():
            if new_operator == symbol:
                new_answer = operations[symbol](last_answer,new_number)
                print(f"{last_answer} {new_operator} {new_number} = {new_answer}")
                againn = input("Do you want to keep going? yes or no?\n").lower()
                if againn == "yes":
                    resume += again
                    last_answer = new_answer
                else:
                    the_end = True
                    print("Goodbye!") 

                

elif resume == "no":
        the_end = True
        print("Goodbye!")    
