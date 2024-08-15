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
import requests # this gets the "requests" module ready to use
response = requests.get('')

```

## Using someone else's script