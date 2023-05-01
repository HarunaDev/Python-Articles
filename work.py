# get binary number
print(bin(66))

# try except block
try: 
    # code that might cause error
    names = ["Jane Doe", "John Doe"] 
    user = names[0] #this line will raise a NameError & next line won't execute
    print(user)

    #using multiple exceptions by specifying them in a tuple
except (NameError, Exception) as e: 
    #check if exception is a NameError to print specific message
    #else print error message
    if isinstance(e, NameError): 
        print("Name error")
    else: 
        print(f"{e}")
# else block 
else:
    # code to execute if there are no exceptions
    print(user)
# finally block
finally:
    # code to execute regardless of an exception or not
    print("end of program")

# module code
def greet(text):
    print(text)

# random code
import random

name = "alvin"
char = random.choice(name)
print(char)

# fcc python try, except 
# sh = input("Enter Hours: ") 
# sr = input("Enter Rate: ") 
# try:
#     fh = float(sh) 
#     fr = float(sr)
# except Exception as e:
#     print("Enter numeric input")
#     quit()

# print(fh,fr)
# if fh > 40:
#     reg = fr * fh
#     otp = (fh - 40.0) * (fr * 0.5)
#     xp = reg + otp
# else:
#     xp = fh * fr
# print("Pay:", xp)

# FCC for loop
list = ["apple","mango", "water melon"]

for fruit in list:
    print("I love", fruit)

## FCC open files with python
# fhand = open("FFC-Python.md", "r")
# check '_io.TextIOWrapper'

# handle opening a wrong file
hand_doc = input("Enter file name: ")

fhand = open(hand_doc)

for line in fhand:
    line = line.rstrip()
    if '#' in line:
        print(line)

# search through file
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('#'):
#         print(line)

# read file as a sequence of characters
# imp = fhand.read()

# print(len(imp))

# count lines in file
# count = 0

# for line in fhand:
#     count = count + 1
# print("lines counted:", count)
