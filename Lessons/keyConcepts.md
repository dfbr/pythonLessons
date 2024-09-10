# Key concepts of Python

As we are going to used it, the key concepts of Python are very similar to many other programming languages so the concepts of this lesson are transferrable. Each programming language has it's own _syntax_ which means the exact examples in Python are probably not valid in any other language.

## Which concepts will we learn?

- Comments
- Variables (and data types)
- Lists
- Dictionaries

## Comments

One of the most important things in a program isn't the instructions that you give to the computer, it's the insight you give to your future self! These are **comments** in the code.

The computer completely ignores comments. They are only for the human.

In Python we make a comment by using a `#` character.

The `#` can appear anywhere on a line and everything after it is ignored and for the human only.

It's a good idea to make comments for the following sorts of things:
- To show an outline structure to your script
- To describe how you're doing something
- To give more description to a function
- To give a reader important information such as options in a script

But comments are mainly for *you* so write yourself comments whenever you feel they are necessary.

There isn't much to try with comments so there are no exercises here but we'll use comments in our next section

### Remember

**Comments are a gift to your future self. Use them and be thankful when you get to read them later!**

## Variables

A variable can be thought of as a bucket with a name. In the bucket you can put anything you like and you can always refer to it with the name of the bucket.

To use a variable you need to _assign_ it. You do this with the `=` sign:

```python
myVariableName = 42
mySecondVariableName = 12
```

You can then use it in your script:
```python
myThirdVariableName = myVariableName + mySecondVariableName
print(myThirdVariableName)
```

The value of a variable is not fixed so you can change it based on the outcome of a statement.

```python
myFavouriteNumber = 4

# now lets make it one bigger
myFavouriteNumber = myFavouriteNumber + 1

# now we can double it
myFavouriteNumber += myFavouriteNumber
```

The `+=` operator is shorthand for saying "add what's on the right to the variable on the left". There are similar operators for other maths operations.

The variable name is case sensitive so `MYVARIABLENAME` and `myvariablename` are two different variables.

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/variables.ipynb)! (Ctrl/Command/Shift click on link to open in a new tab/window)

## Lists

Sometimes we have a lot variables that belong together. They may belong together because they're a group (like all of your names as members of this class), they may belong together because you want to do similar things with all of the different variables.

If you have used other programming languages, this may be familiar to you but you might recognise it as an *array*. For our purposes, arrays and lists are the same.

We could have a variable for each different member of the group:

```python
classMember1 = "David"
classMember2 = "Bjørn"
classMember3 = "Sarah"
classMembern = "Zoe"
```

This works but becomes hard to manage. If we want to print all of the members of the group we would need to have a print statement for each member or if Bjørn leaves the class would we need to shift up each member by one? 

A better way is to group all of the class members together in a variable that is of the **list** type:

```python
# here we define our list
classMembers = ["David",
                "Bjørn",
                "Sarah",
                "Zoe"]

# now we can use classMembers in our program
```

We can then add and remove people from the list or perform tasks against each member of the list.

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/lists.ipynb)! (Ctrl/Command/Shift click on link to open in a new tab/window)

## Dictionaries

We have a group of variables that belong together, but what about a variable that has a set of values that belong together? Yes, there is a Python concept for this too and it's called a dictionary.

What sort of things belong together? Think about a weather station. This could have a set of different values that are collected at the same place and time.

```python
bergenWeatherStationWindSpeed = 14
bergenWeatherStationWindDirection = 189
bergenWeatherStationPrecipitation = 14
bergenWeatherStationTemperature = 12.8
```

It would be nice to hold all of these in one variable. We can do that with a dictionary instead:

```python
bergenWeatherStation = {"windSpeed": 14,
                        "windDirection": 189,
                        "precipitation": 14,
                        "temperature": 12.8}
```

This becomes especially useful when you have many weather stations because you collet them together in a list of dictionaries.

The name of the attribute is called the **key** (e.g. `windSpeed` in our example above). The speed of the wind is called the `value` (e.g. 14 in our example)

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/dictionaries.ipynb)! (Ctrl/Command/Shift click on link to open in a new tab/window)

## Key points

- Use `#` to make a comment to your future self (and others who may read your code)
- If the syntax is wrong, your program won't work as you hope it will. The computer _should_ tell you that _something_ is wrong
- Variables hold a value that you can use in your program
  - Every variable has a `type`
- A list is a set of variables
- A dictionary is a way of storing a variable with different keys and values

# Extra resources

- [Lists](https://www.w3schools.com/python/python_lists.asp)
- [Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

## [Next lesson](makeChoices.md)