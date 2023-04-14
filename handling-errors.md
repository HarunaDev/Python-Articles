# How To Handle Errors In Python - Try, Except, Else & Finally Block

## While coding in Python, you'll most likely run into [errors](https://www.freecodecamp.org/news/common-errors-in-python-and-how-to-fix-them/) that can cause your program to crash, but we'll be looking at how you can handle those errors and prevent your program from crashing

![Error Image](./img/error.jpeg)

## In this article, we will be looking at how to use try-except, `else`, and `finally` block to handle errors in Python

### It will be nice to have prior Python error experience, but don't worry 😁, we will be handling those errors

## Try-Except Block-

In Python, a try-except block, is used to handle exceptions, which are runtime errors that occur when we run our programs. Using the try-except blocks in your program will help you to handle errors when they occur, and prevent your program from crashing. Here's an example of how to use a try-exception block in Python:

```python
# try except block
try: 
    # code that might cause error
    names = ["Jane Doe", "John Doe"] 
    user = namess[0] #this line will raise a NameError & next line won't execute
    print(user)

    #using multiple exceptions by specifying them in a tuple
except (NameError, Exception) as e: 
    #check if exception is a NameError to print specific message
    #else print error message
    if isinstance(e, NameError): 
        print("Name error")
    else: 
        print(f"{e}")
```

In the code above, the block of code that might cause an error are in the try block, there are multiple exemption types that you might run into, but we will only look at two:

1. NameError: Is raised when a variable or function is referenced before it is defined.

2. Exception: This is the base class for all exceptions, you can also inherit it to define custom exceptions

The exeptions are declared in a tuple and saved `as` 'e', then inside of conditionals we can check if 'e' is a NameError using the `isinstance()` function. This allows us to return specific error messages based on the exception.

## Else-

You can include an `else` block after the `except` block, it will only run if no exceptions occur in the try block

```python
# try except block
try: 
    # code that might cause error
    names = ["Jane Doe", "John Doe"] 
    user = namess[0] #this line will raise a NameError & next line won't execute
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
```

## Finally-

The finally block will always be executed regardless if there was an exception or not

```python
# try except block
try: 
    # code that might cause error
    names = ["Jane Doe", "John Doe"] 
    user = namess[0] #this line will raise a NameError & next line won't execute
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
```

## Conclusion

Knowing how to handle exceptions in Python will be a crucial skill in your programming career, Practicing with other [exception types](https://docs.python.org/3/library/exceptions.html) and including what you have learned from this article into your own projects will help you understand it better.
