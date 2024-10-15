# Review of previous lesson

In the last lesson we covered several topics. Here is a quick recap...

- You are learning Python
  - Python is a programming language that runs on many different computers
- We are running Python in a Jupyter notebook
  - This is a way of interactively developing and running Python code
  - Specifically, we are using google colab to run our Jupyter notebooks
- Comments are not interpreted by Python, the are a present to ourselves so we can understand our code
  - Comments come after a `#` character
- A variable is a way of storing a value that we can the use in our program
  - We define a variable as `variableName = variableValue`
  - Variables can have different types, common types include:
    - Integers
    - Floating point numbers
    - Strings
    - Booleans (True or False)
  - Python is case sensitive so `myVariable != MYVARIABLE`
- A list is a set of variables such as the members of a class or a collection of book titles
  - A list is just a certain type of variable
  - We define a list as `listName = [listItem1,listItem2,listItem3]`
  - We access individual items with the number index (starting at 0), e.g.
    - `listName[3]` would be the fourth item in the list
- A dictionary is a set of variables that belong together such as the different readings from a weather station
  - A dictionary is another type of variable
  - We define a dictionary as `dictionaryName = {dictionaryKey1: dictionaryValue1, dictionaryKey2: dictionaryValue2}`
  - We access individual items in the dictionary with `dictionaryName['dictinaryKey1]`
- We can use Python to make choices using `if` statements.
  - The general form of an if statement is:
  
```
  if condition:
    do this
  elif secondCondition:
    do this
  else:
    do this
```