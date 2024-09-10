# What is Python?

Python is a programming language. 

A programming language is a way of asking a computer to do something. The thing you're asking the computer to do can be called "code", a "program" or a "script". They are all subtley different but for our purposes they all mean things that you ask the computer to do. I'll probably use all of these terms as we go through the course.

Like with all programming languages, with Python:
- The computer will do **exactly** what you ask it to
- The computer **cannot guess** and is **not ambiguous**!
  - You must explain each step of a process to the computer, you can't skip step that are *obvious* because they are not obvious to the computer
- If it doesn't understand what you've asked it to do, it will tell you. 
  - This may or may not be a helpful message!

## Why Python?

We use Python for many reasons. Some of the best reasons are:
- It is used in many different places
  - Industry
  - Academia
  - Hobbies
- It is used for many different tasks
  - Data visualisation
  - Processing data
  - Managing computers
  - Hobbies
- It is generally considered easy to learn
- Lots of people have written Python that you can use and adapt for your needs
  - These could be scripts you can use directly or packages/libraries that you can integrate into your programs

## Which version of Python?

**Version 3**. 

Python has been in development since 1991. There are two main versions of Python. We will always be using version **3** of Python. If you are looking for online help, tips, courses etc, make sure they are for version 3. 

Version 2 is now not recommended and is used only for old projects.

## How do I *do* Python?

Python can be used in many different ways. We will be using **Jupyter Notebooks** and running them in **Google Colab**. This is a way of writing Python where you can quickly build scripts and see the output.

Python can also be used as:
- A Jupyter notebook that you run on your own computer (or someone else's)
- A script that you run directly on your computer
  - We will not be going through installing Python on your computer in this course but if you want to do so you can find  [instructions](installPython.md)
- A script that you run on *someone else's computer*
  - This is a common scenario when using a research computer like [NREC](https://nrec.no/) or [NRIS](https://www.sigma2.no/about-us) - the cloud and super computers that UiB runs and has access to
  - We will not be covering this in this course. If you want to know more, come to the drop in session!

## What does a Python script look like?

A Python script is a text file so you, as a human can read it as well as the computer being able to interpret it. 

The following is a complete Python script

```python
"""
A script to show the user the current time.

Author: Matthew Pitkin
Email: m.pitkin@lancaster.ac.uk
Date: 22/06/2020
"""

# import the required packages (this is someone else's code, not Matthew's)
import datetime


def gettime():
    """
    A function to return the current time.

    Returns
    -------
    tuple:
        A tuple containing the hour, minutes and seconds.
    """

    now = datetime.datetime.now()

    return now.hour, now.minute, now.second + 1e-6 * now.microsecond

# get the time
hour, minute, seconds = gettime()

print(f"The current time is {hour}:{minute}:{seconds}")
```

Want to see the output? Let's look together on  [Google Colab](http://colab.research.google.com/github/dfbr/pythonLessons/blob/main/Notebooks/currentTime.ipynb).<!--
https://stackoverflow.com/questions/52131683/open-google-colab-notebook-from-url 
-->

## Key points

- Python is a programming language
- We will use version 3
- We are going program using Jupyter notebooks in [Google colab](https://colab.research.google.com/).

## [Next lesson](jupyterNotebook.md)