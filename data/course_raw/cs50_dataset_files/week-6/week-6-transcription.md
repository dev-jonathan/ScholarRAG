---
link: https://youtu.be/EHi0RDZ31VA
related_files:
  - week-6-notes.md
  - problemset/week-6-cash.md
  - problemset/week-6-credit.md
  - problemset/week-6-dna.md
  - problemset/week-6-hello.md
  - problemset/week-6-mario-less.md
  - problemset/week-6-mario-more.md
  - problemset/week-6-problemset.md
  - problemset/week-6-readability.md
title: "Lecture 6: Week 6 - Python"
type: transcription
week/lecture: "6"
---

# [Lecture 6: Week 6 - Python](https://youtu.be/EHi0RDZ31VA)

TABLE OF CONTENTS:

0:00 - Introduction
1:01 - Python
7:24 - Speller
13:45 - Filter
17:34 - Face Recognition
20:56 - Functions
33:25 - Types
34:48 - Calculator
44:52 - Conditionals
48:09 - Compare
57:22 - Object-Oriented Programming
1:03:00 - Loops
1:13:58 - Meow
1:21:25 - Truncation
1:25:56 - Exceptions
1:33:23 - Mario
1:39:48 - Lists
1:49:18 - Dictionaries
2:00:01 - sys
2:04:04 - pip

## [Introduction](https://youtu.be/EHi0RDZ31VA?t=0)

0:00
[MUSIC PLAYING]

## [Python](https://youtu.be/EHi0RDZ31VA?t=61)

1:01
DAVID MALAN: All right. This is CS50, and this is finally week 6. And this is that week we promised, wherein we finally
1:08
transition from C, this lower-level older language via which we explored
1:13
memory and how really computers work underneath the hood, to what's now called Python, which is a more modern, higher-level language,
1:19
whereby we're still going to be able to solve the same types of problems. But it's going to suddenly start to get much, much easier because what
1:25
Python offers, as do higher-level languages more generally, are what we might describe as abstractions
1:31
over the very low-level ideas that you've been implementing in sections and problem sets and so much more.
1:37
But recall from week 0, where we began. This was our simplest of programs that just printed "hello, world." Things escalated quickly thereafter in week 1,
1:44
where, suddenly, we had all of this new syntax. But the idea was still the same of just printing out "hello, world."
1:50
Well, as of today, a lot of that distraction, a lot of the visual distraction, goes away entirely
1:56
such that what used to be this in C will now be quite simply this in Python.
2:02
And that's a bit of a head fake in that we're going to see some other fancier features of Python. But you'll find that Python's popularity in large part
2:09
derives from just how relatively readable it is and also, as we'll ultimately see, just how exciting
2:16
and filled the ecosystem among Python programmers. That is to say there's a lot more libraries.
2:22
There's a lot more problems that people have solved in Python that you can now incorporate into your own programs in order to stand on their shoulders and get real work done faster.
2:30
But recall, though, from C that we had a few steps via which to actually compile that kind of code. So we got into the habit of make to make our program called hello.
2:38
And then we've been in the habit of running it with ./hello, the effect of which, of course, is to feed all of the zeros and ones that
2:45
compose the hello program into the computer's memory and, in turn, the CPU. We revealed that what make is really doing
2:52
is something a little more specific, namely running clang, the C language compiler specifically, with some automatic command line arguments so as
3:00
to output the name that you want, link in the library that you want, and so forth. But with Python, wonderfully, we're going to get rid of those steps,
3:08
too, and quite simply run it as follows. Henceforth, our programs will no longer be in files ending in .c,
3:15
suffice it to say. Our files starting today are going to start ending with .py, which is an indication to the computer-- macOS, Windows,
3:22
or Linux or anything else-- that this is a Python program. But unlike C, wherein we've been in the habit of compiling our code
3:30
and running it, compiling our code and running it, any time you make a change, with Python, those two steps get reduced into one, such
3:37
that any time you make a change and want to rerun your code, you don't explicitly compile it anymore. You instead just run a program called python, similar in spirit to clang.
3:46
But whereas clang is a compiler, python will see as not only the name of the language, but the name of a program.
3:53
And the type of that program is that of interpreter. An interpreter is a program that reads your code top to bottom, left to right,
3:59
and really does what it says without having this intermediate step of first having to compile it in zeros and ones.
4:06
So with that said, let me do this. Let me flip over here to VS Code. And within VS Code, let me write my first Python program.
4:13
And as always, I can create a new file with the code command within VS Code. I'm going to create this file called hello.py, for instance.
4:20
And quite, quite simply, I'm going to go ahead and simply do print("Hello, world").
4:27
And if I go down to my terminal window, instead of compiling this, I'm instead going to interpret this program by running python, space,
4:34
and the name of the file I want Python to interpret, hitting Enter. And voila. Now you see "hello, world."
4:40
But let me go ahead and compare this at left. Let me also go ahead and bring back briefly a file called hello.c.
4:47
And I'm going to do this as we did in the very first day of C, where I included standard io.h.
4:53
I did int main(void). I did inside of there printf(), quote unquote, "hello, world," backslash n,
4:59
close quote, semicolon. And let me go ahead in VS Code. And if you drag your file over to the right or the left,
5:05
you can actually split-screen things if of help. And what I've done here is-- and let me hide my terminal window--
5:10
I've now compared these two files left and right. So here's hello.c from, say, week 1. Here's hello.py from week 6 now.
5:18
And the obvious-- the differences are perhaps obvious. But there's still some-- there's a subtlety, at least one subtlety.
5:23
Beyond getting rid of lots of syntax, what did I apparently omit from my Python version,
5:29
even though it didn't appear to behave in any buggy way? Yeah?
5:34
Sorry? Say one more time? AUDIENCE: The library. DAVID MALAN: The library. So I didn't have to include any kind of library like the standard I/O library.
5:41
print(), apparently, in Python, just works. AUDIENCE: main() [INAUDIBLE] DAVID MALAN: So I don't need to use main() anymore.
5:47
So this main() function, to be clear, was required in C because that's what told the compiler what the main part of your program is.
5:54
And you can't just start writing code otherwise. What else do you see? AUDIENCE: No semicolon. DAVID MALAN: So there's no more semicolon, wonderfully enough,
6:00
at the end of this line, even though there was here. And things are getting a little more subtle now. What else?
6:06
So the new line. So recall that in printf(), if you wanted to move the cursor to the next line when you're done printing, you had to do it yourself.
6:13
So it seems as though Python-- because when I interpreted this program a moment ago, the cursor did move to the next line on its own.
6:21
They sort of reversed the default behavior. So those are just some of the salient differences here. One, you don't have to explicitly include standard library, so to speak,
6:29
like standard I/O. You don't need to define a main() function anymore. You can just start writing your code.
6:35
You don't need these parentheses, these curly braces. printf() is now called print(), it would seem.
6:40
And you don't need the backslash n. Now, there is one thing that's also a little looser,
6:46
even though I didn't do it here. Even though in C, it was required to use double quotes any times you--
6:51
any time you want to use a string, a.k.a., char\*, in Python, as with a lot of languages nowadays, you can actually get away with just using
7:00
single quotes so long as you are consistent. Generally speaking, some people like this
7:05
because you don't have to hold Shift, and therefore, you just hit one key instead of two. So there's an argument in terms of efficiency.
7:11
However, if you want to use an apostrophe in your string, then you have to escape it. And so in general, stylistically, I'll use double quotes in this way.
7:19
But things are getting a little looser now with Python, whereby that's not actually a requirement.

## [Speller](https://youtu.be/EHi0RDZ31VA?t=444)

7:24
But what's especially exciting with Python, and, really, a lot of higher-level languages, is just how much real work
7:30
you can get done relatively quickly. So you've just spent quite a bit of time, daresay, implementing your spell checker and implementing
7:37
your own dictionary of sorts. Well, let me propose that maybe we should have asked you
7:42
to do that in Python instead of C. Why? Well, let me go ahead and do this. Let me close these two tabs and reopen my terminal window.
7:50
Let me go into a directory called speller that I downloaded in advance for class. And if I type ls in here, you'll notice that it's
7:57
very similar to what you spent time on with problem set 5. But the file extensions are different.
8:02
There's a dictionary.py instead of dictionary.c. There's a speller.py instead of a speller.c. And there's the exact same directories, dictionaries, and texts
8:10
that we gave you for problem set 5. So let me just stipulate that I spent time implementing speller.c in Python.
8:18
And so I gave it a name of speller.py. But I didn't go about really implementing dictionary.py yet.
8:25
And so why don't we go ahead and actually implement dictionary.py together by doing this?
8:30
Let me clear my terminal, do code dictionary.py. And let me propose that we implement, ultimately, four functions.
8:38
And what are those functions going to be? Well, they're going to be the check() function, the load() function, the size() function, and the unload() function.
8:45
But recall that in problem set 5, you implemented your own hash table. And so while there isn't a hash table data type in Python,
8:54
I'm going to go ahead and do this. I'm going to create a variable, a global variable in dictionary.py, called words, and I'm going to make it a set.
9:01
In the mathematical sense, a set is a collection of things that won't contain duplicates. Any duplicates will be filtered out.
9:07
So I'm going to now, after that, creating that one global variable, I'm going to create a function called check(), just as you did.
9:13
And check() takes as input a word. And if I want to check if a word is in that set of words,
9:19
I can simply do word.lower in words.
9:25
And that's it. Let me now define another function called load(), which, recall, took an argument, which was the name of the dictionary you want to load
9:32
into memory. Inside of my load() function, I'm now going to do this. I'm going to say with open(dictionary) as a variable called file.
9:39
And in there, I'm going to go ahead and update the set of words to be the updated version of whatever's in this file as a result of reading
9:47
it and then splitting its lines, whereby this file has a big, long column of words, each of which is separated by a new line,
9:54
splitline is going to split all of those into one big collection. And then I'm just going to go ahead and return True.
10:00
I'm now going to go ahead and define a size function, just as you did. But in Python, I'm going to go ahead and just go ahead and return the length
10:06
of that set of words, where length, or len(), is a function itself in Python.
10:12
And I'm going to do one last function. It turns out that in Python, even though, for this program,
10:17
I'm going to go and implement a function called unload, there's not actually anything to unload in Python, because Python will manage your memory for you.
10:25
malloc() is gone. free() is gone. Pointers are gone. It handles all of that, seemingly magically for now, for you.
10:33
So here then is, I claim, what you could have done with problem set 5 if implementing it in Python instead.
10:39
Let me go ahead and open my terminal window. Let me increase its size. Let me run Python of speller.py, which is the name of the actual program, not
10:46
the dictionary per se that I implemented. Let's run it on a file called holmes.txt because that was a particularly big file.
10:53
And if I hit Enter now, we'll see, hopefully, the same output that you saw in C flying across the screen.
10:59
And eventually, we should see that same summary at the bottom as to how many words seem to be misspelled,
11:04
how many words were in the dictionary, and, ultimately, how fast this whole process was.
11:11
Now, the total amount of time required was 1.93 seconds, which was actually longer than it seemed to take.
11:16
That's because we're doing this in the cloud, and it was taking some amount of time to send all of the text to my screen. But the code was only taking 1.93 seconds total on the actual server.
11:26
And hopefully, these same kinds of numbers line up with your own, the difference being what I did not have to implement for this spell checker is
11:33
your own hash table, is your own dictionary, literally, beyond what I've done using Python here with some of these built-in features.
11:41
So why, you see, why not always use Python, assuming that you prefer the idea of being
11:48
able to whip up within seconds the entirety of problem set 5?
11:53
How might you choose now between languages? And I apologize if you're harboring resentment
11:59
that this wasn't a week earlier. Why Python or why C?
12:05
Any instincts? Any thoughts? There's hopefully a reason?
12:11
Yeah, over here? Yeah? AUDIENCE: I always thought that Python was a little slower than C [INAUDIBLE]
12:20
DAVID MALAN: Ah, really good conjecture. So you always thought that Python was slower than C and takes up more space than C. Odds are that's, in fact, correct.
12:27
So even though, ultimately, this 1.93 seconds is still pretty darn fast, odds are it's a little slower than the C version would have been.
12:35
It's possible, too, that my version in Python actually does take up more RAM or memory underneath the hood.
12:41
Why? Well, because Python itself is managing memory for you. And it doesn't necessarily know a priori how much memory you're going to need.
12:49
You, the programmer might, and you, the programmer writing in C, allocated presumably exactly as much memory
12:55
as you might have needed last week with problem set 5. But Python's got to maybe do its best effort for you
13:01
and try to manage memory for you, and there's going to be some overhead. The fact that I have so many fewer lines of code,
13:08
the fact that these lines of code solve problem set 5 for me, means that Python, or whoever invented Python, they wrote lines of code
13:17
to of give me this functionality. And so if you think of Python as a middleman of sorts, it's doing more work for me.
13:23
It's doing more of the heavy lift. So it might take me a bit more time. But, my gosh, look how much time it has saved in terms
13:30
of writing this code more quickly. And arguably, this code is even more readable, or at least will be after today, week 6, once you have an eye for the syntax
13:38
and features of Python itself. So beyond that, it turns out you can do other things pretty easily as well.

## [Filter](https://youtu.be/EHi0RDZ31VA?t=825)

