# Key concepts of Python

As we are going to used it, the key concepts of Python are very similar to many other programming languages so the concepts of this lesson are transferrable. Each programming language has it's own _syntax_ which means the exact examples in Python are probably not valid in any other language.

## Which concepts will we learn?

- Comments
- Syntax
  - Case sensitivity
  - White space matters
- Variables
  - What is a variable?
  - How do we assign variables?
  - How do we change variables?
  - What type of variables can we have?
- Lists
  - What is a list?
  - What do we use lists for?
  - How do we assign lists?
  - How do we access a list item?
  - How do we add an item to a list?
  - How do we remove an item from a list?
  - Can we select more than one list item?
- Dictionaries
  - What is a dictionary?
  - What do we use disctionaries for?
  - How do we access a dictionary value?
  - How do we add a dictionary item?
  - How do we remove a dictionary item?
- Making choices
  - Why would we want to make a choice?
  - What sort of conditions can we use?
  - What happens after we've made the decision?
- Repeating actions (loops)
  - for loops
  - while loops
- Using other people's code
  - Install a module
  - Import a module to a script
  - Use a function

## Comments

One of the most important things in a program isn't the instructions that you give to the computer, it's the insight you give to your future self! These are comments in the code.

The computer completely ignores comments. They are only for the human.

In Python we make a comment by using a `#` character.

The `#` can appear anywhere on a line and everything after it is ignored and for the human only.

There isn't much to try with comments so there are no exercises here but we'll use comments in our next section...

<!--
I don't think we need a section on this.
## Syntax

Syntax in a programming language is the set of rules to make sure your program is understandable to the computer. This includes:
- How you indent your code
- The punctuation that you use
- The letters and symbols that you use
- Some of the words that you (don't) use

Let's [try it out]()
-->

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

The variable name is case sensitive so `MYVARIABLENAME` and `myvariablename` are two different variables.

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/variables.ipynb)!

## Lists

Sometimes we have a lot variables that belong together. They may belong together because they're a group (like all of your names as members of this class), they may belong together because you want to do similar things with all of the different variables.

We could have a variable for each different member of the group:

```python
classMember1 = "David"
classMember2 = "Bjørn"
classMember3 = "Sarah"
classMembern = "Zoe"
```

This works but becomes hard to manage. A better way is to group all of the class members together in a variable that is of the **list** type:

```python
# here we define our list
classMembers = ["David",
                "Bjørn",
                "Sarah",
                "Zoe"]

# now we can use it in our program
```

We can then add and remove people from the list or perform tasks against each member of the list.

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/lists.ipynb)!

## Dictionaries

We have a group of variables that belong together, but what about a variable that has a set of values? Yes, there is a Python concept for this too and it's called a dictionary.

What sort of things belong together? Think about a weather station. This could have a set of different values that are collected at the same place and time.

```python
windSpeed = 14
windDirection = 189
precipitation = 14
temperature = 12.8
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

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/dictionaries.ipynb)!

## Key points

- Use `#` to make a comment to your future self (and others who may read your code)
- If the syntax is wrong, your program won't work as you hope it will. The computer _should_ tell you that _something_ is wrong
- Variables hold a value that you can use in your program
- A list is a group of variables
- A dictionary is a way of storing a variable with different keys and values

## Additional resources

- [Variable name rules](https://www.w3schools.com/python/gloss_python_variable_names.asp)