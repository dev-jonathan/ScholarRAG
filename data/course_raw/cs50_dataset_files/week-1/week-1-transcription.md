---
link: https://youtu.be/cwtpLIWylAw
related_files:
  - week-1-notes.md
  - problemset/week-1-cash.md
  - problemset/week-1-credit.md
  - problemset/week-1-mario-less.md
  - problemset/week-1-mario-more.md
  - problemset/week-1-me.md
  - problemset/week-1-problemset.md
  - problemset/week-1-world.md
title: "Lecture 1: Week 1 - C"
type: transcription
week/lecture: "1"
---

# [Lecture 1: Week 1 - C](https://youtu.be/cwtpLIWylAw)

TABLE OF CONTENTS:

0:00 - Introduction
1:01 - Machine Code
5:58 - Visual Studio Code for CS50
9:18 - Hello, World
18:41 - From Scratch to C
20:33 - CS50 Library
31:15 - Format Codes
35:48 - Hello, World
36:13 - Hello, You
40:25 - Types
41:26 - Conditionals
47:58 - Variables
50:54 - compare.c
1:01:21 - agree.c
1:09:41 - Loops
1:15:40 - meow.c
1:24:50 - Functions
1:33:33 - calculator.c
1:36:08 - Scope
1:41:45 - Function Composition
1:44:15 - Linux
1:52:39 - Mario
2:08:37 - Integer Overflow
2:13:22 - Truncation
2:16:53 - Type Casting
2:18:14 - Floating-Point Imprecision
2:20:59 - Y2K
2:23:38 - Video Games
2:25:30 - Boeing

## [Introduction](https://youtu.be/cwtpLIWylAw?t=0)

0:00
[INTRIGUING MUSIC]

## [Machine Code](https://youtu.be/cwtpLIWylAw?t=61)

1:01
DAVID MALAN: All right, so this is CS50. And this is week 1, zero index, so to speak.
1:09
And it's not every day that you can say that you've learned a new language, but today is that day. Today, we explore a more traditional and older language called C.
1:18
And rest assured that even if what you're about to see-- no pun intended-- looks very cryptic, very unusual, particularly if you're
1:25
among those less comfortable, cling to the ideas from last week, week zero, wherein we talked about some of those fundamentals of functions
1:32
and loops and conditionals, all of which are coming back today. Indeed, whereas last week, and with problem set 0,
1:37
we focused on learning how to program with Scratch, which, again, you might have played with as a younger student days back.
1:44
Today, we focus on C instead. But along the way, we're going to focus, as always, frankly,
1:50
on learning how to solve problems. But among the goals for today and really on an entire class like this is just to give you week after week all the more tools for your toolkit,
1:58
so to speak, via which to do exactly that. So for instance today, we'll learn how to solve problems all the more
2:03
so with functions, as per last week. We'll do the same with variables. We'll do the same with conditionals, with loops, and with more.
2:10
But we'll also learn at the end of today's class really how not to solve problems. It turns out as powerful as Macs, PCs, cell phones are nowadays,
2:18
there's actually certain things that they can't do very well and information they can't represent very well.
2:24
And that actually leads to a lot of real-world problems, both past and surely future.
2:29
So more on what we're not going to be able to do with programming before long. But beyond that, let's come back to this picture here.
2:36
So this was the very first program that I wrote, that you wrote presumably in some form. And all it does is say "Hello, world."
2:43
But as promised, today, this puzzle piece, or these puzzle pieces together, are going to very quickly start to look more like this.
2:50
And I've deliberately color coded it in a way so that the text on the screen now kind of resembles the puzzle piece.
2:55
So if I go back, notice that we had this, when green flag clicked puzzle piece, mostly in yellow with the green flag, that sort of kicks off
3:02
the whole process once you actually click the button at top right of Scratch's user interface. And then there's the purple block which actually is the verb, the action,
3:11
the function that does something. So if I bring us back over to what we're about to see today, there's going to be some boilerplate, so to speak, some orange text here
3:20
on the screen that for now you just type and take for granted, like you need to write your code like that. But more interesting is going to be the purple.
3:27
And we're going to see today that the function previously called "say" in Scratch is now called "printf" in this language called C.
3:34
But in white here, you'll see similar text to our white oval last week, whereby that's where user input, like your input
3:40
as the programmer, can actually go. So there's a lot of distraction. And honestly, it's these kinds of things that tend to distract and get frustrating early on when
3:47
learning to code for the first time. But the ideas, most importantly, are going to be the same. So how are we going to go about using this.
3:54
Well, it turns out, like last week, you're going to start writing something called source code. So code as we know it, quote, unquote, is more technically called
4:01
"source code." That's what you and I as humans actually write. And indeed it might look a little something like we just saw.
4:07
But unfortunately, computers only speak this, binary-- zeros and ones-- more properly known as machine code, in other words,
4:15
those same patterns of zeros and ones last week, someone guessed, print out "hello, world" on the screen because one of those patterns
4:23
is an H. Another pattern is an E, an L, and L, and an O, and so forth. And then other patterns of those zeros and ones are commands or instructions
4:31
to the computer that literally say, show H-E-L-L-O comma "world" on the screen.
4:37
But machine code would not be nearly as much fun to write if it were indeed in zeros and ones.
4:43
Entirely for us, ideally, you and I are going to write source code, which conceptually is sort of up here, high level.
4:49
But we're going to need a program to convert it to the lower-level machine code so that we don't spend our lives actually having to read and write
4:56
zeros and ones, which back in the day, kind of in yesteryear, you kind of did with things called punch cards and holes on physical sheets of paper.
5:03
We're beyond that because after years and years of innovation, folks have given us higher-level languages instead.
5:09
So here's what we're going to need to do today. If at the end of the day you and I are writing source code
5:14
but we want machine code as output, we need something in the middle that's going to convert that source code to machine code.
5:21
You and I are not going to have to learn or talk about really any more zeros and ones. And the type of program we're going to start using today and introduce you to
5:28
is called a compiler. So a compiler is a program that translates one language to another.
5:34
And it can be any two languages. But today, and often, we'll talk about it in the context of source code
5:39
to machine code. So this is Apple or Google or Microsoft or folks from other companies
5:45
or even volunteers who have written software that do this conversion. You and I are essentially going to download a free compiler
5:51
and use it to actually get our computer to understand the source code that you and I write in these higher-level languages.

## [Visual Studio Code for CS50](https://youtu.be/cwtpLIWylAw?t=358)

5:58
So where are we going to do that? Well, we could actually give you instructions and you could download the appropriate free open-source software
6:05
onto your own Mac or PC. The reality is that creates so many technical support headaches because we all have slightly different computers.
6:11
We all have slightly different versions of Windows or macOS or Linux or other operating systems. And that, too, tends to be a distraction at the beginning of any course
6:19
like this or learning programming. So we're going to use the cloud instead. We're going to use a URL of the form https://cs50.dev.
6:28
And what this will do for you is put inside of your browser window absolutely everything you need for the course, but it's going to use software,
6:36
software called Visual Studio code, otherwise known as VS Code, that's actually free itself.
6:41
It's very popular in industry. It's what "real" programmers use every day. But it's a cloud-based version thereof.
6:47
And so everything will just work for you out of the box. But toward the end of CS50, the goal is going to be to get you off of CS50's infrastructure,
6:55
to get you to download this freely available software onto your own Mac or PC if you so choose so that those training wheels, so to speak,
7:02
can come off. And then even if you never take another class again, you don't need any class's infrastructure moving forward.
7:07
You'll have everything you want and need on your own Mac or PC. But for now, it'll save us a bit of time.
7:13
So in just a bit, I'm going to go to that URL myself on my computer. And I and you will see a user interface that
7:19
looks a little something like this. The colors might be different based on your settings. Fonts might be different, and so forth.
7:24
But in general, it consists of a few different regions. So over here at the top is where we are going to start writing code today.
7:31
So it's a tabbed interface like any number of programs nowadays. And this is that same C code we saw a moment ago.
7:38
So this is where, in a moment, I'm going to start to type it. Over here at the bottom is what we're going to call
7:43
a terminal window, or a console. And the terminal window is where we're going to type commands for compiling our code, for running our code.
7:50
And we'll see today a contrast between a graphical-user interface, or GUI, which has menus and icons and things
7:57
you click and are very familiar with, versus a command-line interface, or CLI. And so we're using both of these together.
8:04
And command-line interface just means, down here, you only use your keyboard. You can click, click, click if you want with your mouse.
8:10
It's not going to generally do much because a command-line interface takes commands at the keyboard. So in a weird sense, it's going to feel like taking
8:16
a step backwards from the Macs, the PCs, the iPhones, and Android phones we all have, which are very graphical.
8:22
But it turns out, once you become a "computer" person or a programmer, you can be a lot more productive, a lot more efficient, I dare say,
8:29
by learning to harness the command-line interface and using both types of interfaces for what each is good at.
8:35
So more on that in just a bit. Over here at left, you're going to see soon a folder interface like Mac OS
8:41
or Windows where any of the files or folders we create in CS50 are going to end up, as well.
8:46
So it gives you the best of both worlds. You can point and click on the left, or you can type commands at the bottom, as we'll soon see.
8:52
And then along here is the so-called activity bar, where there's just VS Code-specific features but also CS50-specific
8:58
features. And if you're in your own version of CS50.dev, you click through in the dot dot dot menu
9:03
or zoom out so you can see everything. You'll see CS50's own rubber duck, virtually speaking, that will be there throughout the course to answer
9:10
any and all of your questions, as well. So more on that soon, too. So here's the code that I propose that we write first,

## [Hello, World](https://youtu.be/cwtpLIWylAw?t=558)

9:18
just like we wrote our very first Scratch program to say "hello, world." So let's go ahead and do exactly this.
9:23
I'm going to switch over to this screen here, where I've already logged into CS50.dev on my computer.
9:29
And just to keep the focus on the code, I've hidden the activity bar. I've hidden the File Explorer, so to speak.
9:36
So you're seeing here the area where all of my tabs are about to go and the terminal window, where all of my commands are going to go.
9:42
But I've just simplified the UI to keep our focus on the interesting parts for now. So how do I go about actually writing and compiling and running some code?
9:53
Well, the teaser is going to be these three steps. One of these is a command called, aptly, Code.
9:58
And Code is just going to let me to open or create a new file, like a file called "hello.c."
10:03
Make is going to be, for now, my compiler that allows me to make the program, that is convert source code into machine
10:11
code, so from C to zeros and ones. And then weirdly, but we'll soon see why, ./hello is going to be the command to run my actual code,
10:19
so the textual equivalent of like double-clicking on a Mac or a PC icon or tapping an icon on your phone.
10:25
So that's it. These three commands are going to allow me to write, to compile, and to run code ultimately.
10:32
So let's go ahead and do that. I'm back in my VS Code interface. I'm going to go ahead and run "code hello.c."
10:39
And notice a couple of details here. So one, there's this weird dollar sign, which has nothing to do with currency,
10:44
but it's just a common convention in the programming world to represent your prompt.
10:50
So if a TF, if I ever say, go to your prompt, we really mean, go to your terminal window. Go to the dollar sign.
10:56
And the dollar sign is where you type the command. Sometimes it's a different symbol, but a dollar sign is conventional.
11:01
Now that I've typed "code" space "hello.c," I'm going to go ahead and hit Enter. And maybe not surprisingly, this gives me
11:07
a brand new tab, a new file if you will, called "hello.c." And just like Word documents have their own file extension, like DOC, DOCX,
11:15
and Excel files have .XLSX and PDFs have .PDF and GIFs have .GIF and so forth,
11:22
so do C files have a file extension by convention that is .C. Now, a couple of minor points.
11:28
Notice that, by convention, I'm almost always going to name my files in lowercase. By convention, I'm never going to use spaces in my file names.
11:36
And my file extension, too, is going to be lowercase. Long story short, accidentally hitting the spacebar
11:41
or using file names with spaces just tends to make life harder when you're in a command-line environment.
11:47
So just beware silly, stupid things like that. So all lowercase, no spaces for now. So my cursor is literally blinking because the program
11:54
wants me to write some code. I'm going to do this from memory. It'll take you presumably some time to acquire the same instincts.
12:00
But I'm going to go ahead and type this first line here, pronounced "include standard io.h"--
12:06
more on that soon-- int main(void), with some parentheses thrown in. Notice what's about to happen here is a little interesting.
12:13
In the code I want to type, I want what we'll call curly braces, the sort of squiggles that you don't use often in English, at least, but are there
12:20
on your keyboard somewhere. But notice what VS Code does, and a lot of programming environments, is it finishes part of my thought.
12:27
So I'm only going to type a left curly brace, but notice I actually get two of them.
12:32
And if I hit Enter, notice that not only does it scooch one down a bit, it also indents my cursor because, just like with pseudocode last week,
12:40
whenever you're doing something logically that should only happen if the thing above it happens, similarly
12:45
is indentation going to be a thing when we actually write code. So VS Code and programs like it just try to save us
12:51
keystrokes so I don't have to waste time hitting the spacebar or hitting Tab or wasting my human time like that.
12:57
All right, so with that said, I'm going to go ahead and type the last of these lines, "printf," where the F is going to mean "formatted," and then a parentheses.
13:05
And notice it gave me two. It gave me the second one for free. Sometimes it will get confused. And you can certainly override this, delete it, and start over.
13:13
And now, unlike Scratch, in C, It turns out I'm going to need to use double quotes anytime
13:18
I'm using an English word or phrase or any human language for that matter. "Hello" comma "world."
13:25
And then at the very end of my line, much like English uses periods, I'm going to use a semicolon in C.
13:32
So that's a lot of talking, but it's not much coding. It's technically six lines of code.
13:37
But honestly, the only interesting one intellectually, as we'll soon see, is really line 5. Like, that is the equivalent of that, say, block.
13:44
Now here's where I'll cross my fingers, hoping that I didn't make any typographical errors. It's going to automatically save for me.
13:50
And I'm going to go back to my terminal window where now I'm going to do that second command, "make" space "hello."
13:56
Common mistake-- you do not say "make hello.c," because you already made that file. You say "make hello," which is the name of the program that in this case I do
14:04
want to create. And Make is smart. It's going to look in my folder. And if it sees a file called "hello.c," it's
14:12
going to convert that source code to machine code and save the results in a simpler shorter-named file just called
14:18
"hello," like an icon on your desktop. Now, hopefully nothing will happen. And that is a good thing, quite paradoxically.
14:25
If you do anything wrong when programming, odds are you're going to see one or many more lines of error sort of yelling
14:31
at you that you made a mistake. Seeing nothing happen is actually a good sign. So the last command, to run my code, recall our three steps here.
14:40
We've written code to create the file, Make to compile the file from source
14:46
code to machine code. So lastly is "./hello." So this now is the equivalent of my double-clicking on a Mac or PC
14:53
or single tapping on a phone. Enter. [SIGHS] So close!
14:58
All right, it's pretty good. I got the H-E-L-L-O comma space "world." But there's something a little stupid about my output.
15:05
What might rub some of you aesthetically the wrong way? Yeah? STUDENT: The dollar sign.
15:11
DAVID MALAN: Yeah, so the dollar sign looks like I was like, "hello, world" dollar sign in my output. But no, that's just kind of a remnant of my prompt starting with a dollar sign.
15:21
And this is a little nitpicky, but this just doesn't feel right, doesn't look right. It's not quite correct. So how can I go about fixing this?
15:27
Well, here's where, at least initially, it's going to take some introduction to just new syntax in C to fix this.
15:33
The simplest instinct might be to do this. Well, let me just hit Enter like that. But this should soon, if not already, rub you
15:40
the wrong way because in general, we're going to see that programming in C and in Python and other languages tends to be line-based.
15:46
Like, you should really start and finish your thought on one line. So if you're in the habit of hitting Enter like this
15:51
and finishing your thought on the next line, generally programming languages don't like that.
15:57
So this is, in fact, not going to do what we expect. And just to show you as much, I'm going to do this.
16:02
Let me go back to my terminal window here. I'm going to rerun "make hello" after making that change.
16:07
Enter. And there we have it, like the first of our erroneous outputs. And it's yelling at me.
16:12
It's missing a terminating character. And there's some red in here, some green, drawing my attention to it.
16:17
Sometimes these error messages will be straightforward. Sometimes you're going to rack your brain a bit to figure them out.
16:23
But for now I've kind of spoiled it. Obviously Enter is not the right solution. So let me clear my terminal window just to hide that error.
16:30
Let me delete this. And let me propose now that I add this incantation here.
16:36
So backslash n, it turns out, is going to be the sort of magical way of ensuring that you actually get
16:43
a new line at the end of your output. So let me go ahead now and rerun "make hello," because I've changed my code.
16:49
I need to now reconvert, recompile the source code to new machine.
16:55
"./hello." And now, there is the canonical "hello, world" program
17:00
that I hoped to write in the first place. So for now, don't worry about the include.
17:05
Don't worry about the standard io. Don't worry about int or main or void or the curly braces. Focus primarily on line 5 here.
17:12
And over the course of today and next week, we'll start to tease apart the other characters that, for now, you should take at face value.
17:18
Questions, though, on any of the steps we've just done? Yeah? STUDENT: Why is the backslash n inside the apostrophes?
17:27
DAVID MALAN: Sure, why is the backslash n inside of the quotation marks, if you will? So short answer is that's just where it needs
17:35
to be because inside of the quotes is the input that you want printf
17:40
to output to the screen. So if you want printf, this function, to output a new line,
17:46
it must be included in the quoted text that you give it. STUDENT: So the backslash n [INAUDIBLE].
17:53
DAVID MALAN: Exactly. Backslash n is a special pattern that "printf no" means, OK, I should
17:58
move the cursor to the next line. Good question. Other questions on any of these steps?
18:04
Yeah? STUDENT: [INAUDIBLE] DAVID MALAN: A good question. So what if you actually want to print backslash n?
18:10
Things get a little tricky there. Let me go ahead and propose that we do this.
18:15
So it turns out-- and this is often the case in programming-- when you want a literal character to appear, you actually put another backslash in front of it.
18:23
But this is not going to be something we do often. But there is in fact a solution to that. But let me propose that beyond that now we compare it
18:30
against what we've actually done. So here is the first Scratch program we wrote with the green flag there.
18:35
Here, recall, is the mental model that I proposed we have for almost everything we do whereby functions are just