13:45
Let me go back into my terminal window. Let me close this dictionary.py. Let me go into a folder called filter, in which
13:52
I have this same bridge that we've seen in the past across the river there. So here's a bridge.
13:57
This is the original version of this particular photograph. Suppose I actually want to write a program that blurs this.
14:02
Well, you might recall from problem set 4 you could write that same code in C by manipulating all of the red, the green, the blue pixels that
14:10
are ultimately composing that file. But let me go ahead and propose this instead. Let me create a file called blur.py.
14:17
And in this file, let me go ahead and just go ahead and import a library.
14:23
So from the Python image library, PIL, let me go ahead and import something called Image, capital I, and Image Filter, capital
14:31
I, capital F. So I'm going to do before = Image.open("bridge.bmp").
14:38
Then let me go ahead and create another variable called after and set that equal to before.filter, and then, in parentheses,
14:46
ImageFilter, spelled as before, dot BoxBlur, and then we'll give it a value of 10.
14:51
How much do I want to blur it, for instance? After that, I'm going to literally call after.save, and let's
14:57
save it as a file called out.bmp. And that's it. I propose that this is how you can now write code in Python to blur an image,
15:05
much like you might have for problem set 4. Now let me go ahead in my terminal window and run python of blur.py.
15:12
When I hit Enter, those four lines of code will run. It seems to have happened quite quickly. Let me go ahead and open now out.bmp.
15:19
And whereas the previous image looked like this a moment ago, let me go ahead and open out.bmp.
15:26
And hopefully, you can indeed see that it blurred it for me using that same code. And if we want things to escalate a little more quickly,
15:32
let me go ahead and do this instead. Let me close blur.bmp. Let me go ahead and open a file called edges.py.
15:39
And maybe, in edges.py, we can use this same library. So from the Python Image Library, import Image and import ImageFilter.
15:47
Let me go ahead and create another variable called before, set it equal to Image.open("bridge.bmp"),
15:53
just like before. Let me create another variable called after, set that equal to before.filter(ImageFilter.FIND_EDGES),
16:03
which comes with this library automatically, and lastly, the same thing-- save this as a file called out.bmp.
16:10
So if you struggled perhaps with this one previously, whereby you wrote for the more comfortable version of problem
16:16
set 4, edge detection, so to speak, well, you might have then created a file that given an input like this,
16:23
the original bridge.bmp, this new version, out.bmp, with just four
16:28
lines of code, now looks like this. So, again, if this is a little frustrating that we had to do all of this in C, that was exactly
16:36
the point to motivate that you now understand nonetheless what's going on underneath the hood. But with Python, you can express the solutions
16:43
to problems all the more efficiently, all the more readily. And just one last one, too-- it's very common nowadays
16:50
in the world of photography and social media and the like to do face detection, for better or for worse. And it turns out that face detection, even
16:56
if you want to integrate it into your own application, is something that lots of other people have integrated into their applications
17:02
as well. So Python, to my point earlier of having this very rich ecosystem of libraries
17:07
that other people wrote, you can literally run a command like pip install face_recognition if you want to add support to your code space,
17:19
or to your programming and environment more generally, for the notion of face recognition. In fact, this is going to automatically install
17:26
from some server elsewhere a library that someone else wrote called face_recognition. And with this library, you can do something like this.

## [Face Recognition](https://youtu.be/EHi0RDZ31VA?t=1054)

17:34
Let me go into a directory that I came with in advance. Let me go ahead and ls in there, and you'll see four files--
17:40
detect.py and recognize.py, which are going to detect faces and then recognize specific faces, respectively, and then two files
17:48
I brought from a popular TV show, for instance. So if I open office.jpg, here is one of the early cast photos from the hit TV
17:55
series The Office. And here is a photograph of someone specific from the show, Toby.
18:03
Now, this is, of course, Toby's face. But what is it that makes Toby's face a face?
18:10
More generally, if I open up office.jpg, and I asked you, the human, to identify all of the faces in this picture,
18:17
it wouldn't be that hard with a marker to sort of circle all of the faces. But how? Why? How do you as humans detect faces, might you think?
18:26
Yeah? AUDIENCE: You have eyes, nose. DAVID MALAN: Features, yeah, like eyes, nose, generally in a similar orientation, even though we all
18:32
have different faces, ultimately. But there's a pattern to the shapes that you're seeing on the screen.
18:38
Well, it turns out this face_recognition library has been trained, perhaps via artificial intelligence over time,
18:43
to recognize faces, but any number of different faces, perhaps among these folks here. So if I go back into my terminal window here,
18:51
let me go ahead and run, say, python of detect.py, which I wrote
18:56
in advance, which uses that library. And what that program is going to do-- it's going to think, do some thinking.
19:03
It's just found some face. And let me go ahead now and open a file it just created called detected.jpg, which I didn't have in my folder a moment ago.
19:12
But when I open this here file, you'll now see all of the faces based on this library's detection thereof.
19:19
But suppose that we're looking for a very specific face among them, maybe Toby's. Well, maybe if we write a program that doesn't just
19:25
take as input the office.jpg, but a second input, toby.jpg, maybe this library, and code more generally,
19:32
can distinguish Toby's face from Jim's, from Pam's, from everyone else in the show, just based on this one piece of training data, so to speak.
19:41
Well let me instead run python of recognize.py and hit Enter.
19:47
It's going to do some thinking, some thinking, some thinking. And it is going to output now a file called
19:52
recognized.jpg, which should show me his face, ideally, specifically.
19:59
And so what has it done? Well, with sort of a green marker, there is Toby among all of these faces.
20:05
That's maybe a dozen or so lines of code, but it's built on top of this ecosystem of libraries.
20:10
And this is, again, just one of the reasons why Python is so popular. Undoubtedly, some number of years from now, Python will be out,
20:16
and something else will be back in. But that's indeed among the goals of CS50, too, is not to teach you C, not to teach you Python, not in a couple of weeks
20:23
to teach you JavaScript and other languages, too, but to teach you how to program. And indeed, all of the ideas we have explored and will now
20:30
explore more today, you'll see recurring for languages in the years to come.
20:36
Any questions before we now dive into how it is this code is working and why I type the things that I did before we forge ahead?
20:45
Any questions along these lines? Anything at all?
20:50
No? All right. So how does Python itself work? Well, let's do a quick review as we did when

## [Functions](https://youtu.be/EHi0RDZ31VA?t=1256)

20:56
we transitioned from Scratch to C, this time, though, from Scratch, say, to Python. So in Python, as with many languages, there
21:02
are these things called functions-- the actions and verbs that actually get things done. So here on the left, recall from week 0, was the simplest of functions.
21:09
We played with, first, the say block, which just literally has the cat say something on the screen. We've seen in C, for instance, the equivalent line of code is arguably
21:18
this here, with printf(), with the parentheses, the quotation marks, the backslash n, the semicolon. In Python now, it's going to indeed be a little simpler than that.
21:27
But the idea is the same as it was back in week 0. Libraries-- so we've seen already in C, and now we've
21:33
already seen in Python that these things exist, too. In the world of C, recall that besides the standard ones, like standard io.h,
21:40
that header file, we could very quickly introduce cs50.h, which was like your entry point, the header
21:45
file for the CS50 library, which gave you a bunch of functions as well. Well, we're going to give you a similar library
21:51
for at least the next week or two, training wheels for Python specifically, that, again, will take off so that you can stand on your own,
21:57
even with CS50 behind you. But the syntax for using a library in Python is a little different.
22:03
You don't include a .h file. You just import, instead, the name of the library.
22:09
All right. What does that actually mean? Well, if there are specific functions in that library you want to use, in Python, you can be more precise.
22:16
You don't just have to say, give me the whole library. For efficiency purposes, you can say, let me import the get_string() function
22:23
from the CS50 library. So you have finer-grained control in Python, which can actually speed things
22:29
up if you're not loading things unnecessarily into memory, if all you want is, say, one feature therein.
22:35
So here, for instance, in Scratch, was an example of how we might use not only
22:40
a built-in function, like the say block, or, in C, in the printf(), but how we might similarly now do the same but achieve this in Python.
22:50
So how might we do this? Well, in Python, or rather, in C, this code looks a little something like this.
22:56
Back in week 1, we declared a variable of type string, even though later we revealed that to be char\*.
23:01
I gave this a variable name of answer for parity with Scratch. Then we use CS50's own get_string() function and asked, for instance,
23:08
the same question as in the white oval here. And then, using this placeholder syntax, these format codes,
23:14
which was printf()-specific, we could plug in that answer to this premade string where the %s is.
23:21
And we saw %i and %f and a bunch of others as well. So this is sort of how, in C, you approximate
23:27
the idea of concatenating two things together, joining two things, just as we did here in Scratch.
23:33
So in Python, it turns out it's not only going to be a little easier, but there's going to be even more ways to do this.
23:39
And so even what might seem today like a lot of different syntax, it really is just different ways, stylistically,
23:45
to achieve the same goals. And over time, as you get more comfortable with this, you too will develop your own style, or, if working for a company
23:51
or working with a team, you might collectively decide which conventions you want to use.
23:56
But here, for instance, is one way you could implement this same idea in Scratch but in Python instead.
24:04
So notice I'm going to still use a variable called answer. I'm going to use CS50's function called get_string(). I'm still going to use, quote unquote, "What's your name?"
24:11
But down here is where we see the most difference. It's, again, not called printf() in Python. It's now called just print().
24:18
And what might you infer the plus operator is doing here? It's not addition, obviously, in a mathematical sense.
24:26
But those of you who have perhaps programmed before, what does the plus represent in this context? AUDIENCE: It's joining the two strings together.
24:32
DAVID MALAN: It's indeed joining the two strings together. So this is indeed concatenating the thing on the left with the thing on the right.
24:38
So you don't use the placeholder in this particular scenario. You can instead, a little more simply, just use plus.
24:44
But you want your grammar to line up. So I still have "hello," and then close quote
24:50
because I want to form a full phrase. Notice, too, there's also one other slightly more subtle difference on the first line.
24:58
Besides the fact that we don't have a semicolon, what else is different? AUDIENCE: You don't declare the type of the variable.
25:03
DAVID MALAN: I didn't declare the type of the variable. So Python still has strings, as we'll see. But you don't have to tell the interpreter what type of variable
25:12
it is. And this is going to save us some keystrokes, and it's just going to be a little more user-friendly over time. Meanwhile, you can do this also a little bit differently if you prefer.
25:21
You can instead trust that the print() function in Python can actually do even more for you automatically.
25:27
The print() function in Python can take multiple arguments separated by commas in the usual way.
25:33
And by default, Python is going to insert for you a single space between its first argument and its second argument.
25:39
So notice what I've done here is my first argument is, quote unquote, "hello," with a comma but no space.
25:45
Then, outside of the quotes, I'm putting a comma because that just means, here comes my second argument. And then I put the same variable as before.
25:52
And I'm just going to let Python figure out that it should, by default, per its documentation, can join these two variables, putting a single space in between them.
26:02
You can do this yet another way. And this way looks a little weirder, but this is actually probably the most common way nowadays in Python
26:09
is to use what's called a format string, or f string, for short. And this looks weird to me still.
26:16
It looks weird. But if you prefix a string in Python with an f, literally, you can then use curly braces inside of that string in Python.
26:26
And Python will not print out literally a curly brace and a closed curly brace. It will instead interpolate whatever is inside of those curly braces.
26:34
That is to say if answer is a variable that has some value, like "David" or something like that, saying f before the first quotation mark,
26:42
and then using these curly braces therein, is going to do the exact same thing of creating a string that says "Hello,"
26:48
comma, space, "David." So it's going to plug in the value for you. So you can think of this as %s but without that second step of having
26:56
to keep track of what you want to plug back in for %s. Instead of %s, you literally put in curly braces,
27:02
what do you want to put right there? You format the string yourself. So given all of those ways, how might we actually
27:10
go about implementing this or using this ourselves? Well, let me propose that we do this here.
27:18
Let me propose that I go back to VS Code. Let me go ahead and open up hello.py again.
27:24
And as before, instead of just printing out something like, quote unquote, "hello, world," let me actually print out
27:31
something a little more interesting. So let me go ahead and, from the CS50 library,
27:36
import the function called get_string(). Then let me go ahead and create a variable called answer.
27:42
Let me set that equal to the return value of get_string() with, as an argument, quote unquote, "What's your name?"
27:50
And then no semicolon at the end of that line, but on the next line, frankly here, I can pick any one of those potential solutions.
27:57
So let me start with the first. So "hello, " + answer.
28:03
And now, if I go down to my terminal window and run python of hello.py, I'm prompted for my name.
28:08
I can type in D-A-V-I-D, and voila, that there then works. Or I can tweak this a little bit. I can trust that Python will concatenate its first and second argument for me.
28:19
But this isn't quite right. Let me go ahead and rerun python of hello.py, hit Enter, and type
28:24
in "David." It's going to be ever-so-slightly buggy, sort of grammatically or visually, if you will.
28:29
What did I do wrong here? Yeah. So I left the space in there, even though I'm getting one for free from
28:35
print(). So that's an easy solution here. But let's do it one other way after running this to be sure--
28:41
D-A-V-I-D. And OK, now it looks like I intended. Well, let's go ahead and use that placeholder syntax.
28:47
So let's just pass in one bigger string as our argument, do "hello," and then, in curly braces, [? answer ?],, like this.
28:55
Well, let me go down to my terminal window and clear it. Let me run python of hello.py and enter, type in D-A-V-I-D, and voila.
29:03
OK, I made a mistake. What did I do wrong here, minor though it seems to be? Yeah? AUDIENCE: [INAUDIBLE]
29:09
DAVID MALAN: So the stupid little f that you have to put before the string to tell Python that this is a special string-- it's a format string, or f
29:16
string-- that it should additionally format for you. So if I rerun this after adding that f, I can do python of hello.py.
29:24
What's your name? David. And now it looks the way I might intend. But it turns out in Python, you don't actually need to use get_string().
29:33
In C, recall that we introduced that because it's actually pretty annoying in C to get strings, in particular to get strings safely.
29:40
Recall those short examples we did with scanf not too long ago. And scanf kind of scans what the user types at the keyboard
29:47
and loads it into memory. But the fundamental danger with scanf when it comes to strings was what?
29:53
Why was it dangerous to use scanf to get strings from a user?
30:00
Why? Yeah? AUDIENCE: What if they give you a really long string you don't have space for? DAVID MALAN: Exactly. What if they give you a really long string
30:07
that you didn't allocate space for? Because you're not going to know as the programmer in advance how long of a string the human is going to type in.
30:13
So you might under-- you might undercut it and therefore have too much memory, or too many
30:19
characters being put into that memory, thereby giving you some kind of buffer overflow, which might crash the computer or, minimally,
30:26
your program. So it turns out in C, get_string() was especially useful.
30:31
In Python, it's not really that useful. All it does is use a function that does come with Python called input().
30:39
And, in fact, the input() function in Python, for all intents and purposes, is the same as the get_string() function that we give to you.
30:47
But just to ease the transition from C to Python, we implemented a Python version of get_string() nonetheless.
30:52
But this is to say if I go to VS Code here, and I just change get_string() to input(), and, in fact,
30:59
I even get rid of the CS50 library at the top, this too should work fine. If I rerun python of hello.py, type in my name, David, and voila,
31:07
I have that now working as well. All right. Questions about this use of get_string() or input() or any of our syntax thus
31:19
far? All right. Well, what about variables?
31:24
We've used variables already, and we already identified the fact that you don't have to specify the type of your variables
31:29
proactively, even though, clearly, Python supports strings thus far, well, in Python, here's how you might declare
31:37
a variable that not necessarily is assigned like a string, but maybe an integer instead. So in Scratch, here's how you could create
31:43
a variable called counter if you want to count things and set it equal to 0. In C, what we would have done is this--
31:50
int counter = 0; that's the exact same thing as in Scratch. But in Python, as you might imagine, we can chip away at this and type
31:59
out this same idea little more easily. One, we don't need to say int anymore. Two, we don't need the semicolon anymore.
32:06
And so you just do what you intend. If you want a variable, just write it out. If you want to assign it a value, you use the equals sign.
32:12
If you want to specify that value, you put it on the right. And just as in C, this is not the equality operator.
32:17
It's the assignment operator from right to left. Recall that in Scratch, if you wanted to increment a variable by 1 or any value,
32:25
you could use this puzzle piece here. Well, in C, you could do syntax like this, which, again, is not equality.
32:32
It's saying add 1 to counter and then assign it back to the counter variable.
32:38
In Python, you can do exactly the same thing minus the semicolon. So you don't need to use the semicolon here.
32:44
But you might recall that in C, there was some syntactic sugar for this idea because it was pretty popular. And so you could shorten this in C, as you can in Python,
32:53
to actually just this. += 1 will add to the counter variable whatever that
32:59
value is. But it's not all steps forward. You might be in the habit of using ++ or --.
33:07
Sorry, those are not available in Python. Why? It's because the designers of Python decided that you
33:12
don't need them because this is-- gets the job done anyway. But there's a question down here in front, unless it was about the same.
33:19
All right. So that's one feature we're taking away. But it's not such a big deal to do += in this case.

