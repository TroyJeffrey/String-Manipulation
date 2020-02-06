#Troy Jeffrey Ameegashie
#STring Manipulation

print("Enter a list of words")
user_list = input(">")

print("The length of the string is :", len(user_list))

first_letter = user_list[0]
print(f"The first letter of the string is :", first_letter)

last_letter = user_list[-1]
print(f"The last letter of the string is :", last_letter)

print(f"Here is the string in upper case :", user_list.upper())

print(f"Here is the string in Title case :", user_list.title())

print(f"The string contains only alphabets. True or False? :", user_list.isalpha())

print(f"Here is the string split up into individual words :", user_list.split(','))

reversed=''.join(reversed(user_list))
print(f"Here is the string reversed : ", reversed)