## [From Scratch to C](https://youtu.be/cwtpLIWylAw?t=1121)

18:41
an implementation, say, in code of algorithms, step-by-step instructions for solving problems.
18:47
The inputs to functions, recall from last week, are called arguments, or in some contexts parameters.
18:52
And sometimes functions can have side effects. Like last time with Scratch, there was the speech bubble
18:58
that magically appeared next to the cat's mouth as a sort of side effect of using the Say block. So just like this then, we had the white oval as input.
19:07
The Say block was the function last week. And then we had this here, side effect. Well, how do we compare these things left to right?
19:14
Well, here's the Say block at left. Let's compare now to the C code at right. Notice a couple of things to adapt from Scratch to C. Print
19:22
is almost the name of the function. It is technically "printf," for reasons we'll eventually see. Notice the parentheses in C are kind of evocative of the oval in Scratch.
19:32
And that's probably why MIT chose an oval, because a lot of languages use parentheses in this way.
19:37
You still write "hello, world" just as we did last week in Scratch. But per our demo thus far, you do need the double quotes--
19:45
and double quotes, not single quotes-- double quotes on the left and right. And in order to get that new line, you need the backslash n.
19:52
And one more thing is missing. Yeah? STUDENT: Semicolon. DAVID MALAN: The semicolon to finish your thought.
19:57
So all of these sort of stupid things now that honestly you will forget initially if you've never programmed before,
20:03
but you'll soon-- within days, within weeks-- develop the muscle memory where all of that stuff just jumps off, jumps off the page right at you.
20:10
All right, so this backslash n is generally known, just so you know, as an escape sequence.
20:16
And so backslash n allows us to specify a character that might otherwise be hard to type. But let's tease apart some of the other things atop that function already.
20:26
So include stdio.h. It turns out that in C, a lot of the functionality that

## [CS50 Library](https://youtu.be/cwtpLIWylAw?t=1233)

20:33
comes with the language is tucked away in separate files. So if you want to use certain functions, you have to tell the compiler,
20:40
hey, I want to do some standard input and output. Like, I want to print some things on the screen.
20:45
And that's because, for now, you can think of printf as living in this file, stdio.h.
20:52
That's a bit of a white lie for now. But in stdio.h is essentially a declaration for printf
20:57
that will teach the compiler how to print things to the screen. So "hash include" here simply tells the compiler
21:05
before it does anything else essentially go ahead and find on the local hard drive a file called stdio.h
21:10
and copy/paste it there so I know now about printf. So this thing, this .h file, is what we'll technically call a header file.
21:19
And if you've ever heard this word, especially if you have programmed before, it represents essentially what
21:24
we'll start calling a library. So a library in the world of programming is just code that someone else wrote that you can use.
21:31
It's usually free and open source, which means you can literally see the code that someone else wrote, or sometimes you pay for it.
21:37
Sometimes it's closed source, which maybe Microsoft wrote it. They won't show you the code, but they will let you use the zeros and ones.
21:43
So libraries are super useful because honestly even I don't really know how printf works.
21:49
I've taken for granted for 25 years that if I use printf, stuff prints on the screen. But someone smarter than me had to actually write
21:56
the code in C that figures out how to get the H, the E, the L-L-O, and so forth onto the Mac screen, the PC screen, the phone screen, or somewhere
22:05
else. So libraries allow us to stand on each other's shoulders and so that someone else can do the hard work,
22:10
and we can now solve problems that are more interesting to us, not the basic commodity stuff that everyone might want in their code.
22:18
So again, library is code that someone else wrote. A header file in C is just a file ending in ".h"
22:23
that gives you access to the same. And so for instance, if you to learn more about these, there are, what are called in the world of programming, manual pages.
22:31
And these are textual files, like a documentation of sorts,
22:37
via which you can just learn how a function works or how you can use its inputs or arguments.
22:42
The reality is they're written for folks who aren't in CS50. They're written for folks who aren't just learning how to program.
22:48
They're written for and by folks who have been programming for years. And so frankly, they're a little hard to understand.
22:53
And so CS50 has its own version thereof at this URL, manual.cs50.io,
22:58
where you'll see not only the official documentation for C, the language, but also staff-written simplifications in layperson's terms
23:07
what all of the various popular functions are, what their inputs, and what their outputs are. So for instance, under stdio.h, you can actually go to that website.
23:17
You can go to a URL like this, where stdio.h is in there. And you can actually see the documentation therefore.
23:24
So let me go ahead and do this. I'm going to go ahead in my browser here, I'm going to go to manual.cs50.io.
23:31
And let me go ahead here and select those functions that are frequently used in CS50. And under stdio.h, you'll see a bunch of functions,
23:39
only one of which we've even discussed called printf. I'm going to click on printf there. And you'll see an interface that at first glance
23:46
might be a little overwhelming, but it's going to start to look more and more familiar. So first of all, you'll see that if you want to use printf under Synopsis,
23:54
you need to include this header file. Like, you literally copy and paste that line into your own code.
23:59
You'll also see this, which for now is a bit arcane, but this is kind of a hint as to what the function is going to look like.
24:07
But more on that soon. But more importantly, you can read a description about it. And because these descriptions, when you're in less comfortable mode,
24:14
are written by me and the course's teaching fellows, teaching assistants, and course assistants, you'll find them to be much more in layperson's terms.
24:20
And so long story short, rely on this site once you want to learn how to use some function and also what other functions exist.
24:27
In fact, if I go back to the main page here, you'll see that there are all of these functions like are frequently
24:33
used in CS50. And there's hundreds more that come with C. But learning a programming language is not about learning all of those
24:40
but rather just getting a sense of where you find answers to questions when you do want to try something new.
24:47
But what is important to know for CS50 today is that we have our own header file called cs50.h which has functions
24:55
that we have written just to make life easier in the first few weeks of the class. These are training wheels that we'll eventually take off.
25:02
But it turns out in C, especially if you've programmed before, it's actually really hard and annoying just
25:07
to get input from users, to get them to type a word or a number or something else.
25:12
Like, C does not make this easy, in part because it's one of the earliest languages that wasn't zeros and ones.
25:17
So you have to do a lot of the heavy lifting yourself. But we'll put on these training wheels today and for a few weeks
25:23
so that we can focus really on the intellectually interesting ideas of C and programming without getting bogged down in certain weeds
25:30
that we will come back to before long. So for instance, CS50's own documentation is there at that URL.
25:36
But within the library are these functions, a function called get_string to get a string of text.
25:44
"String" is a synonym for just text in a programming language. So get_string will prompt the human for a string of text.
25:50
Get_int is shorthand for "get integer," if you want to get a number from the user. Get_float is a little more arcane-- get a floating point number,
25:58
like a real number with a decimal point in it. And dot, dot, dot, there are others, as well.
26:03
So this is to say within CS50, we've got some user-friendly functions via which we can actually get some input.
26:09
And let's go ahead and use one of these, for instance get_string because recall that last week our second program in Scratch
26:15
was this one here, where we didn't just say "hello, world." We said "hello, David," or "hello, Carter,"
26:21
"hello, Julia," whoever it was typing their name in. But to do that, we needed this Ask block in Scratch.
26:28
And then we used the Say block. And then we used the Join block to make all of this work.
26:34
So let's translate this program now into C because it's a little more interesting and representative of the kind of code
26:39
we'll start to write. But we need a slightly different mental model. Still have a function here, which is the implementation in code of an algorithm.
26:47
We still have some inputs called arguments. But previously, I said that the Say block and, in turn,
26:53
printf have side effects, which is just something visually, typically, that happens on the screen.
26:58
Other functions actually have, what we called last week, return values. And this is kind of analogous to a function maybe doing something for you,
27:08
writing down the answer on a slip of paper, and then handing you, the programmer, the slip of paper to do whatever
27:14
you want with it without just broadcasting it to the world with, like, a speech bubble on the screen.
27:19
So a return value is germane for a program like this because recall when we used the Ask block and I typed in my name,
27:26
where did my name end up initially? It didn't go on the screen yet.
27:32
Where did it end up? STUDENT: In an answer. DAVID MALAN: In an "answer" puzzle piece. And that special oval puzzle piece I claimed at the time
27:39
represents a return value, so the metaphorical piece of paper that the answer is written down on so that I can then use it later.
27:46
So that's what we want to get to now in C, a return value that I can then do anything I want,
27:51
whether it's print it to the screen, change it in some way, save it in a database, or anything else. So here, for instance, is what we did with Scratch,
27:58
the input to the Say block-- or the Ask block was "what's your name," quote, unquote. The function, of course, is the Ask function.
28:05
And the return value was "answer." If we now consider how we might translate this to C,
28:10
it's going to look a little weird at first. But it's going to follow a pattern today, next week, the week after any time we do code like this.
28:18
So get_string, I claim, is going to be the most analogous function in C
28:23
to the Ask block. And to be clear, this is a CS50-specific thing, training wheels of sorts. But we'll show you in a few weeks what this function is doing and how you
28:31
cannot use it moving forward once you're comfortable with the language itself. Notice I've put parentheses, left and right,
28:37
as sort of a placeholder for user input. And that user input is going to be "what's your name?"
28:43
But I can't just put "what's your name" in parentheses. What do I minimally need to add in there, too? STUDENT: Quotes. DAVID MALAN: Yeah, so the double quotes, left and right.
28:50
So let me go ahead and add those in. I left a space here, not for a new line. I could move the cursor to the next line.
28:56
But I minimally at least want to move the cursor at least one space over just so it looks pretty, so that when I'm prompted for my name,
29:03
there's a space between the question and my answer. But it could also be backslash n. That's just an aesthetic choice on my part.
29:09
But what do I do with the answer that comes back from get_string? This is where the text is going to look different today.
29:16
In C, you start to use an equals sign from left to right respectively.
29:21
And on the left, you put the name of the variable in which you want to store that return value.
29:29
So a return value is kind of a conceptual thing. You can do with it what you want. And if I want to store it longer term in a variable,
29:36
like x or y or z in math class, I can just give it a name here-- x or y or z or, more reasonably, "answer," or any other English word.
29:45
No spaces, generally lowercase, same heuristics as before, but this means now, ask the user, what's their name?
29:53
Whatever they type in, go ahead and store it from right to left in this variable called "answer."
29:58
But C's not done with us yet. If you've learned Python or certain other languages, you'd kind of be done writing code at this point.
30:04
In C, though, you additionally have to tell the compiler what type of variable
30:09
you want to use. So if it's a string of text, you say "string." If it's an integer, a number, you say "int," as we might have seen before.
30:17
So it's a little more pedantic. It's more annoying, frankly, the more onus on you and me, the programmers. But this just helps the compiler know how
30:24
to store it in the computer's memory. And I'm so close to being done with this line of code, but what's missing?
30:29
STUDENT: Semicolon. DAVID MALAN: So semicolon. And mark my words, if you've never programmed before, sometime this week,
30:34
this semester, you will forget a semicolon. You will raise your hand. You'll get frustrated because you can't understand why your code's not working.
30:41
You will run into stupid issues like that. But do take faith that they are stupid issues. It doesn't mean it's not clicking for you or you're not a programmer.
30:49
It just takes time to see these things if it's a new language to you. So there now is my semicolon.
30:54
All right, let's go ahead then and do something with that return value using the second of the big puzzle pieces in Scratch.
31:02
So when I wanted to say, "hello, David," or whatever the human's name is, I kind of stacked my puzzle pieces like this.
31:09
This is actually similar to Python and maybe some other languages some of you have learned. But C is a little bit different.

## [Format Codes](https://youtu.be/cwtpLIWylAw?t=1875)

31:15
And the closest analog to this Scratch solution is going to look like this.
31:21
I still use printf because printf is the equivalent of Say. Inside of my parentheses, I'm going to go ahead and say, weirdly, "hello, %s."
31:32
So there's no real analog in C of Join. Instead, there's a way to specially format text using printf, hence the F
31:41
in "printf." And what you do in printf is you type whatever English word or human words that you want.
31:47
You then use %s a placeholder. If you want a string of text to be added to your own text,
31:54
you literally write "%s." And let me anticipate a question from the crowd-- how do you print out %s?
31:59
There's a solution to that, too, if you literally ever want to print out %s. But it's deliberately a weird choice of characters
32:07
so that the probability that we ever need to type this ourselves is just low that no one really worries too much about it.
32:12
All right, but that's not quite enough. In addition to saying "hello", comma, space, placeholder %s--
32:19
and just for vocabulary sake, that's a format code. Again, "format" being the F in printf.
32:26
I still need my double quotes around the whole thing. In this case, to match my previous program,
32:31
I am going to go ahead and add the backslash n to move the cursor to the next line. And now I've left a crazy amount of room here, but that's deliberate.
32:39
Does anyone have an instinct for what I'm probably going to want to add after the quotes but still inside of the parentheses?
32:47
STUDENT: The answer. DAVID MALAN: So answer itself. I need to somehow tell printf with a second input,
32:54
otherwise known as an argument, what I want to substitute for that %s. And so I put a comma and then the name of the variable
33:02
that I want printf to figure out how to plug in here. So honestly it's a little annoying, and this is kind of a dated approach.
33:09
Newer, more modern languages, like we'll see later in the course, Python and JavaScript, actually have much more user-friendly ways of doing it.
33:15
But once you wrap your mind around the heuristics, the rules here, it's just formatting a string by plugging in whatever you want
33:23
into this format string, so to speak. And again, the comma here is important.
33:28
This signifies that it takes one input at left and a second input at right. But notice this comma.
33:34
There's technically two commas. But I'm not claiming that this function takes three inputs.
33:40
Why? This comma I'm pointing out doesn't mean the same. STUDENT: It's because that comma's part of the quotation marks
33:46
and it's been part of the string. DAVID MALAN: Exactly. This comma that I'm pointing to is part of the quotation marks and therefore
33:51
part of my string of English text. So this is just English grammar. This is sort of C syntax.
33:57
And again, these are the sort of annoying little details that we're using the same symbol for different things, but context matters.
34:03
So just stare at your code, look carefully left to right, and generally the answer will pop out, no pun intended.
34:10
OK, questions now on this syntax before we actually write it and run it? Yeah? STUDENT: Why is the backslash n not after the answer?
34:18
DAVID MALAN: Why is the backslash n not after the answer? So the way functions work, including printf,
34:24
is that you pass to them one argument inside of the parentheses. And then if you have a second argument, you put it after this comma here.
34:32
But the way printf works is that its first argument is always a string that you want to be formatted for you.
34:39
So anything you want printed on the screen has to go in those quotes. And you can perhaps extrapolate from this.
34:45
If I actually wanted to say multiple things in this sentence, so "hello," maybe first name, last name, I could actually do "hello" comma, %s, space,
34:55
%s, if I had two variables, one called First Name, one called Last Name. But then I would need another comma for a third input to the function.
35:04
And so it's very general purpose in that sense. Questions? Yeah? STUDENT: Can you abstract this further by [INAUDIBLE] the "hello" [INAUDIBLE]??
35:15
DAVID MALAN: OK, so can you abstract away the format string itself, "hello," comma answer?
35:20
Short answer, yes, but not nearly as easily in C as you can in other languages. So that's why we're keeping it simple for now.
35:26
But you're going to love something like Python or JavaScript, where a lot of this complexity goes away. But you'll see also in Python and JavaScript and other languages,
35:34
they still are inspired by syntax like this. So just understanding it now will be useful for multiple languages
35:41
down the line. All right, so let's actually do something with this code rather than just talk about what it might be doing for us.

## [Hello, World](https://youtu.be/cwtpLIWylAw?t=2148)

35:48
Let me go over to, for instance, VS Code again. And I'm going to go ahead now and remove this middle line of printf.
35:56
I'm still in my same file called "hello.c." I'm going to clear my terminal window just to eliminate distraction.
36:02
And to do that, I can literally type "clear." But this is just for aesthetic's sake. That's not functionally that useful.
36:07
Or you can hit Control L to achieve the same on your keyboard. But I'm going to go back to line 5 here, where I previously just

## [Hello, You](https://youtu.be/cwtpLIWylAw?t=2173)