## [Types](https://youtu.be/EHi0RDZ31VA?t=2005)

33:25
Well, what about the actual types involved here beyond actually being able to define variables?
33:31
Well, recall that in the world of C, we had at least these data types, those that came with the language in particular.
33:39
And we played with quite a few of these over time. In Python, we're going to take a bunch of those away.
33:45
In Python, you're only going to have access to a bool, true or false,
33:51
a float, which is a real number with a decimal point, typically, an int, or an integer, and a string, now known as str.
33:58
So Python here sort of cuts some corners, feels like it's too long to write out strings. So a string in Python is called str, S-T-R, but it's the exact same idea.
34:08
Notice, though, that missing from this now, in particular, are double and long, which, recall, actually used more bits in order
34:16
to store information. We'll see that that might not necessarily be a bad thing. In fact, Python just simplifies the world
34:22
into two different types of variables but gets out of the business of you having to decide, do you want a small int or a large int or something along those lines?
34:30
Well, let me go ahead and do this. Let me switch back over to VS Code here. And why don't we actually try to play around with some calculations using
34:37
these data types and more? Let me go ahead and propose that we implement, like we did way back in week 1, a simple calculator.

## [Calculator](https://youtu.be/EHi0RDZ31VA?t=2088)

34:48
So let me do this-- code of calculator.c. So I'm indeed going to do this in C first, just so
34:55
that we have a similar example at hand. So I'm going to include standard io.h here at the top.
35:02
I'm going to go ahead and do int main(void). Inside of main(), I'm going to go ahead and declare a variable called x and set
35:10
that equal to get_int(), and I'm going to prompt the user for that value x. But if I'm using get_int(), recall that actually is from the CS50 library.
35:18
So in C, I'm going to need cs50.h, still, for this example. But back in week 1, I then did something else.
35:24
I then said, give me another variable called y, set that equal to get_int(), and set that equal to that-- pass in that prompt there.
35:31
And then, lastly, let's just do something super simple like add two numbers together. So in C, I'll use printf().
35:37
I'm going to go ahead and do %i backslash n as a placeholder. And then I'm just going to plug in x + y.
35:44
So all of that was in C. So it was a decent number of lines of code to accomplish that task, only three of which
35:50
are really the logical part of my program. These are the three that we're really interested in. So let me instead now do this, code of calculator.py,
35:59
which is going to give me a new tab. Let me just drag it over to the right so I can view these side by side.
36:05
And in calculator.py, let's do this. From the CS50 library, import the get_int() function,
36:11
which is also available. Then let's go ahead and create a variable called x and set it equal to the return value of get_int(), passing in the same prompt--
36:20
no semicolon, no mention of int. Let's then create a second variable y, set it equal to get_int(), prompt the user for y, as before, no int, explicitly, no semicolon.
36:29
And now let's just go ahead and print out x + y. So it turns out that the print() function in Python is further flexible,
36:37
that you don't need these format strings. If you want to print out an integer, just pass it an integer,
36:42
even if that integer is the sum of two other integers. So it just sort of works as you might expect.
36:48
So let me go down into my terminal here. Let me run python of calculator.py. And when I hit Enter, I'm prompted for x.
36:54
Let's do 1. I'm prompted for y. Let's do 2. And voila, I should see 3 as the result--
37:02
so no actual surprises there. But let me go ahead and, you know what?
37:07
Let's take away this training wheel, right? We don't want to keep introducing CS50-specific things. So suppose we didn't give you get_int().
37:14
Well, it turns out that get_int() is still doing a bit of help for you, even though get_string() was kind of a throwaway and we could replace
37:21
get_string() with input(). So let's try this same idea. Let's go ahead and prompt the user for input for both x and y using
37:28
the input() function in Python instead of get_int() from CS50. Let me go ahead and rerun Python of calculator.py and hit Enter.
37:37
So far, so good. Let me type in 1. Let me type in 2. And what answer should we see?
37:43
Hopefully still 3, but nope. Now the answer is 12, or is it?
37:51
Why am I seeing 12 and not 3? AUDIENCE: [INAUDIBLE] two strings. DAVID MALAN: Yeah. So it's actually concatenating what seem to be two strings.
37:59
So if we actually read the documentation for the input() function, it's behaving exactly as it's supposed to.
38:04
It is getting input from the user from their keyboard. But anything you type at the keyboard is effectively a string.
38:09
Even if some of the symbols happen to look like or actually be decimal numbers, they're still going to come to you as strings.
38:15
And so x is a string, a.k.a., str, y is a str, and we've already seen that if you use plus in between two strings, or strs,
38:24
you're going to get concatenation, not addition. So you're not seeing 12 as much as you're seeing 1 2, not 12.
38:32
So how can we fix this? Well, in C, we had this technique where we could cast one thing to another
38:38
by just putting int in parentheses, for instance. In Python, things are a little higher-level such that you can't quite get away with just casting
38:46
one thing to another because a string, recall, is not
38:51
the same thing as a char. A string has zero or more characters. A char always has one.
38:56
And in C, there was a perfect mapping between single characters and single numbers in decimal, like 65 for capital A.
39:05
But in Python, we can do something somewhat similar and not so much cast but convert this input() to an int and convert this input() to an int.
39:15
So just like in C, you can nest functions. You can call one function and pass its output as the input to another function.
39:21
And this now will convert x and y to integers. And so now plus is going to behave as you should-- as you would expect.
39:28
Let me rerun python of calculator.py, type in 1, type in 2, and now we're back to seeing 3 as the result. If this is a little unclear,
39:37
this nesting, let me do this one other way. Instead of just passing input() output into int,
39:43
I could also more pedantically do this. x should actually equal int(x), y should actually equal int(y).
39:52
This would be the exact same effect. It's just two extra lines where it's not really necessary.
39:57
But that would work fine. If you don't like that approach, we could even do it inline. We could actually convert x to an int and y to an int.
40:05
Why? Well, int, I-N-T, in the context of Python itself, is a function. And it takes as input here a string, or str,
40:13
and returns to you the numeric, the integral equivalent-- so similar idea,
40:19
but it's actually a function. So all of the syntax that I've been tinkering with here is sort of fundamentally the same as it would be in C. But in this case,
40:27
we're not casting but converting more specifically. Well, let me go back to these data types.
40:33
These are some of the data types that are available to us in Python. It turns out there's a bunch of others as well
40:39
that we'll start to dabble with today. You can get a range of values, a list of values, which is going to be like an array, but better, tuples, which
40:46
are kind of like x, comma, y, often, combinations of values that don't change. dict for dictionary-- it turns out that in Python, you get dictionaries.
40:57
You get hash tables for free. They're built into the language. And we already saw that Python also gives you a data type known as a set, which is just
41:04
a collection of values that gives you-- gets rid of any duplicates for you. And as we saw briefly in speller-- and we'll play more with these ideas soon--
41:11
it's going to actually be pretty darn easy to get values or check for values in those there data types.
41:17
So that in C, we were able to get input easily, we had all of these functions. In the CS50 library for Python, we're only going to give you these instead.
41:26
They're going to be the same name. So it's still get_string(), not get_str, because we wanted the functions to remain named the same.
41:31
But get_float(), get_int(), get_string() all exist. But, again, get_string() is not all that useful.
41:37
But get_int() and get_float() actually are. Why?
41:42
Well, let me go back to VS Code here. And let me go back to the second version of this program,
41:47
whereby I proactively converted each of these return values to integers.
41:54
So recall that this is the solution to the 1 2 problem. And to be clear, if I run python of calculator.py and input 1 and 2,
42:03
I get back now 3 as expected. But what I'm not showing you is that there's still potentially a bug here.
42:09
Let me run python of calculator.py, and let me just not cooperate. Instead of typing what looks like a number,
42:15
let me actually type something that's clearly a string, like cat. And unfortunately, we're going to see the first of our errors,
42:22
the first of our runtime errors. And this, like in C, is going to look cryptic at first. But this is generally known as a traceback, where
42:28
it's going to trace back for you everything your program just did, even though this one's relatively short. And you'll see that calculator.py, line 1--
42:36
I didn't even get very far before there's an error. And then, with all of these carrot symbols here, this is a problem.
42:42
Why? invalid literal for int() function with base 10, quote unquote, 'cat.'
42:47
Again, just like in C, It's very arcane. It's hard to understand this the first time you read it. But what it's trying to tell me is that cat is not an integer.
42:55
And therefore, the int() function cannot convert it to an integer for you. We're going to leave this problem alone for now.
43:01
But this is why, again, get_int()'s looking kind of good, and get_float()'s looking kind of good because those functions from
43:07
CS50's library will deal with these kinds of problems for you. Now, just so you've seen it, there's another way
43:14
to import functions from these things. If you were to use, for instance, in a program, get_float(), get_int(),
43:20
and get_string(), you don't need to do three separate lines like this. You can actually separate them a little more cleanly with commas.
43:27
And, in fact, if I go back to a version of this program here in VS Code whereby
43:33
I actually do use the get_int() function-- so let me actually get rid of all this and use get_int() as before.
43:39
Let me get rid of all this and use get_int() as before. Previously, the way I did this was by saying from cs50 import get_int()
43:48
if you know in advance what function you want to use. But suppose, for whatever reason, you already have your own function named
43:54
get_int(), and therefore, it would collide with CS50's own, you can avoid that issue, too, by just using that first statement we saw
44:01
earlier. Just import the library itself. Don't specify explicitly which functions you're going to use.
44:06
But thereafter-- and you could not do this in C-- you could specify cs50.get_int(), cs50.get_int(),
44:14
in order to go into the library, access its get_int() function, and therefore, it doesn't matter if you or any number of other people wrote
44:22
an identically-named function called get_int(). You're using here, clearly, CS50's own.
44:28
So this is, again, just more ways to achieve the same solution
44:34
but with different syntax. All right. Any questions about any of this syntax or features thus far?
44:44
No? All right. Well, how about maybe another example here, whereby we revisit conditionals, which was the way of implementing

## [Conditionals](https://youtu.be/EHi0RDZ31VA?t=2692)

44:52
do this thing or this thing, sort of proverbial forks in the road. In Scratch, recall, we might use building blocks like these
44:58
to just check, is x less than y, and if so, say so. In C, this code looked like this.
45:04
And notice that we had parentheses around the x and the y. We had curly braces, even though I did disclaim that for single lines of code,
45:11
you can actually omit the curly braces. But stylistically, we always include them in CS50's code. But you have the backslash n and the semicolon.
45:18
In a moment, you're about to see the Python equivalent of this, which is almost the same.
45:23
It's just a little nicer. This, then, is the Python equivalent thereof. So what's different at a glance here, just to be clear?
45:32
What's different? Yeah? AUDIENCE: [INAUDIBLE] DAVID MALAN: So the conditional is not in parentheses.
45:38
You can use parentheses, especially if, logically, you need to group things. But if you don't need them, don't use them is Python's mindset.
45:45
What else has changed here? Yeah? AUDIENCE: No curly brackets. DAVID MALAN: No curly braces, yeah, so no curly braces around this.
45:51
And even though it's one line of code, you just don't use curly braces at all. Why? Because in Python, indentation is actually really, really important.
46:00
And we know from office hours and problem sets occasionally that if you forgot to run style50 or you didn't manually format your code beautifully,
46:07
C is not actually going to care if everything is aligned on the left. If you never once hit the Tab character or the space bar,
46:14
C, or specifically, clang, isn't really going to care. But your teaching fellow, your TA, is going to care, or your colleague in the real world, because your code's just a mess
46:22
and hard to read. Python, though-- because you are not the only ones in the world that might have
46:29
bad habits when it comes to style-- Python as a language decided, that's it.
46:34
Everyone has to indent in order for their code to even work. So the convention as Python is to use for spaces--
46:40
so 1, 2, 3, 4, or hit Tab and let it automatically convert to the same, and use a colon instead of the curly braces,
46:47
for instance, to make clear what is associated with this particular conditional.
46:53
We can omit, though, the backslash n per before. We can omit the semicolon. But this is essentially the Python version thereof.
46:59
Here in C-- in Scratch, if you wanted to do an if-else, like we did back in week 0, in C, It's very similar to the if, except you add
47:08
the else clause and write out an additional printf() like this. In Python, we can tighten this up.
47:13
if x less than y, colon, that's exactly the same. First line's the same. All we're doing now is adding an else and the second print line here.
47:21
How about in Scratch? If we had a three-way fork in the road-- if, else, if, else. In C, it looked pretty much like that-- if, else, if, else.
47:29
In Python, we can tighten this up. And this is not a typo. What jumps out at you as weird but you got to just get used to it?
47:38
Yeah? AUDIENCE: elif. DAVID MALAN: elif. And honestly, years later, I still can't remember if it's elif or elsif
47:44
because other languages actually do E-L-S-I-F. and now I probably now biased all of you to now questioning this.
47:52
But it's elif in Python. E-L-I-F is not a typo. It's in the spirit of let's just save ourselves some keystrokes.
47:58
So elif is identical to elsif, but it's a little tighter to type it this way.
48:03
All right. So if we now have this ability to express conditionals,

