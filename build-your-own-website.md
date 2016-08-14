# Build Your Own Website
## Code Workshop

As presented by [@cjmlgrto](http://mlgrto.com)

---

## What's a website made of?

-
* The Markup (HTML)
* The Styles (CSS)
-

---

# Part 1: The Markup

---

## The Markup

A file that tells the web browser what kind of content should be displayed

An analogy: list of ingredients for a recipe

---

## HTML

```html

    <h1>Header, Level 1</h1>
    <h2>Header, Level 2</h1>
    <p>Paragraph with <a href="http://apple.com">a link</a></p>

```

---

# Header, Level 1
## Header, Level 2

Paragraph with [a link](http://apple.com)

---

## Common HTML tags

-
* _h1_ to _h6_ for headers
* _p_ for paragraphs
* _a_ ("anchor") for links
* _b_ for bold text
* _i_ for italic text
-

And much more [...](http://www.incimal.com/DATA/TEXTEDOC/html-cheat-sheet-v1.pdf)

---

# Hands-on!

Visit [Codepen.io](http://codepen.io/pen/)

---

### Adding images:

```html

    <img src="http://bukk.it/success.gif"/>

```

### Creating lists:

```html

    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>

```

---

## A basic HTML document

```html

    <!doctype html>
    <html>
        <head>
            <title>Webpage Title</title>
            <meta charset="utf-8">
        </head>
        <body>
            Content goes here!
        </body>
    </html>

```

---

## Creating a webpage

1: Open TextEdit (or Notepad)
2: If using TextEdit, look for _Format_ > _Make Plain Text_ in the menubar
3: Copy and paste the following:

```html

    <!doctype html>
    <html>
        <head>
            <title>YES!!!!</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>WE DID IT</h1>
            <img src="http://bukk.it/webdesign.jpg"/>
        </body>
    </html>

```

4: Save the file as _index.html_ onto your desktop
5: Look for the file on the desktop, and open it

---

## Recap

-
* HTML is content enclosed within _tags_
* The _tags_ tell the web browser what to display
* Different tags serve different purposes
-

[Here](http://www.w3schools.com/html/html_intro.asp) is a good reference for HTML

---

# Part 2: The Styles

---

## The Styles

Another set of rules that the web browser follows

These rules tell the browser what _each tag should look like_

---

## CSS

```css

    h1 {
        color: red;
        font-family: "Comic Sans";
        font-size: 32px;
    }

    p {
        color: blue;
        font-family: "Arial";
        font-size: 16px;
    }

```

---

<h1 style="color:red; font-family: 'Comic Sans MS';">Stranger Things</h1>
<p style="color: blue; font-family: 'Arial';">Where are you, Will Byers?</p>

---

## Common CSS Rules

-
* _color:_ black_;_
* _font-size:_ 32px_;_
* _font-family:_ "Arial"_;_
* _text-align:_ center_;_
* _margin-bottom:_ 16px_;_
-

More [here](http://www.w3schools.com/cssref/)!

---

# Hands-on!

Re-open [Codepen.io](http://codepen.io/pen/)

---

### Giving certain tags certain styles:

```css

    p {
        color: black;
    }

    .whatever {
        color: red;
    }

```

### In the HTML:

```html

    <p>This is black</p>

    <p>This is also black</p>

    <p class="whatever">But this one is red!</p>

```

Notice how we've added it within the _&lt;_ and the _&gt;_ of the tag!

---

Right now, we're _only_ styling text.

But we can do more!!!

---

## Introducting the div tag in HTML

```html

    <div class="alert_box">
        <p>HEY YOU</p>
    </div>

```

---

## Styling div tags

```css

    .alert_box {
        padding: 10px;
        border: 2px solid green;
        background-color: red;
        color: white;
        width: 100px;
        margin-left: 100px;
    }

```

---

<div style="padding: 1rem; border: 2px solid green; background-color: red; color: white; width: 50%; margin-left: 50%;">
HEY YOU
</div>

---

# Try it yourself!

Re-open [Codepen.io](http://codepen.io/pen/)

---

## CSS as a file

1: Open TextEdit (or Notepad)
2: If using TextEdit, look for _Format_ > _Make Plain Text_ in the menubar
3: Copy and paste the following:

```html

    <!doctype html>
    <html>
        <head>
            <title>YES!!!!</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>WE DID IT</h1>
            <img src="http://bukk.it/webdesign.jpg"/>
        </body>
    </html>

```

4: Save the file as _index.html_ onto your desktop
5: Look for the file on the desktop, and open it

---

Note: this is the same as the first file we did, but we are going to modify it

---

6: Add this line in between within the _head_:

```html

    <link rel="stylesheet" href="style.css"/>

```

---

7: Create a new TextEdit/Notepad file
8: Copy and paste the following:

```css

    body {
        background-color: black;
        color: white;
        font-family: "Arial";
    }

    h1 {
        text-align: center;
        margin-bottom: 32px;
    }

    img {
        border: 6px solid white;
    }

```

---

9: Save it as _style.css_ in the same folder as _index.html_
10: Open _index.html_

---

## Recap

-
* CSS are _rules_ for HTML tags
* _Classes_ are ways to differentiate the style of any tag
* HTML _div_s are boxes can be styled using CSS classes
-

A good site: [css-tricks.com](https://css-tricks.com)

---

# Some Fun Stuff

-
* CodePen's a great place to experiment with HTML and CSS, but if you really want to have fun, use a text editor like [Sublime Text](https://sublimetext.com)
* If you're looking to learn more HTML and CSS, [W3Schools](http://www.w3schools.com) is like the online dictionary for web design stuff.
* The best way to learn is to experiment!
* You can always email me [cj@mlgrto.com](mailto:cj@mlgrto.com?subject=Code Inquiry)
* These slides + some extra resources will be emailed to you later today
-

---

## Thank you

---