36:13
said "hello, world." And I'm going to do this instead. I'm going to give myself a variable called string.
36:20
Sorry, I'm going to give myself a variable called answer, the type of which is string. I'm going to set it equal to whatever the return
36:28
value is of get_string, asking an English question, "what's your name?"
36:33
with just a single space just to move the cursor over, followed by a semicolon.
36:38
Then I'm going to go ahead and say printf, quote, unquote, "hello, placeholder, backslash n,"
36:48
comma, and then what goes here again? STUDENT: Answer. DAVID MALAN: This is where answer goes. And then I just need a semicolon on the right of that.
36:56
But I think now that I'm done. But let me point out a couple of details. This got very colorful, very pretty quickly.
37:01
And it's not like the black and white code I had on the screen a moment ago. This is because what programs like VS Code do for us is it "pretty" prints,
37:10
or rather it syntax highlights our code for us. So syntax highlighting means just add some colors to the code
37:17
so that different ideas pop out. So you'll notice, for instance, that printf here, get_string here
37:22
are in purple because they represent functions, just like the Say block. Here, "what's your name?", quote, unquote, in VS Code
37:28
is a light blue instead of white. But it's still going to be consistent if I use strings of text elsewhere, as well.
37:33
So I didn't type anything special. This isn't like Microsoft Word or Google Docs, where I'm highlighting and changing colors of things.
37:39
This is all happening automatically. But it's just unicode text. It's just being interpreted automatically
37:46
and having these colors applied so that things pop out more usefully visually. Now, I've unfortunately made a mistake.
37:52
But I'm going to deliberately induce this one because you, too, will probably make this mistake. I'm going to go ahead and run "make hello"
37:58
again, because I've changed my code. So I have to regenerate the machine code from the new source code. But unfortunately, when I hit Enter now, my God,
38:06
the errors don't even fit on the screen. So let me make this bigger. I'm going to click the little caret symbol here just
38:12
to make my terminal bigger for just a moment. And you'll see that there's more lines of errors than there are of code that I actually wrote,
38:19
often which is written pretty arcanely, again, for programmers who've been writing code for 10, 20 years.
38:24
But there are some details that pop out. So notice the problem is definitely with hello.c.
38:30
So great, it is my fault. This syntax here means that line 5 is the problem.
38:36
And this next 5 means character 5. So you can literally triangulate your bug, your mistake by going to line 5
38:42
and then over five, and it's somewhere in that area. Specifically, "the area is use of undeclared identifier string.
38:49
Did you mean standard in?" I don't think I did. Like, I do want string, and then there's some other complexity here.
38:56
But what's important here is not the specifics of this error but really the implication that it doesn't recognize the word
39:04
"string" or "get_string." Now, why might this be? Yeah? STUDENT: You said that in order to [INAUDIBLE]
39:14
DAVID MALAN: Exactly. Because we are using get_string, which I claimed is a CS50 thing that we'll use for a few weeks,
39:19
C does not know about it out of the box, so to speak. I have to teach the compiler that get_string exists,
39:26
just like I taught the compiler that printf exists by including the appropriate header file. And in this case, quite simply, it's called includeCS50.h.
39:35
That now teaches the compiler, oh, someone else wrote this function already, get_string, and with it this type of variable
39:42
called "string." So now if I go back to my terminal window and rerun the exact same command, "make hello"-- maybe crossing my fingers--
39:49
now nothing in fact goes wrong because the compiler has been brought up to speed with all of the functionality it needs.
39:55
And now if I do ./hello, Enter, there it is, what's my name? And notice the cursor is one space over just
40:01
because I thought that looked prettier than having the cursor right next to the question mark. D-A-V-I-D as my input, and Enter.
40:07
And "hello, David." Questions on any of this code thus far?
40:16
Questions? Any of the code. No? All right, so let's introduce some other functionality into the mix.

## [Types](https://youtu.be/cwtpLIWylAw?t=2425)

40:25
It turns out that there are other types of data, other types of variables in the world, not just strings
40:31
but indeed, per before, we have things called integers, "int" for short, floating point values, "float" for short,
40:38
and a few others as well. So rather than only focus on string, let's get a little more interesting with numbers
40:43
here and see what we can do with something like integers, again "int" for short, by taking a look at not get_string, as before, but now
40:51
how about get_int. And for this, I'm going to give us a few other tools in our toolkit, those format codes to which I alluded earlier, like %s,
40:59
fortunately are pretty straightforward. And here is a list of most of the popular format codes that you might ever care about with printf.
41:07
In particular, we saw %s for string. And you can perhaps guess which one we're going to use for integers.
41:13
STUDENT: %i. DAVID MALAN: Yeah, so %i is what we're going to use for integers. And this is the kind of thing that you can consult in the manual pages or a slide like this.
41:20
There's only a few of them that you might frequently use. But let's go ahead and use integers in a more interesting context, not

## [Conditionals](https://youtu.be/cwtpLIWylAw?t=2486)

41:26
just using functions. But let's revisit this idea of conditionals. And conditionals in Scratch were like these proverbial forks in the road.
41:32
Like, do you want to do this thing or this thing or this other thing? It's a way of making decisions in a program, which
41:38
is going to be super useful and pretty much omnipresent in any problems that we try to solve. So let me give you a few more building blocks
41:45
in C by doing the side-by-side comparison again. So here in Scratch is how we might say if two variables, x and y,
41:53
one is less than the other, then go ahead and say, quote, unquote, "x is less than y." So kind of a stupid program.
41:59
But just to show you the basic syntax for Scratch, this is how you would ask the question, if x is less than y, then say this.
42:07
So Say is the function. "If" is the conditional. And the green thing here we called, what?
42:14
What did we call it? Yeah? STUDENT: A Boolean. DAVID MALAN: A Boolean or a Boolean expression, which is just a fancy way of saying a question whose
42:20
answer is true or false, yes or no, 1 or 0, however you want to think about it.
42:25
In C, the code is going to look like this. So it'll take a little bit of habit, a little bit of muscle memory to develop.
42:32
But you're going to say "if," then in parentheses, you're going to say "x less than y," assuming x and y are variables.
42:39
You're then going to use these curly braces. And then if you want to say, quote, unquote, "x is less than y"
42:45
in C, what function should we use here presumably?
42:50
So printf. So printf, quote, unquote, "x is less than y." So it's a bit of a mouthful, but again notice the pattern.
42:57
Name of the function is printf. In the parentheses, left and right, is the argument to printf,
43:02
which is, quote, unquote, "x is less than y." And again, just for aesthetics, to move the cursor to the next line,
43:07
which you don't have to worry about in Scratch because everything's in speech bubbles, we're adding a backslash n, as well.
43:14
So notice that these curly braces, as they're called, much like the orange puzzle piece here, are kind of hugging the code like this.
43:21
And I'll note that technically speaking in C, If you only have one line of code inside of your conditional,
43:28
you can actually omit the curly braces altogether. And the code will still work if you have one single line of code.
43:34
Why? Just saves people some keystrokes. If you have two lines, three lines, or more in there, you need the curly braces.
43:39
But I'll always draw it with the curly braces in class so it resembles Scratch as closely as possible.
43:44
As an aside to some of you who have programmed before, you might be cringing now because like you really like your curly brace to be over here instead of here, that,
43:52
too, is a stylistic choice. And we'll talk, too, about this in the class. Aesthetically, stylistically there are certain decisions we can make.
43:58
But generally in a class, in a company, you as a student or an employee would simply standardize on one set of rules, so to speak.
44:07
So we'll use these rules for formatting our code in class consistently. All right, any questions on this snippet of C code?
44:16
All right, a couple of others then. So here is how, in Scratch, we might have a two-way fork in the road. If x is less than y, say x is less than y, else say x is not less than y.
44:26
In C, It's going to look pretty much the same. But notice I'm adding an "else" keyword here with another set of curly braces.
44:32
I'm going to have a couple of more printf's. But in C, even though it's clearly keyboard based, it's just text, no more puzzle pieces, it's kind of the same shape,
44:41
so to speak, and it's definitely the same idea. So it's following a pattern. What about a three-way fork in the road, if x is less than y,
44:49
then say x is less than y, else if x is greater than y, say x is greater than y, else if x equals y, then say x is equal to y.
45:01
Well, you can probably see where this is going. On the right-hand side, it looks almost the same.
45:06
In fact, if I add in the printf's, it's really almost the same, at least logically. But there is at least one curiosity, seemingly a typo
45:16
but it's not this time. Yeah? STUDENT: The double equals. DAVID MALAN: Yeah, the double equal signs does not match Scratch,
45:23
but it's not in fact a bug or a mistake in C. Anyone have an intuition for why I did use two equal signs instead of one here?
45:33
Yeah? STUDENT: Because otherwise it could be mistaken for a variable. DAVID MALAN: Exactly. Well, otherwise it would be mistaken for a variable, specifically
45:41
assignment of a variable. So recall that in previous code, when we used the get_string function,
45:47
we used an equals sign to assign, from right to left, the value of a variable.
45:52
And that's a reasonable decision. "Equal" kind of means that the two should ultimately be equal even though you think about it from going right to left.
45:59
Unfortunately, the authors of C kind of [? painted ?] themselves into a corner. And presumably, decades ago when they realized, oh, shoot,
46:05
we've already used a single equal sign, how do we represent equality of two values, the answer they came up with was,
46:12
all right, we'll just use two instead. And thus was born this decision. Is it the best one? Who knows?
46:17
Crazy enough, in other languages, like JavaScript, you have not just one, but two, but also three equal signs
46:23
in a row to solve yet another problem. So reasonable people will disagree as to how good or bad these decisions are.
46:29
But in C, this is what you must do. But there's a bad design decision here, too.
46:38
It's still correct, the code, left and right. But I bet I could critique the quality of the design of both the Scratch code
46:45
and the C code for reasons, what? STUDENT: Do we have to do else if x equals [INAUDIBLE]??
46:51
DAVID MALAN: OK, no, really good intuition. Do we have to ask this third question, "else if x equals y?"
46:57
So short answer, no, logically, right? Just based on arithmetic, either x is less than y or x is greater than y
47:05
or, what's the only other possible answer? They must be equal, logically. So technically, you're just kind of wasting the computer's time
47:13
by asking this question because it already knows, at that point, the answer. And you're wasting your time as the programmer bothering
47:18
to type out more code or more puzzle pieces than you need because logically one stems from the other.
47:24
So I can tighten this up, get rid of the "else, if," just use an "else." And I can do the same thing over here in C, thereby avoiding
47:31
the double equal sign altogether, but not because it's wrong but because you're wasting time, because now you're potentially asking only two
47:38
questions, two Boolean expressions, instead of 50% more by asking a total of three questions at most.
47:46
Other questions then on this kind of code, logically or otherwise?
47:52
No? All right, so if we have these puzzle pieces, so to speak, at our disposal,

## [Variables](https://youtu.be/cwtpLIWylAw?t=2878)

47:58
how can we go about actually using these? Well, suppose that we actually want to do something with values. Let's introduce variables in C, as well.
48:06
We saw an example using a string a moment ago. But what about with something like integers? Well, you might not have used this in Scratch.
48:11
But here's the orange puzzle piece in Scratch via which you can create a variable called counter to count things.
48:17
And you can set it equal to some value like 0. Now, you can perhaps guess where we're going with this. If I want in C a variable called counter and I want to set it equal to 0,
48:27
I use a single equal sign because logically you read it from right to left, or technically it's executed from right to left.
48:34
But that's not enough in C. What's missing from the screen? STUDENT: Data type. DAVID MALAN: I need a what? STUDENT: You need a data type.
48:39
DAVID MALAN: So we need a data type. And if it's going to be an integer, indeed I'm going to use int. And now the other mistake I keep making is--
48:44
STUDENT: Semicolon. DAVID MALAN: So a semicolon at the end of the line. So it's a little more verbose than some languages.
48:50
But if you read it left to right, this is how you tell C to give you a variable called counter of type int
48:56
and initialize it to a value of 0. That's all. All right, how about, in Scratch, if you want to change that variable by 1,
49:04
by adding 1 to it? In Scratch, it's super simple. You just change it by 1 or even negative 1 if you want to go up or down respectively.
49:11
In C, it turns out you have a few different ways to do this. And this looks like it's not mathematically possible,
49:18
but that's because equals is assignment, recall. So this line of code is not saying that counter equals counter plus 1,
49:27
because that's just not possible using typical numbers. But this means take counter's value, add 1 to it,
49:33
and assign it back to the counter variable. So it's like incrementing counter in this way.
49:38
But this is such a common thing in C and in programming to increase or decrease the values of variables,
49:43
there's a more succinct syntax. This is identical. And it might take you a little practice to get used to it,
49:51
but it just saves you some keystrokes. But it similarly adds 1, or whatever number you use there. And this is such a common operation in C especially
49:58
that there's an even tighter way of executing the same idea. And you can literally just say counter++ and then semicolon in this case.
50:08
All three are exactly the same. All three are perfectly correct. But you'll learn over time that typing less on the screen
50:13
is probably going to save you some time. Meanwhile, if we wanted to do the opposite and do something like minus 1
50:19
in Scratch, we could similarly do minus minus in C. Or we could do-- yeah, we could do minus minus in C here at right.
50:28
All right, so just some additional building blocks, translating from scratch to C. Why don't we go ahead and try using this perhaps
50:36
in the following way? Let me go ahead and go back to VS Code. And let me propose that we do something like this.
50:45
In VS Code, I'm going to go ahead and clear my terminal window. I'm going to close "hello.c" by just clicking the X. I'm going to go ahead and create a new file called "compare.c"

## [compare.c](https://youtu.be/cwtpLIWylAw?t=3054)

