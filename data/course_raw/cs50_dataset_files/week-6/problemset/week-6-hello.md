---
link: https://cs50.harvard.edu/x/2024/psets/6/hello/#hello-again
related_files:
  - week-6-notes.md
  - week-6-transcription.md
  - problemset/week-6-cash.md
  - problemset/week-6-credit.md
  - problemset/week-6-dna.md
  - problemset/week-6-mario-less.md
  - problemset/week-6-mario-more.md
  - problemset/week-6-problemset.md
  - problemset/week-6-readability.md
title: Hello, Again
type: exercise
week/lecture: "6"
---

# [Hello, Again](https://cs50.harvard.edu/x/2024/psets/6/hello/#hello-again)

## [Problem to Solve](https://cs50.harvard.edu/x/2024/psets/6/hello/#problem-to-solve)

In a file called `hello.py` in a folder called `sentimental-hello`, implement a program that prompts a user for their name, and then prints `hello, so-and-so`, where `so-and-so` is their provided name, exactly as you did in [Problem Set 1](../../1/). Except that your program this time should be written in Python!

<details>
<summary>Hints</summary>

- Recall that you can get a `str` from a user with `get_string`, which is declared in the `cs50` library.
- Recall that you can print a `str` with `print`.
- Recall that you can create formatted strings in Python by prepending `f` to a string itself. For example, `f"{name}"` will substitute (“interpolate”) the value of the variable `name` where you’ve written `{name}`.
</details>

## [Demo](https://cs50.harvard.edu/x/2024/psets/6/hello/#demo)

```
$ python hello.py
What is your name? David
hello, David
$ python hello.py
What is your name? Inno
hello, Inno
$ python hello.py
What is your name? Kamryn
hello, Kamryn
$
```

## [How to Test](https://cs50.harvard.edu/x/2024/psets/6/hello/#how-to-test)

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

- Run your program as `python hello.py`, and wait for a prompt for input. Type in `David` and press enter. Your program should output `hello, David`.
- Run your program as `python hello.py`, and wait for a prompt for input. Type in `Inno` and press enter. Your program should output `hello, Inno`.
- Run your program as `python hello.py`, and wait for a prompt for input. Type in `Kamryn` and press enter. Your program should output `hello, Kamryn`.

### [Correctness](https://cs50.harvard.edu/x/2024/psets/6/hello/#correctness)

```
check50 cs50/problems/2024/x/sentimental/hello
```

### [Style](https://cs50.harvard.edu/x/2024/psets/6/hello/#style)

```
style50 hello.py
```

## [How to Submit](https://cs50.harvard.edu/x/2024/psets/6/hello/#how-to-submit)

```
submit50 cs50/problems/2024/x/sentimental/hello
```
