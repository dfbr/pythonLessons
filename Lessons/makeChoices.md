# Make choices with Python

One of the main things used to make code more powerfull is making choices. The normal way of doing this is with an `if` statement.

In my life it works like this:
```
if it's morning:
    Drink coffee
if it's afternoon:
    Drink water
if it's evening:
    Drink more water
if it's none of these:
    Sleep
```

Python works in very much the same way. We need to use clear and unambiguous *syntax* to make sure the computer knows how to interpret the instructions.

```python
timeOfDay = "morning"

if timeOfDay == "morning":
    print("Coffee please!")
elif timeOfDay == "afternoon":
    print("Just water right now")
elif timeOfDay == "evening":
    print("Water again please.")
else:
    print("What are you doing awake?")
```

We need to give Python a **condition** that it can evaluate. This is the `timeOfDay == "morning"` part. 

Note the double `=` sign. This doesn't assign a value to a variable, instead it asks the question **is the value on the left equal to the value on the right?**.

The condition doesn't have to be `==`. It can be anything that evaluates to **True** or **False**.

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/choices.ipynb)!

## Key points

- When we want to make a choice we use an `if` statement
- We set a condition that must ultimately evaluate to either `True` or `False`
- After testing a condition, we can take action based on the result

## Extra resources

[List of basic comparison operators](https://www.w3schools.com/python/gloss_python_comparison_operators.asp)

[Python and boolean values](https://realpython.com/python-boolean/) (including using boolean values to construct condition statements)

[![If statements](https://img.youtube.com/vi/-BOBedcjySI/maxresdefault.jpg)](https://www.youtube.com/watch?v=-BOBedcjySI)

