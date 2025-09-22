---
link: https://cs50.harvard.edu/x/2024/psets/1/world/#hello-world
related_files:
  - week-1-notes.md
  - week-1-transcription.md
  - problemset/week-1-cash.md
  - problemset/week-1-credit.md
  - problemset/week-1-mario-less.md
  - problemset/week-1-mario-more.md
  - problemset/week-1-me.md
  - problemset/week-1-problemset.md
title: Hello, World
type: exercise
week/lecture: "1"
---

# [Hello, World](https://cs50.harvard.edu/x/2024/psets/1/world/#hello-world)

<iframe src="https://www.youtube.com/embed/ufB53UE2Cvo?modestbranding=0&rel=0&showinfo=0&end=191&start=103"></iframe>

## [Problem to Solve](https://cs50.harvard.edu/x/2024/psets/1/world/#problem-to-solve)

Thanks to Professor [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) (who taught CS50 when David took it!), “hello, world” has been implemented in hundreds of languages. Let’s add your implementation to the list!

In a file called `hello.c`, in a folder called `world`, implement a program in C that prints `hello, world\n`, and that’s it!

<details>
<summary>Hint</summary>

Here’s the actual code you should write! (Quite the hint, huh?) Best to type it yourself, though, rather than copy/paste, so that you start to develop some “muscle memory” for writing code.

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

</details>

## [Demo](https://cs50.harvard.edu/x/2024/psets/1/world/#demo)

Here’s a demo of what should happen when you compile and execute your program.

```
$ make hello
$ ./hello
hello, world
$
```

## [How to Begin](https://cs50.harvard.edu/x/2024/psets/1/world/#how-to-begin)

Open [VS Code](https://cs50.dev/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

```
$
```

Next execute

```
mkdir world
```

to make a folder called `world` in your codespace.

Then execute

```
cd world
```

to change directories into that folder. You should now see your terminal prompt as `world/ $`. You can now execute

```
code hello.c
```

to create a file called `hello.c` in which you can write your code.

## [How to Test](https://cs50.harvard.edu/x/2024/psets/1/world/#how-to-test)

Recall that you can compile `hello.c` with:

```
make hello
```

If you don’t see an error message, it compiled successfully! You can confirm as much with

```
ls
```

which should list not only `hello.c` (which is source code) but also `hello` (which is machine code).

If you do see an error message, try to fix your code and try to compile it again. If you don’t understand the error message, though, try executing

```
help50 make hello
```

for advice.

Once your code compiles successfully, you can execute your program with:

```
./hello
```

### [Correctness](https://cs50.harvard.edu/x/2024/psets/1/world/#correctness)

Execute the below to evaluate the correctness of your code using `check50`, a command-line program that will output happy faces whenever your code passes CS50’s automated tests and sad faces whenever it doesn’t!

```
check50 cs50/problems/2024/x/world
```

### [Style](https://cs50.harvard.edu/x/2024/psets/1/world/#style)

Execute the below to evaluate the style of your code using `style50`, a command-line program that will output additions (in green) and deletions (in red) that you should make to your program in order to improve its style. If you have trouble seeing those colors, `style50` supports other [modes](https://cs50.readthedocs.io/style50/) too!

```
style50 hello.c
```

## [How to Submit](https://cs50.harvard.edu/x/2024/psets/1/world/#how-to-submit)

No need to submit this one!
