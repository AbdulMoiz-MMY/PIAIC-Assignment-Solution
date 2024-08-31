# ********************** 1. Simple Message  **********************
# Task: Assign a message to a variable and then print that message.

message: str = "HI! everyone"
print(message)

# *********************** 2. Simple Messages **********************
#  Assign a message to a variable and print that message.
change_msg: str = "HEllO"
# Change the value of the variable to a new message, and print the new message.
change_msg = "MY name is Abdul Moiz"
print(change_msg)
# ********************** 3. Personal Message *********************
# Use a variable to represent a person’s name.
person_name: str = "Abdul Moiz"
# Print a message to that person, such as, “Hello Eric, would you like to learn some
# Python today?”
print(f"{person_name}, would you like to learn some python today?")
# ********************* 4. Name Cases ***************************
# ● Use a variable to represent a person’s name.

person_name1: str = "SiR JaHanZaIb taYyAb"

# ● Print the person’s name in lowercase, uppercase, and title case.
# Title Case:
print(person_name1.title())
# Upper Case:
print(person_name1.upper())
# Lower Case:
print(person_name1.lower())

#  ******************** 5. Famous Quote **********************

# Find a quote from a famous person you admire.
quote: str = "A person  who never made a mistake never tried anything new."

# Print the quote and the name of its author.

print(f'Albert Einstein once,"{quote}"')
#  ******************* 6. Famous Quote 2 ****************
# ● Use a variable called famous_person to represent the famous person’s name.
famous_person = "Albert Einstein"
# ● Compose the message and represent it with a variable called message.
message_famous = f'{
    famous_person}  "Renowned physicist known for the theory of relativity."'
# ● Print the message.
print(message_famous)

#  ******************** 7. Stripping Names *********************
# Use a variable to represent a person’s name, and include some whitespace characters
# at the beginning and end of the name.
person_name2: str = "      sir Zia .      "
person_name3: str = "    Khan   "
# Make sure you use each character combination, \t and \n, at least once.
print(f"{person_name2} \n \t {person_name3}")

# Print the name once, so the whitespace around the name is displayed.

print(person_name2)

# Print the name using each of the three stripping functions: lstrip(), rstrip(), and
# strip().

# left-strip:
print(person_name2.lstrip())

# right-strip:
print(person_name2.rstrip())

# Strip:
print(person_name2.strip())

#  *************************** 8. Variable Sum **********************
# Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.
x: int
y: int
z: int
x, y, z = 5, 10, 15

sum = x+y+z
print(x, "+", y, "+", z, " = ", sum)

#  *********************** 9. Variable Swap *************************

# Swap the values of two variables a and b. Print the values before and after the swap.

a = 15
b = 20
# swap the Value
swap = a
a = b
b = swap

print("value of (a)", a)

#  ********************** 10. Favorite Color ************************

# Create a variable with your favorite color and print it.
color = "Black"
print(color)
# Then change the variable name to something else and print the color again.
fav_color = color
print(fav_color)

# ******************** 11. Changing Pet Name ***********************
# Create a variable pet_name and set it to "Buddy".Change the value of pet_name to "Max" and print the new value.
pet_name = "Buddy"
pet_name = "MAX"

print(pet_name)

# ******************* 12. Observing Name Error ********************

# Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a
# variable with a different name (like sunsine) and observe the error.

sunshine = "observe the Error"
# print(sunsine)
print(sunshine)

# ****************** 13. Reassigning Score *************************
# Assign the value 100 to a variable score and print it. Then assign a new value to score
# and print it again.

score = 100
print(score)
score = 80
print(score)

# *************** 14. City Name ******************************
# Create a string variable city and assign it the name of a city you like. Print the city name.
city: str = "Lahore"
print(city)
# *************** 15. Title Case Text *************************
# Create a variable text with the value "python programming" and print it in title case.

learn = "PyThoN pRoGraMmIng"
print(learn.title())

#  **************** 16. Lowercase Conversion *****************
# Assign a string with mixed cases to a variable and print it in all lowercase letters.
learn = "PyThoN pRoGraMmIng"
print(learn.lower())
# *************** 17. Uppercase Conversion *******************
# Assign a string with mixed cases to a variable and print it in all uppercase letters.
learn = "PyThoN pRoGraMmIng"
print(learn.upper())

# ************** 18. Current Temperature *********************
# Create a variable temperature with the value 25. Print "The current temperature is
# [temperature] degrees." using the variable.

temperature = 25
print(f"The current Temperature is {temperature} degrees")

# ************* 19. Printing a Poem ***************************
Poem: str = '''
        Life is an opportunity, benefit from it
                 Life is beauty,admire it

        Life is a dream, realize it
                 Life is a challenge, meet it

        Life is a duty, complete it
                 Life is a game, play it

        Life isa promise,fulfil it
                 Life is sorrow, overcome it

        Life is a song, sing it
                 Life is a struggle, accept it

        Life is a tragedy, confront it
                 Life is adventure, dare it

        Life is luck, make it
                 Life is too precious, do not destroy it

        Life is life, fight for it
'''
print(Poem)