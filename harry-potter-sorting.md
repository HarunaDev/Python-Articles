# Learn About Random Module In Python By Building Hogwarts House Sorter

## In this article, you will learn how to use the Python random module, and you will also write a Python script that sorts users into different Hogwarts houses 🧙‍♂️

![IMAGE](./img/random.jpg)

### Before building our application, we need to understand what a module is and how we can use the random module in our app

## What is a Module in Python

In Python, A module is a file that contains code that you can import and use in other Python programs. A module can have methods you can call in your programs to perform a task without worrying about implementation details.

To create and use a module in your Python program, create a new Python file and write a simple function that takes in a parameter and prints out the parameter with some text. Follow the instructions below:

### Create a module

```bash
code greetings.py
```

### Write a function in the module

```python
def greet(text):
    print(f"Hello, {text}")
```

### Create a new Python file

```bash
code app.py
```

### Import and use module inside the `app.py` file

```python
# import greetings module to program
import greetings

# call the greet function
greetings.greet("Alvin")
```

In the example above, we created a module and imported the module to our Python program and called a method in that module to perform a task.

Python has a standard library of modules, but we will look at the Random module in Python.

### Random Module

The Python `random` library is a built-in module that allows us to generate Pseudorandom numbers. Pseudorandom numbers appear random, but they are generated using a deterministic algorithm.

The `random` library is commonly used in Python for task that requires generating random numerical values in your program. Here are some functions in the `random` library:

1. `random()`: This function returns a pseudorandom floating point number between 0 and 1, inclusive of 0 but exclusive of 1.

    ```python
    import random

    num = random.random()
    print(num) # this will print a random float between 0 and 1
    ```

2. `randint(a, b)`: This function takes two arguments and returns random numbers between `a` and `b` inclusive.

    ```python
    import random

    num = random.randint(1, 5) # This will return a random integer between 1 and 5.
    ```

3. `choice(sequence)`: This function takes in an argument which must be a sequence, for example, a list or [string](https://harunadev.hashnode.dev/what-are-strings-in-python), and returns a random element from that sequence.

    ```python
    import random

    # declare a sequence and call the choice method
    name = "Alvin"
    char = random.choice(name)

    print(choice) # it will print a random character from the string
    ```

4. `shuffle(sequence)`: This function takes a sequence as an argument and shuffles the elements inside it, meaning it modifies the original sequence.

    ```python
    import random

    # declare sequence and call the `shuffle` method
    my_list = ["Apple", "Ball", "Car", "Dog"]
    random.shuffle(my_list)

    print(my_list) # a modified list with shuffled elements     
    ```

There are other [random library](https://www.w3schools.com/python/module_random.asp) functions that you can use in your Python program.

So now we can apply some of the topics we learned to build our sorting app.

## Implementation details

Let us look at some steps we should take as we build our app.

```python
# import random library
# display the app intro and how to play game
# store Hogwarts houses in a list
# get details from the user
# get a random house from the list
# print the result to the user 
```

Now that we have these steps mapped out. Let us begin coding. Type the code snippet below in your Python script:

```python
# import random library
import random

# display the app intro and how to play game
print('''Welcome to Hogwarts School of Witchcraft and Wizardry

Motto: Draco Dormiens Nunquam Titillandus 

Enter your details to get sorted into a house in Hogwarts by the sorting hat.\n''')


# store Hogwarts houses in a list
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# get details from the user
name = input("Enter your full name: ")
location = input("Enter your location: ")

# get random house from list
sorting_hat = random.choice(houses)

# print the result to the user
print(f"\n{name} from {location}, you have been added to {sorting_hat}!")
```

The code above is a Python script that simulates the sorting process at Hogwarts School of Witchcraft and Wizardry. It uses the random module to randomly assign the user to one of the four Hogwarts houses: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin.

The script starts with an introduction and instructions for the game, displaying the motto of Hogwarts: "Draco Dormiens Nunquam Titillandus" which translates to "Never tickle a sleeping dragon.", It then prompts the user to enter their full name and location.

Next, the random.choice() function is used to randomly select one of the four houses from the houses list. The selected house is then printed out along with the user's name and location, indicating that the user has been sorted into that house.

## Conclusion

We were able to create and import a module, and then we learned about the Python random module and some functions that we can perform with it.

Then we applied what we learned in writing our Hogwarts House Sorting script.
