---
link: https://cs50.harvard.edu/x/2024/psets/1/mario/more/#mario
related_files:
  - week-1-notes.md
  - week-1-transcription.md
  - problemset/week-1-cash.md
  - problemset/week-1-credit.md
  - problemset/week-1-mario-less.md
  - problemset/week-1-me.md
  - problemset/week-1-problemset.md
  - problemset/week-1-world.md
title: Mario More
type: exercise
week/lecture: "1"
---

# [Mario More](https://cs50.harvard.edu/x/2024/psets/1/mario/more/#mario)

<iframe src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&rel=0&showinfo=0&start=11"></iframe>

## [Problem to Solve](https://cs50.harvard.edu/x/2024/psets/1/mario/more/#problem-to-solve)

Toward the beginning of World 1-1 in Nintendo’s Super Mario Brothers, Mario must hop over adjacent pyramids of blocks, per the below.

![screenshot of Mario jumping over adjacent pyramids](https://cs50.harvard.edu/x/2024/psets/1/mario/more/pyramids.png)

In a file called `mario.c` in a folder called `mario-more`, implement a program in C that recreates that pyramid, using hashes (`#`) for bricks, as in the below:

```
   #  #
  ##  ##
 ###  ###
####  ####
```

And let’s allow the user to decide just how tall the pyramids should be by first prompting them for a positive `int` between, say, 1 and 8, inclusive.

<details>
<summary>Examples</summary>

Here’s how the program might work if the user inputs `8` when prompted:

```
$ ./mario
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

Here’s how the program might work if the user inputs `4` when prompted:

```
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Here’s how the program might work if the user inputs `2` when prompted:

```
$ ./mario
Height: 2
 #  #
##  ##
```

And here’s how the program might work if the user inputs `1` when prompted:

```
$ ./mario
Height: 1
#  #
```

If the user doesn’t, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

</details>

Notice that width of the “gap” between adjacent pyramids is equal to the width of two hashes, irrespective of the pyramids’ heights.

### [Walkthrough](https://cs50.harvard.edu/x/2024/psets/1/mario/more/#walkthrough)

<iframe src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&rel=0&showinfo=0"></iframe>

### [How to Test Your Code](https://cs50.harvard.edu/x/2024/psets/1/mario/more/#how-to-test-your-code)

Does your code work as prescribed when you input

- `-1` (or other negative numbers)?
- `0`?
- `1` through `8`?
- `9` or other positive numbers?
- letters or words?
- no input at all, when you only hit Enter?

You can also execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

### [Correctness](https://cs50.harvard.edu/x/2024/psets/1/mario/more/#correctness)

In your terminal, execute the below to check your work’s correctness.

```
check50 cs50/problems/2024/x/mario/more
```

### [Style](https://cs50.harvard.edu/x/2024/psets/1/mario/more/#style)

Execute the below to evaluate the style of your code using `style50`.

```
style50 mario.c
```

## [How to Submit](https://cs50.harvard.edu/x/2024/psets/1/mario/more/#how-to-submit)

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2024/x/mario/more
```
