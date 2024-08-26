# Loops (or doing the same thing over and over again)

Often when programming, we want to do the same many times. This is often:
- the same thing while a condition is met
- the same thing for every item on a list

Python, like most programming languages, has tools to help you do this. They are known as `while` loops and `for` loops.

## While loops

A `while` loop will keep carrying out the instructions *while* the condition you give it is true.

```python
volume = 100

while volume > 50:
    print(f"It's too loud at {volume}. Turn it down")
    volume -= 1
print("When the condition is no longer true, we continue with our script")
```
Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/whileLoops.ipynb)

## For loops

A `for` loop is slightly different in that it will do the same thing for every item of a list. When would you use this?
- You have a list of measurements from different weather stations and you want to do the same thing with each of the measurements
- You have a list of class attendees and you want to send all of them a personalised feedback survey
- Anything else where you want to do the same thing to a set of data

Here's the example:

```python
# first we define a list
myList = [1,2,3,4,5]

# now we set up a loop
for item in myList:
    print(f"{item} doubled is {item * 2}")
```

Let's [play with for loops](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/forLoops.ipynb)

## Key points

- We use a `while` loop when we want to do the same thing **while** a condition is met
- We use a a `for` loop when we want to do the same thing **for** every item in a list

## Extra resources

- [While loops](https://www.geeksforgeeks.org/python-while-loop/)
- [For loops](https://www.geeksforgeeks.org/python-for-loops/)