50:54
because the purpose in life of this program is going to be to compare integers on the screen. This time I'm not going to mess up.
51:00
I'm going to preemptively include CS50.h. I'm going to preemptively include stdio.h.
51:07
And here, too, is a very common mistake in learning C. It is not "studio.h."
51:13
So when you email us asking why "studio.h" is not working, that's because that is not the word. It is "standard io.h," meaning standard input and output,
51:22
stuff involving the screen and the keyboard. Then I'm going to go ahead and, just as before, int main(void), but we'll come back to that eventually as to what it means.
51:29
And now inside of "main," which is just where the main part of my program goes,
51:35
again you can think of this as being analogous to "when green flag clicked." This just kicks everything off.
51:40
I'm going to go ahead and do two things. I'm going to go ahead and get an integer called x, and I'm going to prompt the user for that int
51:47
and just say something like, "what's x?", space. Then I'm going to do int y equals get_int, quote, unquote, "what's y?",
51:55
space. And then let's just do something simple like, if x is less than y,
52:00
then go ahead and print out, quote, unquote, "x is less than y backslash n," semicolon.
52:08
So it's not a very deep program. It's just going to do what most any human brain could do pretty quickly. But it's at least demonstrating how we might use now
52:17
something like a conditional in code. So let me go ahead and re-- let me compile this code for the first time, make compare, enter.
52:25
Nothing bad happens, which is good. "./compare" is how I run the program.
52:31
And just to tease this apart, dot, as we'll soon see, essentially means that the file is in your current folder.
52:36
So dot means in your current folder. And we'll eventually see that dot dot means your parent folder, like the one that contains wherever
52:43
I am on my computer's hard drive. All right. ./compare. What's x? 1.
52:49
2 for y. And hopefully it should say that x is less than y.
52:54
So pretty straightforward. Proof by example. And hopefully this would work in other cases, too. But if I flip that around and I rerun it, ./compare, and I do 2 and 1,
53:04
nothing's going to happen. But you would expect that because there's only one Boolean expression deciding whether or not
53:11
I should actually type this out. So what's going on? Well, if this helps you, you might find it
53:17
useful to think about the logic of any program, be it in Scratch or C, as kind of a flowchart of sorts.
53:22
And we'll put up a few of these over time just in case you're a particularly visual thinker. And this represents what it is I just did.
53:28
So here in this picture is where the program starts conceptually. And any time you see a diamond, think of that as a Boolean expression,
53:35
a question that's being asked. And the question being asked is, is x less than y? That has two possible answers, true or false, yes or no respectively.
53:44
So let me propose, per the arrow, that if the answer is true, then print out, per this rectangle, "x is less than y," just quote, unquote, and then stop.
53:52
That's it for the program. But logically, if x is not less than y, that is that question's answer is false, we'll just skip right to the end
54:00
and stop. So this is a control-flow diagram. It's just a pictorial way that you could write
54:05
on a piece of paper that just represents what it is the program is doing. And this gets a little more interesting if now we
54:12
do something else with the code. For instance, instead of just concluding that it's less than 1 or the other,
54:20
let's go back to the code here. Let me clear my terminal window. And let me add an "else." So else, go ahead and print out "x"--
54:29
I don't think I want to say this-- "greater than y." It's not quite right.
54:35
What would be reasonable to say here? STUDENT: "x is not less than y. DAVID MALAN: Yeah, subtle, but "x is not less than y" because it could be equal.
54:43
We don't know if we're only checking two scenarios here.
54:48
So if I recompile this, make compare, ./compare. Now if I do 1, comma 2, I still get the same answer.
54:55
If I rerun ./compare 2, comma 1, I now get the opposite answer.
55:01
It's not as good as might be ideal. It'd be nice to know if it's equal to or greater than. But at least that's all of the code that we have here.
55:08
And just to now paint a picture, if I go back to my control-flow diagram, my flow chart here,
55:13
this is what it looked like before logically. Now that I've added in a second branch, so to speak,
55:21
now, if the answer is false, I first print out x is not less than y, and then I stop the program.
55:28
So same idea, but the decision tree, if you will, if you've taken a 10 or the like, is getting a little bit bigger now
55:34
conceptually. All right, what if we do something more than this? Let's actually have that third condition. Let me go back into my code here.
55:40
I'm going to hide the terminal window just to make room for more code. And I'm going to say, "else if x is greater
55:47
than y," then go ahead and say not "x is not less than y," but rather "x is greater than y."
55:55
And then down here, I'll do an "else if x equals equals y," then I can go ahead and say printf, "x is equal to y backslash n,"
56:06
close quote. All right, so now if I run it-- let me open my terminal window again. Let me rerun make compare.
56:13
Let me rerun ./compare. 1 and 2 are the same. Let me rerun it.
56:18
2 and 1 are the same. Let me rerun it a third time. 1 and 1 are now in fact equal.
56:26
So this works correctly. But why did I make a point of using these "else if"s?
56:31
Put another way, couldn't I just make my life a little simpler and just say, if this, then that?
56:39
If this, then that. If this, then that. Just ask all three questions. Keep the code simple.
56:44
Don't bother with these else's. Would this work for me? Yeah? STUDENT: It just seems like [INAUDIBLE] the program
56:52
doesn't have to run the rest. DAVID MALAN: Yeah, so it saves a little bit of time because in this case, just like in English, this is like asking three separate questions.
57:00
And it's not harnessing any information from previous questions in order to decide whether you should bother asking that other question.
57:08
In other words, if x is less than y-- and you already figured that out because it's 1 and 2 respectively-- you're
57:14
going to print this. Why would you waste time asking this question when it's not going to be true? Why would you waste time asking this question when
57:21
it's not going to be true? And so the point I wanted to make here, which is that if we visualize that particular design,
57:27
what the flow chart looks like is actually this. And let me zoom in at the top. If you ask the question "is x less than y," well,
57:34
you're going to go ahead and say, x less than y. Then if you go down to the next question, you're still going to ask is x greater than y.
57:41
And then below that, you're still going to ask is x equal equal to y? So no matter what x and y are, you're asking one, two, three questions all
57:50
of the time. But if we actually go in and do what we did the first time, where if I go back to my code and I undo this edit and add back the "else if"s--
57:59
and now let me go back to the flow chart, which I claim is bad because it's one, two, three questions, one
58:05
or two of which might not be necessary-- now if I visualize what I just did, the flow chart gets a little more complicated looking,
58:12
but it's going to be better designed, more efficient. Why? Well, because if I start at the top here, I ask one question,
58:19
is x less than y. If the answer is true, OK. I say x less than y. And then, boom, I sort of cheat and go all the way
58:25
to the end of the program and stop, having asked only one question. If, though, x is not less than y, OK, fine, I'll ask you a second question.
58:33
But if the answer is true, boom, I print out x is greater than y, and then I stop.
58:38
And only in a perverse case where x actually equals y, which I'm going to claim is very unlikely or infrequent,
58:46
only then am I going to ask one, two, three questions to figure out whether
58:51
or not to print something at all. So this is what we mean by distinguishing between correctness
58:56
of code-- because it's still correct-- but this version is better designed because hopefully you're going to go down this branch or this branch rather than the longest one
59:04
frequently. Any questions now about this code or this visualization thereof?
59:13
Yeah? STUDENT: I don't know if [INAUDIBLE]
59:19
DAVID MALAN: A perfect segue. Why did I bother, though, even asking this question? Don't need to because when I hit this button--
59:25
hopefully I have the right slide in place-- this would be even better than that design.
59:30
So thank you for teeing that up. This is the same picture. It sort of got bigger because there's fewer nodes,
59:35
fewer shapes in the picture. Notice that if x less than y, boom, we say as much, and we stop. If x is not less than y but it's greater than y, boom, we stop.
59:43
Or if it's not greater than, we immediately conclude x indeed is equal to y.
59:49
And again, we stop. So this picture is about as efficient and as
59:54
well designed as we can make our logic. That's about as good as we can solve this problem. So if I go back to my code now to make my C code
1:00:02
match that, the only thing I need to do is stop wasting the computer's time. Don't ask that third question.
1:00:08
Just logically, mathematically conclude that of course it's going to be equal at that point in the story.
1:00:16
All right, any other questions on this? STUDENT: [INAUDIBLE] DAVID MALAN: Sorry, a little louder?
1:00:23
STUDENT: [INAUDIBLE] DAVID MALAN: Really good question.
1:00:29
What if I put in something that's not a number? So here, too, is where the CS50 library and the implementation of get_int
1:00:35
will be your friend. So for instance, if I run ./compare and I want to compare cats and dogs,
1:00:41
I could type in "cats," Enter. It's just going to prompt me again and again. It's not going to let me type in "dogs" either.
1:00:47
It's going to force me to give it an integer. C does not do that by default. And in fact, as we'll soon see over the course of CS50,
1:00:55
C is actually a very dangerous language at the end of the day because it just trusts that the human is doing what it wants.
1:01:00
And as such, a lot of today's software that is hacked in some ways, if it's using C or another language called C++,
1:01:07
are actually very vulnerable to certain types of hacking, whereas other languages that we'll get to in the class are less so for reasons
1:01:14
like this. All right, so besides this, let's consider just one other data type.

## [agree.c](https://youtu.be/cwtpLIWylAw?t=3681)

1:01:21
how about. So besides strings, besides chars, there's some others on this list here.
1:01:26
Sorry, besides strings, besides integers, there's this other data type here in C known as a char for a single character.
1:01:33
So here, let me just tease this apart. A string is indeed a string of text. It is zero or more characters together.
1:01:40
A char is always precisely one character. Not all languages bother distinguishing between a single character
1:01:48
and a string of characters. But in C, a string is typically multiple characters, but technically can be zero.
1:01:54
Coincidentally, it could be one. But it's capable of being more. But a char is literally, as the word implies, a single character.
1:02:02
All right, given that, notice that in the CS50 library, besides get_string, besides get_int, we also have get_char,
1:02:08
so another handy function for just getting a single character from the user. Now, why would it be useful to get a single character from the user?
1:02:14
Well, what if you're just doing something that you and I do pretty frequently when you install new software or fill out some form?
1:02:20
You agree to some form of terms and conditions. So in fact, let me go back over to VS Code here. And let me propose that I create a new program called agree.c,
1:02:29
so something akin to asking for the user's agreement. So in VS Code, I'm going to type "code agree.c."
1:02:35
And I'm going to do some quick boilerplate. So include CS50.h, include stdio.h, int main(void).
1:02:43
And then inside of main, which is like the "green flag clicked," I'm going to do this. Go ahead and get a character from the user,
1:02:51
and ask them something simple like, "Do you agree?," expecting a yes/no response.
1:02:56
But at the beginning of this line, I need to put the return value somewhere. So I'm going to put it in a variable called
1:03:02
C. And in programming, if you're just getting a single value, it's OK sometimes to use X and Y or C when you're using--
1:03:11
in larger programs, you'll benefit from using actual words like "answer," like we did from the get go.
1:03:16
But C has to be a specific type. So I'm going to literally say "char," and then I'm going to finish my thought with a semicolon.
1:03:23
And here's now how I could check if the user agrees or not. I could do something like this. If the value of C equals equals, quote, unquote,
1:03:31
lowercase 'y,' then go ahead and print out "Agreed backslash n."
1:03:38
Else if the variable C has a value equal to lowercase 'n', let's go ahead
1:03:44
and print out, say, "Not agreed," as though I'm agreeing or not to some terms and conditions.
1:03:49
But notice these are not typos. What did I do ever so subtly different from last time I used text?
1:03:56
Yeah? STUDENT: Single quotes instead of double quotes. DAVID MALAN: Single quotes instead of double quotes. So here's the heuristic.
1:04:02
When using strings, which are generally multiple characters, have to use double quotes. When using a single character, you should use single quotes
1:04:09
around the single character. So let me go ahead now and, make agree. Nothing went wrong, which is good. ./agree, Enter,
1:04:16
and let me go ahead and type in y for yes. It seems to work. Let me run it again. ./agree. n for no, and it seems to work.
1:04:24
And just if I type in something random like question mark, I don't know, it doesn't crash. It just ignores me because I only had two Boolean expressions there.
1:04:32
But notice that it's actually a little buggy arguably. Let me run it again. ./agree, Enter.
1:04:38
How about capital Y because, like, my Caps Lock is down. OK, it just ignores me. Let me do it again. ./agree, capital N because my-- oops--
1:04:46
because my Caps Lock is down. OK, it just ignores me. But this should make sense because I'm literally checking for lowercase.
1:04:52
So how could I fix this? How could I fix this without just changing lowercase to uppercase,
1:05:00
because that would then break it in the other direction? Yeah? STUDENT: [INAUDIBLE]
1:05:06
DAVID MALAN: Yeah, let's just add another branch here, so to speak.
1:05:12
So if variable C equals equals capital Y, then I can go ahead here
1:05:18
and say printf agreed. And then let me close my terminal to make more room.
1:05:23
Otherwise, down here, else if C equals equals capital N, let's go ahead and again say printf not agreed.
1:05:31
And I claim that this would actually now work. It's a four-way fork in the road, but I'm at least
1:05:36
checking for lowercase, uppercase, lowercase, uppercase for y and n respectively.
1:05:41
I claim that this is correct, but this too, even if you've never programmed before, should start today
1:05:47
to rub you the wrong way. Like, we can do better. This isn't the best design.
1:05:53
Why might that be? Yeah? STUDENT: Could you change the character c to be uppercase, like before you even
1:06:00
[INAUDIBLE]? DAVID MALAN: Ah, clever. So could we change the variable c to just be forced to uppercase
1:06:07
or maybe forced to lowercase? No matter what the human types, we just do that ourselves so that way we can just simplify this again to two possible scenarios.
1:06:15
I love that, but we haven't seen any functions yet in C that would let me change things to uppercase or lowercase.
1:06:20
So we'll get there, but a good instinct and correct. Other thoughts? STUDENT: Use "or." DAVID MALAN: So we could use "or" in some sense, like a logical "or."
1:06:28
What I don't like about this, to be clear, is that it's repeating itself. And there's this principle in programming, and in life in general,
1:06:35
like, don't repeat yourself unnecessarily. And by that I mean I literally have the same line 10 as 14.
1:06:41
I have the same line 18 as 22. And if anything, one, I literally wasted twice as much time as I needed to.
1:06:48
Put another way, per our discussion of Scratch, what if I go in and just change something like, I want to be more excited, like "Agreed!"?
1:06:55
Well, I might forget to change it in the other place. And let's just claim for today's purposes that that looks stupid, it's a bug, because I want them to be consistent.
1:07:02
So don't invite situations where you might change something in one place but not another.
1:07:07
Just only write it in one place total. So I like this idea of "or"-ing things together. So let me go ahead and delete what I just did.
1:07:14
And just to be clear, too, while this is on the screen, when you highlight code in VS Code based on how we've configured it, these dots just show you
1:07:21
how much I've indented because in C, stylistically, the convention is generally to indent four spaces and maybe four more spaces.
1:07:29
So those dots just help you count without having to manually eyeball things yourself. But let me delete those lines.
1:07:36
Let me delete these lines. And this is going to look a little weird, but the way you can "or" two thoughts together, so to
1:07:43
speak, like "or" them together, is you don't say "or," but you use two vertical bars, which syntactically
1:07:50
means the English word "or." And you can just ask the other question, if C equals,
1:07:55
quote, unquote, capital 'Y.' And then down here, I can say or C equals equals capital 'N.'
1:08:02
So it adds a little more code to each of those lines, but it doesn't add redundancy, because I've not duplicated my printf.
1:08:09
I've not added more curly braces unnecessarily. Now as an aside, there's the opposite of "or", logically is the word "and."
1:08:17
Just so you've seen it, I could do this. "&&" in C is how you express that the thing on the left must be true
1:08:24
and the thing on the right must be true. But why would this make no sense in this context of line 8?
1:08:30
STUDENT: It can't be uppercase and lowercase. DAVID MALAN: Yeah, at least to my knowledge, a character can't be both lowercase and uppercase.
1:08:36
That just makes no logical sense. So indeed "or" is what we want in this case. Other questions?
1:08:43
STUDENT: In CS50.h, is there a way to directly compare strings [INAUDIBLE]??
1:08:49
DAVID MALAN: Good question. Via CS50.h, is there a way to compare strings. Short answer, no.
1:08:54
But C is going to give us that capability. And in fact, next week, among the things we'll do is actually compare strings.
1:08:59
And if you've programmed before, you'll see in C that it actually doesn't work the way that you might expect.
1:09:04
But that's a problem, too, that we will solve. But that transcends CS50. That's a question for C. Other questions on this kind of logic?
1:09:15
Just to make this real then, anytime you click one of those EULAs or terms and conditions on a form in a piece of software,
1:09:22
odds are there is code as simple as this underneath the hood. Maybe it's graphical. Maybe it's checking for you clicking this button
1:09:27
or maybe hitting the Enter key. But underneath the hood is presumably some kind of conditional checking for those kinds of outputs.
1:09:35
All right, how about another building block from last time, which we'll now translate to C, namely loops, things that happen again and again?

## [Loops](https://youtu.be/cwtpLIWylAw?t=4181)

1:09:41
And these, too, are everywhere in code. So in Scratch, here's how we might meow three times, super simple.
1:09:47
In C, it's going to look a little weird. But you will get used to this over time if you've never programmed before.
1:09:52
It looks like a mouthful, OK. But let's tease it apart line by line.
1:09:57
And you'll see that you won't have that reaction frequently because it's all going to start to look very similar to itself.
1:10:03
But what are we doing here? In C, you don't have the luxury of these cute and fun puzzle pieces
1:10:09
that just do the work for you, repeat three times. In fact, in C and programming in general, sometimes
1:10:16
the work is on us to actually figure out, OK, how can I use functions, variables, conditionals, and loops
1:10:21
and implement some idea like repetition, like looping? And in C, here's how this might work.
1:10:27
How can I go about doing something like printing "meow" three times? Well, I know about variables now.
1:10:33
We're about to see loops. And I've seen how I can update variables by plussing or minusing
1:10:39
some value to them. Let's combine those ideas. So first, I'm doing what with this highlighted line in English?
1:10:46
If a friend cared to ask you, like, 'what is this line of code doing' later today, what would you say? STUDENT: It's creating a variable called "counter" and setting it equal to 3.
1:10:54
DAVID MALAN: Good, it's creating a variable called "counter" and setting it equal to 3. I'll use slightly new jargon.
1:11:01
I'm defining a variable, would be the term of our "called counter" and setting it equal to 3. So I'll use my hand to represent the counter.
1:11:07
And that's all a variable is. It's like storage in some case that I'm representing information, using my hand in this case or the computer's memory here.
1:11:14
Now what happens when using a loop in C? There's different types of loops, one of which is called a for loop-- oop--
1:11:20
one of which is called a while loop-- spoiler. A while loop works like this. Inside of parentheses is a Boolean expression just like inside
1:11:28
of a conditional that asks a question. But this time the question is going to determine, do you keep going through the loop again and again and again?
1:11:37
So it's not a one-time thing potentially. It is checked again and again and again to decide when it is time to stop looping, to stop cycling.
1:11:44
All right, so it's asking this question first. Is counter greater than 0? OK, obviously the answer is true because I'm still holding up three fingers.
1:11:52
So what happens? C goes inside of the curly braces per the indentation
1:11:58
and executes printf of "meow," which prints out a "meow" on the screen. The next line of code executes, which, recall,
1:12:04
is the same as just subtracting 1 from counter. So I think I take down one finger, so I'm left with two.
1:12:10
And what happens next? Well, this you just kind of have to memorize. Once you get to the end of the inside of a loop,
1:12:16
you go back to the beginning of a loop here and ask the same question, the same Boolean expression.
1:12:22
So is 2 greater than 0? OK, obviously so. So you go into it, you print a "meow."
1:12:27
You go into it and decrement counter further by one. So now my hand is holding up one.
1:12:33
Now we wrap back around to the Boolean expression. Is 1 greater than 0? Obviously.
1:12:38
We print out a third "meow." We then decrement counter again, and my hand goes to zero.
1:12:43
We go back around once more. Is 0 greater than 0? No. And now the program just terminates.
1:12:49
Or if there were more code here, it would just jump outside of the curly braces and keep going lower on the screen.
1:12:56
So that's all that's happening. And so this is what MIT has the luxury of doing with pictures. But at MIT, someone probably essentially wrote
1:13:03
code that looks like this to give us the illusion, the abstraction of this.
1:13:09
So what we're learning today is how they invented these puzzle pieces by just using lower-level plumbing, if you will, like this here.
1:13:17
Yeah? STUDENT: What would happen if you created the variable "counter" inside of the curly braces?
1:13:23
DAVID MALAN: A really good question. What would happen if you created the variable inside of the curly braces?
1:13:28
Short answer, it just wouldn't work in C, because if I were to try with my slide here,
1:13:33
for instance, to move this line of code here down inside of this, for instance,
1:13:39
now the very top line is trying to use counter before it even exists.
1:13:44
So C is very literal it. Reads top to bottom, left to right. And if it hasn't seen you define or create a variable yet,
1:13:50
you're going to get some scary error message on the screen instead. All right, other questions on this here code?
1:13:59
No? All right, so if we want to then maybe tighten this up a bit, let me propose that we could do this instead.
1:14:05
So besides this version of the code, let me just do something more canonical, more conventional. So you're totally fine with using a variable like counter .
1:14:13
It's what Scratch uses by default. It's very verbose. It does what it says. Frankly, once you get comfy with programming,
1:14:18
like most typical programmers, whenever they have a single integer in a program whose sole purpose in life is to count,
1:14:24
they'll just use "i" for integer just like I used "c" for character. When you have larger programs, you don't want
1:14:29
to start using A and B and C and D and E and F and so forth for your variables
1:14:35
because nothing's going to make any sense. But when you're doing something super simple like counting with an integer,
1:14:40
using a short-named variable is totally stylistically reasonable. But I can tighten this up further, not just renaming counter to i.
1:14:48
What else can I do, if you recall? Over here? STUDENT: [INAUDIBLE] DAVID MALAN: Sure.
1:14:53
STUDENT: A for loop? DAVID MALAN: Oh, OK, for loop. Yes, that was my spoiler. But while in a while loop, I can tighten this up slightly more.
1:15:00
Over here? STUDENT: Instead of i equals i minus 1. DAVID MALAN: Yeah, instead of i equals i minus 1,
1:15:06
I can actually tighten this up this way. And we didn't see the minus before, but it's the same idea-- i minus equals 1, or even more succinctly, i minus minus.
1:15:15
So when you get comfortable with programming, any of these approaches are correct. This would be more conventional at this point.
1:15:21
So if you want to write code like most other people write code, adopt ultimately these kinds of conventions.
1:15:28
All right, so that just does the exact same thing, though. But let's now put this into practice.
1:15:33
Let me go back to VS Code here. Let me go ahead and clear my terminal and close agree.c from before.

