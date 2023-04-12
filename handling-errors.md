# How To Handle Errors In Python - Try, Except, Else & Finally Block

## While coding in Python, you'll most likely run into [errors](https://www.freecodecamp.org/news/common-errors-in-python-and-how-to-fix-them/) that can cause your program to crash, but we'll be looking at how you can handle those error and prevent your program from crashing

## In this article we will be looking at how to use try-except, else and finally block to handle errors in Python, and we'll also see how we can redirect the error to a log file

### It will be amazing to have prior Python error experience  but don't worry 😁, we will be handling those errors

## Try-Except Block -

In Python, a try-except block is used to handle exceptions, which are runtime errors that occur when we run our programs. Using the try-except blocks in your program will help you handle these error when they occur and also prevent your program from crashing. Here's an example of how to use try-exception block in Python:

```python
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
```

In the code above, the block of code that might cause an error is indented in the try block, there are multiple exemption types that you might run into but we will only look at two:

1. NameError: This is raised when a variable or function is referenced before it is defined.

2. Exception: This is the base class for all exceptions, you can also inherit it to define custom exceptions

The exeptions are declared in a tuple and saved `as` 'e', then inside of conditionals we can check if 'e' is a NameError using the `isinstance()` function.
