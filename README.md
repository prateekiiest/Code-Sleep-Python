# Code Sleep Python

-------------------------------------------------

[![codebeat badge](https://codebeat.co/badges/d22e7b1f-d101-47c4-a866-a843459e516c)](https://codebeat.co/projects/github-com-prateekiiest-code-sleep-python-master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8a2a1adf12034f0ab92d99dac6da7ef8)](https://www.codacy.com/app/prateekkol21/Code-Sleep-Python?utm_source=github.com&utm_medium=referral&utm_content=prateekiiest/Code-Sleep-Python&utm_campaign=badger)
[![Build status](https://ci.appveyor.com/api/projects/status/ugq1vwa8045p307g?svg=true)](https://ci.appveyor.com/project/prateekiiest/code-sleep-python)
[![Build Status](https://travis-ci.org/prateekiiest/Code-Sleep-Python.svg?branch=master)](https://travis-ci.org/prateekiiest/Code-Sleep-Python)
[![License MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/LICENSE)
[![chat on Slack](https://img.shields.io/badge/chat%20on%20-Slack-blue.svg)](https://join.slack.com/t/code-sleep-python/shared_invite/enQtMzE0NTIwNzY0MTM1LWFhNGY0NWQ0MDIxNjZmMzgyMzlhOTk3YTY4YjQwNjJmOGIyMTZiNzA4MzkwZWE0ZjgyOWQ2MmMzMWJlMDExMjY)
[![made with &hearts in Python](https://img.shields.io/badge/made%20with%20%E2%9D%A4%20in-Python-red.svg)](http://shields.io/#your-badge)


#### [Join Slack](https://join.slack.com/t/code-sleep-python/shared_invite/enQtMzE0NTIwNzY0MTM1LWFhNGY0NWQ0MDIxNjZmMzgyMzlhOTk3YTY4YjQwNjJmOGIyMTZiNzA4MzkwZWE0ZjgyOWQ2MmMzMWJlMDExMjY)

![](codesleeppython.png)


## About

**If you are into Python and have been writing code in Python for the last few months, you have come to the right place.**

This project is for all the **Python lovers** out there.

#### Description
This repository contains a curated list of some of the awesome small projects made in Python that you can code away this summer.

It includes analysis of different Python modules, a deep analysis of the Python statistics modules and dataframes like Pandas.

It has some projects on classification, correlation and regression which are the fundamental building blocks of Machine Learning and Neural Networks.

The repository is still under development. Only the source code has been uploaded so far. Implementations and results using Jupyter Notebooks will be implemented shortly.

New to Python? Take a look [here](https://github.com/prateekiiest/Code-Sleep-Python#getting-started-with-python).

#### Downloading and Running

A step-by-step guide to download all the codes from here and test yourself in your local machine.

```
  git clone https://github.com/prateekiiest/Code-Sleep-Python.git

  cd Code-Sleep-python
  cd Code-Sleep-Python  # all the codes are present Here

  ipython notebook

```
This will open a new jupyter notebook in your localhost where you can run all the codes and test it for yourself.

----------------------------------------------


#### See Project Ideas [here](https://github.com/prateekiiest/Code-Sleep-Python/wiki/Winter-of-Code-Project)

----------------------------------------------------

## Projects

* [Tic-Tac-Toe](https://github.com/prateekiiest/Code-Sleep-Python#tic-tac-toe)
* [Hangman](https://github.com/prateekiiest/Code-Sleep-Python#hangman)
* [Caesar-Cipher](https://github.com/prateekiiest/Code-Sleep-Python#caesar-cipher)
* [Translations of Hamlet](https://github.com/prateekiiest/Code-Sleep-Python#translations-of-hamlet)
* [Classification](https://github.com/prateekiiest/Code-Sleep-Python#classification)
* [Whisky Classification](https://github.com/prateekiiest/Code-Sleep-Python#whisky-classification)

* [Bird Migration](https://github.com/prateekiiest/Code-Sleep-Python#bird-migration)
* [Social Network Analysis](https://github.com/prateekiiest/Code-Sleep-Python#social-network-analysis)
* [Prime](https://github.com/prateekiiest/Code-Sleep-Python#prime-number-finder)
* [Website status check](https://github.com/prateekiiest/Code-Sleep-Python#website-status-check)
* [Encryption-Techniques](#encryption-techniques)
* [Inception Tic-Tac-Toe](https://github.com/prateekiiest/Code-Sleep-Python#inception-tic-tac-toe)
* [Sprint](https://github.com/prateekiiest/Code-Sleep-Python#sprint)
* [Floating Text](#floating-text)
* [Koch Curve](https://github.com/prateekiiest/Code-Sleep-Python#koch-curve)
* [Superellipse](https://github.com/prateekiiest/Code-Sleep-Python#superellipse)
* [Cricket Notification](https://github.com/prateekiiest/Code-Sleep-Python#cricket-notification)

----------------------------------

### Tic-Tac-Toe

Tic-Tac-Toe (or noughts and crosses) is a simple strategy game in which two players take turns placing a mark on a 3x3 board, attempting to make a row, column, or diagonal of three with their mark. In this homework, we will use the tools we've covered in the past two weeks to create a Tic-Tac-Toe simulator and evaluate basic winning strategies.

![](https://upload.wikimedia.org/wikipedia/commons/8/8e/TicTacToe-6549127nnXOp.gif)

Players soon discover that best play from both parties leads to a draw. Because of the simplicity of Tic-Tac-Toe, it is often used as a pedagogical tool for teaching the concepts of good sportsmanship and the branch of artificial intelligence that deals with the searching of game trees. It is straightforward to write a computer program to play Tic-Tac-Toe perfectly, to enumerate the 765 essentially different positions (the state space complexity), or the 26.830 possible games up to rotations and reflections (the game tree complexity) on this space.

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/tic-tac-toe/code.py)**

-----------------------------------

### Hangman

Hangman is a simple game where a player will guess a word letter by letter.

![](http://daramcq.github.io/img/hangman-game-5.png)

In this project, you will create a program that generates a random word that you must guess.

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Hangman/code.py)**

--------------------------------------------

### Caesar-Cipher

A cipher is a secret code for a language. In this study, we will explore a cipher that is reported by contemporary Greek historians to have been used by Julius Caesar to send secret messages to generals during times of war.

The Caesar cipher, also known as a shift cipher, is one of the simplest forms of encryption. It is a substitution cipher where each letter in the original message (called the plaintext) is replaced with a letter corresponding to a certain number of letters up or down in the alphabet.


In this way, a message that initially was quite readable ends up in a form that can not be understood at a simple glance.

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Caesar-cipher/code.py)**

------------------------------------------------

### Translations of Hamlet

In this case study, we will find and plot the distribution of word frequencies for each translation of Hamlet. Perhaps the distribution of word frequencies of Hamlet depends on the translation.

![](http://www.aboutlanguageschools.com/images/language-translations.jpg)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/translation_hamlet/code.py)**

-----------------------------------------------------

### Classification

In this case study, we will analyze a dataset consisting of an assortment of wines classified into "high quality" and "low quality", and will use k-Nearest Neighbors to predict whether or not other information about the wine helps us correctly guess whether a new wine will be of high quality.

![](http://homepages.inf.ed.ac.uk/rbf/HIPR2/classb.gif)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Classification/code.py)**

----------------------------------------------

### Whisky Classification

In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library designed for simple and interactive plotting. We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.You can go through the article - **[here](http://www.geeksforgeeks.org/project-scikit-learn-whisky-clustering/)**

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/whisky_classification/code.py)**

---------------------------------------------

### Bird Migration

In this case study, we will continue taking a look at patterns of flight for each of the three birds in our dataset.Documentation of this project available - **[here](http://www.geeksforgeeks.org/tracking-bird-migration-using-python-3/)**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/BrantaLeucopsisMigration.jpg/300px-BrantaLeucopsisMigration.jpg)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Bird_migration/code.py)**

-------------------------------------------------

### Social Network Analysis

Homophily is a network characteristic. Homophily occurs when nodes that share an edge share a characteristic more often than nodes that do not share an edge. In this case study, we will investigate homophily of several characteristics of individuals connected in social networks in rural India.

![](https://images.pond5.com/social-media-animation-after-effect-046838541_iconm.jpeg)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/social_network/code.py)**

----------------------------------------------------


### Prime number finder

The implementation of Sieve of Eratosthenes is used to find prime numbers.

![](https://i.pinimg.com/564x/cc/c7/55/ccc7554b4ae9ee9781b752832224f3ef--sieve-of-eratosthenes-prime-factorization.jpg)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Prime/code.py)**

----------------------------------------------------

### Website status check

A simple website crawler to check the return code of a website. It returns with a message indicating whether the website is online, redirected, or not found.

![](http://yootheme.com/media/docs/assets/images/warp/error_pages_404.jpg)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/website_status_check/website_status_check.py)**


----------------------------------------------------

### Encryption-Techniques

Encryption is an interesting piece of technology that works by scrambling data so it is unreadable by unintended parties. The technology comes in many forms, with key size and strength generally being the biggest differences in one variety from the next. This repo has implementations of different encryption techniques. More [here](https://en.wikipedia.org/wiki/Encryption).

![](http://img.bityard.net/blog/aes.png)

**[CODE](Encryption-Techniques/)**

----------------------------------------------------

----------------------------------------------------

### Inception Tic-Tac-Toe

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Inception%20TicTacToe/inceptionTTT.py)**

----------------------------------------------------

### Sprint

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Sprint/sprint.py)**

----------------------------------------------------

### Floating Text

Floating Text is a simple program which displays a given String as a floating string on the terminal.

![demo](/floating_text/floating_text.gif)

**[CODE](/floating_text/floating_text.py)**

----------------------------------------------------

### Koch Curve

A Fractal is geometrical figure, each part of which has the same statistical character as the whole. Koch Curve (also known as the **Koch snowflake**) is a mathematical fractal curve constructed recursively using an equilateral triangle (See figure). The progression for the area of the snowflake converges to 1.6 times the area of the original triangle, while the progression for the snowflake's perimeter diverges to infinity. Consequently, the snowflake has a finite area bounded by an infinitely long line. **[more info](https://en.wikipedia.org/wiki/Koch_snowflake)**

This program traces out a 4 level Koch curve.

![](https://upload.wikimedia.org/wikipedia/commons/f/fd/Von_Koch_curve.gif)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Koch%20Curve/koch%20curve.py)**

----------------------------------------------------

### Superellipse

A superellipse, also known as a Lamé curve after Gabriel Lamé, is a closed curve resembling the ellipse, retaining the geometric features of semi-major axis and semi-minor axis, and symmetry about them, but a different overall shape.

**[more info](https://en.wikipedia.org/wiki/Superellipse)**

![](https://upload.wikimedia.org/wikipedia/en/2/24/Superellipse_anim.gif)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Superellipse/test.py)**

----------------------------------------------------

### Cricket Notification

A simple program to get the score and match status if India is playing. This information is obtained from the terminal.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgwxUvr7AfngMuzr4a8tc69jexGPoPeSdCTiDZhvlXqgZTH_wxgg)

**[CODE](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/Code-Sleep-Python/Cricket_Notification/cricket_notification.py)**

----------------------------------------------------


----------------------------------------------------

## Wanna Contribute ?

![](https://raw.githubusercontent.com/prateekiiest/Code-Sleep-Python/master/contribute.jpg)

Its simple. Just fork/clone the repository and see the **Contributing Guidelines** [here](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/CONTRIBUTING.md)

## Saw a BUG !!

![](https://2shopper.files.wordpress.com/2013/08/ace-ventura-jim-carrey-funny.jpg)

Let me know about that. Feel free to open a new issue about any bug or problem you encounter.




----------------------------------------------------

## New to Python ? Get Started below

### Getting started with Python

New to Python? No problem! Take a look at the following resources:

- [Python beginners guide](https://wiki.python.org/moin/BeginnersGuide)
- [Python course by Google](https://developers.google.com/edu/python/) (online course)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/book/) (book)
- [MIT: Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) (open courseware)
- [Python for Developers](http://ricardoduarte.github.io/python-for-developers/)(book)
- [How to Think Like a Computer Scientist](http://openbookproject.net/thinkcs/python/english3e/)(book)
- [Byte of Python](https://python.swaroopch.com/)(book)
- [Pycharm EDU](https://www.jetbrains.com/pycharm-edu/) - A helpful program that teaches Python. It includes many lessons on basic Python. It also has tests, checks, and hints to help you through each programming activity!


--------------------------------------

## Contributors :octocat:

To see a list of all contributors see [here](https://github.com/prateekiiest/Code-Sleep-Python/blob/master/CONTRIBUTORS.md)

--------------------------