## [meow.c](https://youtu.be/cwtpLIWylAw?t=4540)

1:15:40
And let me go ahead and create a file called "meow." So code meow.c. And let me do this the sort of wrong way.
1:15:47
Let me include stdio.h. at the top, int main(void) thereafter.
1:15:52
Inside of there, let me do printf "meow." And then you know what? I don't want to keep typing that.
1:15:58
Let me just go ahead and copy/paste two more times. So I claim this is correct, make meow.
1:16:04
./meow, done. I've got code that prints "meow" three times. But this, again, should already rub you the wrong way.
1:16:11
Why? Yeah? STUDENT: There's duplication. DAVID MALAN: Because what? STUDENT: There's duplication.
1:16:17
DAVID MALAN: Because I have duplication. I mean, I literally copied and pasted it. And that's kind of a good rule of thumb. If you, in the future, start finding yourself copying and pasting code
1:16:24
within the same program, you're probably doing something wrong. There's a better way to design it even if it's correct.
1:16:30
So this is clearly a candidate for a loop. So let me go ahead and actually do that. Let me just go ahead and remove all of this duplication.
1:16:37
Let me give myself a variable called i, set it equal to 3.
1:16:42
Let me go ahead and give myself a while loop and check that i is greater than 0. Inside of this loop, let me print out just "meow" once.
1:16:50
But I'll reuse that code again and again because here I'm going to do i minus minus.
1:16:56
So that's the exact same code, the tight version of it that we saw a moment ago. Let me go ahead and "make meow" again, ./meow, and it still works.
1:17:04
Why is this version better? Because if you want the cat to meow five times, you change it in one place.
1:17:10
If you want to make the cat a dog, you change the meow to a woof in one place,
1:17:15
albeit changing the file name eventually, but changing it in one place, not worrying about changing it again and again and again.
1:17:22
But there are other ways to do this. For instance, let me propose that.
1:17:30
And actually, let's see, let me propose that instead of just doing it this way, just to be clear--
1:17:36
yeah, let's go ahead and propose that instead of doing this, we can actually count in different directions. I'm kind of forcing this idea of starting at 3, going down to 0.
1:17:44
But when normal humans in this room, if you ever count something, you probably do 1, 2, 3, and done. Like, that's how we would count in the real world.
1:17:51
Well, we can do that, too, here code-wise. We could initialize i to 1.
1:17:56
We could check that i is less than or equal to 3. And we've not seen this syntax before, but there's
1:18:03
no easy way on a typical keyboard to type a less than or equal sign like in a math book. So we use two characters, a less-than sign and then an equal sign
1:18:11
back to back. And that means less than or equal to. And this is the same idea so long as I plus plus i inside of it
1:18:18
because that'll start at 1, then 2, but it won't stop then. It will go up to until i is equal to 3.
1:18:25
Once i becomes 4, then that Boolean expression isn't going to be true. So it stops after three "meow"s total.
1:18:32
But there's another way, too, and this is probably the most conventional and the way you should do it
1:18:37
even though it's just as correct. In CS, if you've seen already last week, we almost always start counting from 0.
1:18:43
Why? Just because, so we're not wasting a pattern of bits. So generally when you start writing code that counts,
1:18:49
you should, quote, unquote, "almost always" start at 0, count up to but not through the total you
1:18:56
care about so you don't get one extra by accident. And so this would be the most conventional way
1:19:01
of doing what we just described. But they're all correct. You can make an argument that all of them are equally good.
1:19:07
This is what most people, quote, unquote, "would do." OK, other questions on this here syntax or logic?
1:19:15
No? All right, how about--
1:19:21
we got some cookies on the horizon. But before we get there, let's meow a few more times, if we may. So how about doing a little bit differently versus the while loop.
1:19:31
And I think we heard it over here. Turns out there's another type of loop altogether. So this one here.
1:19:37
And this one, if you can believe it, is probably even more conventional than the other way. And this is going to be thematic in programming.
1:19:43
There's rarely one way, one right way to do things. You're going to have bunches of different tools in your toolkit.
1:19:49
And your code might look different from someone else's because each of you tends to reach for a different tool in that toolkit.
1:19:54
And here's another tool-- and as you proposed earlier-- a for loop. A for loop is just another way of achieving the exact same idea
1:20:02
using slightly different syntax. And it's appealing, frankly in general, because it's a little more succinct.
1:20:08
It just saves some keystrokes even though you have to memorize the order in which it works. This code is identical to this code here functionally.
1:20:18
But aesthetically, of course, it looks different. How does it work? In a for loop, notice that in the parentheses
1:20:24
is not a single simple Boolean expression. There are three things. One, before a semicolon, is a place to initialize a variable
1:20:33
to do your counting typically. Second is the Boolean expression. So it's still there. It's just surrounded on the left and the right by two other things.
1:20:40
Lastly is the update. What do you want to do at the end of every loop through this block of code?
1:20:45
So you can probably imagine where we're going with this. How does this work? The first thing that happens is that a variable
1:20:51
called i is defined and initialized to the value of 0. That happens once and only once. Then we check the condition.
1:20:58
Is 0 less than 3? Obviously yes. So now we don't do the plus plus yet.
1:21:03
We go into the loop. And this is where the for loop's a little confusing at first. We print out "meow." Then what happens?
1:21:09
There's no more lines. So we go back to the for loop, and we increment i at that point.
1:21:14
So now i is 1. Then we check the condition. i is less than 3? Yes, because 1 is less than 3.
1:21:20
We go back into the loop and print "meow." Now we go back to the plus plus, so i is now 2.
1:21:26
We check the condition. 2 is less than 3 obviously. So we go back into the loop and print "meow." Then we do the increment. i is now 3.
1:21:34
Is 3 less than 3? No, so we exit the loop, and we're done, or we keep
1:21:41
going down here if there's more code. But how many times did I say "meow?" 1, 2, 3 total, when my hand was 0, 1, and 2.
1:21:52
Questions on this alternative syntax? It takes some getting used to, but most people would write loops using a for loop, I would say.
1:21:58
STUDENT: Could you now in the curly braces, use just one line of code? DAVID MALAN: Yes. If you really want to be cool and save syntax,
1:22:05
yes, it is correct and common to eliminate the curly braces if you only
1:22:11
have one line of code therein. We in class will always put the curly braces there because this is the kind of thing where, if you get forgetful, you go in later
1:22:19
and add a second line. Like, darn it, like you forgot the curly braces, things will not work as expected. So in general, use the curly braces, but you do not have to strictly.
1:22:27
Other questions on 6? Yes? STUDENT: [INAUDIBLE]
1:22:33
DAVID MALAN: Can be used without, what? STUDENT: [INAUDIBLE] DAVID MALAN: Oh, could you do it without the condition?
1:22:39
Yes, there are very fancy things you can do that we won't focus on today. But yes, if you want to get rid of the condition, you could get rid of this
1:22:48
here. And that would actually make the loop go forever, which may be a good thing if it's like a clock
1:22:53
that you want to tick forever, but often not a good thing in code. Good question, though.
1:22:58
All right, so beyond that, let's just go ahead and put this into context. Just in case it helps you to think about this,
1:23:04
this is just another flow chart, if you're more of a visual thinker, that represents what it is this loop is now doing.
1:23:11
Previously, all of our arrows went from top to bottom and stopped. But now there's an arrow going back, up, and around
1:23:16
because of this loop, this cycle. So when we start this program, we set i equal to 0. We then check, is i less than 3?
1:23:23
Obviously it is, so we print "meow." We increment i, and then we go back to that same condition.
1:23:29
We check the condition. We print "meow." i plus plus, go back, go back.
1:23:36
Now, if i equals 3, 3 is not less than 3, so the answer is false. And we stop.
1:23:41
So again, it's just another way of thinking about how the code in Scratch, how the code in C
1:23:46
might alternatively work in each of these contexts. But there's this one other puzzle piece in Scratch,
1:23:53
recall, that's not the repeat block, which is for finite numbers of repetitions, but forever.
1:23:59
And in C, there is a way to do this, but it's a little weird looking. There's no forever keyword. But you can use the while loop or, as you inferred,
1:24:08
you can actually use the for loop without a condition in the middle. So here, I can actually say this.
1:24:14
If I want to do something forever, I want to make sure that the answer to my question, the Boolean expression,
1:24:20
is always true, always true, always true, the easiest way to achieve that goal is just literally write "true" there
1:24:27
because true is true no matter what. And it's a trick for making the loop forever go around and around, as you might if you
1:24:33
want the cat to live forever and meow incessantly or if it is a clock that you want to tick forever or the like.
1:24:39
So here, for instance, is how we might have a cat meow endlessly,
1:24:44
using this so-called for loop instead. But recall that in Scratch, we also had this ability

## [Functions](https://youtu.be/cwtpLIWylAw?t=5090)

1:24:50
to create some of our own puzzle pieces. And this, too, is something that we're going to be able to do here in C.
1:24:55
And let me propose that we do exactly that by introducing the C analog of this.
1:25:03
So here, for instance, is, in Scratch, our definition of a function called meow whose sole purpose in life
1:25:10
was to just play the sound "meow" until it's done. This is going to look a little weird at first. But you'll notice some similarities with main.
1:25:17
So recall this thing I keep typing with main, int main(void), int main(void). That's just the "when green flag clicked" equivalent for today.
1:25:25
But if you want to create your own puzzle piece or your own function in C, you, for now, literally do this.
1:25:31
You say, void, the name of the function you want to create, and then void in parentheses. And technically what this means is that this function has no return value.
1:25:39
It doesn't hand you anything back like get_string or get_int. And the "void" in parentheses means it takes no inputs.
1:25:45
It only meows. You don't have to tell it how to meow. It's just going to meow. So no arguments, so to speak.
1:25:51
This literally just prints out "meow." But what this does for me is it abstracts away the idea of meowing.
1:25:56
I don't need to know how to use printf or that you're using printf to make the cat meow. I now have a function in life called meow because in Scratch, recall,
1:26:05
I used it like this. When the green flag is clicked, I could repeat three times this new custom
1:26:10
puzzle piece. But in C, I could now do this. In my main program, I can use a for loop just like we saw a moment ago,
1:26:18
copy/pasted from earlier. But now I can call my own C function called meow.
1:26:25
And let me go ahead now and do this. If I go over to my C code here, back in VS Code, let me go ahead
1:26:33
and delete everything inside main. Let me go ahead and do for int i equals 0, i is less than 3, i++.
1:26:42
Inside of my curly braces, let me go ahead and say "meow." But I now need this meow function to exist because if I
1:26:49
do "make meow" again, notice error. "Implicit declaration of function meow is invalid in C99"--
1:26:56
the 1999 version of C. What does that mean? Well, it doesn't know what the meow function is.
1:27:02
And the meow function is not in CS50.h. It's not in stdio.h. I have to create it.
1:27:08
So let me type out or really copy/paste what I had on the screen a moment ago-- "void meow meow"--
1:27:13
[CHUCKLES] "void meow(void)" printf, quote, unquote, "meow," close quote,
1:27:20
semicolon. But here, too, let me scooch this down a bit so you can see all the code at once.
1:27:26
Let me now do make meow. And unfortunately, I still have an error. If I scroll up, still on line 7 of meow.c,
1:27:36
my compiler thinks that meow is invalid, that it does not exist.
1:27:42
This too is a common mistake. And as simple as this code might be in spirit, where did I screw up?
1:27:50
Yeah, in the middle. STUDENT: You need to define the function like above where you use it. DAVID MALAN: Yeah, I need to define the function before I use it.
1:27:57
So again, C is going to take you literally. If you try to call meow on line 7, you better not define it on line 11.
1:28:03
You better define it higher up. So the simplest fix is going to be just to do this.
1:28:09
Let me clear my terminal. Let me highlight and just delete the meow function. And let me just paste it up here.
1:28:15
And this will actually solve the problem. Make meow now works. And if I do ./meow, that, too, works.
1:28:22
But this isn't really the best solution because if your solution is constantly, oh, well, just put it up there, put it up there, put it up there,
1:28:28
I bet we could contrive a situation where one function needs to be above the other, but it needs to be above the other. And that's just not going to work in general.
1:28:35
And more importantly, it just pushes main lower and lower and lower in your file.
1:28:40
But the whole point of your main function is like, that's the entry point. That is what happens when the green flag is clicked.
1:28:46
And so just in terms of user conventions, it's just useful for main to always be at the top of a file because then you can find it fast.
1:28:53
Your friends can, your TFs can find it quickly if it's at the top. So the other solution here would be to leave meow at the bottom
1:29:01
and leave main at the top. But this is the only time, if I may, that copy/paste is OK.
1:29:07
What I've highlighted here in line 11 is what's called the function's prototype. It is enough information to give you the return type, the name of the function,
1:29:16
and the return value-- and any arguments. And so if you just copy/paste that one line and end it with a semicolon
1:29:25
up there, that's enough of a hint to the compiler that, OK, it doesn't exist yet, but it will.
1:29:32
And it will look like that. That's the only time it's OK to copy/paste the very first line of a function you've written
1:29:39
to the top of the file with a semicolon so that you can make the compiler happy.
1:29:45
So if I do make meow now, still no errors. ./meow, and it now works.
1:29:51
But let me add one final feature, coming back to Scratch here. And then it's time for a snack.
1:29:57
So here, recall, was sort of the last fancy thing we did in Scratch, where we created not only our own custom puzzle piece,
1:30:04
but it took an input so that we didn't need to keep using the loop ourself. We could just let the meow function be told how many times
1:30:11
do you want the cat to meow. So in C, we don't have to make that many changes except this.
1:30:16
We change the prototype to take an argument inside of parentheses. And this is the syntax for that.
1:30:23
If you want your own function in C to take one or more arguments, you give the arguments a name, n, or whatever you want to call it.
1:30:30
But you have to tell C what the type of that input is. So it's an int n. So it knows it's a number.
1:30:36
And then you can just use n in your program. So instead of hard coding, typing manually the number 3,
1:30:41
I'm just using n here. So this is equivalent to what I did with Scratch, by just dragging and dropping
1:30:46
the n variable there. And then "meow" will get printed that many times. If I want to then use this-- notice, this is the last version of the cat
1:30:54
that we did last week-- you just say "meow" this many times. So in C, this is where now the code gets very succinct
1:31:03
because all the main part of the program does is meow three times. So this, again, is an abstraction.
1:31:08
I don't need to know, care, or remember how meow is implemented. I just need to know what its return value, its name, and any arguments
1:31:16
thereto are. So if I make this change, I think we can get the cat
1:31:21
to meow any number of times. Let me go back over to my C code here. Let me go back into the file and change "void" here to be int n,
1:31:31
where n just means number. I could use i, but n tends to be a quantity instead of a counter.
1:31:36
I then, inside of this function, am going to do a for loop-- for int i get 0; i less than n--
1:31:43
instead of 3-- i++. And then inside of here, I'll paste that "meow" again.
1:31:49
I need to change my prototype to be identical, so another copy/paste, or just manually edit it.
1:31:54
But now notice what's cool about main, is that now I can meow maybe three times.
1:32:00
Make meow, Enter, ./meow. OK, or if I really want to be cool, I can change this to 30,000 times.
1:32:09
Go back here, make meow. Increase the size of my terminal window for a dramatic pre-break flourish.
1:32:16
And there are 30-- that was a fast cat. There are 30,000 meows. I think now let's go ahead and take-- that's a lot-- a 10-minute break.
1:32:22
We'll see you in 10. Cookies are now served outside. All right, so we are back.
1:32:29
And I realize this has been a lot so far, right? So there's a lot of new syntax. There's a lot of translation of Scratch over to C.
1:32:36
But among the goals of having spent last week in Scratch and having spent problems at 0 in Scratch is that none of today's ideas
1:32:44
are really all that new. It's just a lot of syntax that will get more comfortable and more in your muscle memory as time passes.
1:32:52
Up until now, though, we've focused largely on these side effects, like things happening on the screen.
1:32:58
And that was akin to the speech bubble appearing in the world of Scratch. But let's focus for just a bit-- before we then explore things
1:33:05
we can't do very well in code-- on return values instead in C. We've seen them already.
1:33:10
Like, get_string returns a value. Get_int returns a value, a string and an int respectively.
1:33:16
But what if we want to make our own functions that don't just meow and visually have this side effect of meowing on the screen
1:33:21
but actually hand us back some value? Well, I bet we can do this in C, as well.
1:33:26
Well, let me propose that to go that route-- let me go back to VS Code here. And let's make our very simple calculator

