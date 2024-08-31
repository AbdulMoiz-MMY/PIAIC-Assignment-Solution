print("WELCOME TO MY CALCULATOR")
print("HELLO! MY dear User")

number_1 = int(input("Enter the first number : "))
number_2 = int(input("Enter the second number : "))
print("Please select the following options.")
print("=> Addition")
print("=> Subtraction")
print("=> Multiplication")
print("=> Division")
print("=> Modulus")


print("Type the correct spell according option")

select_option = input("Select Option: ")

if select_option == "Addition":
    print(number_1, " + ", number_2, " = ", number_1+number_2)
elif select_option == "Subtraction":
    print(number_1, " - ", number_2, " = ", number_1-number_2)
elif select_option == "Multiplication":
    print(number_1, " * ", number_2, " = ", number_1*number_2)
elif select_option == "Division":
    print(number_1, " / ", number_2, " = ", number_1/number_2)
elif select_option == "Modulus":
    print(number_1, " % ", number_2, " = ", number_1 % number_2)

else:
    print("Please select only following options")
