# Using other people's code

One of the reasons that we choose Python is because there is lots of other people's code already available. How do we use it?

There are two main ways:
- Using a module of code in your own script
- Taking someone else's script and running it on your computer
  - You may need to edit it to make it work exactly how you want

## Importing external code

The main way of using someone else's code is through a module.

People have written code that can be `import`ed to your script and you can then access the functionality just like you do with the `print()` function.

Here is an example:

```python
# first we import "pandas" with the shortened name "pd" (this just means we need to type less)
import pandas as pd

# now we use the function "read_csv()" from pandas to download a file with earthquake data in it
# we want to use this data so we assign it to a variable called df (short for dataframe, a pandas convention)
df = pd.read_csv('https://corgis-edu.github.io/corgis/datasets/csv/earthquakes/earthquakes.csv')

# to show it we got the data, lets print the first record
print(df.iloc[0])

```

There are LOTS of modules for many, many different things. In fact, there are so many it's impossible to know what they all do so you will need to search for the right module for your task.

Some common modules that _may_ be useful are:
- sys
- datetime
- matplotlib
- pandas
- requests
- beautifulSoup

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/externalCode.ipynb)

## Using someone else's script

## Key points

- We can use modules to make it easier to perform common tasks
- We will need to search for a module
- We will need to read the documentation to use a module