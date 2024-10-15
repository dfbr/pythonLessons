# Using other people's code

One of the reasons that we choose Python is because there is lots of other people's code already available. How do we use it?

There are two main ways:
- Using a package of code in your own script
- Taking someone else's script and running it on your computer
  - You may need to edit it to make it work exactly how you want

## Importing external code

The main way of using someone else's code is through a package.

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

There are LOTS of packages for many, many different things. In fact, there are so many it's impossible to know what they all do so you will need to search for the right package for your task.

Some common packages that _may_ be useful are:
- os
  - For interacting with the operating system of the computer
- sys
  - For doing things like listing directory contents
- datetime
  - For handling dates and times including finding differences between dates and times
- matplotlib
  - For making data visualisations
- pandas
  - For doing data analysis
- requests
  - For getting files from the internet

In colab, most these packages are already installed. If you are working on your own computer, you may need to install them yourself using the [`pip` command](https://packaging.python.org/en/latest/tutorials/installing-packages/).

If you want to use a package in colab that isn't already installed, you can still use `pip` to install it but you need to add an `!` before the `pip` like this: `!pip install matplotlib`

Let's [try it out](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/externalCode.ipynb)

## Using someone else's script

You can of course use your [favourite search engine](https://duckduckgo.com/) to find a script that does what you want to do (or ask a [friendly AI](https://chat.uib.no) to write one for you). But when things get specific it's unlikely that you'll find an exact match or get an exact program from your AI. 

In this case, you can copy a Python script into a blank notebook and start editing it from there. 

### But what does that script *do*?

You can of course read the script through to understand what it does. If the script is written clearly, it should be understandable. As I'm sure you've guessed, there are tools to help here. You can use [UiB's ChatGPT](https://chat.uib.no) to explain a script to you.

Try it with this:
- Copy the example below to a new jupyter notebook.
- Make a new directory/folder in the notebook called "images" and copy some image files to it (e.g. png, gif or jpeg files)
- Use the example script to resize the images in your directory to 500 x 500
- Save them with the the word `resized_` before to the original filename

```python
# first we import "Image" from the PIL package
from PIL import Image
# next we import the os package because we want to interact with files
import os

input_folder = './images'
output_folder = './images'
desired_size = (100, 100)

for filename in os.listdir(input_folder):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.thumbnail(desired_size)
        img.save(os.path.join(output_folder, filename))
```

[Try it out](https://colab.research.google.com/). (Ctrl/Command/Shift click on link to open in a new tab/window)

You can of course also use ChatGPT to make these changes for you and providing you understand it's output (and can safely test it) then this is a perfectly acceptable way of programming.

## Key points

- We can use packages to make it easier to perform common tasks
- We will need to search for a package
- We will need to read the documentation to use a package
- When we use someone else's script, we may need to edit it

## [Next lesson](programmingErrors.md)