import string
import random

char1 = list(string.ascii_lowercase)
char2 = list(string.ascii_uppercase)
char3 = list(string.digits)
char4 = list(string.punctuation)
# char  = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

char_num = input("How many cahracter you want for the password?:")

while True:
    try:
        char_num = int(char_num)
        if char_num < 6:
            print('Please enter at least 6 characters..')
            char_num = input('Please enter the number again:')
        else:
            break
    except:
        print('Enter numbers only..')
        char_num = input("How many cahracter you want for the password?:")

random.shuffle(char1)
random.shuffle(char2)
random.shuffle(char3)
random.shuffle(char4)

sec1 = round(char_num * 0.3)
sec2 = round(char_num * 0.2)

password = []

for i in range(sec1):
    password.append(char1[i])
    password.append(char2[i])

for i in range(sec2):
    password.append(char3[i])
    password.append(char4[i])

password = "".join(password)
print(password)