## [calculator.c](https://youtu.be/cwtpLIWylAw?t=5613)

1:33:33
that just adds some numbers together. But the same calculator, we'll soon see, is going to get us into trouble if you don't understand what the computer is
1:33:40
doing underneath the hood. Let me go ahead and run code of, say, calculator.c.
1:33:47
And in here, let me go ahead and give myself access to the CS50 library with CS50.h, the stdio.h library with stdio.h,
1:33:56
int main(void), which, again, we'll just take for granted today that we have to include atop any of these programs.
1:34:03
And let's just add two numbers together-- super simple calculator. So it gives me a variable called x.
1:34:08
Assign it the return value of get_int. And I'll ask the user to give us x.
1:34:13
Give me another variable called y. Assign it the return value of get_int again. But this time, ask the user for y.
1:34:20
And then, lastly, let's just go ahead and print out the value of x plus y.
1:34:26
But I don't think I can get away with something like this, x plus y semicolon, because if I
1:34:33
do this, based on what we've seen before, what's actually going to get printed out? STUDENT: x plus y.
1:34:38
DAVID MALAN: Right, literally like x plus y. So I think this is where I need the F in "printf" for formatting.
1:34:43
What I think I really want to do is print out the value of some placeholder because, what do I want to substitute for percent i
1:34:51
maybe as a second argument to printf intuitively? Maybe just x plus y.
1:34:56
So indeed, I can get away with this because it turns out in C, there's a bunch of arithmetic operators, all of the ones that you might expect,
1:35:03
including addition, subtraction, multiplication, division, and even this one, the so-called modulo operator,
1:35:09
which generally gives us the ability to calculate a remainder when you divide one number by another. But I'll keep it simple with addition.
1:35:15
And indeed, with printf, if I want to print out the value of x plus y, I can do that.
1:35:21
But I have to tell printf what kind of value to expect, an integer, thus the percent i instead of %s for string.
1:35:29
And I think this should do the job. So let me go back to my terminal. Make calculator, Enter.
1:35:34
All is well so far. ./calculator, and let's keep it simple-- 1 for x, 2 for y. And indeed, I get 3 as the output.
1:35:42
It's not very dynamic. It can't do a subtraction or multiplication or much more. But it does at least do those kinds of calculations.
1:35:49
But let me propose now that we maybe make a reusable addition function, right, because addition is something I'm going to do a lot.
1:35:56
And maybe it should be abstracted away with a function just like meowing was abstracted away a moment ago.
1:36:02
So let me go ahead and instead of doing this, let me go ahead and give myself a function called add,

## [Scope](https://youtu.be/cwtpLIWylAw?t=5768)

1:36:08
but instead of last time where I had a meow function, I'm obviously going to call this "add" instead.
1:36:14
And instead of last time, taking in no arguments, I think I want add to work a little differently.
1:36:21
I don't want add necessarily to take an argument yet, but I do want add to return some type of value.
1:36:27
And just intuitively, what type of value should an addition function return? STUDENT: An integer. DAVID MALAN: An integer, so an int.
1:36:33
So I'm going to change void, which means the absence of a return value-- nothing's coming back-- to literally "int."
1:36:39
But I'm not going to change the thing inside parentheses yet. I'm going to go ahead and copy my prototype up here.
1:36:47
And I'm going to make this change, return x plus y. And then here, instead of printing out x plus y, let's go ahead and do this.
1:36:57
Let me give myself a third variable just for now. z equals the return value of this brand-new
1:37:02
add function that's going to add x plus y for me. And then let me print out the value of z. Instead of x plus y, I'm outsourcing now to this add function
1:37:10
so it will do the addition of x plus y. So similar in spirit to meowing, but the return values, I claim,
1:37:19
are about to create an issue. So let me make calculator again. And there's definitely some errors.
1:37:24
So here we have, "use of undeclared identifier x." And that's on line 17.
1:37:30
So that's pretty far down in the file. So specifically, my compiler does not like my use of x on line 17.
1:37:37
But wait a minute, x is clearly defined on line 8.
1:37:42
What intuitively might explain this issue even if you've never programmed before?
1:37:48
Yeah? STUDENT: Well, because x and y are defined in the main function, not the add function.
1:37:53
DAVID MALAN: Yeah, because x and y are defined in the main function, not in the add function. So the term of art here that we're about to introduce
1:37:59
is something called "scope." So "scope" just refers to the context in which variables exist--
1:38:05
the context in which variables exist. So by that, I mean this. On line 8, I've declared x.
1:38:11
On line y, I've declared-- [CHUCKLES] on line 9, I've declared y. But the catch is-- and here's where the curly braces are helpful--
1:38:18
those variables only exist in the context of the outer curly braces
1:38:25
that are nearest to them, like this. So I can use x and y on lines 10, 11, 12, and even up to 13,
1:38:31
but not thereafter. So I certainly can't use x down here on line 7. But this is a problem, because if add's purpose in life is to add x and y
1:38:39
but add can't access x plus y, well, we have an issue of scope. Like, x and y are not in scope for this add function.
1:38:46
But that's OK because remember that every function we've seen thus far can have maybe a return value or a side effect,
1:38:53
but it can also take 0 or one or two or more inputs, known as arguments.
1:38:59
So what if I instead do this? Let me clear my terminal window. And let me update add to not take nothing
1:39:05
as input but maybe two integers. And I'll call them arbitrarily a and b. But I have to tell the compiler what type of arguments
1:39:12
they are-- two integers, one after the other. And now what I can do is this.
1:39:18
Let me change this up here, too-- int a, int b-- just so that the prototype is exactly the same.
1:39:23
And the only purpose of this prototype is just to avoid the previous error, where the compiler didn't realize add was going to exist
1:39:30
because it came later in the file. So here on line 11 now, if I want to add two values, x and y,
1:39:37
this is now the syntax. We saw syntax in Scratch for passing in inputs to tell it how many times to meow.
1:39:44
So this is just telling add what two numbers to add together.
1:39:50
So now I have to change this to a plus b, for reasons we'll soon see. And let me see if this is right.
1:39:56
Make calculator. So far so good. ./calculator. Let's do 1 and 2 for x and y respectively.
1:40:02
And hopefully we should, again, see 3. Now, what's going on? So here, again, if I zoom in on my add function, this "int" here on the left,
1:40:11
on line 15, means what about add? STUDENT: [INAUDIBLE] DAVID MALAN: This means that it has a return value, that it's an int.
1:40:18
So it's going to hand me back, metaphorically, a slip of paper with an answer on it that is of type integer.
1:40:24
It's not a word, like my name. It's a number instead. These mentions of int here and here are inside the parentheses, which means
1:40:33
this function, add, takes two inputs. The first is an int. The second is an int.
1:40:38
And just so we have something to call them, I call them a and b respectively. So what happens essentially when I call the add function now on line 11,
1:40:49
I'm kind of passing in x. I'm passing in y. But the add function is going to think of them as a and b respectively.
1:40:56
It could call them anything I want. I could change this to the word "first" and "second." And then I could literally change this to "first + second."
1:41:03
Those are perfectly acceptable as argument or variable names. But who really cares? Like, a and b for such a simple function is perfectly reasonable, too.
1:41:12
Technically, if your mind is going there, I could even call them the exact same thing.
1:41:18
But let me propose for today, certainly don't do that because it just confuses things if you've got x's and y's here, x's and y's here,
1:41:24
but they're clearly different. Just don't do that. Try to come up with different variables just to keep yourself sane.
1:41:29
But here, I have a function that takes now two integers, a and b respectively. It just returns the sum of them so that I can now store the return
1:41:37
value of add in a variable called z. And then, quite simply, print it out.

## [Function Composition](https://youtu.be/cwtpLIWylAw?t=6105)

1:41:45
But there's one other thing I can do here. Now, if we think about design, even if you've never programmed before,
1:41:51
do I really need the variable z? Because I'm defining it on line 11, and then I'm quickly using it on line 12,
1:41:58
and that's it? Like, sometimes you don't need variables. And they might make your code more readable. But strictly speaking-- and this is just kind of like substitution in math--
1:42:06
if z is the same thing as "add (x, y)," well, let me go ahead and just delete line 11 altogether.
1:42:12
Let me get rid of mention of z. You can actually get away with doing this. And much like the Join block in Scratch, where I kind of overlaid it
1:42:20
on the Say block, kind of stacking them, you can stack functions in C, or nest them really, kind of mathematically.
1:42:26
Honestly, it makes it a little harder to read because your mind has to dive in conceptually deeper and deeper into this second argument.
1:42:33
But it's perfectly acceptable, too. And just to connect the dots to maybe something from high school,
1:42:38
this is kind of analogous to a function in math class being like f of x, where f is some function name,
1:42:43
x is some arbitrary input to that function. And when you start to put functions inside of functions
1:42:49
so that the output of one becomes the input to the next, it's like using this syntax, f of g of x and so forth.
1:42:54
If you've never seen that before, don't worry. But if you have, it's a way to connect some of these dots.
1:42:59
Any questions, though, on just this idea of now having a function that doesn't just have a side effect
1:43:05
but instead has a return value? Yeah, in back?
1:43:11
STUDENT: In our declaration of main, why did we show it as returning an integer instead of void? DAVID MALAN: In our definition of main, why did I do, what?
1:43:19
STUDENT: Why do we show it as returning an integer instead of returning as void? DAVID MALAN: Oh, a really good question that I was trying
1:43:24
to sweep under the rug for today. But in every one of our programs thus far, I have indeed said "int main(void)."
1:43:31
Technically speaking, whenever you write a program and it finishes running, it actually returns a value somewhat secretly.
1:43:37
It returns the number 0 by convention, which means all is well. And it can return any other integer if something goes wrong.
1:43:44
In fact, on your Mac, PC, or even phone, if you've ever gotten like a weird message on the screen, like something went wrong
1:43:50
and it's like a weird numeric code, like error negative 129, or something arbitrary like that, that tends to mean that some program running
1:43:57
on your Mac, PC, or phone had something go wrong with the main function. And that is the number that was returned.
1:44:03
But that's more than we want to talk about today. But we'll come back to this. But main always returns a number.
1:44:08
By default, it is 0. More on that soon. All right, so with that said, let's actually tease

## [Linux](https://youtu.be/cwtpLIWylAw?t=6255)

1:44:15
apart what it is we've been using underneath the hood here a little bit by returning to VS Code's interface itself.
1:44:21
It turns out that all this time, even though I keep alluding to macOS and Windows, which like 99% of us
1:44:27
are probably running on our laptops or desktops, there's actually other very popular operating systems in the world,
1:44:32
among which is Linux. So Linux is a very popular operating system, the thing that turns on-- the thing that boots up
1:44:39
when you first turn on a computer. And it's very commonly used for servers nowadays.
1:44:44
All of CS50's own servers run some version of Linux. Those students more comfortable sometimes
1:44:51
run Linux on their own Macs or PCs even. So Linux is a very popular operating system.
1:44:56
And it's particularly characterized by its textual interface, its command-line interface, even though it also comes with graphical ones,
1:45:03
as well. So again, this term we started today with, a graphical user interface is a thing with menus and buttons.
1:45:09
It's literally what you and I use every day on our devices, otherwise known as a GUI. But today onward, you'll get more comfortable
1:45:15
with and more practice with this terminal window down here, which represents a command-line interface, or CLI.
1:45:22
And just so you have a mental model of what's going on in the cloud here, when you access cs50.dev, you are accessing this version of VS Code
1:45:31
in the cloud, a piece of software just running in a browser. But that piece of software is automatically
1:45:36
connected to your very own personal server in the cloud, so to speak. Technically speaking, it's a "docker container."
1:45:43
But it means that you have essentially your own mini server in the cloud that only you have access to.
1:45:50
And that server or container is running an operating system called Linux. And in fact, every time I've been running a command down here,
1:45:58
whether it's code or make or ./hello or anything else, I've been running commands from here in Sanders Theatre on a server somewhere
1:46:06
in the cloud, my own Linux container or server. And you'll have the same yourself.
1:46:12
This is the thing that we have pre-configured for you by installing the compiler in so many other pieces of software
1:46:18
you'll soon see in the class. But underneath the hood, then, of Linux is a soon-to-be familiar environment
1:46:24
that allows you to run different types of commands. And those commands include things like this. And this is something you'll develop muscle memory for over time.
1:46:32
But I wanted to give you a sense of some of the most popular textual commands because we're essentially about to take away
1:46:38
muscle memory you have from a GUI world and have you type out words that represent double-clicking on things, dragging on other things,
1:46:46
and other such commands that you and I take for granted. It'll be a little painful at first in the first days or weeks,
1:46:51
but it will make you far more productive long term so that even after CS50, if you start using your programming skills in some other domain, class,
1:46:59
or real-world job, you'll just be a lot faster at the keyboard and able to do more work more quickly.
1:47:04
So with that said, let me go back to VS Code over here. I'm going to go ahead and open up my File Explorer over here.
1:47:11
And you'll see at left all of the files that I've created thus far in class and all of the programs
1:47:17
that I've compiled thus far in class. I also have this source 1 directory, which you can download from the course's website, which has all of today's code
1:47:25
pre-written in advance, so you don't have to type everything that I literally type. But all of these files are things that I've created.
1:47:31
And you'll see that in white are the C files. And grayed out are actually the binary files, the machine code
1:47:38
that I created that I was running. So you can click on any of these files in VS Code to open them.
1:47:45
For instance, here is hello.c. And voila, it opens in the text editor. But if I try to open "hello," that's not going to work,
1:47:52
because that's zeros and ones. And frankly, the computer could show me all those zeros and ones, but it's just not going to be useful.
1:47:58
And honestly, it's too easy to make one mistake and break the whole thing. So instead, VS Code says that it can't display the text, because it's binary
1:48:05
or maybe unsupported more generally. So know that you want to only click on the .c files when writing C code.
1:48:12
But let me go ahead and do something else. Suppose that I decide that, wait a minute, we're nearing the end of class.
1:48:18
And we're not done yet, but what if I want to change hello.c to goodbye.c or if I want to change meow.c to woof.c and turn it into a dog?
1:48:26
Well, let's actually do that. I could go over here and right click or Control click on the file,
1:48:32
just like on a Mac or PC. I can find the Rename option. And I can do it all via the GUI.
1:48:37
But you should get more comfortable using commands like these here. And among the commands on this list are "mv" for move, a.k.a.
1:48:45
rename. So for instance, if I want to change meow.c to be woof.c instead,
1:48:52
I literally type "mv" space, the original file name, space, and the new file name.
1:48:58
So this is very similar to what I've already been doing with the code program or the make program.
1:49:03
I not only type the name of the command but also the thing that I want to code or the thing that I want to make.
1:49:08
In this case, I type the thing that I want to move from old to new. Now, if I hit Enter in a moment, watch on the left-hand side,
1:49:15
meow.c in the GUI should automatically change even though I'm doing this all via the command-line keyboard interface.
1:49:23
And now it becomes woof.c. I mean, it's not all that exciting. But this is just to say that they are one and the same.
1:49:29
One is a GUI, one is a CLI, but it's the same exact thing. Moreover, let me go ahead and close now the GUI
1:49:35
at left, the so-called explorer. And in my terminal window alone, now I'm kind of out of my element,
1:49:41
like wait a minute, what was the file I created earlier? Well, there's other commands as well. On this list is, coincidentally, "ls," which lists
1:49:50
the file in your current folder. And as you might have gleaned here, "mv" for move, "ls" for list,
1:49:56
CS people like to be succinct, terse, and type the minimal number of keystrokes. That's why these are all abbreviated commands instead of full words.
1:50:04
But if I go back to my terminal window and type "ls," voila, there is exactly the same contents of my server but displayed textually.
1:50:13
And there's some heuristics here. In green with an asterisk is all of the programs that I made with make that are executable.
1:50:21
So the asterisks just means this is executable with dot-slash. Meanwhile, the source 1 directory, which only I have because I downloaded it
1:50:27
in advance, has a slash to indicate that it's a folder instead of a file. But all of these white files ending in .c we created together here today.
1:50:36
Now, what if I really am embarrassed by my very first program, hello.c?
1:50:42
Well, I can very destructively go and use the rm command for remove.
1:50:48
And rm hello.c is going to prompt me, a little cryptically, "remove regular file 'hello.c'?"
1:50:54
And amazingly, this rm program has code just like we wrote earlier for agree.c,
1:51:01
where I can type 'y' to delete it. I can type 'n' not to delete it. But let's delete it. Let's go ahead and hit y, enter.
1:51:08
Nothing seems to happen. But in general, that's a good thing. But if I type "ls" again, notice what is now missing?
1:51:14
And in fact, the list is a little shorter. So it's one line instead of two. "hello.c" is now gone.
1:51:20
Now, if you do that, there are not easy ways to get the file back. So don't do that unless you really want to.
1:51:26
But there are backups maintained of these files, as well. Well, what else is there, too? Well, there's all of these other commands.
1:51:32
And you'll experience them over time. Like, "cp" is copy. "mkdir" is make directory. "rmdir" is remove directory.
1:51:40
And for instance, let me just show you one folder. If I type "ls," there's that source 1 folder
1:51:45
that I claimed I downloaded in advance. If you want to see what's there, you can type "cd" for change directory, source 1, enter.
1:51:53
And voila, notice that your prompt has now changed. And let me clear the screen. Just as a visual reminder of where you are, you can see before the dollar sign
1:52:03
now the name of the folder that you're inside of. So in Mac or Windows, you'd see obviously a graphical folder. Here, you just see a little textual reminder of where you now are.
1:52:11
And if I type "ls," you'll see that I wrote a crazy number of files before class. And each of these represents different versions of the files
1:52:18
that we've been coding here in real time that I usually have printouts of just to go through things in series so you have copies online, as well.
1:52:25
So in short, all of these commands, if you've never used them before, they will soon become like muscle memory. And they do the most basic of operations.
1:52:31
But there will be other commands that we'll see over time that do even much more than that. But let's go ahead now and solve some actual problems.

