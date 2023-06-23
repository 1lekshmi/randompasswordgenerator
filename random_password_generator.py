import random

# function to shuffle all the characters in the string
def shuffle_char(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


# the generated password should be 8 characters long and include
# 2 uppercase letters from A-Z = ASCII code (65-90)
# 2 lowercase letters from a-z = ASCII code (97-122)
# 2 digits from 0-9 = ASCII code (48-57)
# 2 punctuation signs such as !, ?,  ", # etc ASCII code (32-47,58-64,91-96)

uppercase_letter1 = chr(random.randint(65,90))
uppercase_letter2 = chr(random.randint(65,90))

lowercase_letter1 = chr(random.randint(97,122))
lowercase_letter2 = chr(random.randint(97,122))

digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))

punctuation1 = chr(random.randint(32,47))
punctuation2 = chr(random.randint(58,64))

password = uppercase_letter1 + uppercase_letter2 + lowercase_letter1 + lowercase_letter2 + digit1 + digit2 + punctuation1 + punctuation2
password = shuffle_char(password)

print(password)