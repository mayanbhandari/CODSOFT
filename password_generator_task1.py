#Password Generator TASK-1
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
password_letters = int(input("How many letters would you like in your password?\n")) 
password_symbols = int(input(f"How many symbols would you like?\n"))
password_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Password (letters,symbols,numbers in order) using string
# password = "" #Empty string variable

# for char in range(1, password_letters + 1):
#   password = password + random.choice(letters) #String concatenation

# for char in range(1, password_symbols + 1):
#   password = password + random.choice(symbols) #String concatenation

# for char in range(1, password_numbers + 1):
#   password = password + random.choice(numbers) #String concatenation

# print(password)

#Hard Level (mixture of letters, symbols, numbers) using list
password_list = []

for char in range(1, password_letters + 1):
  password_list += random.choice(letters)

for char in range(1, password_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, password_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list) #To shuffle the list
print(password_list)

password = "" #Empty string variable
for char in password_list:
  password += char

print(f"Your password is: {password}") 