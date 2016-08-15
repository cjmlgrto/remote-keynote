# Programming in Python
## Code Workshop

As presented by [@cjmlgrto](http://mlgrto.com)

---

## What we'll learn

-
* Intro to Programming
* Storing and using data
* Decisions
* Functions
-

---

# Part 1: Intro to Programming

---

## Automating and Calculating

Programming was invented so humans don't have to do things over and over again

Programming is essentially writing a _set of instructions_ that a computer has to follow

---

## Calculating

Given any two numbers,

1: Add them together
2: Half it
3: If the answer is higher than the first number, say yes
4: Otherwise, say no

---

## In Python Code

```python

    x = 4
    y = 2
    answer = x + y
    halfed_answer = answer / 2
    if halfed_answer > x:
        print "yes"
    else:
        print "no"

```

---

# Part 2: Storing and using data

---

## Variables

There are different kinds of variables:

-
* _Integers_, which computers can use to do math, e.g. _42_
* _Strings_, which is text that computers can display, e.g. _"hello world"_
-

---

## Variables in Python

```python

    age = 58
    name = "John Cena"
    bio = "My favorite number is 42"

```

---

## Using variables

```python

    bill = 42 + 56
    tip = 5
    total = bill + tip
    note = "Have a nice day!"
    print(total)
    print(note)

```

---

# Part 3: Decisions

---

## If-Else Decisions

We use calculators to do math.

We use computers to do _so much more_.

With _decisions_, we can get a computer to do different sets of actions for different scenarios.

---

## If-Else in Python

```python

    price = 10
    if price < 50:
        print("That's cheap!")
    else:
        print("That's expensive...")

```

---

## More advanced decision making

```python

    color = "red"

    if color == "red":
        print("Stop!")
    elif color == "yellow":
        print("Slow down.")
    else:
        print("Green means go!")

```

### The code above, translated to human-speak:

1: The color right now is red.
2: If the color is red, say "Stop!"
3: _Else, if_ the color is yellow, say "Slow down."
4: _Otherwise_ if it isn't red or yellow, say "Green means go!"


---

# Part 4: Functions

---

## Bringing it all together with functions

In math, we can write a function that looks like _f(x) = 3x_

The above function means, input any _x_ and it will give an output of _3 times x_

We can re-use _f(x)_ over and over again giving it different values for x without having to write down _3 times x_ over and over again.

Programming functions in code is essentially the same, _except you can do more than just math!_

---

## An example function in Python

```python

    def f(x):
        answer = 3 * x
        return answer

```

### The code translated in human-speak

So the code above means we're _def_ining a function called _f(x)_

And then we calculate _3 times x_ and store it in a variable called _answer_

Then, to 'spit out' our answer, we _return_ the variable answer

---

## How to use functions in Python

We can then re-use our function, _f(x)_ multiple times in our code! Like so:

```python

    blah = f(3)
    another_blah = f(blah)
    print(another_blah)

```

We can 'pass' variables into our function, f(x) and it will spit out 3 times whatever we put in!

---

## A more advanced function

```python

    def print_receipt(subtotal):
        tax = 0.1 * subtotal
        total = subtotal + tax
        if total > 50:
            print("You bought lots today!")
        else:
            print("Have a nice day!")
        return total

```

Then, to use our function, we can write:

```python

    subtotal = 500
    total = print_receipt(subtotal)
    print("Here's what you have to pay:")
    print(total)

```

We should then get:

_"You bought lots today!"_
_Here's what you have to pay:_
_550.00_

---

## Recap

-
* _Variables_ are a way to name and store data in the computer
* _Decisions_ allow computers to figure out what to do next
* _Functions_ allow us to condense lines of code into one line and re-use it over and over
-

A great way to learn more about python is through [here](https://www.python.org/about/gettingstarted/). Note that it's quite detailed and can get technical. But pretty useful.

---

# Some Fun Stuff

-
* To install and play with Python on your computer, check [this out](http://www.macworld.co.uk/how-to/mac/coding-with-python-on-mac-3635912/) if you use a Mac, [and this](http://www.howtogeek.com/197947/how-to-install-python-on-windows/) if you use Windows.
* Want to sharpen your Python skills? [Here's a neat list](http://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/) of do-able challenges.
* The best way to learn is to experiment!
* You can always email me [cj@mlgrto.com](mailto:cj@mlgrto.com?subject=Code Inquiry)
-

---

## Thank you

---