## [Mario](https://youtu.be/cwtpLIWylAw?t=6759)

1:52:39
And it's no coincidence that we keep showing or alluding to Super Mario Brothers in some form, an older game
1:52:44
from the Nintendo Entertainment System, that allows you ultimately to have this two-dimensional world, where Mario moves up and down
1:52:50
and side scrolls from left to right. But you'll see we can distill even some aspects of "Mario"
1:52:55
into some fairly representative programming problems. And in fact, let me propose that we consider this screen
1:53:02
from the original Super Mario Brothers. So there's these four blocks in the sky, each with a question mark.
1:53:09
And if you click on one of these-- or if Mario jumps up underneath each of these question marks, he
1:53:15
gets like a coin or something else that pops out. Let's distill this, though, into its essence and consider in C, how can
1:53:22
we make, not a blue sky yet, not a green grassy hill, and so forth, but how can we just make four question marks in a row,
1:53:28
because I dare say that we do have the building blocks via which to do this. Well, the simplest way might be to go over here and run code of mario.c.
1:53:38
And then in mario.c, let's include some stdio.h so we have printf. Let's do int main(void), as we keep doing.
1:53:45
And inside of main, let's keep it super simple-- 1, 2, 3, 4, backslash n.
1:53:51
Doesn't get much simpler than that. This is not going to be the prettiest of games. But if I make Mario now, ./mario, I get my four question marks in the sky.
1:54:00
All right, so it's not all that interesting. But this is clearly a candidate for what type of programming feature.
1:54:07
STUDENT: Scratch. DAVID MALAN: Not to Scratch, though Scratch would make it more interesting. yeah? STUDENT: A loop.
1:54:12
DAVID MALAN: So some kind of loop, right? So print the thing out iteratively instead. So let me do that. Instead of just printing this out all at once,
1:54:19
let me go ahead and remove this and do for int i gets zero; i less than 4;
1:54:25
i++. And then in here, let me go ahead and print out just one question mark instead.
1:54:30
And now let's run this. So "make mario" to recompile it, ./mario. And does anyone not want me to hit Enter yet?
1:54:37
Why? STUDENT: Because it's gonna print a new line. DAVID MALAN: Yeah, it's going to print out a new line every time.
1:54:43
So notice it's four question marks, but there each on its own line. All right, well, let me fix this.
1:54:49
It's obviously because of the backslash n. So let me remove that. Let me rerun make mario, ./mario.
1:54:55
And it's better in one way but worse in another. So wait, but now the dollar sign is doing
1:55:01
that thing where it's on the same line, which just looks stupid if nothing else. So how can I fix that?
1:55:07
Yeah? STUDENT: [INAUDIBLE] DAVID MALAN: Yeah, so logically, we don't have that many building blocks
1:55:14
today. It's a lot of new syntax, but it's not that many new ideas. Let's just use printf to print out literally one and only
1:55:21
one of these backslash n's, but outside of the loop so it happens after all four of those have been printed.
1:55:27
All right, let me do make mario again, ./mario. And OK, now we're back in business. So sort of silly syntactical details, but if you
1:55:35
reduce the problem to its essence, it should hopefully, logically, become clear over time.
1:55:41
All right, well, how about not just something like that but vertical? Well, we've done something vertical already. And so I can imagine we could change the program
1:55:47
to very simply print out three bricks instead of four question marks. But what if we consider a two-dimensional world?
1:55:53
And later on in this game if you go underground, everything looks like this with lots of bricks. And let me propose, for the sake of discussion,
1:55:59
that this big wall here is like a 3-by-3 grid of bricks. So it's not just a single brick.
1:56:05
It's like three by three, or nine total. Now things get interesting. And let me go back to mario.c.
1:56:11
I could take the easy road out and just say, all right, well, let's printf, how about 1, 2, 3, backslash n, close quote.
1:56:21
And then, OK, let me just copy/paste. And I'm using hashes instead of the actual bricks.
1:56:26
But aesthetically, it's pretty close. Let me now go ahead and "make mario" again, ./mario.
1:56:33
And it doesn't quite look like a square. But that's just because the hashes are a little taller than they are wide. But it is correct, but not well designed.
1:56:40
So here, too, what would be better designed than just hardcoding, typing literally all of these hashes?
1:56:48
Yeah? STUDENT: We could use maybe two loops. DAVID MALAN: Interesting, two loops. And why two loops instead of one?
1:56:56
STUDENT: Oh, wait, nevermind. Well, I was going to say you could do it one for vertical and one for horizontal.
1:57:01
DAVID MALAN: OK, it's the right instinct. So one for vertical, one for horizontal. And even though these predate most of us, old-school typewriters you might know or might
1:57:08
recall that if you feed a piece of paper into it, you can print like line, then it scrolls, line, then it scrolls, line, then it scrolls.
1:57:16
This is kind of how the terminal window works, too. You can print rows and columns, but you have to print one row at a time, one row at a time, one row at a time.
1:57:24
It's not easy, but it is possible to go backwards and go up and down. But just going row by row by row is more typical.
1:57:31
So how can I do this? Well, I could use at least one and maybe even indeed two loops. And this is where we're just now composing different ideas
1:57:39
from today and even last week. So let me go ahead and say, for int i gets 0; i less than 3--
1:57:45
for a 3-by-3 grid-- i++. And now let me cheat slightly.
1:57:51
Let me print out just three of these here, and that's it. So I'm kind of cheating.
1:57:56
I'm printing out rows dynamically, but I'm still printing three columns all in one breath.
1:58:02
But let's see what happens. Make mario, ./mario, and it does work.
1:58:07
But what if you said, no, I want 4 by 4 or 5 by 5 or 6 by 6? Now I have to change the 3 to a 6, and I have to add another three hashes here.
1:58:17
Things get messy if we don't do this mathematically. So let me now do this instead. Why don't I go ahead and print out every row at a time.
1:58:26
But for each row, let me use another loop to decide, like, rat-a-tat-tat, from left to right, how many do I want to print.
1:58:33
So to do this, I could do another for loop. I could call this variable something different. j is pretty common.
1:58:39
We start at i, we go to j. If you go past k, maybe l, you're probably doing something wrong. You don't want nested, nested, nested loops, but two is OK.
1:58:46
j equals 0; j is less than 3; j++.
1:58:52
And then here, I can print out a single one of these and no new line. I don't want to screw up like I did before.
1:58:58
So I'll just do one. Let me go ahead and do make mario now, ./mario. But when I hit Enter, this is not correct yet.
1:59:06
What's it going to look like? STUDENT: A single line? DAVID MALAN: A single line of nine hashes, I think,
1:59:12
because I never used a single backslash n. So that looks wrong. So between what line number should I insert a printf of backslash n?
1:59:23
Let me look a little farther back if I can. How about over here? Yeah? STUDENT: 10 and 11.
1:59:28
DAVID MALAN: Between 10 and 11. So I'm going to go in here. I'm going to add printf, quote, unquote, "backslash n" semicolon.
1:59:34
Let me go back and recompile mario-- ./mario. And crossing fingers-- voila, perfect.
1:59:41
I printed out now a 3-by-3. Now, it's correct. It's not, if we want to be really nitpicky, maybe still not
1:59:48
the best design. Where am I perhaps repeating myself?
1:59:53
Yeah? STUDENT: [INAUDIBLE] DAVID MALAN: Yeah, I mean, it's not a huge deal. But now I have two, people would call these magic numbers.
2:00:00
"Magic" in the sense of, where did that come from? You just randomly put it in the middle of your code. And you also put the same thing here.
2:00:06
Now I have to make sure I don't screw up and make one change but not the other. So it turns out we can factor these out. I can actually do something like this, int n equals 3.
2:00:15
And then I can just change this to n and this to n, which is marginally better because now I only have to change n in one place if I want
2:00:22
to make this thing bigger or smaller. It's still going to work the same. So make mario, ./mario.
2:00:27
There's our 3-by-3. But if I want to make a 5-by-5, let me change the n to 5, rerun make mario,
2:00:35
./mario. And now it's a bigger grid, 5-by-5. But this is a little fragile.
2:00:40
And it turns out there's another trick we should introduce. It turns out that C supports what are called constants,
2:00:45
whereby if you have a variable that you want to exist because it's useful but you don't want to accidentally change it,
2:00:50
or if you're working with a partner in class or a colleague at work, you don't want your partner or colleague to accidentally change
2:00:57
that value with their own code, you can go into your code and tell C, this is actually a constant integer, a const, so to speak.
2:01:05
And this will just prevent you or someone else from doing something stupid by accidentally changing it elsewhere.
2:01:11
The code is still going to work the same, ./mario, but you won't be accidentally able to change it very easily to something
2:01:18
else. And honestly, what we've now done, too, is set ourselves up to make this more dynamic. Let me go up here, and let me add the CS50 library so that we have access
2:01:27
to get_int because now we could do something fancy like ask the get_int function for the size of this brick wall.
2:01:36
And then we can use n dynamically. So for instance, let me increase the size of my terminal, make mario,
2:01:42
./mario, size 3. Gives me a 3-by-3. ./mario size 5 gives me a 5-by-5.
2:01:50
./mario, how about 50, gives me a crazy big one, but it's all dynamic. And now I don't have to even change the code.
2:01:56
It just now works. As an aside, if you're wondering how I type so darn fast, sometimes it's just because I'm hitting the up arrow.
2:02:03
It turns out that Linux will remember, if you configure it this way, all of your previous commands. So if you hit up, up, up, I can go through the past couple of hours
2:02:12
of commands that I've typed, which is useful sometimes-- not for hours of commands but the past few-- just to save yourself some keystrokes.
2:02:18
And another trick in a terminal window is to do this. If I do ./ma and I get bored and I don't want to type out "rio,"
2:02:28
I can also just hit Tab, and it will autocomplete based on the characters that do match. So those kinds of tricks, too, will save you time over time.
2:02:36
But let's do this. It's kind of broken, arguably, if I do this. How about "cat?"
2:02:44
All right, well, that works. That prevents me from doing something stupid because get_int only accepts integers.
2:02:51
But it will accept 0, which does nothing. It will accept negative 1, which does nothing.
2:02:56
And that's not bad. It's not doing something weird. But it would be nice to catch that and force the user
2:03:01
to give us a positive integer instead so we at least see something on the screen. So let me go back into my code, and let me propose that now
2:03:08
that we have the CS50 library, why don't we do something like this? I'm going to change this. I'm going to get rid of the constant just in case
2:03:14
the user needs to type it again. And what if I do this? While n is less than 1--
2:03:20
so if it's 0, negative 1, negative 2, or whatever, let's go ahead and again ask the user for an int, and ask them for the size again.
2:03:28
And therefore, only once n is not less than 1 will this loop break out and will proceed with the rest of the code.
2:03:36
So now let me try this. Make mario, ./mario 0--
2:03:42
didn't like that. Negative 1-- didn't like that. Negative 2-- didn't like that. 3-- it did like that.
2:03:48
So using a loop now, I can ensure that the human is providing me with input that I actually want.
2:03:55
So this is correct. But I dare say 6 through 10 could be done better.
2:04:01
Why is this poorly designed instinctively?
2:04:06
Yeah? STUDENT: There's repetition. DAVID MALAN: What's the repetition, to be clear, what lines? STUDENT: Lines 6 and 9.
2:04:12
DAVID MALAN: 6 and 9. OK, so they're literally the same, and that's generally not a good thing. And maybe I could change this one to remind the user like, hey,
2:04:19
that's not a positive number. So you might want to customize the message. But just having copy/paste here for the most part is not a good thing.
2:04:26
So it turns out-- and there's just one feature of C we wanted to introduce you to today-- it turns out there's one other way that would actually help us
2:04:33
eliminate this redundancy of using get_int twice and particularly asking literally the same question-- size--
2:04:39
twice in duplicate. So I'm actually going to go into my code here, and I'm going to delete the loop as we've written it thus far.
2:04:45
And instead of using a while loop, I'm going to introduce instead something that we typically call a do while loop, which is a little bit different.
2:04:52
Indeed, we begin with the keyword "do," and then inside of the curly braces, what I'm going to do here is that thing I might want to do once and more times thereafter.
2:05:02
So for instance, I'm going to say n equals get_int quote, unquote, "size."
2:05:08
And then at the bottom of this block of code, then I'm going to use the keyword "while," as well as parentheses as always
2:05:15
for a Boolean expression. And here. I'm going to ask the question, do this while n is less than 1.
2:05:21
But there's one fix I still need to do here because notice on the current line 8, I actually haven't given n a type.
2:05:28
I haven't declared n yet. But it would not be correct to declare n here, inside of that do block.
2:05:37
But why might that be? Why would it not be a good thing to declare n inside of these curly braces?
2:05:44
Yeah, so recall that this is an issue of scope. Recall that the scope of a variable is generally
2:05:49
confined to the most recently opened curly braces in which that variable is declared. And so if I declare this variable on line 8,
2:05:56
I'm not going to be able to use it on line 10. But there is a fix, even though it might look a little strange. I'm going to go above my do block here.
2:06:04
And before I go into this loop, I'm actually going to declare n to be an integer, but semicolon, end of thought.
2:06:10
I'm not going to bother giving it a value, because I know logically I'm going to end up giving it a value anyway now on line 9.
2:06:17
And so what's different about this version of the code is that the do while loop ensures that we prompt the user for input at least
2:06:24
once. And then while that input is not what we expect, for instance less than 1, then
2:06:30
it's going to execute again, again, again. And indeed, the semantics are just that. Do the following while this Boolean expression is true.
2:06:38
So if I go ahead now and rerun make mario, compiles OK-- ./mario.
2:06:44
And now I'll go ahead and input something that's not correct, like 0. But I'm prompted again.
2:06:49
I'll input something like negative 1, and I'm prompted again. But if I go ahead and input, for instance, 10,
2:06:54
now, because that's a positive integer, I indeed get a 10-by-10 grid of bricks.
2:07:02
And there's one other thing we should introduce here, too, in C, too. C supports comments. And a couple of you have asked about this
2:07:07
if you come from other programming languages. Suppose I want to remember what it is I just did with this program.
2:07:13
Let me go in between lines 5 and 6 here and do "// prompt user for positive
2:07:20
integer." This is what's known as a comment. And it's grayed out only in the sense that the compiler is not
2:07:25
going to care about this. The computer is not going to care about this. This is a note to self, like a sticky note in the context of Scratch.
2:07:31
And it starts with "//," which essentially tells the compiler ignore this, this is for the human, not for the computer.
2:07:37
But this comment, so to speak, is a way of just reminding yourself, reminding your colleague, reminding your TF what it
2:07:43
is a few lines of code are meant to do. And now this comment might be print, and how about n-by-n grid of bricks?
2:07:53
And what's nice about comments is that theoretically you can get away with, or someone else can get away with, just reading this comment
2:08:00
and then not even have to look at the rest of the code. They can look at this comment and not have to look at the rest of the code
2:08:05
because you've described for them what it's meant to do. Yeah? STUDENT: I just had a question about the hashtag [INAUDIBLE]
2:08:13
DAVID MALAN: Sure. STUDENT: That's for [INAUDIBLE] DAVID MALAN: Correct, the hash sign in Python is a comment,
2:08:19
is not the same thing in C. In C, hash include means to include the library's
2:08:24
header files in that way. Other questions on these here tricks?
2:08:31
No? All right, so as promised, what is maybe C not actually good at?

## [Integer Overflow](https://youtu.be/cwtpLIWylAw?t=7717)