## [Compare](https://youtu.be/EHi0RDZ31VA?t=2889)

48:09
what can we actually do with them? Well, let me go over to VS Code here. And let me propose that we revisit maybe another program from before,
48:18
where we just compare two integers in particular. So I'm in VS Code. Let me open up a file called, say, compare.py.
48:25
And in compare.py, we'll use the CS50 library just so we don't risk any errors, like if the human doesn't type an integer.
48:32
So we're going to go ahead and say from cs50 import get_int(). And in compare.py, let's get two variables-- x = get_int(),
48:39
and prompt the user for x. So "What's x?" To be a bit more verbose, y = get+int("What's y? ")
48:47
And then let's go ahead and just compare these two values. So if x is less than y, then go ahead and print out with print("x is less
48:55
than y"), close quote, elif x is greater than y,
49:01
go ahead and print out "x is greater than y," close quote, else,
49:07
go ahead and print out "x is equal to y"-- so the exact same program,
49:12
but I've added to the mix getting a value of x and y. Let me run python of compare.py.
49:18
Enter. Let's type in 1 for x, 2 for y. x is less than y. Let's run it once more.
49:24
x is 2. y is 1. x is greater than y. And just for good measure, let's run it a third time. x is 1.
49:30
y is 1. x is equal to y. So the code, daresay, works exactly as you would expect, as you would hope.
49:37
But it turns out that in the world of Python, we're actually going to get some other behavior that might actually
49:44
have been what you expected weeks ago, even though C did not behave this way. In the world of Python and in the world of strings, a.k.a.
49:52
strs, strings actually behave more like you would expect. So by that I mean this.
49:58
Let me actually go back to this code. And instead of using integers, let me go ahead and get rid of--
50:05
I could do get_string(), but we said that that's not really necessary. So let's just go ahead and change this to input().
50:11
And actually, you know what? Let's just start fresh. Let's give myself a string called s and use the input() function and ask
50:16
the user for s. Let's use another variable called t just because it comes after s and use
50:21
the input() function to get t. Then let's compare if s and t are the same. Now, a couple of weeks ago, this backfired.
50:28
And if I tried to compare two strings for equality, it did not work. But if I do if s == t, print("Same"), else,
50:38
let's go ahead and print("Different"). I daresay, in Python, I think this is going to work as you would expect.
50:44
So python of compare.py, let's type in cat and cat. And indeed those are the same.
50:49
Let me run it again and type in cat and dog, respectively. And those are now different.
50:55
But in C, we always got "Different," "Different," "Different,"
51:00
even if I typed the exact same word, be it cat or dog or high or anything else. Why, in C, were s and t always different a couple of weeks ago?
51:08
Yeah? AUDIENCE: Because it was comparing the value of the char* with the memory address. DAVID MALAN: Exactly.
51:14
In C, string is the same thing as char*, which is a memory address. And because we had called get_string() twice,
51:20
even if the human typed the same things, that was two different chunks of memory at two different addresses.
51:25
So those two char\*s were just naturally always different, even if the characters at those addresses were the same.
51:31
Python is meant to be higher-level. It's meant to be a little more intuitive. It's meant to be more accessible to folks who might not necessarily
51:38
know or want to understand those lower-level details. So in Python, ==, even for strings just works the way that you might expect.
51:48
But in Python, we can do some other things, too, even more easily than we could in C. Let me go back to VS Code here.
51:55
Let me close compare.py. And let's reimplement a program from C called agree, which allowed us to prompt the user for a yes/no question, like,
52:02
do you agree to these terms and conditions or something like that. So let's do code of agree.py.
52:08
And with agree.py, let me go ahead and-- actually, let's go ahead and do this.
52:14
Let me also open up a file that I came with in advance. And this is called agree.c.
52:20
And this is what we did some weeks ago when we wanted to check whether or not the user had agreed to something or not.
52:26
So we used the CS50 library, the standard I/O library, we had a main() function, we used get_char(). And then we used == a lot, and we used the two vertical bars,
52:35
which meant logical or. Is this thing true or is this thing true? And if so, printf() "Agreed" or "Not agreed."
52:42
So this worked. And this is relatively simple. That's the right way to do it in C. But notice
52:47
it was a little verbose because we wanted to handle uppercase and lowercase, uppercase and lowercase.
52:53
So that did start to bloat the code, admittedly. So let's try to do the same thing in Python and see what we can do the same or different-- no pun intended.
53:02
So let me do this. In agree.py, why don't we try to get input from the user as before?
53:08
And I will use-- I could use get_string(), but I'll go ahead and use input(). So s = input("Do you agree? ") in double quotes.
53:17
And then let's go ahead and check if s == "Y"--
53:24
and it's not vertical bar now, it's actually more readable, more English-like-- or s == "y," then go ahead and print out "Agreed" as before,
53:34
elsif-- see, I did it there-- elif s == "N" or s == "n,"
53:43
go ahead and print out "Not agreed." So it's almost the same as the C version, except that I'm using,
53:51
literally, O-R instead of two vertical bars. So let's run this-- so python of agree.py. Enter.
53:57
Do I agree? Yes, for little y. Let's do it again. python of agree.py, capital Y. Yes.
54:02
That works there. And if I do it again with lowercase n, and if I do it with capital N, this program, too, seems to work.
54:10
But what if I do this? Let me rerun python of agree.py. Let me type in Yes.
54:16
OK, it just ignores me. Let me run it again. Let me type in no. It just ignores me. Let me try it very emphatically, YES in all caps.
54:22
It just ignores me. So there's some explosion of possibilities that ideally we should handle, right?
54:27
This is bad user interface design if I have-- the user has to type Y or N, even if yes and no in English are perfectly reasonable and logical, too.
54:37
So how could we handle that? Well, it turns out in Python, we can use something like an array,
54:43
technically called a list, to maybe check a bunch of things at once. So let me do this.
54:49
Let me instead say not equality, but let me use the in keyword in Python
54:54
and check if it's in a collection of possible values. Let me say if s is in--
54:59
and here comes, in square brackets, just like-- in square brackets, quote unquote, "y", quote unquote, "yes,"
55:09
then we can go ahead and print out "Agreed," elif s in this list of values, lowercase "n" or lowercase "no,"
55:20
then we can print out, for instance, "Not agreed." But this is a bit of a step backwards because now
55:25
I'm only handling lowercase. So let me go into the mix and maybe add capital "Y"--
55:32
wait a minute, then maybe capital "YES," then maybe "YeS," also-- I mean, weird, but we should probably support this and "YEs."
55:41
I mean, there's a lot of combinations. So this is not going to end well. Or it's just going to bloat my code unnecessarily.
55:47
And eventually, for longer words, I'm surely going to miss capitalization. So logically, whether it's in Python or C or any language,
55:54
what might be a better design for this problem of handling Y and Yes,
56:00
but who cares about the capitalization? AUDIENCE: Don't use capitals or [INAUDIBLE]
56:07
DAVID MALAN: So OK, so don't use capitals. You could only support lowercase. That's fine.
56:12
That's kind of a copout, right? Because now the program's usability is worse. AUDIENCE: Convert it. DAVID MALAN: Oh, we could convert it to lowercase, yeah.
56:19
Though I did hear you say we could just check the first letter, I bet that's going to get us into trouble. And we probably don't want to allow any word starting
56:26
with Y, any word starting with N, just because it logically-- especially you want the lawyers happy, presumably.
56:33
You should probably get an explicit semantically correct word like Y or N or yes or no. But, yeah, we can actually go about converting this to something
56:41
maybe smaller. But how do we go about converting this? In C, that alone was going to be pretty darn annoying because we'd have to use
56:48
the tolower() function on every character and compare it for equality.
56:53
It just feels like that's a bit of work. But in Python, you're going to get more functionality for free.
56:58
So there might very well be a function, like in C, called tolower() or toupper(). But the weird thing about C, perhaps in retrospect,
57:06
is that those functions just kind of worked on the honor system. tolower() and toupper() just trusted that you would pass them an input,
57:15
an argument, that is, in fact, a char. In Python, and in a lot of other higher-level languages,

## [Object-Oriented Programming](https://youtu.be/EHi0RDZ31VA?t=3442)

57:22
they introduced this notion of Object-Oriented Programming, which is commonly described as OOP.
57:28
And in the world of Object-Oriented Programming, your values can not only-- your variables,
57:34
for instance, and your data types can not only have values. They can also have functionality built into them.
57:40
So if you have a data type like a string, frankly, it just makes good sense that strings should be uppercaseable, lowercaseable, capitalizable,
57:48
and any number of other operations on strings. So in the world of object-oriented programming functions,
57:54
like toupper() and tolower() and isupper() and islower() are not just in some random library that you can use.
57:59
They're built into the strings themselves. And what this means is that in the world of strings in Python,
58:06
here, for instance, is the URL of the documentation for all of the functions, otherwise known as methods, that come with strings.
58:13
So you don't go check for a C-type library like we did in C. You check the actual data type, the documentation, therefore, and you
58:20
will see in Python's own documentation what functions, a.k.a. methods, come with strings.
58:26
So a method is just a function. But it's a function that comes with some data type, like a string.
58:32
So let me propose that we do this. In the world of object-oriented programming,
58:38
we can come back to agree.py. And we can actually improve the program by getting
58:44
rid of this crazy long list, which I wasn't even done with, and just canonicalize everything as lowercase.
58:50
So let's just check for lowercase y and lowercase yes, lowercase n, lowercase no, and that's it.
58:55
But to your suggestion, let's force everything that the user types into lowercase, not because we want
59:01
to permanently change their input-- we can throw the value away thereafter-- but because we want to more easily logically compare it
59:09
for membership in this list of values. So one way to do this would be to literally do s = s.lower().
59:18
So here's the difference. In the world of C, we would have done this-- tolower and pass in the value s.
59:25
But in the world of Python, and, in general, object-oriented programming-- Java is another language that does this--
59:32
if s is a string, a.k.a. str, therefore, s is actually what's known in Python as an object.
59:38
An object can not only have values or attributes inside of them, but also functionality built in.
59:43
And just like in C, with a struct, if you want to go inside of something, you use the dot operator.
59:49
And inside of this string, I claim, is a function, a.k.a., method,
59:54
called lower(). Long story short, the only takeaway, if this is a bit abstract, is that instead of doing lower and then, in parentheses,
1:00:01
s, in the world of object-oriented programming, you kind of flip that and you do s dot name of the method, and then open paren and close paren if you
1:00:08
don't need to pass in any arguments. So this actually achieves the same. So let me go ahead and rerun agree.py, and let me type in lowercase y.
1:00:17
That works. Let me run it again, type in lowercase yes. That works let me run it again, type in capital Y. That works.
1:00:24
Let me type in capital YES, all capital-- all uppercase YES. That too works. Let me try no.
1:00:31
Let me try no in lowercase. And all of these permutations now actually work
1:00:37
because I'm forcing it to lowercase. But even more interestingly, in Python, if you're sort of becoming a languages
1:00:42
person, if you have a variable s that is being set the return value of input()
1:00:48
function, and then you're immediately going about changing it to lowercase, you can also chain method calls together in something like Python by doing this.
1:00:57
We can get rid of this line altogether, and then I can just do this, .lower. And so whatever the return value of input() is, it's going to be a str.
1:01:05
Whatever the human types in, you can then immediately force it to lowercase and then assign the whole value to this variable
1:01:12
called s. You don't actually have to wait around and do it on a separate line altogether.
1:01:20
Questions, then, on any of this?
1:01:26
No? All right. Let me do one other that's reminiscent of something we did in the past. Let me go into VS Code here, clear my terminal.
1:01:32
Let's close both the C and the Python version of agree. And let's create a program called uppercase.py, whose purpose in life
1:01:39
is to actually uppercase a whole string. In the world of C, we had to do this character by character by character.
1:01:45
And that's fine. I'm going to go ahead and do it similarly here in Python, whereby I want to convert it character by character.
1:01:53
But unfortunately, before I can do that, I actually need some way of looping in Python, which we actually haven't seen yet.
1:02:00
So we need one more set of building blocks. And, in fact, if we were to consult the Python documentation, we'd see this and much more.
1:02:06
So, in fact, here's a list of all of the functions that come with Python. And it's actually not that long of a list,
1:02:11
because so much of the functionality of Python is built into data types, like strings and integers and floats and more.
1:02:18
Here is the canonical source of truth for Python documentation. So as opposed to using the CS50 manual for C,
1:02:25
which is meant to be a simplified version of publicly available documentation, we'll generally, for Python,
1:02:32
point you to the official docs. I will disclaim they're not really written for introductory students.
1:02:39
And they'll generally leave some detail off and use arcane language. But at this point in the term, even if it might be a little frustrating at first, it's
1:02:45
good to see documentation in the real world because that's what you're going to have after the course. And so you'll get used to it through practice over time.
1:02:52
But with loops, let's introduce one other feature that we can compare to Scratch. Here, for instance, in Scratch, is how we might have repeated something three

## [Loops](https://youtu.be/EHi0RDZ31VA?t=3780)

