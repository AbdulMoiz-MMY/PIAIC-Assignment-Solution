userName = str(input("Enter your Name: "))
user_msg01 = f"Hello,{userName.title()} ! Let's explore your favorite numbers."
print(user_msg01)

numbers = []
numbers.append( int(input("Enter your First favorite number: ")))
numbers.append(int(input("Enter your Second favorite number: ")))
numbers.append(int(input("Enter your Third favorite number: ")))

even_odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_odd_list.append((num,"Even"))
    else:
        even_odd_list.append((num, "Odd"))
    
for num, status in even_odd_list:
        print(f"The Number {num} is {status}")
print("\nHere's your favorite numbers and their squares.")

for num in numbers:
     print(f"The number {num} and its square: ({num}, {num**2})")

sum_numbers = sum(numbers)

print(f"\nAmazing! the sum of your favorite number is: {sum_numbers}")

prime = True

if sum_numbers <= 1:
    prime = False
else:
    for i in range(2, int(sum_numbers**0.5) + 1):
        if sum_numbers % i == 0:
            prime = False
            break

if prime:
    print(f"Wow, {sum_numbers} is a prime number!")
else:
    print(f"{sum_numbers} is not a prime number, but it's still special!")
