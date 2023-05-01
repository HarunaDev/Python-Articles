# How To Handle Data In Files With Python - A Beginners Guide

![File image](./img/text-file.jpeg)

## In this lesson, we will be handling data inside of a text file with Python

### We will also look at files in Python as a sequence of lines that we can iterate through and also perform certain methods on

### This lesson will help you use python to work with secondary data on your computer

Before now, In your python programs you have probably been working with data that you pass in through the terminal, and the ones you construct using Strings, Lists, Dictionaries etc.

But we will use python to work with data inside of a text file. We can do this by creating a handle with the `open()` function, this handle specifies how python should treat the file.

It takes in some arguments but we will be looking at `file` & `mode` in this lesson. You can create a handle using the code below:

```python
fhandle = open(<file>, <mode=''>)
```

We stored the `open` function inside a variable `fhandle` 