1:03:00
times, like meowing on the screen. In C, there were a bunch of ways to do this. And the clunkiest was maybe to do it with a while loop
1:03:07
where we declare a variable called i, set it equal to 0, and then, iteratively, increment i again and again until it exceeds--
1:03:14
until it equals 3, each time printing out "meow." In Python, we can do this in a few different ways as well.
1:03:22
The nearest translation of C into Python is perhaps this. It's almost the same, and logically, it really is the same,
1:03:29
but you don't specify int, and you don't have a semicolon. You don't have curly braces. But you do have a colon.
1:03:35
You don't use printf(). You use print(). And you can't use i++, but you still can use i += 1.
1:03:42
So logically, exactly the same idea as in C-- It's just a little tighter. I mean, it's a little easier to read, even though it's very mechanical,
1:03:49
if you will. You're defining all of these. You're defining this variable and changing it incrementally. Well, recall that in C, we could also use a for loop, which at first glance
1:03:58
was probably more cryptic than a while loop. But odds are by now, you're more comfortable or more in the habit of using loops-- same exact idea.
1:04:04
In Python, though, we might do it like this. We've seen how, in square brackets, you can have lists of values, like y, yes,
1:04:13
and so forth. Well, let's just do the same thing with numbers. So if you want Python to do something three times, give it
1:04:19
a list of three values, like 0, 1, 2, and then print out "hello, world"
1:04:24
that many times. Now, this is correct, but it's bad design.
1:04:29
Even if you've never seen Python before, extrapolate mentally from this. Why is this probably not the right way or the best way to do this looping?
1:04:38
AUDIENCE: Because if you wanted to do it more than, like, three times, you have to [INAUDIBLE].. DAVID MALAN: Yeah. If you want to do it four times, five times, 50 times, 100 times,
1:04:46
I mean, surely, there's a better way than enumerating all of these values. And there is. In fact, in Python, there's a function called range() that actually returns
1:04:55
to you very efficiently a range of values. And by default, it hands you the number 0 and then 1 and then 2.
1:05:02
And if you want more than that, you just change the argument to range() to be how many values do you want.
1:05:07
So if you passed in range of 50, you would get back 0 through 49, which effectively allows you to do something 50 times in total.
1:05:15
So this is perhaps the most Pythonic way, so to speak. And this is actually a term of art. Pythonic isn't necessarily the only way to do something.
1:05:23
But it's the way to do something based on consensus in the Python community. So it's pretty common to do this.
1:05:30
But there's some curiosity here. Notice I'm declaring a variable i, but I'm never actually using it.
1:05:36
In fact, I don't even increment it because that's sort of happening automatically. Well, what's really happening here is automatically in Python,
1:05:43
on every iteration of this loop, Python is assigning i to the next value.
1:05:50
So initially, i is 0. Then it goes through an iteration. Then i is 1. Then i is 2.
1:05:55
And then that's it if you only asked for three values. But there's this other technique in Python, just so you know,
1:06:00
whereby if you're the programmer, and you know you don't actually care about the name of this variable, you
1:06:06
can actually change it to an underscore, which has no functional effect per se. It just signals to the reader, your colleague, your teaching fellow,
1:06:14
that it's a variable, and you need it in order to achieve a for loop. But you don't care about the name of the variable
1:06:19
because you're not going to use it explicitly anywhere. So that might be an even more Pythonic way of doing things.
1:06:25
But if you're more comfortable seeing the i and using the variable more explicitly, that's fine. Underscore does not mean anything special.
1:06:32
It's just a valid character for a variable name. So this is convention, nothing more technical than that.
1:06:38
What about a forever loop in Scratch, like literally meow forever. Well, over here, we can just use in C, while(true) printf() "meow,"
1:06:46
again and again and again. In Python, it's almost the same.
1:06:51
You still get rid of the curly braces. You add the colon. You get rid of the semicolon. But there's a subtlety.
1:06:57
What else is different here? Yeah? So True is uppercase. Why?
1:07:03
Who knows? The world decided that in Python, True is capitalized and False is capitalized.
1:07:08
In many other languages, daresay most, they are not. It's just a difference that you have to keep in mind or remember.
1:07:15
All right. So now that we have looping constructs, let me go back to my code here.
1:07:20
And recall that I proposed that we re-implement a program like uppercase, force an entire string to uppercase. And in C, we would have done this with a for loop, iterating from left to right.
1:07:29
But what's nice in Python frankly, is that it's a lot easier to loop in Python than it is in C because you can loop over
1:07:37
anything that is iterable. A string is iterable in the sense that you can iterate over it
1:07:43
from left to right. So what do I mean by this? Well, let me go ahead and, in uppercase.py, let's first prompt the user for a variable called before and set that
1:07:51
equal to the return value of input(), giving them a prompt of "Before," colon.
1:07:57
Then let's go ahead, as we did weeks ago, and print out just the word "After," just to make clear to the user what is actually going to be printed.
1:08:08
Then let me go ahead and specify the following loop-- for-- and previously you saw me use i, but because I'm dealing with
1:08:16
characters, I'm actually going to do this instead-- for c in before, colon, print out c.upper.
1:08:24
And that's it. Now, this is a little flawed, I will concede. But let me run this-- python of uppercase.py.
1:08:31
Let's type in something like cat, C-A-T in all lowercase. Enter. All right. Well, you see "After," and I did get it right in the sense
1:08:39
that it is capital C, capital A, capital T, but it looks a little stupid. And in order to fix this, we actually need
1:08:45
to introduce something that's called named parameters. So let me actually go ahead and propose that we can fix this problem
1:08:55
by actually passing in another argument to the print() function. And this is a little different syntactically from C.
1:09:01
But if I go back to VS Code here, it turns out that there's two aesthetic problems here. One, I did not want the new line automatically inserted after "After."
1:09:10
Why? Because, just like in week 1, I want them to line up nicely-- or in week 2.
1:09:15
And I don't want a new line after C-A-T. So even though at first glance a moment-- a bit ago, it might have seemed nice that Python just does the backslash n for you,
1:09:23
it can backfire if you don't actually want a new line every time. So the syntax is going to look a little weird.
1:09:29
But in Python, with the print() function, if you want to change the character that's automatically used at the end
1:09:36
of every line, you can literally pass in a second argument called end and set it
1:09:43
equal to something else. So if you want to set it equal to something else,
1:09:48
and that something else is nothing, "", then that's fine. You can actually specify end="".
1:09:57
Down here, too, if you want to specify that at the end of every one of these characters should be nothing, I can specify end="".
1:10:05
What this implies is that by default in Python, the default value of this end parameter is actually always backslash n.
1:10:13
So if you want to override it and take that away, you just literally change it to "" instead.
1:10:19
And now if I clear my-- if I rerun this program, uppercase.py, type in cat in all lowercase, now you'll see--
1:10:27
oh, two minor bugs here. One was just stupid. I had one too many spaces here. But you'll notice that I didn't move the cursor to the next line
1:10:35
after CAT was printed in all uppercase. And that we can fix by just printing nothing. It turns out when you don't pass print() an argument at all,
1:10:43
it automatically gives you just the line ending, nothing else. So I think this will move the cursor as expected.
1:10:49
So let me clear it now, run python of uppercase.py and hit Enter, type in cat in all lowercase, cross my fingers this time,
1:10:55
and now I have indeed capitalized this, character by character by character, just like we did in C.
1:11:03
But honestly, this, too, not really necessary-- it turns out I don't need to loop over a whole string,
1:11:08
because strings themselves come with methods. And if you were to visit the documentation for strings, you would see that indeed, upper is a method that comes with every string,
1:11:17
and you don't need to call it on every character individually. I could instead get rid of all of this and just print out--
1:11:25
for instance, I can just print out before.upper.
1:11:31
And the upper() function that comes with strings will automatically apply it to every character they're in and, I think, achieve the same result.
1:11:39
So let me go ahead and try this again-- python of uppercase.py, type in cat, enter, and indeed, it works exactly the same way.
1:11:46
Let me take this one step further. Let me go ahead and combine a couple of ideas now here.
1:11:51
Let me go ahead and, for instance, let me get rid of this last print() line. Let me change my logic to be after equals the return value of this.
1:12:00
And now I can use one of those f strings and plug this in maybe here, After. And I can get rid of the new line ending.
1:12:06
I can specify this is an f string. So I'm just changing this around a little bit logically so that now I have a variable called after that
1:12:13
is the uppercase version of before. And now, if I do python of uppercase.py, type in cat, that too now works.
1:12:21
And if I-- actually let me add a space there, if I run python of uppercase.py, type in cat, that too now works.
1:12:28
And lastly here, if you don't want to bother creating another variable like this, you can even
1:12:33
put short bits of code inside of these format strings. So I, for instance, could go in here into these curly braces
1:12:40
and not just put a variable name. I can actually put Python code inside of the curly braces, inside of my string.
1:12:48
And so now if I run Python of uppercase.py, type in cat, even that too now works.
1:12:54
Now, which one is the best? This is kind of reasonable to put the bit of code inside of the string.
1:12:59
I would not start writing long lines of code inside of curly braces that start to wrap, no less, because then it's
1:13:04
just going to be a matter of bad style. But this, again, is to say that there's a bunch of different ways
1:13:09
to solve each of these problems. And so up until now, we've generally seen not named parameters.
1:13:15
end is the first parameter we've ever seen that has a name, literally, end. Up until now in C and up until a moment ago in Python,
1:13:23
we've always been assuming that our parameters are positional. What matters is the order in which you specify them, not necessarily something
1:13:33
else. Whew. OK, that was a lot. Any questions about any of this here?
1:13:42
No? All right. It feels like a lot. Let's take our 10-minute break here. Fruit roll-ups are now served. We'll be back in 10.
1:13:50
All right. We are back. And recall that as we left off, we had just introduced loops.

## [Meow](https://youtu.be/EHi0RDZ31VA?t=4438)

1:13:58
And we'd seen a bunch of different ways by which we could get, say, a cat to meow. Let's actually translate that to some code
1:14:04
and start to make sense of some of the programs with which we began, like creating our own functions, as we did for the speller example
1:14:11
at the very beginning, and actually do this a little more methodically. So let me go over to VS Code here. Let me go ahead and create a program called meow.py, instead of meow.c
1:14:20
as in the past. And suffice it to say if you want to implement the idea of a cat,
1:14:25
we can do better than just saying print("meow"), print("meow"), print("meow").
1:14:31
This, of course, would work. This is correct if the goal is to get the thing to meow three times. But when I run python of meow.py, it's going to work as expected,
1:14:40
but this is just not good design, right? We should minimally be using a loop. So let me propose that we improve this per the building blocks we've seen.
1:14:47
And I could say something like, for i in range(3), go ahead and print out now, quote unquote, "meow."
1:14:54
So this is better in the sense that it still prints meow, meow, meow. But if I want to change this to a dog and change the meow to a woof
1:15:01
or something like that, I can change it in one place and not three different places-- so just, in general, better design.
1:15:07
But what if now, much like in Scratch and in C, I wanted to create my own meow() function which did not come with either
1:15:14
of those languages as well. Well, as a teaser at the start of class, we saw that you can define your own functions
1:15:20
with this keyword def, which is a little bit different from how C does it. But let me go ahead and do this indeed in Python and define my own function
1:15:29
meow(). So let me go ahead and do def meow(), and then, inside of that function,
1:15:36
I'm just going to literally do for now, quote unquote, "meow" with print(). And now down here, notice, I can actually go ahead and just call meow().
1:15:46
And I can go ahead and call meow(), and I can call meow(). And this is not the best design at the moment.
1:15:52
But Python does not constrain me to have to implement a main() function, as we've seen thus far.
1:15:58
But I can define my own helper functions, if you will, like a helper function called meow().
1:16:03
So let me go ahead and just run this for demonstration's sake and run python of meow.py. That does seem to work.
1:16:09
But this is not good design. And let me go ahead and actually do this-- for i in range(3),
1:16:15
now let me call the meow() function. And this, too, should work. If I do python of meow.py, there we have meow, meow, meow.
1:16:23
But I very deliberately did something clever here. I defined meow at the top of my file.
1:16:29
But that's not the best practice because as in C, when someone opens the file for the first time, whether you,
1:16:34
a TF, a TA, a colleague, you'd like to see the main part of the program at the top of the file, just because it's easier mentally to dive right in
1:16:42
and know what this file is doing. So let me go ahead and practice what I'm preaching and put the main part
1:16:47
of my code, even if there's no main() function per se, at the top of this file. So now I have the loop at the top.
1:16:53
I'm calling meow() on line 2, and I'm defining meow() on lines 5 and 6. Well, instinctively, you can perhaps see where this is going.
1:17:00
If I run Python of meow.py and hit Enter, there's one of those tracebacks that's tracing my error.
1:17:06
And here, my error is apparently on line 2 in meow.py. And you'll notice that, huh, the name 'meow' is not defined.
1:17:15
And so previously, we saw a different type of error, a value error. Here we're seeing a name error in the sense
1:17:20
that Python does not recognize the name of this function. And intuitively, why might that be, even if the error is a little cryptic?
1:17:27
Yeah? AUDIENCE: [INAUDIBLE] top to bottom. DAVID MALAN: Yeah, Python, too-- as fancier as it seems to be than C,
1:17:33
it still takes things pretty literally, top to bottom, left to right. So if you define meow() on line 5, you can't use it on line 2.
1:17:40
OK, so I could undo this, and I could flip the order. But let me just stipulate that as soon as we have a bunch of functions,
1:17:46
it's probably naive to assume I can just keep putting my functions above, above, above, above. And honestly, that's going to move all of my main code, so to speak,
1:17:53
to the bottom of the file, which is sort of counterproductive or less obvious. So it turns out in Python, even though you don't need a main() function,
1:18:01
it's actually quite common to define one nonetheless. So what I could do to solve this problem is this.
1:18:08
Let me go ahead and define a function called main() that takes no arguments, in this case.
1:18:14
Let me indent that same code beneath it. And now let me keep meow() defined at the bottom of my file.
1:18:20
So if we read this literally, on line 1, I'm defining a function called main(). And it will do what is prescribed on lines 2 and 3.
1:18:27
On line 6, I'm defining a function called meow(), and it will do what's prescribed on line 7-- so fairly straightforward,
1:18:33
even though the keyword def is, of course, new today. If I run, though, python of meow.py, you'd
1:18:38
like to think I'll see three meows. But I see nothing. I don't see an error, but I see nothing.
1:18:45
Why? Intuitively, what explains the lack of behavior?
1:18:50
I didn't call main(). So this is the thing even though it's not required in Python to have a main()
1:18:55
function, but it is conventional in Python to have a main() function, you have to call the function yourself.
1:19:02
It doesn't get magically called as it does in C. So this might seem a little stupid-- and that's fine-- but it is the convention in Python.
1:19:09
Generally, the very last line of your file might just be to literally this, call main(), because this satisfies the constraint that main() is defined
1:19:18
on line 1 meow() is defined on line 6, but we don't call anything until line
1:19:24 10. So line 10 says call main(). So that means execute this code. Line 3 says call meow(), which means execute this code.
1:19:32
So now it all works because the last thing I'm doing is call main(). You can think of C as just kind of secretly having
1:19:38
this line there for you the whole time. But now that we have our own functions, notice that we can enhance this
1:19:45
implementation of meow() to maybe be parameterized and take actually an argument itself. So let me make a tweak here.
1:19:51
Just like in C, and just like in Scratch, I can actually let meow() meow a specific number of times.
1:19:58
So let me do this. Wouldn't it be nice, instead of having my loop in main(), to instead just distill main() into a single line of code and just pass
1:20:05
in the number of times you want the thing to meow? What I could do in meow() here is I have to give it a parameter.
1:20:11
And I could call it anything I want. I'm going to call it n for number, which seems fine. And then, in the meow() function, I could do this--
1:20:18
for i in range of, not 3, but n now, I can tell range() to give me a range
1:20:25
that is of variable length based on what n is. And then I indent the print() below the loop now.
1:20:31
And this should now do what I expect, too. Let me run python of meow.py.
1:20:36
Enter. And there's 3. But if I change the 3 to a 5 and rerun this, python of meow.py,
1:20:43
now I'm getting five meows. So we've just seen a third way how, in Python, now we
1:20:48
can implement the idea of meowing as its own abstracted function. And I can assume now that meow() exists.
1:20:54
I can now treat it as out of sight, out of mind. It's an abstraction. And frankly, I could even put it into a library, import it from a file,
1:21:02
like we've done with CS50, and make it usable by other people as well.
1:21:07
So the takeaway here, really, though, is that in Python, you can, similarly to C, define your own functions.
1:21:13
But you should understand the slight differences as to what gets called automatically for you.
1:21:19
All right. Other differences or similarities with C? Well, recall that in C, truncation was an issue.

