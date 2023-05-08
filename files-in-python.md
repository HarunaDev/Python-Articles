# How To Handle Data In Files With Python - A Beginners Guide

![File image](./img/text-file.jpeg)

## In this lesson, we will be handling data inside of a text file with Python

### We will also look at files in Python as a sequence of lines that we can iterate through and also perform certain methods on

### This lesson will help you use python to work with secondary data on your computer

Before now, In your python programs, you have probably been working with data that you pass in through the terminal, and the ones you construct using Strings, Lists, Dictionaries etc.

## How to handle files in Python

But we will use python to work with data inside of a text file. We can do this by creating a handle with the `open()` function, this handle specifies how python should treat the file.

It takes in some arguments but we will be looking at `file` & `mode` in this lesson. You can create a handle using the code below:

```python
fhandle = open(<file>, <mode=''>)
```

We stored the `open` function inside a variable `fhandle`, and this function takes in two arguements, the first arguement specifies what file in your computer you want to open.

The second arguement specifies how you want python to treat the file, we will only cover three modes in this lesson, which are;

- `'r'` (read-only): This mode opens a file for reading. The file pointer is placed at the beginning of the file. If the file doesn't exist, an error is raised.

    When we don't specify the mode, python handles our file in read mode by default.

- `'w'` (write): This mode opens a file for writing. If the file already exists, it's contents are truncated. If the file doesn't exist, a new file is created.

- `'a'` (append): This mode opens a file for appending. If the file already exists, new data is written at the end of the file. If the file doesn't exist, a new file is created. The file pointer is placed at the end of the file.

## Files as a sequence in Python

A `file handle` open for read can be treated as a sequence of lines, and we can use the (for)[] loop to iterate through each line in the sequence. It is good to know that a sequence is an ordered set.

We can iterate through the lines in the file using the code snippet below;

```Python
fhandle = open(<file>)
for line in fhandle:
    print(line)
```