2:08:37
Well, let me propose that we consider what's actually inside of your computer. At the end of the day, whether it's a Mac, PC, iPhone, Android, phone,
2:08:45
or some other computer device, there's something that looks like this. And this is memory, otherwise known as RAM, or random access memory,
2:08:51
for reasons we'll get to in a few weeks. But this is where data is stored. This is where "hello, world" is stored.
2:08:56
This is where 1 and 2 and all of those numbers are stored. Any data in your program is stored ultimately in the computer's memory.
2:09:03
And the most important takeaway for today is that all of us only have a finite amount of memory in our devices.
2:09:10
You might have a high-end device which has a lot of memory, but it's still finite, which means you can only
2:09:15
count so high with that device. You can only store so many files with that device. There are fundamental physical limitations even though mathematically,
2:09:24
theoretically, we should be able to count toward infinity. So what are the implications for this? Well, consider this.
2:09:30
In the world of numbers, as per week 0, if you're only using three digits-- and I've grayed out the fourth one just to make the point-- if you're only
2:09:37
using three digits, we can count from 0 to 1 in decimal, to 2, to3, to 4,
2:09:43
to 5, to 6, to 7. And as soon as you count to 8, you technically, per last week,
2:09:50
need a fourth bit. But if you don't have it, the number 7 might seem
2:09:55
to be followed by what number instead? STUDENT: 0. DAVID MALAN: 0. The number overflows, so to speak, right?
2:10:03
You carry the 1. But if there's no place to put the 1, because there's no fourth light bulb, if there's no fourth transistor, if there's no fourth bit,
2:10:09
the lower bits, the zeros, are going to be mistaken for the number you and I know is 0.
2:10:15
So integer overflow is a thing in computers whereby if you don't have enough memory, if you count high enough,
2:10:21
the number will wrap around back to 0. Or sometimes it will wrap around to a negative number, depending on whether the code supports negative and positive numbers and 0
2:10:30
alike. So that has some very real world implications in integer overflow that's sort of a fundamental limitation of how
2:10:36
numbers are typically stored. Now, thankfully, we typically don't store things based on number of digits but number of bits.
2:10:42
And a bit is just a 0 or 1. And recall from last week that a common unit of measure is minimally eight bits, or a byte, but even more commonly is 32.
2:10:51
So for instance, here are 32 bits, all zeros. And if you do out the math, this is the number
2:10:56
you and I know in decimal is of course 0. But if I change all 32 zeros to ones, this is a really big number now.
2:11:03
If we're only using positive numbers, not negatives, what number roughly is this, 32 ones?
2:11:10
It's roughly 4 billion in total-- roughly 4 billion in total. Why?
2:11:16
Well, if you've got 32 bits, each can be two possible values, 0 or 1, that's 2 to the 32nd power, which is roughly--
2:11:22
I'll stipulate-- roughly 4 billion total. The problem is, what if you want to count to 4,000,000,001?
2:11:29
That's a bit of a white lie. It's not precisely that. But what if you want to count just higher than that? You'd need a 33rd bit because all of the others
2:11:36
are going to go to 0 at that point, and you might count from 1 to 2 to 3 to 4 billion back to 0, or worse if you're dealing with negative numbers,
2:11:45
too. So the fact that there are finitely many bits used in computers is a problem.
2:11:51
And negative numbers do add a complexity because this is specifically the 4 billion in question-- 4,294,968,295.
2:12:00
That is as high as you can count with 32 bits if you don't bother with negatives. But if you want negative numbers, you've got to half
2:12:07
that because you've got to save half of them for negative, half of them for positive, give or take. And so if you're supporting negative numbers, as you probably
2:12:14
should for a calculator, for Microsoft Excel, Google Spreadsheets, you can only count as high up as 2 billion roughly,
2:12:21
or negative 2 billion roughly instead. So it turns out that when you are using data types in C,
2:12:29
you have some control over how many bits are actually used. And this list is longer than we've covered today,
2:12:34
but we did talk about integers for a while. Those are, by convention nowadays, 32 bits.
2:12:40
If that's not enough, you can upgrade your variables to longs, which tend to be 64 bits instead, which isn't just twice as big as an integer,
2:12:49
it's actually 64 bits, which is exponentially more. It's an unpronounceable number, at least for me.
2:12:54
That's a crazy big number, but it's available to you. Moreover, we can see this if we actually are a little reckless with how
2:13:02
we're using code. And just so you know too, though, there are functions even in CS50's library that let you use these larger values, get long of course, will get you a long.
2:13:10
And this one's a little non-obvious, but "%li" is the format code for printf,
2:13:16
just so you know, for printing a long integer and not just an integer. So it's two characters instead of one.

## [Truncation](https://youtu.be/cwtpLIWylAw?t=8002)

2:13:22
Suppose, though, we actually want to use code involving some large numbers. It turns out that certain bad things can happen.
2:13:29
So let me go ahead and do this. I'm going to go back over to VS Code here, and I'm going to modify my calculator to do something that, at glance, should
2:13:35
be perfectly reasonable. Let me go ahead and open up calculator.c, as before. And where we left off, we had this add function.
2:13:42
And you know what? I'm going to simplify it back to its very original version. I'm going to go ahead and get rid of the add function
2:13:47
and just distill it to its essence, which is not to add any more. But let's just do division. I want to print out this time maybe x divided by y.
2:13:55
So here we go. x divided by y is a nice simple program in my calculator. Let me do make calculator again, ./calculator.
2:14:03
And let's divide something like 1 divided by 3, which should-- hm, OK, weird.
2:14:08
It gave me 0 instead of probably 0.3333333, as you might have expected for 1/3.
2:14:16
So what might the takeaway there be? Why am I seeing zero perhaps?
2:14:22
Yeah? STUDENT: If 0's the integer [INAUDIBLE],, then if you want decimals [INAUDIBLE].. DAVID MALAN: Yeah, so 0 is an integer.
2:14:29
And indeed, that's what I'm telling the thing to print. And in fact, if we go over to my little cheat sheet here of format codes,
2:14:34
I'm currently using %i. I should actually, when I do division of numbers that might have floating point
2:14:41
values, a decimal point that floats left to right, otherwise known as a real number, I want to use %f for float instead.
2:14:47
So I'm actually going to go back to my code here. And let's try this-- %f instead of %i.
2:14:52
And let me go ahead and "make calculator." Huh, all right. Well, this didn't work then.
2:14:57
"Format specifies type 'double,' but the argument has type 'int.' All right, so that, too, is not quite working.
2:15:05
So I think I actually need to make a change here further. Let me actually go ahead and do this.
2:15:10
It turns out that besides integers, there are these things called floats, and also doubles. A float uses 32 bits, and a double uses 64 bits.
2:15:19
And that doesn't necessarily mean you can count higher as much as it means you can have more numbers after the decimal point.
2:15:24
So if you want a more precise value, you throw memory at it by using a double and 64 bits instead of a float.
2:15:30
But we'll keep it simple, and let me go ahead and do this. Let me just do the math using the type of variable that I should be here.
2:15:37
Let me do not int, but float z equals x divided by y.
2:15:43
And now let me go ahead and print out the value of z. Strictly speaking, I don't need the variable. But I'm trying to be pedantic and actually use a float explicitly
2:15:50
this time so we see a real number. All right, let me go ahead and do make calculator, ./calculator.
2:15:57
1 divided by 3 equals-- damn, now it's just showing me more zeros, which clearly isn't the case.
2:16:04
Well, this is because of an issue that we'll generally call truncation. So truncation is just a term of art that means if you take an integer
2:16:12
and you divide it by an integer, even if you get a fractional value, the fraction just gets thrown away because you're only
2:16:18
doing integer-based math. So if there's anything after the decimal point, it just gets truncated, literally discarded.
2:16:25
So what should 1 divided by 3 be? Obviously, 0.33333333-- ad nauseum.
2:16:31
Fortunately, you throw away everything after the decimal point, which leaves you still with just 0.
2:16:37
And even though I'm seeing more zeros, that's because we threw away all of the 3's. That is just what happens when you use integers and do
2:16:44
any kind of division like that. But there is a solution. We can actually convert, or cast, integers to floating point values.

## [Type Casting](https://youtu.be/cwtpLIWylAw?t=8213)

2:16:53
So we can tell C, I know this is an integer now. But go ahead and treat it as though it has a decimal point, even
2:16:59
if it's .0 At the end of the number. So I can go into this, and I can use parentheses and literally write
2:17:06
"float" in parentheses. And over here for y, I can literally use parentheses and convert y to a float.
2:17:12
The term of art here is type casting. You're converting one type to another effectively, or technically treating
2:17:19
one type as though it's another even if it doesn't necessarily have a mathematical impact.
2:17:24
But what it means now is that z will be defined by dividing one float by another.
2:17:31
So truncation will not now happen. So let me do make calculator, ./calculator.
2:17:36
And now 1 divided by 3, there it is. Now the math is actually correct. But my God, we had to jump through hoops just to get this to work.
2:17:45
So to be clear, the two issues we-- well, the issue we encountered was truncation. If you divide an int by an int, you will get an int no matter
2:17:52
what it should be mathematically. But if you instead type cast the values, the variables to a floating point
2:17:59
value, or a double for that matter, then a float divided by a float will give you a float and preserve all of those 3's.
2:18:06
But here's another catch, or at least a limitation potentially with computers. What if I go ahead here and do--

## [Floating-Point Imprecision](https://youtu.be/cwtpLIWylAw?t=8294)

2:18:14
let me do this. Let me show you one trick here, even though the syntax is a bit weird. Instead of printing out %f alone, let me print out % dot,
2:18:25
maybe 5f So this is weird syntax. And it's only specific to printf.
2:18:32
"%.5f" means 'show me five decimal places specifically.' So if I do make calculator, ./calculator, 1, 3, voila,
2:18:40
I get five decimal places. If I want six, let's do this. I'll change the code to 6.
2:18:45
Make calculator, ./calculator, 1, 3, and now I get six 3's instead.
2:18:52
All right, well, wouldn't it be nice to be even more precise? Let's give me 20 significant digits after the decimal point.
2:18:59
So make calculator, ./calculator, 1 divided by 3, and-- woo.
2:19:04
So your middle school teacher seems to have lied to you at this point.
2:19:09
1 divided by 3 is apparently not 0.33333 with a line over it,
2:19:14
or just infinite number of 3's. OK, that's not quite the right conclusion, though.
2:19:19
Oops. Why might I be seeing these weird numbers instead
2:19:24
of just lots of 3's, intuitively?
2:19:31
Why this rounding error? Yeah? STUDENT: The computer just has a [? limited ?] [? memory. ?] So there's [INAUDIBLE]
2:19:37
DAVID MALAN: Exactly. The computer only has limited memory, finite memory. So it just can't represent every possible number in the universe
2:19:44
because we know from grade school there are infinitely many of those numbers. So what you're essentially seeing is the closest it can actually get.
2:19:52
It's rounding to the nearest floating point value, if you will. And it also relates to how the numbers themselves are represented
2:19:58
in memory underneath the hood. I can do a little better, though. Let me zoom out. And let me upgrade, so to speak, from 32 bits to 64 bits and use
2:20:06
doubles instead. I can still use %f. You don't use %d for double. Let me do make calculator again, ./calculator, 1, 3.
2:20:14
I get more 3's but still some rounding. It's more precise, but it's not 100% accurate,
2:20:21
because that's just not going to be possible in terms of the computer's memory. So this is a whole other issue known as floating point imprecision, which
2:20:29
is another type of limitation. We saw integer overflow, if integers can only
2:20:34
count so high before you run out of bits and things wrap around. Floating point imprecision means that you can't possibly
2:20:40
represent the infinite number of real numbers that exist in the universe if you only have a finite amount of memory.
2:20:46
You would need an infinite number of bits, it would seem. So these are two issues that actually fundamentally
2:20:51
can influence the correctness not only of your code but code in the real world. And case in point, back in my day-- I graduated in 1999-- and a lot of the world

## [Y2K](https://youtu.be/cwtpLIWylAw?t=8459)

2:20:59
thought the world was going to end around then because around the time the years rolled over from 1999 to 2000,
2:21:06
there was a lot of old software still running in the world. And in fact, that old software, reasonably so,
2:21:12
only used two digits to represent years. Why? Memory was very expensive early on. And if you could use half as much memory to store a year, that was a win.
2:21:20
That saved you money. That saved you memory. The problem though, of course, is that a lot of old software from the '70s and prior was still running in 1999.
2:21:29
And unless companies or individuals updated that software, 1999 might be mistaken for the year 1900 instead of 2000,
2:21:39
because all of the code just assumed that, of course, we're talking about the 1900s. This code is not going to be running 50 years later,
2:21:45
but it was still in that case. So people had to scramble, and they essentially had to solve this by using more digits, so upgrading from two to four.
2:21:53
Nowadays, and really since the '70s too, we've used 32-bit integers to keep track of time,
2:21:59
specifically keeping track of the number of seconds using an integer from January 1, 1970, the so-called epoch whereby
2:22:08
that's just an arbitrary date early on where we just started counting time. So all of the clocks in your Macs, PCs, and phones pretty much
2:22:14
just have a single integer that gets updated every second, but it's just keeping track not of absolute time per se,
2:22:20
but how many seconds have passed since January 1, 1970, just because that's the date humans chose.
2:22:25
The problem is you can only count as high as 4 billion, give or take, with 32 bits and actually 2 billion, give or take,
2:22:31
if you support negative numbers, as well. And the problem with that is that we're about to trip over the same issue
2:22:37
again in not too long from now. This is the 2038 problem because in the year 2038, on that date, mark my words,
2:22:45
things could break again. Why? Because that 32-bit value is going to accidentally wrap
2:22:50
around back to a 0 or a negative value. So we're going to go through the whole darn process again.
2:22:56
Now, thankfully the solution, as you might expect, is kind of just to kick the can even further down the road
2:23:01
and use 64 bits, which I think will get us another 290 million years of runway.
2:23:07
It's more than twice. So it's not our problem anymore at that point. But that's fundamentally going to be the solution.
2:23:12
But it will still be finite. So we're just deferring to our descendants
2:23:18
to actually deal with the issue some millions of years from now if these things are still running. So if that does happen, here's the specific date
2:23:26
that, in 2038, all of a sudden our clocks will still think because a negative number will get subtracted to the current epoch time.
2:23:32
So it will think we're back in 1901. So this has had some fun and very real world implications.

## [Video Games](https://youtu.be/cwtpLIWylAw?t=8618)

2:23:38
So for instance, this is the game Pac-Man, which you might have played. It kind of came out around my day, back in time.
2:23:44
And if you get to the 256th level, this unfortunately is what happens because they didn't really
2:23:50
expect that players would spend all this much time playing Pac-Man apparently. And they didn't really have a condition saying,
2:23:56
you win if you get to the 255th or 266th level. And so what happens here essentially is that the whole screen gets very
2:24:02
garbled because there's an integer in the original Pac-Man that counts to 256, but that's too big, so it wraps back around to 0.
2:24:11
And it doesn't know when to stop printing fruits on the screen, as in this case, to collect.
2:24:16
Another example of this is actually from the original Donkey Kong game, which looks something like this in my day, too, whereby in Donkey Kong,
2:24:24
there was this mathematical formula, whereby the number of seconds you have to solve the game was a function of 10 times
2:24:31
your current level number plus the number 4. That dictated how many seconds you get. So of course, the higher the level, you get more and more time
2:24:39
as the level climbs. Unfortunately, once you hit level 22, the math ends up being 10 times
2:24:47
22 plus 4, which gives you the number 260. And they, too, were using 8-bit values, a single byte
2:24:55
to represent numbers, which means 260 is bigger than 256.
2:25:00
And the way that math worked out was, well, 260 minus 256, if it wraps back around, gave people four seconds to solve level
2:25:08
22, which is just impossible. Like, Mario can't even get up a couple of levels or so from where he actually was.
2:25:15
So that, too, was sort of a well-known bug, as well, since that works out to be there.
2:25:20
Lastly, and this one is all the more real, in 2015, Boeing 787 was documented as having not a hardware bug but a software bug

## [Boeing](https://youtu.be/cwtpLIWylAw?t=8730)

2:25:30
in the following sense. "A model 787 airplane that has been powered continuously for 248 days
2:25:37
can lose all of its power due to the control unit simultaneously going
2:25:42
into failsafe mode. This condition was caused by a software counter that will overflow
2:25:48
after 248 days of continuous power. Boeing at the time was in the process of developing a CPU software upgrade that
2:25:55
will remedy the unsafe condition." And people did the math. It turns out that Boeing was probably using an integer that was 32 bits.
2:26:02
And they were keeping track of time not in seconds but hundredths of seconds, because if you do out the math, after a 32-bit value has reached 4 billion--
2:26:12
or 2 billion one hundredths of a second, the number wraps around back to 0,
2:26:18
or negative 2 billion. And the implications was literally the plane's power would stop. And if you can believe it, if you grew up with Windows, macOS, or whatnot,
2:26:26
anyone want to conjecture what the solution was until Boeing updated their software?
2:26:33
STUDENT: Turn it off, turn it back on. DAVID MALAN: Turn the plane off, and turn it back on because that has the effect of resetting its memory and therefore
2:26:41
all of its variables back to 0. So this is ultimately to say as you dive into problem set 1, your first in C,
2:26:47
you, too, will make quite a few mistakes when it comes to correctness. You, too, will encounter opportunities for better design and better style.
2:26:54
In the real world, there are very much these issues. So even if you struggle, know that for better or for worse, you're in very good company.
2:27:00
But some three months from now, you will be in much better shape because this was week 1, and this is CS50.
2:27:06
[APPLAUSE]
2:27:11
[INTRIGUING MUSIC]
