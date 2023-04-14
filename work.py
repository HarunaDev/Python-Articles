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