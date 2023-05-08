# What Are Strings In Python?

## In this article, we will look at Strings as a built-in data type in Python and some methods that you can perform on a string

## It is important to know what strings are and how you can use them when writing your programs

![String Image](https://images.pexels.com/photos/12749141/pexels-photo-12749141.jpeg?auto=compress&cs=tinysrgb&w=600)

### An understanding of [arrays](https://www.w3schools.com/python/python_arrays.asp) in Python or any other language will be helpful if you want to understand this article

***  

## Strings

In Python, a string is a sequence of characters enclosed in either single quotes (' '), double quotes (" ") or triple quotes (''' ''')

Strings are one of the built-in primitive data types in Python and are used to manipulate how the computer prints and handles text data. For example:

```python
# Single quotes string
print('hello world')

# Double quotes string
print("It's a good day")

# Triple quotes string
print('''Multi
Line
String''')
```

But under the hood, A string in Python is a sequence of characters, or an array of characters, where each character is indexed by its position in the string.

Which allows us to perform array-like methods to manipulate the data in the string. As we can see here:

1. String Indexing: You can access individual characters in a string using the square brackets notation `[i]`, and the 'i' represents the index which starts from 0 for the first character and increases subsequently for the rest. For example:

    ```python
    # String Indexing
    my_string = "hello world"

    first_char = my_string[0] # h
    second_char = my_string[1] # e
    last_char = my_string[-1] # d
    ```

2. String Slicing: You can get a substring from a string using slicing, this allows you to specify the range of indices. you use a colon `:` to separate the start and end index. The start index is inclusive while the end index is excluded. For example:

    ```python
    my_string = "hello world"
    substring = my_string[2:-2] # "llo wor"
    ```

3. String Iteration: A string being an array of characters allows us to iterate through each character using a [`for`](https://www.freecodecamp.org/news/for-loops-in-python-with-example-code/) loop. For example:  

    ```python
    my_string = "hello"

    for char in my_string:
        print(char) # This will print each character in my_string on individual line in your terminal
    ```

4. String Length: You can find the length of a string by using a global function `len()` to get the number of characters in that string. For example:

    ```python
    my_string = "hello"

    length = len(my_string) # 5
    ```

## Conclusion

We have talked about strings and how they are a sequence of characters, and this allows us to perform array-like methods on the string.  

So when next you're writing code, see your strings as an array that stores a sequence of characters.
