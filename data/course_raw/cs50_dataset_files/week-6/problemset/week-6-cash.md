---
link: https://cs50.harvard.edu/x/2024/psets/6/cash/#cash
related_files:
  - week-6-notes.md
  - week-6-transcription.md
  - problemset/week-6-credit.md
  - problemset/week-6-dna.md
  - problemset/week-6-hello.md
  - problemset/week-6-mario-less.md
  - problemset/week-6-mario-more.md
  - problemset/week-6-problemset.md
  - problemset/week-6-readability.md
title: Cash
type: exercise
week/lecture: "6"
---

# [Cash](https://cs50.harvard.edu/x/2024/psets/6/cash/#cash)

## [Problem to Solve](https://cs50.harvard.edu/x/2024/psets/6/cash/#problem-to-solve)

In a file called `cash.py` in a folder called `sentimental-cash`, write a program that asks the user how much change is owed and then spits out the minimum number of coins with which said change can be made. You can do this exactly as you did in [Problem Set 1](../../1/), except that your program this time should be written in Python, and you should assume that the user will input their change in dollars (e.g., 0.50 dollars instead of 50 cents).

## [Demo](https://cs50.harvard.edu/x/2024/psets/6/cash/#demo)

```
$ python cash.py
Change: 0.41
4
$ python cash.py
Change: 0.01
1
$ python cash.py
Change: 0.15
2
$ python cash.py
Change: 1.60
7
$
```

## [Specification](https://cs50.harvard.edu/x/2024/psets/6/cash/#specification)

- Use `get_float` from the CS50 Library to get the user’s input and `print` to output your answer. Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
  - We ask that you use `get_float` so that you can handle dollars and cents, albeit sans dollar sign. In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ but the customer pays with a $10 bill), assume that your program’s input will be `9.75` and not `$9.75` or `975`. However, if some customer is owed $9 exactly, assume that your program’s input will be `9.00` or just `9` but, again, not `$9` or `900`. Of course, by nature of floating-point values, your program will likely work with inputs like `9.0` and `9.000` as well; you need not worry about checking whether the user’s input is “formatted” like money should be.
- If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.
- Incidentally, so that we can automate some tests of your code, we ask that your program’s last line of output be only the minimum number of coins possible: an integer followed by a newline.

## [How to Test](https://cs50.harvard.edu/x/2024/psets/6/cash/#how-to-test)

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

- Run your program as `python cash.py`, and wait for a prompt for input. Type in `0.41` and press enter. Your program should output `4`.
- Run your program as `python cash.py`, and wait for a prompt for input. Type in `0.01` and press enter. Your program should output `1`.
- Run your program as `python cash.py`, and wait for a prompt for input. Type in `0.15` and press enter. Your program should output `2`.
- Run your program as `python cash.py`, and wait for a prompt for input. Type in `1.60` and press enter. Your program should output `7`.
- Run your program as `python cash.py`, and wait for a prompt for input. Type in `23` and press enter. Your program should output `92`.
- Run your program as `python cash.py`, and wait for a prompt for input. Type in `4.2` and press enter. Your program should output `18`.
- Run your program as `python cash.py`, and wait for a prompt for input. Type in `-1` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
- Run your program as `python cash.py`, and wait for a prompt for input. Type in `foo` and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.
- Run your program as `python cash.py`, and wait for a prompt for input. Do not type anything, and press enter. Your program should reject this input as invalid, as by re-prompting the user to type in another number.

### [Correctness](https://cs50.harvard.edu/x/2024/psets/6/cash/#correctness)

```
check50 cs50/problems/2024/x/sentimental/cash
```

### [Style](https://cs50.harvard.edu/x/2024/psets/6/cash/#style)

```
style50 cash.py
```

## [How to Submit](https://cs50.harvard.edu/x/2024/psets/6/cash/#how-to-submit)

```
submit50 cs50/problems/2024/x/sentimental/cash
```
