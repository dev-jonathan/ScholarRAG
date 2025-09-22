---
link: https://cs50.harvard.edu/x/2024/psets/1/me/#hello-its-me
related_files:
  - week-1-notes.md
  - week-1-transcription.md
  - problemset/week-1-cash.md
  - problemset/week-1-credit.md
  - problemset/week-1-mario-less.md
  - problemset/week-1-mario-more.md
  - problemset/week-1-problemset.md
  - problemset/week-1-world.md
title: Hello, It’s Me
type: exercise
week/lecture: "1"
---

# [Hello, It’s Me](https://cs50.harvard.edu/x/2024/psets/1/me/#hello-its-me)

## [Problem to Solve](https://cs50.harvard.edu/x/2024/psets/1/me/#problem-to-solve)

In a file called `hello.c`, in a folder called `me`, implement a program in C that prompts the user for their name and then says hello to that user. For instance, if the user’s name is Adele, your program should print `hello, Adele\n`!

<details>
<summary>Hints</summary>

- Recall that you can get a `string` from a user with `get_string`, which is declared in `cs50.h`.
- Recall that you can print a `string` with `printf`, which is declared in `stdio.h`.
- Recall that you can format a `string` with `printf` with `%s`.
</details>

## [Demo](https://cs50.harvard.edu/x/2024/psets/1/me/#demo)

```
$ make hello
$ ./hello
What's your name? Adele
hello, Adele
$ ./hello
What's your name? David
hello, David
$
```

## [How to Begin](https://cs50.harvard.edu/x/2024/psets/1/me/#how-to-begin)

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir me
```

to make a folder called `me` in your codespace.

Then execute

```
cd me
```

to change directories into that folder. You should now see your terminal prompt as `me/ $`. You can now execute

```
code hello.c
```

to create a file called `hello.c` in which you can write your code.

## [Walkthrough](https://cs50.harvard.edu/x/2024/psets/1/me/#walkthrough)

Here’s a “walkthrough” (i.e., tour) of this problem, if you’d like a verbal overview of what to do too!

<iframe src="https://www.youtube.com/embed/wSk1KSDUEYA?modestbranding=0&rel=0&showinfo=0"></iframe>

## [How to Test](https://cs50.harvard.edu/x/2024/psets/1/me/#how-to-test)

### [Correctness](https://cs50.harvard.edu/x/2024/psets/1/me/#correctness)

In your terminal, execute the below to check your work’s correctness.

```
check50 cs50/problems/2024/x/me
```

### [Style](https://cs50.harvard.edu/x/2024/psets/1/me/#style)

```
style50 hello.c
```

## [How to Submit](https://cs50.harvard.edu/x/2024/psets/1/me/#how-to-submit)

```
submit50 cs50/problems/2024/x/me
```
