import random
charset = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
length = 16
password = []
for i in range(0, length, 1):
    password.append(random.choice(charset))
print(''.join(password))
