import random


small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
num = "123456789"
symbols = "@,.-_"

all = symbols+num+small
lenth = 8
passs = "".join(random.sample(all,lenth))

print(passs)
