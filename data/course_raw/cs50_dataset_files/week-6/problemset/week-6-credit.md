---
link: https://cs50.harvard.edu/x/2024/psets/6/credit/#credit
related_files:
  - week-6-notes.md
  - week-6-transcription.md
  - problemset/week-6-cash.md
  - problemset/week-6-dna.md
  - problemset/week-6-hello.md
  - problemset/week-6-mario-less.md
  - problemset/week-6-mario-more.md
  - problemset/week-6-problemset.md
  - problemset/week-6-readability.md
title: Credit
type: exercise
week/lecture: "6"
---

# [Credit](https://cs50.harvard.edu/x/2024/psets/6/credit/#credit)

## [Problem to Solve](https://cs50.harvard.edu/x/2024/psets/6/credit/#problem-to-solve)

In a filed called `credit.py` in a folder called `sentimental-credit`, write a program that prompts the user for a credit card number and then reports (via `print`) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in [Problem Set 1](../../1/). Your program this time should be written in Python!

## [Demo](https://cs50.harvard.edu/x/2024/psets/6/credit/#demo)

```
$ python credit.py
Number: 378282246310005
AMEX
$ python credit.py
Number: 5555555555554444
MASTERCARD
$ python credit.py
Number: 1234567890
INVALID
$
```

## [Specification](https://cs50.harvard.edu/x/2024/psets/6/credit/#specification)

- So that we can automate some tests of your code, we ask that your program’s last line of output be `AMEX\n` or `MASTERCARD\n` or `VISA\n` or `INVALID\n`, nothing more, nothing less.
- For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
- Best to use `get_int` or `get_string` from CS50’s library to get users’ input, depending on how you to decide to implement this one.

## [Hints](https://cs50.harvard.edu/x/2024/psets/6/credit/#hints)

- It’s possible to use regular expressions to validate user input. You might use Python’s [`re`](https://docs.python.org/3/library/re.html) module, for example, to check whether the user’s input is indeed a sequence of digits of the correct length.

## [How to Test](https://cs50.harvard.edu/x/2024/psets/6/credit/#how-to-test)

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

- Run your program as `python credit.py`, and wait for a prompt for input. Type in `378282246310005` and press enter. Your program should output `AMEX`.
- Run your program as `python credit.py`, and wait for a prompt for input. Type in `371449635398431` and press enter. Your program should output `AMEX`.
- Run your program as `python credit.py`, and wait for a prompt for input. Type in `5555555555554444` and press enter. Your program should output `MASTERCARD`.
- Run your program as `python credit.py`, and wait for a prompt for input. Type in `5105105105105100` and press enter. Your program should output `MASTERCARD`.
- Run your program as `python credit.py`, and wait for a prompt for input. Type in `4111111111111111` and press enter. Your program should output `VISA`.
- Run your program as `python credit.py`, and wait for a prompt for input. Type in `4012888888881881` and press enter. Your program should output `VISA`.
- Run your program as `python credit.py`, and wait for a prompt for input. Type in `1234567890` and press enter. Your program should output `INVALID`.

### [Correctness](https://cs50.harvard.edu/x/2024/psets/6/credit/#correctness)

```
check50 cs50/problems/2024/x/sentimental/credit
```

### [Style](https://cs50.harvard.edu/x/2024/psets/6/credit/#style)

```
style50 credit.py
```

## [How to Submit](https://cs50.harvard.edu/x/2024/psets/6/credit/#how-to-submit)

```
submit50 cs50/problems/2024/x/sentimental/credit
```
