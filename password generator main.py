import string
import random


all_list = string.ascii_letters + string.digits + string.punctuation + string.digits + string.ascii_uppercase + string.ascii_lowercase



length = int(input("Enter the length of the password: "))


password = ''.join(random.choices(all_list, k=length))


print("Your password is:", password)