## [Truncation](https://youtu.be/EHi0RDZ31VA?t=4885)

1:21:25
Truncation is whereby if you, for instance, divide an int by an int, and it's a fractional answer, everything after the decimal point
1:21:34
gets truncated by default because an int divided by an int in C gives you an int.
1:21:39
And if you can't fit the remainder in that integer, everything at the decimal gets cut off.
1:21:44
So what does this mean? Well, let me actually go back to VS Code here. Let me go ahead and open, say, calculator.py again,
1:21:52
and let's change up what the calculator now does. Let me do this. Let me define a variable called x, set it equal to the input() function,
1:22:00
prompting the user for x. Let me ask the user for y, let me not repeat past mistakes,
1:22:05
and let me proactively convert both of these to ints. And I'll do it in one pretty one-liner here so that I definitely get x and y.
1:22:13
And on the honor system, I just won't type cat. I won't type dog, even though this program is not really complete without error checking.
1:22:19
Now, let me go ahead and declare a third variable, z = x / y, and now let's just go ahead and print out z.
1:22:26
I don't need a format code. I don't need an f string. If all you want to do is print a variable, print() is very flexible.
1:22:32
You can just say print(z), in parentheses. Let me run python of calculator.py, hit Enter.
1:22:38
Let's type in 1 for x, 3 for y. I left out a space there.
1:22:43
And oh, interesting. What seems to have happened here? Let me fix my spacing and rerun this again-- python of calculator.py-- so 1,
1:22:52 3. What did not happen? AUDIENCE: It doesn't truncate. DAVID MALAN: Yeah. So it didn't truncate.
1:22:58
So Python is a little smarter when it comes to converting one value to another. So an integer divided by an integer, if it ends up
1:23:05
giving you this fractional component, not to worry now, you'll get back what is effectively a float in Python here.
1:23:11
Well, what else do we want to be mindful of in, say, Python?
1:23:17
Well, recall that in C, we had this issue of floating point and precision whereby if you want to represent a number, like 1/3, and on a piece
1:23:24
of paper, it's, like, 0.3 with a line over it because the 3 infinitely repeats--
1:23:29
but we saw a problem in C last time when we actually played around with some value. So, for instance, let me go back to VS Code here.
1:23:37
And this is going to be the ugliest syntax I do think we see today. But there was a way in C, using %f, to show more than the default number
1:23:45
of digits after the decimal point, to see more significant digits. In Python, there's something similar.
1:23:50
It just looks very weird. And the way you do it in Python is this. You specify that you want an f string, a format string.
1:23:56
And I'm just going to start and finish my thought first-- f before "". If you want to print out z, you could literally just do this.
1:24:04
And so this is just an f string, but you're interpolating z. So it doesn't do anything more than it did a moment ago when I literally just
1:24:12
passed in z. But as soon as you have an f string, you can configure the variable to print out to a specific number of digits.
1:24:19
So if you actually want to print out z to, say, 50 decimal points,
1:24:24
just to see a lot, you can use crazy syntax like this. So it's just using the curly braces, as I introduced before.
1:24:31
But you then use a dot after a colon, and then you specify the number of digits that you want and then an f to make clear
1:24:37
it's a float. Honestly, I google this all the time when I don't remember the syntax. But the point is the functionality exists.
1:24:43
All right. Let me go down here and rerun python of calculator.py. And unfortunately, if I divide 1 by 3, not all of my problems are solved.
1:24:52
Floating point precision is still a thing. So be mindful of the fact that there are these limitations
1:24:59
in the world of Python. Floating point precision remains. If you want to do even better than that, though, there
1:25:04
exist a lot more libraries, third-party libraries, that can give you much greater precision for scientific purposes,
1:25:11
financial purposes, or the like. But what about another problem from C, integer overflow? If you just count to high, recall that you might accidentally
1:25:19
overflow the capacity of an integer and end up going back to 0, or worse, going negative altogether.
1:25:25
In Python, this problem does not exist. In Python, when you have an integer, a.k.a.
1:25:31
int, even though we haven't needed to use the keyword int, it will grow and grow and grow.
1:25:37
And Python will reserve more and more memory for that integer to fit it. So it is not a fixed number of bits.
1:25:43
So floating point imprecision is still a problem. Integer overflow-- not a problem in the latest versions of Python,
1:25:51
so a difference worth knowing. But what about other features of Python that we didn't have in C?

## [Exceptions](https://youtu.be/EHi0RDZ31VA?t=5156)

1:25:56
Well, let's actually revisit one of those tracebacks, one of those errors I ran into earlier, to see how we might actually solve it.
1:26:03
So let me go back to VS Code here. And just for fun, let me go ahead and do this. Let me clear my terminal.
1:26:09
And let me change my calculator to actually have a get_int() function. We've seen how to define our own functions. Let me not bother with the CS50 library.
1:26:15
Let me just invent my own get_int() function as follows. So def get_int(), and just like the CS50 function,
1:26:22
I'm going to have get int take a prompt, a string to show the user to ask them for an integer. And now I'm going to go ahead and return the return value of input(),
1:26:31
passing that same prompt to input()-- because input(), just like get_string(), shows the user a string of text.
1:26:37
But I do want to convert this thing here to an int. So this is just a one-liner, really, of an implementation of get_int().
1:26:44
So this is kind of like what CS50 did in its Python library, but not quite. Why? Because there's a problem with it.
1:26:51
So let me do this. Let me define a main() function just by convention. Let me use this implementation of get_int() to ask the user for x.
1:26:57
Let me use this get_int() function to prompt the user for y. And then let me do something simple like print out x + y.
1:27:05
And then, very last thing, I have to call main(). And this is a minor point, but I'm deliberately
1:27:10
putting multiple blank lines between my functions. This too is Pythonic. It's a matter of style. style50 will help you with this.
1:27:17
It's just meant for larger files to really make your functions stand out and be a little more separated visually from others.
1:27:24
All right. Let me go ahead and run Python of calculator.py. Enter. Let me type in 1.
1:27:29
Let me type in 3. And that actually works. 1 plus 3 is 4. Let me do the more obvious.
1:27:35
1 plus 2 gives me 3. So the calculator is in fact working until such time as I, the human,
1:27:41
don't cooperate and type in something like cat for x. Then we get that same traceback as before,
1:27:47
but I'm seeing it now in this file. And let me zoom in on my terminal just to make clear. We don't need to see the old history there.
1:27:55
Let me type in cat, Enter, and you'll see the same traceback. And you'll see that, OK, here's where now there's
1:28:03
multiple functions involved. So what's going on? The first problem is at line 12 in main().
1:28:08
But that's not actually the problem because main() calls my get_int() function. So on line 6 of calculator.py, this is really the issue--
1:28:17
so, again, it's tracing everything that just happened from top to bottom here-- and value error-- invalid literal for int() with base 10,
1:28:25
'cat,' which is to say, like before, cat is not an integer in base 10 or any
1:28:30
other base. It just cannot be converted to an integer. So how do you fix this, or, really, how does the CS50 library fix this?
1:28:38
You won't have to write much code like this. But it turns out that Python supports what are called exceptions.
1:28:44
And generally, an exception is a better way of handling certain types of errors because in C, recall
1:28:50
that the only way we could really handle errors is by having functions return special values.
1:28:56
malloc() could return null, which means it ran out of memory. Something went wrong.
1:29:01
Some functions we wrote in C could return 1, could return 2, could return negative 1.
1:29:07
Recall that we could write our own functions that return values to indicate something went wrong. But the problem in C is that if you're stealing certain values,
1:29:15
be it null or 1 or 2 or 3, your function can never return null or 1 or 2 or 3
1:29:23
as actual values. Why? Because other people are going to interpret them as errors. So you kind of have to use up some of your possible return values
1:29:30
in a language like C and treat them specially as errors. In Python and other languages--
1:29:37
Java and others-- you don't have to do that. You can instead have more out of band error handling, known as exceptions.
1:29:43
And that's what's happening here. When I run calculator.py and I type in cat, what I'm seeing here
1:29:49
is actually an exception. It's something exceptional, but not in a good way. This exception means this was not supposed to happen.
1:29:57
The type of exception happens to be called a value error. And within the world of Python, there's this whole taxonomy, that is to say,
1:30:03
a whole list of possible exceptions. ValueError is one of the most common. We saw another one before, name error, when I said
1:30:09
meow when Python didn't know what meow meant. So this is just an example of an exception. But what this means is that there is a way for me to try to handle this
1:30:18
myself. So I'm actually going to go ahead and do this. Instead of get_int() simply blindly returning the integer conversion
1:30:26
of whatever input the user gives me, I'm going to instead literally try to do
1:30:31
this instead. So it's kind of a aptly named phrase. It literally means that. Please try to do this, except if something goes wrong,
1:30:39
except if there is a ValueError, in which case
1:30:45
I want Python to do something else, for instance, quote unquote, "Not an integer."
1:30:50
So what does this mean? It's a little weird, the syntax. But in the get_int() function, Python will first try to do the following.
1:30:57
It will try to get an input from the user. It will try to convert it to an integer. And it will try to return it.
1:31:03
But if one of those operations fails, namely the integer step in this case, then an exception could happen.
1:31:09
And you might get what's called a ValueError. Why? Because the documentation tells you that might happen. Or, in my case, I experienced it firsthand,
1:31:16
and now I want to catch this kind of exception in my own code. So if there is a ValueError, I'm not going
1:31:22
to see that crazy traceback anymore. I'm instead going to see, quote unquote, "Not an integer."
1:31:28
But what the CS50 library does for you technically is it lets you try again and again and again.
1:31:33
Recall in the past, if I type in cat and dog and bird, it's just going to keep asking me again and again until I actually give it an int.
1:31:39
So that kind of implies that we really need a loop inside of this function. And the easiest way to do something forever
1:31:45
is to loop while true, just like in C, but a capital T in Python.
1:31:50
And what I'm going to do now is implement a better version of get_int() here because what's it going to do?
1:31:57
It is going to try-- it's going to do this forever. It's going to try to get an input, convert it to an int, and return it.
1:32:03
And just like break breaks you out of a loop, return also breaks you out of a loop as well, right?
1:32:10
Because once you've returned, there's no more need for this function to execute. So long story short, you won't have to write much code like this yourself.
1:32:17
But this is essentially what the CS50 library is doing when it implements
1:32:23
the Python version of get_int(). So what happens now? If I run python of calculator.py, and I type in cat, I get yelled at,
1:32:31
but I'm prompted again because of the loop. I type in dog. I'm yelled at, but I'm prompted again. I type in bird, yelled at, but I'm prompted again.
1:32:38
If I type in 1, then I type in 2, now it proceeds because it tried and succeeded this time as opposed to trying and failing
1:32:46
last time. And technically, the CS50 library doesn't actually yell at you with "Not an integer."
1:32:51
So technically, if you want to handle the error, that is to say, catch the exception, you can actually just say, oh, pass,
1:32:58
and it will just silently try again and again. So let me go ahead and run this. python of calculator.py works almost the same.
1:33:06
But notice now it works just like the C version. It doesn't yell at you, but it does prompt you again and again and again.
1:33:13
But I'll do 1 and 2, and that now is satisfied. So that then is exceptions which you'll encounter,
1:33:18
but you yourself won't have to write much code along those lines. Well, what else can we now do?

## [Mario](https://youtu.be/EHi0RDZ31VA?t=5603)

1:33:23
Well, let's revisit something like this for Mario, recall, whereby we had this two-dimensional world with things
1:33:29
in the way for Mario, like this column of three bricks. Let me actually play around now for a moment with some loops
1:33:35
just to see how there's different ways that might actually resonate with you just in terms of the simplicity of some of these things.
1:33:41
Let me go ahead and create a program called mario.py. And suppose that I want to print a column of three bricks.
1:33:47
It kind of doesn't get any easier than this in Python. So for i in range(3), just go ahead and print out a single hash--
1:33:55
done. That then is what we took us more lines of code in the past. But if I run mario.py, that there gets the job done.
1:34:03
I could change the i to an underscore, but it's not bad to remind myself that i is what's really doing my counting.
1:34:09
Well, what else could we do beyond this? Well, recall that in the world of Mario, we prompted the user, actually,
1:34:17
for a specific height. We didn't just always hardcode 3. So I could actually do something like this.
1:34:23
Let me actually open up from today's code that I came with in advance
1:34:28
and pull up this C version of Mario. So this was from some time ago, in week 1.
1:34:34
And this is how we implemented a loop that ensures that we get a positive integer from the user by just doing while
1:34:43
and is not positive, and then we use this for loop to actually print out that many hashes. Now, in Python, it's actually going to be pretty similar,
1:34:50
except for the fact that in Python, there is no do while loop. But recall that a do while loop was useful
1:34:55
because it means you can get the user to try something and then maybe try again, maybe try again, maybe try again. So it's really good for user input.
1:35:02
So let's actually do this. Let me borrow the CS50's library get*int() function, just so we don't have to re-implement that ourselves again and again.
1:35:10
Let me, in Python, do this the Pythonic way. In Python, if you want to prompt the user to do something again and again
1:35:17
and again, potentially, you deliberately, by convention, induce an infinite loop. You just get yourself into an infinite loop.
1:35:24
But the goal is going to be try something, try something, try something, and as soon as you have what you want, break out of the loop
1:35:30
instead. So we're implementing the idea of a do while loop ourselves. So I'm going to do this. n, for number, equals get_int(),
1:35:37
and let's ask the user for a height. Then let's just check. If n is greater than 0, you know what?
1:35:44
Break. We've got the value we need. And if not, it's just going to implicitly keep looping again and again
1:35:50
and again. So in Python, this is to say-- super common-- to deliberately induce an infinite loop and break out of it when you have
1:35:57
what you want. All right? Now I can just do the same kind of code as before. for i in range not of--
1:36:03
rage sometimes-- for i in range, not 3, but n, now I can go ahead and print out--
1:36:10
oops-- a hash like this. If I open my terminal window, it's going to work almost the same, but now mario is going to prompt me for the height.
1:36:17
So I could type in 3, or I could type in 4, or I could be uncooperative and type in 0 or negative 1 or even cat.
1:36:25
And because I'm using the CS50 library, cat is ignored. Because I'm using my while loop and breaking out
1:36:32
of it only when n is positive, I'm also ignoring the 0 and the negative 1.
1:36:37
So, again, this would be a Pythonic way of implementing this particular idea.
1:36:43
If I want to maybe enhance this a bit further, let me propose that,
1:36:49
for instance, we consider something like the two-dimensional version--
1:36:55
or the horizontal version of this instead. So recall that some time ago, we printed out,
1:37:00
like, four question marks in the sky that might have looked a little something like this. Now, the very mechanical way to do this would be as follows.
1:37:09
Let me close my C code. Let me clear my terminal. And let me just delete my old mario version here.
1:37:16
And let's just do this-- for i in range(4), let's go ahead and print out a question mark, all right?
1:37:23
I'm going to run python of mario.py, enter, and, ugh, it's still a column instead of a row.
1:37:30
But what's the fix here, perhaps? What's the fix? Yeah?
1:37:35
AUDIENCE: The end equals [INAUDIBLE] DAVID MALAN: Yeah. We can use that named parameter and say end=""
1:37:41
to just suppress the default backslash n. But let's give ourselves one at the very end of the loop
1:37:46
just to move the cursor correctly. So now if I run python of mario.py, now it looks like what it might have in the sky here.
1:37:53
But it turns out Python has some neat features, too, more syntactic sugar, if you will, for doing things a little more easily.
1:37:59
It turns out in Python, you could also do this. You could just say print("?" * 4).
1:38:06
And just like + means concatenation, \_ here means, really, multiply the string by itself that many times, so sort
1:38:14
of automatically concatenate it with itself. So if I run python of mario.py, this too works-- so,
1:38:19
again, just some features of Python that make it a little more pleasant to use so you don't always have to slog through implementing
1:38:25
a loop or something along those lines. Well, what about something more two-dimensional, like in the world of this brick here?
1:38:32
Well, in the context of this sort of grid of bricks, we might do something like this in VS Code.
1:38:38
Let me go back to mario.py, and let me do a 3-by-3 grid for that block,
1:38:43
like we did in week 1. So for i in range(3)-- I can nest loops, just like in C-- for j in range(3),
1:38:52
I can then print out a hash here. And then let's leave this alone even though it's not quite right yet.
1:38:58
Let's do python of mario.py. OK, it's, like, nine bricks all in a column, which so your mind might
1:39:04
wander to the end parameter again. So, yeah, let's fix this-- end="", but at the end of that loop,
1:39:10
let's just print out a new line. So this logically is the same as it was in C But in this case,
1:39:16
I'm now doing it in Python, just a little more easily, without i++, without a conditional, I'm just relying on this for i in syntax using range().
1:39:26
I can tighten this up further, frankly. If I already have the outer loop, I could do something like this. I could print out a single hash times 3.
1:39:34
And now if I run python of mario.py, that works, too. So I can combine these ideas in interesting ways as well.
1:39:40
The goal is simply to seed you with some of these building blocks. All right. How about code that was maybe a little more logical in nature?

## [Lists](https://youtu.be/EHi0RDZ31VA?t=5988)

1:39:48
Well, in Python, we indeed have some other features as well, namely lists. And lists are denoted by those square brackets,
1:39:54
reminiscent of the world of arrays. But in Python, what's really nice about lists is that their memory is automatically handled for you.
1:40:02
An array is about having values contiguously in memory. In Python, a list is more like a linked list.
1:40:09
It will allocate memory for you and grow and shrink these things. And you do not have to know about pointers.
1:40:14
You do not have to know about nodes. You do not have to implement linked lists yourself. You just get list as a data type in Python itself.
1:40:22
Here, for instance, is some of the documentation for lists specifically. And in particular, lists also, like strings, or strs,
1:40:29
have methods, functions that come with them, that just make it easy to do certain things.
1:40:34
So, for instance, if I wanted to maybe do something like taking averages
1:40:40
of scores, like we did some time ago, we can do that using a combination of lists and the function called len(), which I alluded to earlier,
1:40:47
which will tell you the length of a list. Now, how might we do this? Well, if we read the documentation for len(),
1:40:52
it turns out there's other functions there too that might be helpful. So let me go back to VS Code here. Let me close mario.py.
1:40:59
And let me open a file called scores.py, reminiscent of something we did weeks ago, too. Let me go ahead and, just for demonstration's sake,
1:41:06
give myself a variable called scores that has my three test scores or whatnot from weeks ago.
1:41:11
So I'm using square brackets, not curly braces, as in C. This is a linked list, or a list in Python.
1:41:17
And let me get the average of these values. Well, I could do this-- average =, and it turns out in Python,
1:41:24
you just get a lot of functionality for free. And those functions sometimes take not single arguments,
1:41:29
but lists as their arguments. So, for instance, I can use Python's built-in sum() function and pass
1:41:35
in those scores. I can then divide that sum by the length of the scores list as well.
1:41:41
So length of a list just tells you how many things are in it. So this is like doing magically 72 plus 73 plus 33, all divided by 3 in total.
1:41:51
If I want to now do the math out, I can print the result. So I can print out, using an f string and maybe some prefix text here.
1:41:59
Let's print out that average here. So let me do python of scores.py, enter, and there
1:42:06
is the average, slightly imprecisely. But at that point, I'm not doing so well anyway. So that's fine. So at this point, we've seen that we have sort of more functionality than C.
1:42:17
In C, how would we have computed the average weeks ago? I mean, we literally created a variable. We then had a loop.
1:42:22
We iterated over the array. We added things together. It was just so much more work. It's nice when you have a language that comes with functions, among them len(),
1:42:30
among them sum(), that just does more of this for you. But suppose you actually want to get the scores from the user.
1:42:37
In C, we used an array, and in C, we used get_int(). We can do something a little similar here.
1:42:42
Let me propose that instead of hardcoding those three values, let me do this. from cs50 import get_int().
1:42:49
Now let me give myself an empty list by just saying scores equals open bracket, closed bracket.
1:42:55
And unlike C, where you just can't do this-- you can't say give me an array and I'll figure out the length later, unless you resort
1:43:03
to pointers and memory management or the like, in Python you can absolutely give yourself an initially empty list.
1:43:09
Now let's do this. for i in range(3), let's prompt the human for three test scores.
1:43:15
So the first score will be the return value of get_int(), prompting the user for their score.
1:43:20
And now, if I want to add this score to that otherwise empty list, here's where methods come into play, functions
1:43:27
that come with objects, like lists. I can do scores, plural-- because that's the name of my variable from line 3-- .append,
1:43:35
and I can append that score. So if we read the documentation for lists in Python, you will see that lists come with a function, a method called append(),
1:43:43
which literally just tacks a value onto the end, tacks a value onto the end, like all of that annoying code we would have written in C to iterate with
1:43:52
pointer and pointer and pointer to the end of the list, append it, malloc() a new node. Python does all of that for us.
1:43:58
And so once you've done that, now I can do something similar to before. The average equals the sum of those scores divided
1:44:04
by the length of that list of scores. And I can again print out, with an f string, the average value
1:44:11
in that variable like this. So, again, you just have more building blocks at your disposal when it comes to something like this.
1:44:19
You can also do this, just so you've seen other syntax. It turns out that instead of doing scores.append, you could also do this.
1:44:28
You could concatenate scores with itself by adding two lists together like this.
1:44:36
This looks a little weird. But on the left is my variable scores. On the right here, I am taking whatever is in that list,
1:44:44
and I'm adding the current score by adding it to its own list. And this will update the value as we go.
1:44:51
But it does, in fact, change the value of score as opposed to appending to the initial list.
1:44:58
All right. How about some other building blocks here? Let me propose this.
1:45:04
Let me close out scores.py. Let me open up a file called phonebook.py,
1:45:09
reminiscent of what we did weeks ago in C. And let me give myself a list of names. We won't bother with numbers just yet.
1:45:15
Let's just play with lists for another moment. So here is a variable called names. It has maybe three names in it-- maybe Carter and David
1:45:22
and John Harvard, as in past weeks. And now let me go ahead and ask the user to input a name--
1:45:29
because this is going to be like a phone book. I want to ask the user for a name and then look up that person's name and the phone book, even though I'm not bothering
1:45:35
by having any phone numbers just yet. How could I search for, a la linear search, someone's name?
1:45:41
Well, in Python I could do this. for name-- rather, for n in names, if the current name equals what the human typed in,
1:45:53
then go ahead and print out "Found," then break out of this loop.
1:45:58
Otherwise, we'll print out "Not found" at the bottom. All right. So let's try this-- python of phonebook.py.
1:46:05
Let's search for maybe Carter. That's easy. He's at the beginning. Oh, hmm. Well, he was found, but then I printed "Not found."
1:46:11
So that's not quite what I want. How about David? D-A-V-I-D. "Found," "Not found"--
1:46:16
all right, not very correct. How about this? Let's search for Eli, not in the list.
1:46:21
OK. So at least someone not being in the list is working. But logically, for Carter, for David, and even John,
1:46:28
why are we seeing "Found" and then "Not found?"
1:46:37
Why is it not found? Yeah? AUDIENCE: You need to intend the print(). DAVID MALAN: OK. I don't have seem to have indented the print(), but let me try this.
1:46:45
If I just go with the else here-- let me go up here and indent this and say else--
1:46:50
I'm not sure logically this is what we want, because what I think this is going to do if I search for maybe Carter--
1:46:57
OK, that worked. So it's partially fixed the problem. But let me try searching for maybe David.
1:47:03
Oh, now we're sort of the opposite problem-- "Not found," "Found." Why? Well, I don't think we want to immediately conclude
1:47:09
that someone's not found just because they don't equal the current name in the list.
1:47:15
So it turns out we could fix this in a couple of different ways. But there's kind of a neat features of Python.
1:47:22
In Python, even for loops can have an else clause. And this is weird. But the way this works is as follows.
1:47:29
In Python, if you break out of a loop, that's it for the for loop.
1:47:34
If, though, you get all the way through the list that you're looping over, and you never once call line 8-- you never break out of the loop--
1:47:42
Python is smart enough to realize, OK, you just went through lines 5 through 8. You never actually logically called break.
1:47:49
Here's an else clause to be associated with it. Semantically, this is weird. We've only ever seen if and else associated with each other.
1:47:55
But for loops in Python actually can have else as well. And in this case now, if I do python of phonebook.py, type in Carter,
1:48:03
now we get only one answer. If I do it again and type in David, now we get only one answer. Do it again with John.
1:48:08
Now we get only one answer. Do it with Eli. Now we get only one answer. So, again, you just get a few more tools in your toolkit
1:48:14
when it comes to a language like Python that might very well make solving problems a little more pleasant.
1:48:20
But this is kind of stupid in Python. This is correct, but it's not well designed, because I don't need to iterate over lists like this so pedantically
1:48:28
like we've been doing for weeks in C. I can actually tighten this up, and I can just do this.
1:48:33
I can get rid of the loop, and I can say if name in names, then print out, quote unquote, "Found."
1:48:39
That's it in Python. If you want Python to search a whole list of values for you, just let Python do the work.
1:48:45
And you can literally just say if the name that the human inputted is in names, which is this list here, Python will use linear search for you,
1:48:55
search automatically from left to right, presumably, looking for the value. And if it doesn't find it then and only then will
1:49:02
this else clause execute instead. So, again, Python's just starting to save us some time because this, too, will find Carter, but it will not find,
1:49:10
for instance, Eli. All right? So we get that functionality for free. But what more can we perhaps do here?

## [Dictionaries](https://youtu.be/EHi0RDZ31VA?t=6558)

1:49:18
Well, it turns out that Python has yet other features we might want to explore, namely dictionaries, shortened as dict.
1:49:25
And a dictionary in Python is just like it was in C and, really, in computer science in general.
1:49:31
A dictionary was an abstract data type. And it's a collection of key value pairs it looks a little something like this.
1:49:36
If in C, if in Python, if, in any language, you want to associate something with something, like a name with a number,
1:49:43
you had to, in problem set 5, implement the darn thing yourself by implementing an entire spell checker with an array and linked list
1:49:50
to store all of those words in your dictionary. In Python, as we saw earlier, you can use a set, or you can use,
1:49:57
more simply, a dictionary that implements for you all of problem set 5's ideas.
1:50:03
But Python does the heavy lifting for you. A dict in Python is essentially a hash table, a collection of key value pairs.
1:50:11
So what does this mean for me in Python? It means that I can do some pretty handy things pretty easily.
1:50:18
So, for instance, let me go back here to VS Code, and let me change my phone book altogether to be this.
1:50:25
Let me give myself a list of dictionaries. So people is now going to be a global list.
1:50:32
And I'm going to demarcate it here with open square bracket and closed square bracket. And just to be nice and neat and tidy, I'm
1:50:39
going to have these people no longer just be Carter and David and John,
1:50:45
as in the previous example. But I want each of the elements of this list to be a key value
1:50:52
pair, like a name and a number. So how can I do this? In Python, you can use this syntax.
1:50:58
And this is, I think, the last of the weird looking syntax today. You can define a dictionary that is something like this
1:51:06
by using two curly braces like this. And inside of your curly braces, you get to invent
1:51:12
the name, the keys, and the values. So if you want one key to be the person's name, you can do,
1:51:18
quote unquote, "name" and then, quote unquote, "Carter." If you want another key to be "number," you can do, quote unquote, "number,"
1:51:24
and then, quote unquote, something like last time, "1-617-495-1000," for instance, for Carter's number there.
1:51:31
And collectively, everything here on line 2 represents a dictionary. It's as though, on a chalkboard, I wrote down "name, Carter, number,
1:51:40
+1-617-495-1000," row by row by row in this table.
1:51:45
This is simply the code equivalent thereof. If you want to be really nitpicky or tidy, you could style your code to look like this,
1:51:52
which makes it a little more clear, perhaps, as to what's going on. It's just starting to add a lot of whitespace to the screen.
1:51:58
But it's just a collection of key value pairs, again, akin to a two-column table like this.
1:52:04
I'm going to undo the whitespace just to kind of tighten things up because I want to cram two other people in here.
1:52:09
So I'm going to go ahead and do another set of curly braces with, quote unquote, "name" and "David," quote unquote, "number"--
1:52:17
and we'll have the same number, so "+1-617-495-1000." And then, lastly, let's do another set of curly braces for a name of say
1:52:25
"John," and John Harvard's number, quote unquote, "number" will be "+1"--
1:52:34
let's see-- "949-468-2750" is always John Harvard's number.
1:52:40
And then, by convention, you typically end even this element with a comma. But it's not strictly necessary syntactically.
1:52:46
But stylistically, that's often added for you. So what is people? people is now a list of dictionaries, a list of dictionaries.
1:52:54
So what does that mean? It means I can now do code like this. I can prompt the user with the input() function for someone's name if the goal
1:53:02
now is to look up that person's number. How can I look up that number? Well, for each person in the list of people, let's go ahead and do this.
1:53:10
If the current person's name equals equals whatever name the human
1:53:16
typed in, then get that person's number by going into that person and doing,
1:53:22
quote unquote, "number," and then go ahead and print out something like this f string "Found" that person's number.
1:53:31
And then, since we found them, let's just break out all together. And if we get through that whole thing, let's just, at the very end, print
1:53:37
out "Not found." So what's weird here? If I focus on this code here, this syntax obviously is new.
1:53:44
The square brackets, though, just means, hey, Python, here comes a list. Hey, Python, that's it for the list.
1:53:49
Inside of this list are three dictionaries. The curly braces mean, hey, Python, here comes a dictionary.
1:53:55
Hey, Python, that's it for the dictionary. Each of these dictionaries has two key value pairs-- "name" and its value, "number" and its value.
1:54:03
So you can think of each of these lines as being like a C struct, like with typedef and struct.
1:54:09
But I don't have to decide in advance what the keys and the values are going to be. I can just, on the fly, create a dictionary like this,
1:54:15
again, reminiscent of this kind of chalkboard design. All right. So what am I actually doing in code?
1:54:21
A dictionary in Python lets you index into it,
1:54:26
similar to an array with numbers in C. So in C, this is a little bit different.
1:54:32
In C, you might have been in the habit of doing person.name. But because it's a dictionary, the syntax in Python
1:54:38
is you actually use square brackets with strings as being inside the square brackets rather than numbers.
1:54:45
But all this is now doing is it's creating a variable on line 11, setting that number equal to that same person's number.
1:54:53
Why? Because we're inside of this loop, I'm iterating over each person one at a time.
1:54:58
And that's what for-- that's what n does. It assigns the person variable to this dictionary, then this dictionary,
1:55:06
then this dictionary automatically for me-- no need for i and i++ and all of that.
1:55:11
So this is just saying, if the current person's name equals the name we're looking for, get a variable called number and assign it
1:55:17
that person's number, and then print out that person's number. So whereas last time we were just printing "Found" and "Not found,"
1:55:23
now I'm going to print an actual number. So if I run python of phonebook.py and I search for Carter, there then is his number.
1:55:29
If I run python of phonebook.py, type in John, there then is John's number. And if I search for someone who's not there, I instead just get "Not found."
1:55:38
So what's interesting and compelling about dictionaries is they're kind of known as the Swiss Army knives of data structures
1:55:45
in programming because you can just use them in so many interesting, clever ways. If you ever want to associate something with something else,
1:55:52
a dictionary is your friend. And you no longer have to write dozens of lines of code as in P set 5.
1:55:58
You can write single lines of code to achieve this same idea. So, for instance, if I, too, want to tighten this up,
1:56:04
I actually don't need this loop altogether. An even better version of this code would be this.
1:56:10
I don't need this variable, technically, even though this will look a little uglier. Notice that I'm only creating a variable called number
1:56:16
because I want to set it equal to this person's number. But strictly speaking, any time you've declared a variable
1:56:21
and then used it in the next line, eh, you don't really need it. So I could do this. I could get rid of that line.
1:56:27
And instead of printing "number" in my curly braces, I could actually do person, square brackets,
1:56:33
and you might be inclined to do this. But this is going to confuse Python because you're mixing double quotes
1:56:38
on the inside and the outside. But you can use single quotes here, compellingly. So you don't have to do it this way.
1:56:45
But this is just to show you, syntactically, you can put most anything you want in these curly braces
1:56:51
so long as you don't confuse Python by using the same syntax. But let me do one other thing here.
1:56:58
This is even more powerful. Let me propose that if all you're storing is names and numbers, names and numbers, I can actually
1:57:05
simplify this dictionary significantly. Let me actually redeclare this people data structure
1:57:14
to be not a list of dictionaries, but how about just one big dictionary?
1:57:19
Because if I'm only associating names with numbers, I don't technically need to create special keys
1:57:24
called "name" and "number." Why don't I just associate Carter with his number, +1-617-495-1000?
1:57:32
Why don't I just associate, quote unquote, "David" with his number, +1-617-495-1000?
1:57:41
And then, lastly, let's just associate John with his number, +1-949-468-2750?
1:57:51
And that too would work. But notice that I'm going to get rid of my list of people
1:57:57
and instead just have one dictionary of people, the downside of which is that you can only have one key, one value, one key, one value.
1:58:04
You can't have a name key and a number key and an email key and an address key and any number of other pieces of data that might be compelling.
1:58:11
But if you've only got key value pairs like this, we can tighten up this code significantly so that now, down here,
1:58:17
I can actually do this. If the name I'm looking for is somewhere in that people dictionary,
1:58:24
then go ahead and get the person's number by going into the people dictionary, indexing into it at that person's name,
1:58:32
and then printing out "Found," for instance, that here number,
1:58:39
making this an f string, else you can go ahead and print out "Not found" in this case here.
1:58:44
So, again, the difference is that the previous version created a list of dictionaries, and I very manually,
1:58:49
methodically, iterated over it, looking for the person. But what's nice again about dictionaries is
1:58:55
that Python gives you a lot of support for just looking into them easily. And this syntax, just like you can use it for lists,
1:59:01
you can use it for dictionaries as well. And Python will look for that name among the keys in the dictionary.
1:59:08
And if it finds it, you use this syntax to get at that person's number.
1:59:15
Whew, OK. A lot all at once, but are there any questions on this here syntax?
1:59:21
We'll then introduce a couple of final features with a final flourish. Yes? AUDIENCE: This way [INAUDIBLE] break [INAUDIBLE]..
1:59:28
DAVID MALAN: In this case, I do not need to use break because I don't have any loop involved. So break is only used, as we've seen it, in the context of looping
1:59:37
over something when you want to terminate the loop early. But here Python is doing the searching for you.
1:59:42
So Python is taking care of that automatically. All right. Just a couple of final features so that you have a couple of more building
1:59:50
blocks-- here is the documentation for dictionaries themselves in case you want to poke around as to what more you can do with them.
1:59:56
But it turns out that there are other libraries that come with Python, not even third-party, and one of them

## [sys](https://youtu.be/EHi0RDZ31VA?t=7201)

2:00:01
is the sys library, whereby you have system-related functionality.
2:00:07
And here's its official documentation, for instance. But what this means is that certain functionality that was just
2:00:12
immediately available in C is sometimes tucked away now into libraries in Python.
2:00:18
So, for instance, let me go over to VS Code here, and let me just create a program called greet.py, which
2:00:23
is reminiscent of an old C program that just greets the user using command-line arguments. But in C, recall that we got access to command-line arguments with main()
2:00:31
and argc and argv. But none of those have we seen at all today.
2:00:36
And, in fact, main() itself is no longer required. So if you want to do command-line arguments in Python,
2:00:43
you actually do this. From the sys library, you can import something called argv.
2:00:48
So argv still exists. It's just tucked away inside of this library, otherwise known as a module.
2:00:54
And I can then do this. If the length of argv, for instance, does not equal 2,
2:01:00
well, then, we're going to go ahead and do what we did-- or rather, let's do this. If the length of argv does equal 2, we're
2:01:06
going to go ahead and do what we did a couple of weeks ago, whereby I'm going to print out "hello,"
2:01:11
comma, and then argv bracket 1, for instance, so whatever is in location 1 of that list.
2:01:18
Else, if the length of argv is not equal to 2-- that is, the human did not type two words at the prompt--
2:01:24
let's go ahead and print out "hello, world" by default. So we did the exact same thing in C. The only difference here is that this now
2:01:31
is how you get access to argv. So let me run this-- python of greet.py and hit Enter. "hello, world" is all I
2:01:38
get. And actually, I got an extra line break because out of habit, I included backslash n, but I don't need that in Python.
2:01:43
So let me fix that. python of greet.py-- "hello, world." But if I do python of greet.py, D-A-V-I-D,
2:01:50
now notice that argv equals 2. If I instead do something like Carter, argv now equals 2.
2:01:56
But there is a difference. Technically, I'm typing three words at the prompt, three words at the prompt,
2:02:02
but argv still only equals 2 because the command python is ignored from argv.
2:02:07
It's only the name of your file and the thing you type after it. So that's then how we might print out arguments in Python using argv.
2:02:16
Well, what else might we do using some of these here features? Well, it turns out that you can exit from programs using this same sys
2:02:25
library. So let me close greet.py. Let me open up exit.py just for demonstration's sake.
2:02:30
And let's do something like this. Let's import sys. And if the length of sys.argv--
2:02:37
so here's just another way of doing this. And actually, I'll do it the same first-- from sys import argv.
2:02:44
If the length of argv does not equal 2--
2:02:49
well, let's actually yell at the user with something like "Missing command-line argument."
2:02:54
And then what we can do is exit out of the program entirely using sys.exit(),
2:03:01
which is a function therein. But notice that exit() is a function in sys. So you know what? It's actually more convenient in this case.
2:03:07
Let's just import all of sys. But because that has not given me direct access to argv, let me do sys.argv here and sys.exit() here.
2:03:16
Otherwise, if all is well, let's just go ahead and print out something like "hello, sys.argv," bracket 1, close quote, and that will print out "hello,
2:03:27
so-and-so." And when I'm ready to exit with a non-0-- with a 0 exit status, I can actually start to specify these things here.
2:03:35
So just like in C, if you want to exit from a program with 1 or 2 or anything else, you can use sys.exit.
2:03:41
And if you want to exit with a 0, you can do this here instead. So we have the same capabilities as in C,
2:03:48
just accessed a little bit differently. Let me propose that--
2:03:53
let's see. Let me propose that-- how about this?
2:03:59
How about this?

## [pip](https://youtu.be/EHi0RDZ31VA?t=7444)

2:04:04
If we want to go ahead and create something a little more interactive, recall that there was that command a while back, namely
2:04:12
pip, whereby I ran pip install face_recognition. That's one of the examples with which we began.
2:04:17
And that allows me to install more functionality from a third party into my own code space or my programming environment more generally.
2:04:24
Well, we can have a little fun with this, in fact. Let me go back to VS Code here. And just like there's a command in Linux called cowsay,
2:04:30
whereby you can get the cow to say something, you can also use this kind of thing in Python. So if I do pip install cowsay, this, if it's not installed already,
2:04:39
will install a library called cowsay. And what this means is that if I actually want to code up a program called, like, moo.py, I can import the cowsay library,
2:04:48
and I can do something simple like cowsay.cow, because there's a function in this library called cow(),
2:04:55
and I can say something like "This is CS50," quote unquote. How do I run this program?
2:05:01
I can run python of moo.py, and-- oh, underwhelming. If I increase the size of my terminal window, run python of moo.py,
2:05:09
we have that same adorable cow as before, but I now have programmatic capabilities with which to manipulate it.
2:05:15
And so, in fact, I could make this program a little more interesting. I could do something like name = quote--
2:05:22
or rather, name = input("What's your name?") and combine some of today's ideas. And now I can say not "This is CS50," but something like,
2:05:29
quote unquote, "Hello," comma, person's name. And now, if I increase the size of my terminal, rerun python of moo.py,
2:05:36
it's not going to actually moo or say "This is CS50." It's going to say something like "hello, David," and so forth.
2:05:42
And suffice it to say through other functions, you can do not only cows but dragons and other fancy things, too.
2:05:48
But even in Python, too, can you generate not just ASCII art, but actual art and actual images.
2:05:54
And the note I thought we'd end on is doing one other library. I'm going to go back into VS Code here.
2:05:59
I'm going to close moo.py. I'm going to do pip install qrcode, which is the name of a library
2:06:06
that I might want to install to generate QR codes automatically. And QR codes are these two-dimensional bar codes.
2:06:12
If you want to generate these things yourself, you don't have to go to a website and type in a URL. You can actually write this kind of code yourself.
2:06:19
So how might I do this? Well, let me go into a new file called, say, qr.py.
2:06:26
And let me do this. Let me go ahead and import this library called qrcode.
2:06:34
Let me go ahead and create a variable called image, or anything else. Let me set it equal to this library's qrcodes function called
2:06:40
make-- no relationship to C. It's just called make because you want to make a QR code. Let me type in, maybe, the URL of a lecture video here on YouTube--
2:06:48
so, like, youtu.be/xvFZjo5PgG0, quote unquote.
2:07:01
And then I can go ahead and do img.save because inside of this image variable,
2:07:07
which is a different data type that this library gave me-- it doesn't come with Python per se-- I can save a file like qr.png, And I can save it in the PNG format, the Portable
2:07:18
Network Graphic. And so just to be clear, what this should hopefully do for me is create a QR code containing that particular URL,
2:07:26
but not as text, but rather as an actual image that I can send, I can post online, or, in our case, generate into my code space,
2:07:34
and then open. And so, with all that said, we've seen a bunch of new syntax today, a bunch of new features.
2:07:39
But the ideas underlying Python are exactly the same as they've been in C.
2:07:45
It's just that you don't have to do nearly as much heavy lifting yourself. And here, for instance, in just three lines of code,
2:07:51
can you generate a massive QR code that people can scan, as you can in a moment with your phones, and actually
2:07:57
link to something like a CS50 class. So let me go ahead and run python of qr.py.
2:08:03
It seems to have run. Let me run code of qr.png, which is the file I created.
2:08:09
I'll close my terminal window, allow you an opportunity to scan this here very CS50 lecture.
2:08:17
And-- and-- is someone's volume up?
2:08:25
[RICK ASTLEY, "NEVER GONNA GIVE YOU UP"] There we go. What a perfect ending. All right. That was CS50. We'll see you next time.
2:08:32
[MUSIC PLAYING]
