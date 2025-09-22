---
link: https://youtu.be/4vU4aEFmTSo
related_files:
  - week-2-notes.md
  - problemset/week-2-caesar.md
  - problemset/week-2-problemset.md
  - problemset/week-2-readability.md
  - problemset/week-2-scrabble.md
  - problemset/week-2-substitution.md
title: "Lecture 2: Week 2 - Arrays"
type: transcription
week/lecture: "2"
---

# [Lecture 2: Week 2 - Arrays](https://youtu.be/4vU4aEFmTSo)

TABLE OF CONTENTS:

0:00 - Introduction
1:01 - Story Time
6:04 - Compiling
28:43 - Debugging
47:28 - Memory
52:41 - scores.c
57:45 - Arrays
1:14:01 - Strings
1:33:12 - String Length
1:44:34 - uppercase.c
1:50:05 - Command-line Arguments
1:57:58 - Cowsay
1:59:50 - Exit Status
2:05:48 - Cryptography

## [Introduction](https://youtu.be/4vU4aEFmTSo?t=0)

0:00
[MUSIC PLAYING]

## [Story Time](https://youtu.be/4vU4aEFmTSo?t=61)

1:01
DAVID MALAN: All right. This is CS50. This is week 2 wherein we will ultimately learn how to use memory,
1:08
but we thought we'd first begin with a bit of story time. And in fact, allow me to walk over to our brave volunteers who
1:14
have joined us already. First here on my left, we have who? AKSHAYA: Hi, I'm Akshaya.
1:19
I'm a first year in Mathews, and I'm planning on concentrating in chemical and physical biology and CS.
1:25
DAVID MALAN: Wonderful, welcome. And let me have you hang on to the microphone first because we've asked Akshaya to tell us a short story.
1:31
So in your envelope, you have the beginnings of a story. If you wouldn't mind reading it aloud. And as she reads this, allow us to give some thought as to what
1:38
level Akshaya reads at, so to speak. AKSHAYA: All right, it's a long one, get ready.
1:43
One fish, two fish, red fish, blue fish. DAVID MALAN: All right, very well done.
1:50
What grade level would you say she reads at if you think back to your middle school, grade school, when maybe teacher said you read at this level or maybe this level or this one
1:59
here? So OK, no offense taken yet. AUDIENCE: 1st grade.
2:05
DAVID MALAN: I'm sorry? AUDIENCE: 1st grade. DAVID MALAN: 1st grade. OK, so first grade is just about right. And in fact, according to one algorithm, this text here,
2:12
one fish, two fish, red fish, blue fish, would indeed be considered to actually be 1st grade or just before first grade.
2:17
So let's-- and why is that, though? Why did you say 1st grade? AUDIENCE: It's very basic.
2:23
DAVID MALAN: It's very basic. But what is it about these words that are very basic? Do you want to identify yourself? AKSHAYA: Sure.
2:28
They're all one syllable and they're very simple like colors and stuff like that. DAVID MALAN: Spot-on. So like they're very short words they're very short sentences.
2:35
And you would expect that of a younger person. All right, let's go ahead and hand the mic to your next volunteer
2:40
here if you'd like to introduce yourself. ETHAN: Yes. Hi, I'm Ethan. I'm a first year in Canada, and I'll be concentrating in economics.
2:46
DAVID MALAN: Wonderful. And in your folder, we have another story to share. ETHAN: Congratulations.
2:52
Today is your day. You're off to great places. You're off and away. DAVID MALAN: So this text might sound familiar, particularly
2:59
on the heels of high school, perhaps. What grade level might he be reading at?
3:05
So maybe 5th grade. And why 5th grade? AUDIENCE: [INAUDIBLE] DAVID MALAN: OK.
3:11
Yeah. So a little more complicated. Like the words-- we've got some more punctuation, we have an apostrophe,
3:16
we have longer sentences. And indeed, according to one algorithm, not quite 5th grade, but we would adjudicate your reading level to be 3rd.
3:22
But let's see if we can't do one final flourish here if you'd like to introduce yourself and your story.
3:28
MIKE: Hi, I'm Mike. I'm also a first year. I'm in Weld, and I'm planning on concentrating in biomedical engineering.
3:34
DAVID MALAN: Welcome. And your tale? MIKE: It was a bright, cold day in April and the clocks were striking 13.
3:41
Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors
3:49
of victory mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.
3:55
DAVID MALAN: All right, so escalated quickly. And someone's guess at this reading level? AUDIENCE: 1984.
4:01
DAVID MALAN: What's that? Oh, OK, 1984 is indeed the text in question, and in what grade did you perhaps read that book?
4:08
So I'm hearing 8th, I'm hearing 10th. So indeed, 10th grade is what a certain algorithm would actually adjudicate that reading level to be at.
4:14
And consider now the heuristics. So we started with very small words, very small sentences, very easy words, and then things sort of escalated into more interesting, more
4:21
sophisticated English, more interesting sentence construction and the like. So I bet if we could somehow capture those characteristics of text,
4:30
the length of the words and the lengths of the sentences and the position of the punctuation, I daresay,
4:35
even using week 1 material and, today, week 2 material, we'll be able to actually write code and implement an algorithm like that
4:41
can take these spoken words, put them to paper, and actually analyze roughly what that reading level might be.
4:47
So that's just a teaser of what lies ahead. For now, allow us to thank our volunteers, each of whom gets a wonderful parting gift here to read at home.
4:55
[APPLAUSE] All right. And Thank you all so much.
5:01
So with that said, there's another domain that we'll explore this week, and indeed, what you'll find in the coming weeks
5:07
is that beyond just focusing on some of the fundamentals and the basics like we've really done in the past couple of weeks talking about loops
5:14
and conditionals and Boolean expressions, really building blocks or puzzle pieces that we can assemble together,
5:19
we're going to increasingly start talking about applications of these ideas which, after all, is why any field is perhaps
5:25
important and applicable. So here, for instance, we'll consider not only reading levels today, and in turn, in problem set 2 this week, but also the world of cryptography,
5:33
which is the art, the science of scrambling, encrypting information, and ciphering it in such a way
5:39
that you can send a message securely through the internet, through the air, through any medium even though someone might intercept it.
5:46
Ideally, thanks to cryptography, they shouldn't be able to decrypt it or actually determine what it there says.
5:53
So for instance, if you were to receive a message like this, at first glance, it's indeed a bit cryptic.
5:59
Three words maybe, but by day's end, we'll have decrypted even this message for you.

## [Compiling](https://youtu.be/4vU4aEFmTSo?t=364)

6:04
So up until now, though, we've had some sort of conceptual training wheels on. And I gave us this picture last week when we introduced the tool make via
6:12
which you can make programs out of your source code because you need to turn that source code into machine code, the 0's and 1's.
6:18
And in the middle here was this thing called a compiler. But it really has been kind of an abstraction for us,
6:23
and we've sort of had these metaphorical and physical training wheels here in the sense that we haven't really
6:30
needed to care like what the compiler is doing, how it works and so forth. But today, what we thought we'd do is peel back a bit of that layer so
6:38
that even though after today you'll continue to be able to use commands like make and sort of return to the beautiful abstraction that is not caring about some
6:46
of these lower-level details, we'll offer you a glimpse of how some of these things work. Because so that inevitably when something goes wrong,
6:52
you've got some bug, you're having some problem, you'll have a bottom-up understanding of what it could actually be.
6:58
And indeed, these basics, you'll find, will very often help you troubleshoot problems and really solve problems more generally.
7:05
So here, for instance, is the code that we keep coming back to. And this code here is the simplest of C programs that just says "hello, world."
7:12
This is the source code. This, we claimed, was the corresponding machine code. And it was that program called a compiler that
7:18
converted one into the other. But let's dive a little more deeply this week into what we mean by compiling code.
7:25
Like what is happening so that by day's end, nothing really feels like magic anymore. It's not just that it goes from source code to machine code
7:33
and that's that, you understand what's actually being done for you, and frankly, what other humans have done over the decades to make
7:40
make as beautifully abstract and as simple as it now might seem to be. So here are a couple of commands that you've
7:47
been in the habit of running when you want to first compile your code and then execute your code. But it turns out that make is actually running another command for you.
7:56
The first of several white lies we'll tell in the course is that make itself is not a compiler, per se.
8:02
It's actually a program that automatically runs a compiler for you. And by that, I mean this.
8:07
Let me go over to VS Code here and let me create our familiar hello.c program.
8:13
And I'm going to go ahead and do include stdio.h, int main void, and inside
8:20
of the curly braces, printf "hello," comma, "world," backslash n semicolon. So that's the code that we keep writing again and again.
8:27
And up until now, if I wanted to compile that, I would do make hello dot slash hello, and voila, now my program is made
8:35
and it actually executes. But what's actually going on underneath the hood there is that make is running an actual compiler for you,
8:43
and the reveal today is that the compiler we have been using is something called Clang for C language.
8:49
And this is just another program whose purpose in life is actually to do the conversion of source code to machine code.
8:54
But it turns out that Clang by itself can be used very simply like you see here, clang hello.c,
9:00
but it doesn't behave nearly as user-friendly as you might like. So in particular, let me go ahead and do this.
9:06
I'm going to go ahead and remove my compiled program by running rm for remove, which I alluded to briefly last time.
9:12
And then I'm going to say y for yes, remove that regular file. And if I go ahead now and run just clang of hello.c and hit Enter,
9:21
it seems to be successful, at least insofar as there's no error messages. But if I try to do dot slash hello, Enter,
9:27
there is no such file or directory called hello. That is because by default, Clang somewhat goofily like just
9:34
outputs a file name called a dot out. Like why a? Well, it's sort of a simple name. a dot out, technically for assembler output,
9:42
but this just means this is the default file name that Clang is going to give us. So OK, it turns out I can do dot slash a dot out Enter, and voila,
9:49
that now is my program, but that's just a stupid name for a program. It's not very user-friendly.
9:54
It's certainly not an icon you would want to put on people's desktops or phones. So how can we do better?
10:00
Well, it turns out, with Clang, we can configure it using what we'll call command line arguments.
10:05
And command line arguments are actually something we've been using thus far, we just didn't slap this word on it, but command line arguments
10:12
are additional words or shorthand notation that you typed at your command prompt that somehow
10:18
modify the behavior of a program. And you can perhaps guess where this is going. It turns out that if I actually want to create a program called hello--
10:28
not a.out, which is the default, I can actually do this-- clang, space, dash lowercase o, space, hello,
10:36
or whatever I want to call the thing, space, hello.c. And now if I hit Enter, nothing seems to happen,
10:42
but now if I do ./hello and Enter, now I've actually got that program.
10:48
So why is make useful? Well, it just saves us the trouble of having to type out this longer line of command any time
10:55
we actually want to compile the code. But in fact, it gets even worse than that with commands like clang or compilers in general
11:01
because consider this code here. Not just the version of "hello, world," but maybe the second version wherein
11:08
last week, I started to get user input by adding the CS50 Library using get_string and then saying, "hello," comma, "David."
11:14
Well, if I go back to VS Code and I modify this program to be that same one--
11:19
so let me go ahead and include cs50.h at the top. Let me get rid of this simple print line and instead give myself
11:27
a string called name equals get_string, "What's your name?"
11:33
Question mark, just like we did in Scratch. Then I can do printf, quote-unquote, "hello," comma.
11:39
And previously I typed "world." I obviously don't want to type "David" because I want it to be dynamic. What did I type last week for as a placeholder?
11:47
So yeah, just-- not Command-S, but %S. So %S in this case, which is a placeholder for any such string.
11:53
Then I can still do my new line, close, quote, comma, and then I can substitute in something like the value of the name variable.
12:00
All right, so if I go ahead now and compile this, now last week, I could just do make hello and I'm on my way,
12:06
it worked just fine. But if I instead do clang manually, it turns out that this is not going to be sufficient now. clang -o hello, space, hello.c.
12:16
Exact same thing I typed a moment ago, but I think I'm going to see some errors.
12:21
So what's this error hinting at here? Well, at the very bottom, it's a bit arcane with its output,
12:27
and much of this you can ignore, but there are some certain key words. What's the first maybe keyword you recognize in these three
12:33
lines of erroneous output? So it mentions main. That's not that much of a clue because that's the only thing I wrote so far.
12:40
Second line, though, get_string. There's some issue with an undefined reference to get_string.
12:46
Now why might that be? I did include cs50.h, but that's apparently not
12:51
enough to teach the compiler about get_string. Well, it turns out that if you're using a third-party library, one
12:58
that doesn't necessarily come with C the language, something like CS50's, it turns out that you additionally have to tell the compiler that you
13:05
want to use that library. And not just by including the header file, but by an additional command as well.
13:11
So when you run Clang, you want to provide an additional rather command line argument.
13:16
Literally -l for library, which is a term I used last week, cs50. A library is just code that someone else wrote
13:23
that you want to use in your project. So if I really want to compile this version that uses the CS50 Library,
13:29
I can still do clang o hello hello.c, but before I finish my thought,
13:34
I need to tell the compiler to link, so to speak, in the library CS50.
13:40
And now I hit Enter, the error message goes away, I can do ./hello, I can type in my name, and voila, we're back to week 1.
13:47
And this is why, suffice it to say, we introduce make, which is not a CS50 thing. This is a popular tool that real people in the real world
13:54
use to automate these kinds of processes. So unbeknownst to you, make has been using the -o for you. make, unbeknownst to you, has been using -l cs50 for you
14:03
just because it makes our lives easier. But today, we thought we would deliberately peel back this layer so we at least understand
14:11
what's going on behind this abstraction that is make itself and compiling more generally.
14:17
So let me propose that compiling itself is not quite what we've described it to be.
14:22
Compiling is like this catch-all phrase that apparently I claim goes from source code to machine code. But if we really want to get pedantic, which we'll do briefly,
14:30
but this is not a sign of things to come because this, too, will be abstract away, compiling is just one of four steps that are involved
14:39
in turning source code that you and I write into those 0's and 1's. But through an understanding of these four steps
14:45
today, you'll hopefully better understand how to troubleshoot issues like that and just know what's happening because it's not, in fact, magic.
14:51
It's just the result of years of humans developing these four steps here. So when you run make, what's happening?
14:58
Or in turn, when you run clang, four different things are happening. And the first one is called pre-processing.
15:04
So what is this all about? Well, let's consider this code here. And this code is a little bit interesting
15:09
insofar as it's one of the more complicated examples from last week. And you'll notice, for instance, that I had include stdio at the top
15:18
so I could use printf. I had main down here, whose purpose in life was just to meow three times.
15:24
And then recall we made our own meow function just like we did in week 0 with Scratch that just printed out, quote-unquote, "meow."
15:31
But I also included this line here, which we called what?
15:37
This was a prototype. And why did I have to include it there? Or equivalently, what would happen if I didn't include a prototype up
15:45
at the top there? Yeah? AUDIENCE: [INAUDIBLE]
15:51
DAVID MALAN: Exactly. If I didn't include it up here, the program, when trying to compile main, would not know what meow is because it's not defined until later.
15:59
So this is kind of like a little hint of what is to come. Alternatively, we could just move this whole thing up at the top of the file,
16:05
but I claim that just devolves into a big mess eventually once you have many different functions. Like you can't realistically put them all at the top to solve this problem.
16:13
So these prototypes solve that problem. So nothing new here. Just a reminder of what motivated this one line of prototype.
16:20
Now let's consider this simpler program, which is just the one we wrote most recently in VS Code.
16:26
This program prompts the human for their name and then says hello to that person. But it has two includes at the top of the file.
16:33
And in fact, any line of C that starts with this hash symbol is what we'll call now a preprocessor directive.
16:40
It's not really a word you need to remember in your vocabulary, but it is a little bit different from most every other line
16:46
because it starts with that hash. That's a special symbol in C. And what this means is the following.
16:52
This very first line, cs50.h, is indeed a file that I and CS50 staff wrote and we installed somewhere in VS Code for you, somewhere in the cloud.
17:02
And I've claimed you need to use this header file in order to use get_string.
17:07
So just logically, what is probably inside of cs50.h?
17:15
Yeah? AUDIENCE: Function [INAUDIBLE].
17:23
DAVID MALAN: Super close. So the function called get_string that does the getting of a string, but it's not quite as much as the function itself.
17:30
It's actually a little bit less than that, but you're on the right track. What is inside of cs50.h, presumably?
17:37
Just a what? Just a prototype for?
17:43
Which function? get_string. So admittedly, there's some other stuff in there, too, but the important line for today's discussion is that inside of cs50.h
17:51
is indeed one line of code that defines what the return value, what the name is, and what the arguments, if any, are to get_string,
17:59
and some other stuff. And so what happens effectively when you compile your code,
18:05
step 1 is this pre-processing line. And essentially, there is some code that someone else wrote inside of the clang compiler that looks for a line that starts with hash include,
18:13
and when it sees that, it goes and finds this file and effectively copies and pastes the contents of that file right there into your code
18:21
so that you don't have to go find the file, copy and paste it, and make a mess of your own code. So in particular, it's effectively as though you're copying and pasting
18:29
the prototype of get_string to the very top of your file, thereby teaching the compiler that it exists.
18:35
By that same logic, what is probably in stdio.h?
18:41
The prototype for? For printf. And indeed, exactly that. So this line effectively gets replaced with the equivalent
18:49
of the prototype for printf, which, for today's purposes, is a bit more complicated, so let me wave my hand at the dot-dot-dot
18:55
just because it takes a variable number of arguments depending on how many placeholders or format codes you have.
19:00
But effectively, that, too, is what's happening. So the preprocessor step, step 1 of 4, just
19:06
does that find and replace, if you will. Now there's some-- again, some other stuff in that file, and this, too, is kind of a white lie. printf
19:12
probably has its own file because that's a really big library, but the essence of it is exactly this.
19:17
So preprocessing converts all of those hash include lines to whatever the underlying prototypes are
19:24
within the file plus some other stuff. Now compiling we use it as this catch-all phrase, but it turns out,
19:29
it has a very specific meaning that's worth knowing about even though after today, you can go back to using compiling as the sort of catch-all phrase.
19:37
So when you've got this same code here after the pre-processing step has happened.
19:42
So this is essentially happening in the computer's memory. It's not changing your hello.c file permanently or anything like that.
19:49
This code gets, quote-unquote, "compiled" into something
19:54
that looks more like this. And this is a scarier language that we won't spend time on in this particular class.
20:00
This is what's known as assembly language. And back in the day, before there was C, humans
20:06
wrote this to program their computers. Similarly, before there was assembly code back in the day,
20:12
humans very initially used what instead? AUDIENCE: 0's and 1's. DAVID MALAN: So 0's and 1's-- like they actually wrote the machine code
20:19
painfully, be it in code or be it in punch cards like physical objects or the like. So again, these are sort of abstractions,
20:25
but we're rewinding for today in time. But what this compiler for C is doing is converting C
20:30
into this other language called assembly language. And even though this looks very esoteric, there's at least some juicy things in here.
20:37
If I highlight get_string, it's mentioned in this code. printf is mentioned in this code. And even some of these keywords here that
20:44
are spelled a bit weirdly, this relates to subtracting and moving something in memory and calling a function, calling a function.
20:51
So there's some semantics that are probably somewhat familiar even though this is not code we ourselves will write.
20:56
But unfortunately, this is not yet machine code, and that's where step 3 comes in.
21:02
So step 3 of this four-step process is technically called assembling. And assembling just takes that assembly code and converts it, thankfully,
21:12
to the thing we do care about, the 0's and 1's. So assembling takes assembly code converts it to 0's and 1's.
21:18
As an aside, and I alluded to this earlier, the reason that Clang names its files a.out by default, assembler output,
21:26
is a side effect of that being one of the steps in this process, dealing with assembly language and its subsequent output.
21:33
All right, so here are some 0's and 1's, but unfortunately, there's still that fourth and final step, which is a word that I also used earlier,
21:41
namely linking. So let me take a step back and look at this code here. And even though this code is exactly as I wrote in VS Code in hello.c--
21:50
so no copying and pasting, no prototypes have been plugged in here, this is my code, technically, there's
21:55
three different files involved in compiling even something relatively simple like this. There's obviously this thing itself, hello.c, which I wrote.
22:03
There's apparently cs50.h, and there's apparently stdio.h.
22:08
But technically-- and you don't have to know this file name, per se, somewhere else on the computer's hard drive, so to speak,
22:15
is a cs50.c file, which actually contains the staff's implementation of get_string and get_int and get_float
22:22
and all of those other functions. Somewhere on the server's hard drive is stdio.c
22:28
that implements printf and all of these other functions as well. So the dot c is just inferred from the dot h here.
22:34
You don't ever mention the dot c file, but someone else wrote those files, someone else stored them in the server for you--
22:41
CS50 staff in this case. So technically, even when compiling a relatively short program like this,
22:47
you're really combining three files at least at the end of the day. And I'll write them from left to right. hello.c,
22:54
which I wrote, cs50.c, which the staff wrote, and then stdio.c as well.
23:01
So somewhere there's these three files. And Clang, our compiler, needs to compile each of these
23:08
into the corresponding 0's and 1's. Lastly, this is not yet sufficient because these 0's and 1's haven't
23:17
been linked together. I mean, I deliberately left a gap here to imply that these are three separately-compiled files.
23:22
So that fourth and final step called linking takes all of these 0's and 1's and an intelligent way
23:28
combines them into just one final file named hello, named a.out,
23:35
whatever the file name is of choice. So what you and I for the past week have just been calling compiling--
23:40
and that's what a normal person will use henceforth to describe this whole process, technically, there's
23:46
these four different steps underneath the hood, each of which is sort of a representative of an evolution of technology over the years.
23:55
And nowadays, if we fast forward a few weeks in class, when we start talking about Python, which is another more modern language, that, too, is going to be conceptually even
24:03
higher level, even though underneath the hood, there's going to be some lower-level principles at work.
24:09
So any questions on just terminology or these processes known as compiling?
24:16
Yeah? AUDIENCE: I didn't really understand what compiling means. [INAUDIBLE]
24:21
DAVID MALAN: Sure. Compiling, if I rewind, is the process of taking your source code, which
24:29
looks like this, recall-- whoops, this, and converting it into assembly code.
24:35
So preprocessing just converts all of those hash include lines and a few others to their equivalents.
24:41
So that's step 1. Compiling converts the C code into the underlying assembly code.
24:46
The assembling step, step 3, converts the assembly code to 0's and 1's. And then the fourth step, linking, combines
24:54
all of the 0's and 1's from the one, the two, the three or more files that are involved in your project and links them
25:00
all together for you magically. But at the end of the day, all of this is happening automatically for you.
25:06
If I jump now to the end here, whereby just by running make, which, in turn, runs clang for you, like all of this
25:14
is abstracted away. But the key here is that even with these commands that we've been running,
25:19
be it the make command or the clang command, everything should be explainable what you are typing at the prompt
25:28
ultimately. Each of those things has a purpose. So any questions, then, on what we've just
25:33
now called compiling even though it's only when you take another CS course that you might spend more time on assembly
25:40
language or these lower-level details? Yeah? AUDIENCE: [INAUDIBLE]
25:47
DAVID MALAN: A good question. Are there other types of compilers? Yes. Back when I took CS50, I used a popular compiler called GCC, the GNU Compiler
25:57
Collection, which still exists actually in the code space that you're using for CS50. Clang is somewhat more recent.
26:04
It's gaining popularity. And frankly, we use it in large part because it's error messages are slightly more user-friendly.
26:09
You might not believe us because if you encountered some errors with your code this past week, they were probably just as arcane as the error messages I saw,
26:16
but it's better than it was some years ago. And there's alternatives to compiling, too, but more on that when we get to Python as well.
26:24
Other questions? No? All right. Well, what are the implications of the fact that we're going from source code
26:31
to machine code? Well, it stands to reason that if you can compile code, maybe you can decompile it-- that is, go in the reverse direction.
26:38
Go from 0's and 1's to actual source code. Now that would be handy if you want to go in as a programmer and change
26:45
something in a program that you or someone else already wrote. It's maybe not ideal for your intellectual property,
26:51
though, if you are the person who wrote that program in the first place. If you are Microsoft and you wrote Microsoft Word or Excel
26:57
that people with Macs and PCs and phones have installed on their devices, it doesn't actually sound very appealing if any old customer
27:04
can take those 0's and 1's and reverse them, reverse engineer them, so to speak, into the original source code
27:11
because then they can have their own version of Microsoft Word and make changes to it without really having put in all of the R&D
27:17
that it might have taken to build the first version thereof. But it turns out that reverse engineering--
27:22
so doing things in the opposite direction-- is easier said than done because there are multiple ways, as you've seen already,
27:29
to implement programs. Like loops alone, you can use for loops, while loops, even do-while loops.
27:35
And so there's other ways-- there's multiple ways to solve the same problem. So even if you try to reverse engineer a program
27:41
and convert machine code back to source code, there's not necessarily going to be an obvious way to do so.
27:48
And the reality is, that it ends up being such a mess because you lose the variable names typically,
27:53
you lose the function names typically, that what you end up looking at might very well be C code, but it's completely difficult for you,
28:01
even a good programmer, to read. And generally, the mindset is, if you're really good enough
28:06
to decompile code in that way and read it subsequently even without good variable names, good function
28:11
names, good documentation and the like, could probably have just implemented the program in the first place yourself without jumping through those hoops.
28:18
So there's some practicality pushing back on what are otherwise potential threats to, say, your intellectual property.
28:25
But that's not going to be the case later on in the term when we do get to languages like Python to some extent, other languages
28:31
like JavaScript. Some of those are actually going to be readable by anyone. Any of your customers, any of your friends,
28:36
and your family that actually use your programs. So with that said, let's introduce now another tool to our toolkit

## [Debugging](https://youtu.be/4vU4aEFmTSo?t=1723)

28:43
that will hopefully make some of the pain from this past week when you did encounter bugs a little more manageable.
28:49
And indeed, part of the process of writing code to this day is debugging it. And it is a rare thing to write a program,
28:56
be it in C or any other language, and get it 100% right the first time. I mean, to this day, I still, 20-plus years later, still write buggy code.
29:05
Hopefully a little bit less of it, but any time you're adding a new feature, any time you're doing something for the first time,
29:10
you're not necessarily going to see all of the possible mistakes. So even in industry, bugs are omnipresent, which is really to say,
29:18
having techniques to debug code-- that is, eliminate bugs, is super compelling. Now just for a bit of history, here is Admiral Grace Hopper,
29:26
who was actually in not only the military, but also on the faculty of Harvard years ago
29:33
and worked on a Harvard computer called the Harvard Mark I, which is actually on display at the School of Engineering and Applied
29:39
Sciences if you take a tour over there sometime. But also when working on the Harvard Mark II, she is known for having at least popularized the phrase "bug" to mean
29:50
a mistake in a computer's program-- a mistake in a computer's code.
29:55
And the etymology of this supposedly is this here logbook wherein she and her colleagues were documenting processes being computed
30:02
on computers, that a moth actually got stuck in one of the relays, one of the mechanical-- the electric relays inside
30:09
of the very old now computer, and someone very cleverly wrote, "First actual case of bug being found."
30:16
So it wasn't she who actually discovered it, but this was a story she was thereafter fond of telling as a famed computer
30:22
scientist thereafter. We now know bugs to be all too familiar when it comes to writing our own code,
30:28
and I thought I would deliberately write some buggy code based on some of the programs with which we experimented last week.
30:34
So let me go back over to VS Code here and let me propose that I do something somewhat simplistic just like this to print out
30:44
a column of bricks of height 3. So I'm going into VS Code and I'm going to deliberately call this program
30:50
buggy.c because I intend to do this poorly. I'm going to include stdio.h as before, int main void as before.
30:58
And in here, if I want to print a pyramid of height 3, I'm going to do 4 int i gets--
31:04
all right, I'm still new to programming in my mind here, so I know I'm supposed to start counting at 0, OK.
31:09
And I want to do this until I count up to 3, so I'm going to do that. And then i++ I remember from class in this way.
31:16
And now I might go ahead and print out just a hash mark, backslash n, which I do want because I want to move this cursor to the next line
31:23
to make this vertical. But of course, if you've noticed with your eye already, when I do make buggy,
31:29
it compiles OK. So no typos, no syntactical errors. But when I run this, I'm going to see how many bricks.
31:37
So four in this case. Now this is meant to be a simplistic example so that we don't spend time trying to figure out what the bug is, but rather,
31:44
focus on techniques for actually identifying the bug. So-- finding, rather, the bug.
31:50
So what's one of the first tools in your toolkit? Literally one you have already. printf is your friend.
31:55
And it is a very quick and dirty tool for just seeing what's going on inside of the computer when
32:02
you don't have more sophisticated tools or even the time to use them. And so in this case, for instance, what I'd propose is that--
32:09
all right, I'm obviously seeing four hashes. And let me play a little slow here. It'd be helpful for me to understand why logically I'm ending up with four, even
32:18
though I'm starting at 0 like I remember from class and I'm going up to 3 as we did in class, like I'm just not seeing it in this particular story.
32:25
So what I would commonly do is go into my code and just help me see what's going on, and I might literally write a printf line like, i is %i,
32:35
backslash n, comma, and then just print out the value of i. I just want to see on every iteration, what
32:41
is i, what is i, what is i just to help me see what the computer already knows. So let me go ahead and recompile buggy, let me rerun buggy,
32:49
and then let me make my terminal window bigger just to make clear what's going on. And now it's a little more pedantic.
32:56
Now i is 0, I get a hash. i is 1, I get a hash. i is 2, I get a hash.
33:01
Wait a minute. i is 3, I get a hash. So clearly now, it should be maybe more obvious to you,
33:07
especially if the syntax itself is unfamiliar, I certainly don't want this last one printing, or maybe equivalently, I don't want the first one printing.
33:14
So I can fix this in a couple of ways, but the solution, the most canonical solution is probably to do what with my code?
33:22
To change to what to what? Yeah? AUDIENCE: [INAUDIBLE] DAVID MALAN: Yeah. So change the less than or equal sign to just a less than sign.
33:31
So even though this is like counting from 0 to 3 instead of 1 through 3,
33:36
it's the more typical programmatic way to write code like this. And now, of course, if I do make buggy--
33:43
and I'll increase my terminal window again, ./buggy, now I see what's going on inside of the code.
33:49
Now it matches my expectations, and so now the bug is gone. Now of course, if I'm submitting this or shipping it,
33:55
I should delete the temporary printf. And let me disclaim that using printf in this way just to help you
34:00
see what's going on is generally a good thing, but generally adding a printf and a printf and a printf and a printf--
34:06
like it starts to devolve into just trial and error and you have no idea what's going on, so you're just printing out everything.
34:13
Let me propose that if you ever find yourself slipping down that hill into just trying this, trying this, trying this,
34:20
you need a better tool, not just doing printf. And frankly, it's annoying to use printf because every time you add a printf,
34:26
you have to recompile the code, rerun the code. It's just adding to the number of steps.
34:31
So let me propose instead that we do this. I'm going to go back into VS Code here and I'm
34:37
going to write a different program that actually has a helper function, so to speak.
34:42
A second function whose purpose in life is maybe just to print that column for me. So I'm going to say this-- void print_column,
34:50
though I could call it anything I want, and this function is going to take a argument or a parameter called
34:56
height which will tell it how many bricks to print, how many vertical bricks. I'm going to do the same kind of logic. for int i equals 0.
35:05
i is less than-- I'm going to make the same mistake again-- less than or equal to height, i++. And then inside of this for loop, let me go ahead and print out the hash mark.
35:14
So I've made the same mistake, but I've made it in the context now of a helper function only because in main,
35:20
what I'd like to do now, just to be a little more sophisticated is get int from the user for the height.
35:27
And when I do get that int, I want to store it in a variable called n, but I do need to give that variable a type like last week.
35:34
So I'll say that it's an integer. And now, lastly, I can print_column, passing in-- actually, I'll
35:40
call it h just because height is h. Print column h, semicolon.
35:46
OK, so it's the exact same program except I'm getting user input now. So it's not just going to be 3, it's going to be a variable height,
35:53
but I've done something stupid. AUDIENCE: [INAUDIBLE] DAVID MALAN: I've done two stupid things.
35:58
So this, of course, is not supposed to be there, so I'll fix that. And someone else. What else have I done?
36:05
AUDIENCE: [INAUDIBLE] DAVID MALAN: Yeah. I'm missing the prototype.
36:11
And this is, let me reiterate, probably the only time where copy-paste is OK. Once you've implemented the function, you
36:17
can copy paste its first line at a semicolon so that it teaches the compiler that this function will exist.
36:25
AUDIENCE: [INAUDIBLE] DAVID MALAN: Three stupid things. OK. Thank you. So, good.
36:31
Include cs50.h. And now, anyone want to go for four?
36:36
No? All right. Slightly unintended here. So let's see. make buggy.
36:42
OK, no syntax errors thanks to you all. So the code compiles, but of course, when I run buggy
36:47
and I type in something like 3 manually, I'm still going to get 1, 2, 3 4 out.
36:52
So let me now introduce a more powerful tool that's generally known as a debugger. And within the VS Code environment that you're using,
36:58
we actually have a command that makes it a little easier to use this tool, but we didn't write the tool itself. You are about to see a very graphical, a very popular industry standard
37:07
tool called a debugger, but we'll start the debugger using a CS50-specific command called debug50, which just makes it easier with a single command
37:15
to start the debugger without having to configure a text file with all of your preferred settings and all of that. It's just an annoying hoop otherwise to jump through.
37:22
So what I'm going to do is go back to my code here. I have already compiled it, but just for good measure,
37:27
I'll make buggy again because the debugger needs your code to be compiled. It's not going to help with syntax errors
37:33
like the stupid mistakes I just made unintentionally, it will help you though with programmatic errors, logical errors
37:40
in your code once your code is running. So to run debug50, I'm going to do this. debug50, space, and then
37:47
the exact same command I would normally run to just run the program itself. So ./buggy.
37:53
So exact same thing, ./buggy, but I prefix it now with debug50. When I hit Enter, a whole bunch of--
37:59
another error is going to pop up on the screen, which is a good reminder because this will happen to you, too, invariably.
38:04
It's reminding me that I have to set what's called a breakpoint. And as that word suggests, it is the point
38:10
at which you want your code to break. Not break in make the situation worse sense, but rather,
38:15
where do you want to pause? Execution, break, execution-- like hitting the brakes on a car
38:20
so the program doesn't run all at once. And you can put this any number of places, and you might have done this accidentally
38:26
if you've ever hovered over the gutter of VS Code, the left-hand side next to your line numbers.
38:32
See the little red dot that appears? If I click on any of these lines, that's going to set a breakpoint, so to speak.
38:38
And I want to break execution at main. So I'm just going to click to the left of line 6 in this case.
38:44
That makes it a darker red circle, a stop sign of sorts that tells the debugger to pause execution on that line,
38:51
though I could put it elsewhere if I so choose. Let me go ahead and rerun debug50 ./buggy, Enter,
38:57
and now a bunch of things are going to happen on the screen. It's going to look a little overwhelming perhaps at first glance,
39:03
but there's some useful stuff that just happened. So one, my code is still here, but the line that I set the breakpoint on is--
39:12
rather, the first line of actual executable code at or below the breakpoint I set is highlighted in this yellowish green
39:20
here, which says, this line of code has not yet been executed. We broke at this point, but if I click a button, this line of code
39:28
will be executed. Because up until now, every C program you write runs as fast as that.
39:33
I want to pump the brakes and pause here. But notice a few other aspects of the window here.
39:39
So notice that up here some weirdness. There's mentions of variables and we're familiar with these. Local is a term we'll use this week.
39:45
But there's this variable h, which weirdly, where did the value 21912 come from?
39:51
So it turns out, in C, before you initialize a variable with a value
39:57
by literally typing the number 3, or by using a function like get_int, it often contains what's called a garbage value.
40:04
More on those in a couple of weeks. But a garbage value is you can think of it as like remnants of whatever was in the computer's memory
40:10
before you ran your program. And that's a bit of a oversimplification, but you cannot trust that a variable will have a certain value in this case
40:18
if you did not put one there yourself. So for now, h is nonsensical.
40:23
It's a garbage value it means nothing. But once I execute this line, it should contain whatever the human types in.
40:29
All right. Down here, there's a watch section, which is a more sophisticated feature. Down here is what's called the call stack.
40:34
More on that in the future. But what this means for now is that I'm executing the main function, not, for instance, print_column.
40:40
So notice up here, these are the most useful controls within the interface. If I hit this Play button, it's just going
40:46
to actually run my program to the end of it without bothering me further. However, I can actually step over this line of code and execute it,
40:54
or I can step into this line of code and actually poke around the contents of get_int if it's available on the system.
41:01
So conceptually you can either execute this line or you can dive down conceptually deeper and see what's inside of that function.
41:08
Lastly, this will let you step out, this will allow you to restart the whole process, and this will just stop the debugger.
41:13
So these buttons are going to be our friends. And the one I'll click first is the first one I described,
41:19
which is step over. So step over doesn't mean, skip this step, it just means execute it,
41:26
but don't bother me by going into the weeds of what is on the specific line, namely get_int. So when I click this button in a moment, you'll
41:32
see that my terminal, which is still at the bottom, prompts me for a height. I'm going to go ahead and type 3.
41:38
As soon as I hit Enter, what part of the screen probably will change based on what I've said?
41:44
So h, the variable h should hopefully take on the number 3.
41:50
And I'll probably see a different line of code highlighted, probably line 9 next once I'm done executing line 8.
41:57
So let me go ahead and hit Enter and watch the top-left of the screen. And voila, h now has the value 3, and execution has now paused on line 9
42:08
because the debugger is allowing me to step through my code line by line. Now let me go ahead and print out-- let me go ahead and just say, all right,
42:16
I'm done with this. Let's go ahead and run the rest of the program. It clearly got the value 3. But wait a minute--
42:22
oh, and at this point, it closed the window in which I would have seen the output, I would have still seen four hashes.
42:28
So let me actually do this again. Let me go back into debug50 by running the exact same command again.
42:34
It's going to think for a moment, it's going to reconfigure the screen. I'm going to do the exact same thing. I'm going to step over this line, but I'd
42:41
like to actually see what's going on inside of my print_column function. So this time, instead of just saying run to the end
42:48
and close all the windows on me, let me go ahead and step into my print_column function.
42:54
So don't step over, step into. Because if I step over-- and now this is what I meant to show earlier,
43:00
you can see that it's still printing out 4. So in fact, let me undo this, let me just stop the whole thing.
43:05
Let me rerun the command a final time. So it goes back to where we began before. It's going to prompt me again once I step over line 8 for a number like 3.
43:15
But this time, instead of stepping over line 9, let's poke around. I wrote print_column, so let's look at print_column step by step,
43:23
step into it, and watch what happens to the yellow highlight. It now jumps logically to the inside of print_column,
43:30
thereby letting me walk through this code. And now I can just step over each of these lines one at a time.
43:35
So stepping over. OK, so what did it do? It did that whole narrative that I did verbally last week
43:41
where it compared i against height. It then went inside of the loop. When I click Step Over, watch what happens in my terminal-- one hash
43:48
prints out. Now line 14 is highlighted again. It's comparing per the Boolean expression, i,
43:54
is it less than or equal to height? If so, it's going to go ahead and print out the hash.
43:59
It's going to do this again, print out the hash. But notice at the top-left of the screen, height
44:05
is still the same, it's still 3, but what has been changing, apparently?
44:10
i on each iteration. So the debugger is letting me see what's going on slowly inside of this loop
44:16
because i keeps getting incremented. So if I step over this line now, notice that I've now printed 3.
44:21
So ideally I want this loop to end, but if I click Step Over once more, notice that the value of i at top-left is 3,
44:29
but 3 is less than or equal to height-- oh, now I get it, if I play along here.
44:35
Now I see why less than or equals to, mathematically, is clearly incorrect. And as soon as that light bulb goes off, you can just sort of
44:43
bail out, click the red Stop button to turn the debugger off, go back in, fix your code, and voila, recompile, run it,
44:50
and you're back in business. So the takeaways here really are just what tools now exist? Printf is your friend, but only for quick-and-dirty debugging techniques.
44:59
Get into the habit now of using debug50, and in turn, VS Code's debugger.
45:04
You will invariably not take this advice, say, for problem set 2 as you first begin because it's
45:11
going to feel easier and quicker just to use printf, just to use printf, just to use printf. And the problem with that logic is that you
45:17
begin to build up like technical debt, so to speak, where you really should have learned it earlier, you really should have learned it earlier,
45:23
you really should have learned it earlier, at which point, you end up spending more time wasted using printf
45:29
and doing things manually than if you had just spent 10 minutes, 30 minutes just learning the user interface
45:35
and the buttons of a proper debugger. So please take that advice because it will save you
45:40
significant amounts of time over time.
45:45
Questions on printf or debugging in this way?
45:52
Any questions on this? No? OK. So let me give you a third and final technique for debugging, which has been
45:59
looming over us here for some time. So there is actually this technique known as rubber duck debugging.
46:05
And in the absence of a roommate who is taking CS50 or who has taken CS50 or knows how to program, in the absence of having a TF or TA or CA
46:13
sitting next to you, in the absence of having a family member available to ask questions of, if you have simply an inanimate object on your desk,
46:22
goes the tradition, just talk to that inanimate object. Better yet, if it's an adorable rubber duck in this way.
46:27
And the idea of rubber duck debugging is that simply by verbalizing literally out loud to this inanimate object--
46:34
probably with the door closed and no one knowing that you're talking to this rubber duck, you invariably end up hearing any illogic in your own thoughts, at which point
46:44
the proverbial light bulb tends to go off and you're like, oh, I'm an idiot. It's supposed to be less than, not less than or equal to.
46:50
So literally just explaining to a duck or any inanimate object what's going on in your code will quite frequently just
46:57
help you see in your mind's eye what it is you've been doing wrong. So rubber duck debugging is indeed a very effective technique
47:05
even if you don't happen to have a small or large rubber duck. Of course, you're also welcome to use the CS50 Duck who
47:12
lives at cs50.ai, and also within a pane in VS Code at cs50.dev.
47:17
You can ask the CS50 Duck about concepts you don't understand, or you can even copy paste certain lines of code
47:23
with which you might be having trouble and ask the duck for its own advice. All right.

## [Memory](https://youtu.be/4vU4aEFmTSo?t=2848)

47:28
So, with those tools in our toolkit, let me propose now that we do--
47:33
that we introduce now a few lower-level features of C itself and better understand how we can start solving some of those problems
47:40
like the readability of text or the encryption of data. These were our so-called types last week when
47:47
we introduced at least a subset of them or used them just to store data in a certain format, so to speak.
47:53
Like in week 0, we said that everything at the end of the day is just 0's and 1's, binary. And I claimed conceptually that how a computer knows if a set of bits
48:03
is a number versus a letter versus a color or a sound or an image or a video
48:08
is just context-dependent, like you're using Photoshop or you're using Microsoft Word or something else. But last week, we saw a little more precisely that it's
48:16
not quite as broad strokes as that. It's more about what the programmer has told the software is
48:23
being stored in a given variable. Is it an integer? Is it a char, a character? Is it a whole string?
48:29
Is it a longer integer or the like? So you now have this control. The catch, though, recall, though, is that each of these types
48:36
has only a finite amount of space allocated to it. So for instance, an integer is typically 4 bytes,
48:43
and 4 bytes is 32 bits because it's 8 times 4. 32 bits, we claimed, is roughly 4 billion,
48:49
but if you want to represent negative and positive numbers, the biggest integer you can store is like 2 billion.
48:55
Now that's really big for a lot of applications, but years ago, Facebook, for instance, was rumored to be using integers when they had fewer users.
49:04
But now that they have billions of users-- 3-plus billion users, an integer is no longer big enough for the Facebooks,
49:12
the Googles, the Microsofts and so forth of the world. So we also have longs, which use twice as many bytes, but exponentially
49:21
bigger range of values. Meanwhile, a bool, interestingly, is a byte, which is kind of bad design in what sense?
49:29
Why might that be bad design? It's only-- it should only be 2-- 1 bit, rather, because a 0 or 1 should suffice.
49:36
Turns out, it's just easier to use a whole byte even though we're wasting seven of those bits, but bools are represented nonetheless with 1 byte.
49:43
Chars are going to be 1 byte. Floats tend to be 4 bytes. Doubles tend to be 8 bytes.
49:49
Some of this is system-dependent, but nowadays on modern computers, this tends to be a useful rule of thumb. The only one I can't commit to here is a string
49:56
because a string, recall, is a sequence of text. And maybe it has no characters, one character, two, 10, 100.
50:02
So it's a variable number of bytes presumably where each byte represents a given character.
50:08
So with that said, how do we get from an actual computer to information being represented therein?
50:16
Well, let me remind us that this is what's inside of our Macs, PCs, phones. Even though this isn't a scale and it might not be the same shape,
50:22
this is memory, random access memory. And on these black chips, on the circuit board here, are the bytes that we keep talking about.
50:29
In fact, let's go ahead and zoom in on one of these chips, fill the screen here. And just for an artist's depiction's sake,
50:35
let me propose that if you've got, I don't know, a megabyte, a gigabyte-- like a lot of bytes packed into this chip nowadays,
50:43
it stands to reason that no matter how many of them you have, we could just number them from top to bottom
50:48
and we could say that this is byte 1, or you know what? This is byte 0, 1, 2, 3, and this is maybe byte 1 billion or whatever it is.
50:55
So you can think of memory as having addresses or just locations, numeric indices that identify each of those bytes
51:03
individually. Why a byte? Individual bits are not that useful, so 8, again, 1 byte
51:08
tends to be the de facto standard. Let me-- so, for instance, if you're storing just a single character,
51:14
a char, it might be stored literally in this top-left corner, so to speak, of the chip of memory.
51:20
If you're storing maybe an integer, 4 bytes, it might take up that many bytes. If you're storing a long, it might take up that many bytes instead.
51:28
Now we don't have to dwell on the particulars of the circuit board and these traces and all the connections, so let me just abstract
51:34
this away and claim that what your computer's memory really is is just kind of this canvas, I mean kind of in the Photoshop sense.
51:41
If you've ever made pictures, it's just a grid of pixels, up, down, left, right, that's really all your memory is.
51:46
It's this canvas that you can manipulate the bits on to store numbers anywhere you want in the computer's memory.
51:53
So in fact, let's zoom in here and let's consider how your computer is actually storing information using just these bytes.
52:01
At the end of the day, no matter how sophisticated your Mac, your PC, your phone is, like this is all
52:07
it has access to for storing information. It's a canvas of bytes, and what you do with this
52:13
now really invites design decisions. So let's consider this. Here is an excerpt from a program wherein maybe I'm
52:20
prompting the user for three scores. Like three test, scores, exam scores, something like that. And the purpose in life of this program is maybe
52:27
to average those three scores together if you want to get a sense of where you stand in some class. So we can certainly whip up some code like this.
52:33
And in just a moment, let me go ahead and flip over to VS Code here. And I'll write up a new program called scores.c.

## [scores.c](https://youtu.be/4vU4aEFmTSo?t=3161)

52:41
And in this, let me go ahead and first include stdio.h,
52:46
int main void at the top. And in here, let me go ahead and assume that, eh,
52:51
it's not been the greatest semester. So my first score, which I'll call score1, was a 72,
52:56
my second score was a 73, but my third score, score3, was like a 33.
53:03
Now you might remember these numbers in another context, they might spell a message, but in this case, it's just integers.
53:08
It's just numbers because I'm telling the computer to treat these as ints. Now if I want to figure out what my average is, I can do a bit of math.
53:15
So let me just print out that my average is-- and I don't want to shortchange myself. I'm not going to use %i because I don't want to lose even anything after
53:23
the decimal point. So we're going to use a float instead. And my average i claim will be score1 plus score2 plus score3
53:33
divided by 3, semicolon. With parentheses, because just like grade school math,
53:38
like order of operations, I parenthesize the numerator, so I can divide the whole thing by 3. But I have screwed up already.
53:45
I am going to shortchange myself and not give myself as high a grade as I deserve, but this one's subtle.
53:51
What have I done wrong? Yeah, I might want to cast these scores to floats
53:59
because if you do integral math, divide an integer or the sum of an integers--
54:05
some integers by an integer, it's going to be an integer as the result, so it's going to throw away anything after the decimal point.
54:12
Even if it's something-point-1, something-point-5, something-point-9, that fraction is going to be thrown away.
54:18
There's a bunch of ways to fix this. I could just use floats or doubles for all of these. I could cast score1, score2, or score3 as you propose.
54:26
Frankly, the simplest way is just change the denominator because so long as I've got one float involved in the math,
54:31
this will promote the whole arithmetic expression to being floating point math instead of integer math.
54:37
So let me go ahead now and do make scores, Enter. So far, so good. ./scores, and my average seems to be not great,
54:45
but 59.33333-- so in the third. But I would have lost that third if I hadn't
54:50
used a float in this particular way. Well, let's consider now what's actually going on inside of the computer
54:56
when I store these three variables. So, back to the grid here, just my canvas of memory. It doesn't really matter where things end up.
55:03
I might put it here, I might put it there, the computer makes these decisions. But for the artist's sake, I'm going to put it at the top left-hand corner
55:10
here. So, score1 is containing the integer 72.
55:15
Why is it taking up four squares, though? Because?
55:22
It's an integer. And on this system, an integer is 4 bytes. So I've drawn it to scale, if you will. score2 is the number 73,
55:30
it also takes 4 bytes. By coincidence, but also by convention, it will likely end up next to the first integer
55:38
in memory because I've only got three variables going on anyway, so the computer quite likely will store them back to back to back.
55:44
And indeed, by that logic, score3, containing the number 33, is going to fill in this space here.
55:50
We'll consider down the road what happens if things get fragmented-- something's here, something's here, something's here, but for now, we
55:55
can assume that this is probably contiguous, though not necessarily so. All right, so that's pretty straightforward,
56:01
but what's really going on? Well, these are just bytes of memory-- that is, bits of memory times 8.
56:07
And so what's really going on is this pattern of 0's and 1's is being stored to represent 72.
56:14
This pattern of 0's and 1's is being stored to represent 73, and similarly, 33.
56:19
But that's a very low level detail that we don't really care about, so we'll generally just think about these as numbers like 72, 73, 33.
56:27
All right. So if we go back to the actual code, though, here, I wonder if this is the best idea.
56:35
These three lines of code are correct. I got my 59 and 1/3 for my average, which I claim
56:41
is correct, but code-wise, this should maybe rub you the wrong way.
56:46
Even if you hadn't programmed before CS50, why might this not be the best approach to storing things
56:53
like scores in a program? How might this get us in trouble?
56:58
Yeah? AUDIENCE: [INAUDIBLE]
57:03
DAVID MALAN: Yeah. It's not the best because you have to use a whole bunch of different variables for each score. They're almost identically named, though, but just imagine
57:11
in almost any question involving the design of your code, what happens is n, the number of things involved, gets larger?
57:18
Am I really going to start writing code that has score4, score5, score6, score10, score20?
57:23
I mean, your code is just going to look like this mess of mostly copy-paste except that the number at the end of the variable is changing.
57:30
Like that should make you cringe a little bit because it's not going to end well eventually. And typographical errors are going to get in the way most likely
57:37
because we'll make mistakes. So how can we do a little bit better than that? Well, let me propose that we introduce what we're going to now call an array.

## [Arrays](https://youtu.be/4vU4aEFmTSo?t=3465)

57:45
An array is a sequence of values back to back to back in memory.
57:52
So an array is just a chunk of memory storing values back to back to back. So no gaps, no fragmentation.
57:59
From left to right, top to bottom, just as I already drew. But these arrays in C, at least, are going
58:05
to give a slightly new syntax that addresses exactly your concern. So here instead is I would propose how you define a one variable--
58:14
not three, one variable called scores, plural, each of whose values
58:19
is going to be an int, and you want three integers tucked away in that variable.
58:25
So now I can pluralize the name of my variable because by using square brackets and the number 3, I'm telling the compiler,
58:32
give me enough room for not one, not two, but three integers in total. And the computer is going to do me a favor by storing them back
58:39
to back to back in the computer's memory. Now assigning values to these variables is almost the same,
58:45
but the syntax looks like this. To assign the first value, I do scores, bracket, 0 equals whatever, 72.
58:53
scores, bracket, 1 equals 73; scores, bracket, 2 equals 33.
58:58
And it's square brackets consistently. And notice, this is a feature-- or a downside of C.
59:04
We very frequently use the same syntax for slightly different ideas. This first line tells the computer, give me an array of size 3.
59:12
These next three lines mean, go into this array at location 0 and put this value there.
59:18
Location 1, put this value there; location 2, put this value there. So same syntax, but different meaning depending on the context here.
59:24
But the equal sign indeed means that this is assignment from right to left just like last week.
59:30
So what does this mean in the computer's memory? Well, in this case here, we now have a slightly different way of doing this.
59:38
And actually, let me do it first in code. Let me go back to VS Code here, and let me
59:43
propose that instead of having these three separate variables, let me give myself an int, scores variable of size 3,
59:52
and then do scores, bracket, 0 equals 72; scores, bracket, 1 equals 73;
59:58
scores, bracket, 2 equals 33. And now I have to change this syntax slightly, but same idea.
1:00:05
scores, bracket, 0; scores, bracket, 1; and lastly, scores, bracket, 2.
1:00:12
So a couple of key details. I started counting at 0. Why? That's just the way it is with arrays.
1:00:18
You must start counting at 0 unless you want to waste one of those spaces. And what you definitely don't want to do is
1:00:23
go into scores, bracket, 3 because I only ask the computer for three integers.
1:00:29
If I blindly do something like this, you're going too far. You're going beyond the end of the chunk of memory
1:00:34
and bad things will often happen. So we won't do that just yet. But for now, 0, 1, and 2 are the first, second, and third locations.
1:00:43
So if I recompile this code-- so make scores seems OK. ./scores, and I get the exact same answer there.
1:00:50
But let me make it more dynamic because this is a little stupid that I'm compiling a program with my scores hardcoded.
1:00:56
What if I have a fourth exam tomorrow or something like that? So let's make it more dynamic and I think the syntax will start to make a little more sense.
1:01:03
Let's go ahead and use get_int and ask the user for a score. Let's go ahead and get_int and ask the user for another score.
1:01:10
Let's go ahead and get_int and ask the user for a third score, now storing the return values in each of those variables.
1:01:18
If I now do make scores-- oh, darn it. a mistake.
1:01:24
Similar to one I've made before, but we didn't see the error message last time. What'd I do wrong? Yeah?
1:01:30
AUDIENCE: [INAUDIBLE] DAVID MALAN: OK. What did I do wrong-- how about over here? AUDIENCE: [INAUDIBLE] DAVID MALAN: Yeah.
1:01:35
So I'm missing the CS50 header file. So how do you know that? Well, implicit declaration of function get_int.
1:01:40
So it just doesn't know what get_int is. Well, who does know what get_int is? The CS50 Library, that should be your first instinct.
1:01:47
All right. Let me go to the top here and let me go ahead and squeeze in the CS50 Library like this.
1:01:52
Now let me clear my terminal. make scores again. We're back in business. And notice, I don't need to do -l cs50.
1:02:00
make is doing that for me for clang, but we don't even see clang being executed,
1:02:05
but it is being executed underneath the hood, so to speak. All right, so ./scores, here we go.
1:02:10
72, 73, 33. Math is still the same, but now the program is more interactive.
1:02:17
Now this, too, hopefully should rub you the wrong way. This is correct, I would claim, but bad design still.
1:02:25
Reeks of week 0 inefficiencies. Yeah? AUDIENCE: [INAUDIBLE]
1:02:33
DAVID MALAN: OK. So I could ask the human how many scores do you want to input? Let's come back to that. But I think even in this construct, what better could I do?
1:02:42
Use a loop, right? Because I'm literally doing the same thing again and again. And notice, this number is just changing slightly.
1:02:48
I would think that a little plus-plus could help there. get_int Score, get_int Score, get_int Score-- that's the exact same thing.
1:02:53
So a loop is a perfect solution here. So let me go over into this code here, and I can still for now
1:02:59
declare it to be of size 3, but I think I could do something like this-- for int i get 0, i is less than 3,
1:03:07
so I'm not going to make the same buggy mistake as I made earlier. I++. Inside of the loop now, I can do scores, bracket, i, and now
1:03:15
arrays are getting really interesting because you can use and reuse them, but dynamically go to a specific location.
1:03:22
Equals get_int, quote-unquote, "Score." Now I can type that phrase just once and this loop ultimately
1:03:29
will do the same thing, but it's getting better. The code is getting better designed because it's more compact
1:03:34
and I'm not repeating myself. 72, 73, 33. Still works the same, but we're iteratively improving the code here.
1:03:42
Now how else-- there's one design flaw here that I still don't love
1:03:48
it's a little more subtle. Any observations? AUDIENCE: [INAUDIBLE]
1:03:57
DAVID MALAN: Ah, interesting. So instead of dividing by 3.0, maybe I should divide it by the array size, which at the moment is technically still 3,
1:04:05
but I do concur that that is worrisome because they could get out of sync.
1:04:10
But there's something else that still isn't quite right. Yeah? AUDIENCE: [INAUDIBLE]
1:04:19
DAVID MALAN: I'm OK moving to this zero-indexed model. So this is a new term of art. To index into an array means to go to a specific location.
1:04:27
So here, I'm indexing into location i, but i is going to start at 0 and then 1 and then 2.
1:04:33
I'm actually OK with that. Even though in common day life we would say score1, score2, score3, as a programmer, I just have to get into the habit
1:04:39
of saying score0, score1, score2 now. But something else. Yeah?
1:04:45
AUDIENCE: I could compute the average. DAVID MALAN: I could also compute the average in a loop because indeed, this is only going-- so solving the problem halfway.
1:04:54
I'm gathering the information in the loop, but then I'm manually writing it all out. So it does feel like there should be a better solution here.
1:05:01
But let me also identify one other issue I really don't like, and this is, indeed, subtle. I've got 3 here, I've got 3 here, and I essentially have 3 here,
1:05:11
albeit a floating point version. This is just ripe for me making a mistake eventually and changing one
1:05:16
of those values, but not the other two? So how might I fix this? I might at least do something like this.
1:05:22
I could say integer maybe n for scores, I'll set that equal to 3.
1:05:28
I could then use n here, I could use n here. I could use n here, but that's a step backwards
1:05:33
because I don't want an int because I'm going to run into the same math issue as before, but I could convert it-- that is, cast it to a float,
1:05:40
and we did that briefly last week. But there's one other thing I could do here that we did introduced last week.
1:05:47
This is better because I don't have a magic number floating around in multiple places.
1:05:53
Yeah, if I really want to be proper, I should probably say this should be a constant integer. Why?
1:05:58
Because I don't want to accidentally change it myself. I don't want to be collaborating with a colleague and they foolishly change it on me.
1:06:04
This just sends a stronger signal to the compiler, do not let the humans change this value.
1:06:10
And now just to point out one other feature of C, if you have a number like this, like the number 3,
1:06:16
I've deliberately capitalized this variable name really for the first time. Any time you have a constant, it tends to be a convention
1:06:22
to capitalize it just to draw your attention to it. It doesn't mean anything technically. Capitalizing a variable does nothing to it,
1:06:28
but it draws attention visually to it to the human. So if you declare something as a constant, it's commonplace to capitalize it just because.
1:06:37
Moreover, if you have a constant that you might want to occasionally modify-- maybe next semester when there's four exams or five exams instead of three,
1:06:45
it actually is OK sometimes to define what might be called a global variable, a variable that is not
1:06:52
inside of curly braces, it's literally at the top of the file outside of main,
1:06:57
and despite what I said about scope last week, a global variable like this on line 4 will be in scope
1:07:05
to every function in this file. So it's actually a way of sharing a variable across multiple functions, which is generally fine if you're
1:07:13
using a constant. If you intend to change it, there's probably a better way than actually using a global variable, but this is just
1:07:21
in contrast to what I previously did, which I would call, by contrast, a local variable.
1:07:26
But again, I'm just trying to reduce the probability of making mistakes somewhere in the code. And I do agree.
1:07:32
I don't like that I'm still adding all of these scores manually even though clearly I had a loop a moment ago.
1:07:39
But for now, let's at least consider what's been going on inside of the computer's memory. So with this array, I now have not three variables, score1, score2, score3.
1:07:48
I have one variable, an array variable, called scores, plural. And if I want to access the first element, its scores, bracket, 0.
1:07:57
If I want to access the second element, its scores, bracket, 1. If I want to access the third element, it's scores, bracket, 2.
1:08:03
If I were to make a mistake and do scores, bracket, 3, which is the fourth element, I'd end up in no man's land here,
1:08:11
and worst case, your program could crash or something weird will happen, spinning beach balls, those kinds of things.
1:08:17
Just don't make those mistakes. And C makes it easy to make those mistakes, so the onus is really on you programmatically.
1:08:25
Questions on this use of arrays?
1:08:31
Question on this use of arrays? Yeah, in back. AUDIENCE: Is there any way [INAUDIBLE]?
1:08:43
DAVID MALAN: A really good question. Is there any way to create an array just by using syntax alone without prompting the human for it?
1:08:49
Short answer, yes. If you want to have an array of integers called, for instance, array,
1:08:56
you could actually do like 13, 42, 50, something like this, would give you an array if you use this syntax.
1:09:04
This would give you an array of size 3 where the three values by default are 13, 42 and 50.
1:09:10
It's not syntax we'll use for now, but there is syntax like that. It's not quite as user-friendly, though, as other languages
1:09:15
if you've indeed programmed before. Other questions on this use of arrays?
1:09:24
Yeah, in front. AUDIENCE: [INAUDIBLE] DAVID MALAN: Is there a way to copy what?
1:09:30
AUDIENCE: [INAUDIBLE] DAVID MALAN: Oh, is there a way to calculate the length of an array?
1:09:36
Short answer, no, and I'm about to show you one demonstration of this. Those of you who have programmed before in Java, in JavaScript,
1:09:43
in certain other languages, it's very easy to get the length of an array. You essentially just ask the array, what's its length?
1:09:49
C does not give you that capability. The onus is entirely on you and me to remember, s as with another variable,
1:09:56
like n, how long the array is. And so in fact, let me go ahead and do this.
1:10:01
I'm going to go ahead and open up a baking style, a program that I wrote in advance here which kind of escalates quickly,
1:10:09
but there's not really too many new ideas here except for the array specifics. So this is scores.c premade this time.
1:10:19
And notice what I have. One, I've included cs50.h and stdio.h at the top, so that's the same.
1:10:25
I have declared a constant called n, set it equal to 3. That is now the same as of my most recent change.
1:10:31
I did introduce an average function, which was one of the remaining concerns
1:10:36
that I could compute the average with some kind of loop, too. That average function is going to return a float, which is what.
1:10:42
I want my average to be a float with the fraction. But notice this. In answer to your question, if I want a function called
1:10:50
average to do something iterate over an array step by step by step, add up all the numbers, and divide by the total number of numbers,
1:10:58
I need to give it the array of numbers, and I need to tell it how many of those numbers are.
1:11:03
So I literally have to pass in two values. Meanwhile, this code is the same as before inside of main.
1:11:09
I'm declaring a variable called scores of size n. I'm iterating from i to n.
1:11:16
And actually-- yep. And then in this loop, I'm assigning each of the scores a return
1:11:22
value of get_int. The last line of main is this-- print out the average with f, but don't just do it manually by adding and dividing with parentheses.
1:11:31
Call the average function, pass in the length of the array and the array itself, and hope that it returns a float that then gets plugged into percent f
1:11:41
So I would claim that pretty much all of this, even though it's a lot, should be familiar. There's no real new ideas except for this use of the global variable now
1:11:50
and this average function. So let me scroll down to the average function because this is the takeaway from this final example.
1:11:57
In this example here-- let me scroll up to the average function, copy-pasted the prototype for the very first line.
1:12:04
And here's how I'm computing the average. There's different ways of doing this, but here's an accumulator way.
1:12:11
On line 28, I'm declaring a variable inside of the average function called sum, and I'm just initializing it to 0.
1:12:17
Why? Mentally I want to add up all of the person scores and then I want to divide by the total and that's my mathematical average.
1:12:24
So here's my loop where I'm iterating from 0 up to, but not through the length-- so that should be three times.
1:12:32
I am adding to the sum variable whatever is at the i-th location, so to speak,
1:12:37
of the array. So this is array, bracket 0; array, bracket, 1; array, bracket, 2 on each iteration.
1:12:43
And then the last thing I'm doing is a nice one-liner. I'm dividing the sum, which is an int, which is the sum of 72, 73, 33,
1:12:51
divided by the length, which is 3, but 3 is not a float, so I cast it to a float
1:12:56
so that the end value, hopefully, is going to be 59.33333 and so forth.
1:13:03
So the only thing that's weird syntactically is this, though. When you define a function in C that takes an argument that isn't just
1:13:10
a simple char, isn't just a simple integer, it's actually an array, you don't have to know the array's length in advance.
1:13:17
You can just put square brackets after the name you give it. And I don't have to call it array. I could call it x or y or z or anything else.
1:13:23
I called it array just to make clear that it's an array, but you do need to know the length somehow.
1:13:30
OK. Questions on combining those ideas in that there way?
1:13:37
Any questions?
1:13:42
No? All right. Well, we've only dealt with numbers thus far. It would be nice to actually deal with letters and words and paragraphs
1:13:50
and the like, much like our readability example, but I think first, some snacks and some fruit are served in the transept.
1:13:56
So we'll see you in 10. See you in 10. All right. So we're back.

## [Strings](https://youtu.be/4vU4aEFmTSo?t=4441)

1:14:01
And up until now, we've been representing just numbers underneath the hood, but we've introduced arrays, which gave us this ability, recall,
1:14:07
to store numbers back to back to back. So it turns out, you actually had this capability for the past
1:14:13
week even though you might not have realized it. And let me propose that we first consider very simple example of three
1:14:19
chars instead of three integers. And for simplistically, I'm going to call them c1, c2, and c3 just for the sake of discussion.
1:14:25
But I'm going to put our familiar characters, "HI!" in those variables using single quotes because again.
1:14:32
That's what you do when using individual chars to make the point that I can store three chars in three separate variables.
1:14:40
So let me go ahead and go over to VS Code here and let me create something called hi.c. And in this program, I'll first include stdio.h, int main void as before.
1:14:50
And then inside of main, let's just do exactly that. Char c1 equals, quote-unquote, capital H. Char C2 equals,
1:14:57
quote-unquote, capital I. Char C3 equals, quote-unquote, exclamation point.
1:15:02
So clearly not the best approach, but just for demonstration's sake. And here now that you understand hopefully
1:15:09
from week 1 that really number-- and really, from week 0, that numbers are just letters, which can be something more, too.
1:15:16
We can really just use our basic understanding of C to tinker with these ideas now and see them such
1:15:21
that there is indeed going to be no magic happening for us ultimately. So let me go ahead and print out three characters-- %c, %c, %c, backslash n.
1:15:31
And then print out c1, c2, c3. So I've got three separate placeholders. And we haven't really had occasion to use %c, but it means put char here,
1:15:40
unlike %s, which is put a whole string here, or %i, put an integer. Let me go ahead and make hi, no syntax errors, ./hi,
1:15:49
and it should print out "HI!" in exclamation points because I'm printing out just three simple characters.
1:15:54
But per our discussion as far back as week 0, letters are just numbers and numbers are just letters,
1:16:01
it just depends on the context in which we use them. So let me change this %c to an i. And I'm going to add a space just so that you can obviously
1:16:08
separate one number from another. Change this to i, change this to i, but still print out c1, c2, c3.
1:16:14
So no integers, per se. Let me just print out those chars. Let me do make hi, no errors, ./hi, and now I see 72, 73, 33.
1:16:26
So in the case of chars and ints, you can actually treat one as the other so long as you have enough bits to fit one in the other.
1:16:33
You don't have to cast even or do anything explicitly. You do have to cast one of-- converting an integer to a float to make clear to the compiler
1:16:41
that you really intend to do this because that could be destructive if it can't quite represent the number as you intend.
1:16:47
But in this case here, I think we're OK just poking around and seeing what's going on underneath the hood.
1:16:52
Well, what is going on underneath the hood memory-wise? Well, something very similar. Here's that canvas of memory.
1:16:57
And maybe we got lucky and it's in the top left-hand corner like this-- c1, c2, c3.
1:17:03
But these are just three individual characters, but we're getting awfully close to what we last week called
1:17:08
a string, which are just characters, a sequence of characters from left to right. And in fact, I think if we combine this revelation that these are just
1:17:19
numbers underneath the hood back to back to back combined with the idea of an array from earlier, we can
1:17:25
start to see what's really going on. Because indeed, underneath the hood, this is just a number, 72, 73, 33.
1:17:31
And really, if we go lower level than that, it's these three patterns of 0's and 1's. That's all that's going on inside of the computer,
1:17:39
but it's our use of int that shows it to us as an integer. It's our use of char that makes it clear that it's a char, or equivalently,
1:17:47
%i and %c respectively. But what exactly is a string? Well, it's really just a sequence of characters,
1:17:54
and so why don't we go there? Let me propose that we actually give ourselves an actual string, call it s-- we'll use double quotes this time.
1:18:02
So if I go back to VS Code here, let me shorten this program and just give myself a single string s, set it equal to "HI!"
1:18:10
in double quotes. And then below that, let's go ahead and print out %s, backslash n,
1:18:16
and then s itself. And then, turns out, for reasons we'll soon see, I do need to include the CS50 Library so as
1:18:23
to use the actual keyword string here even though I'm not using get_string, but more on that another time.
1:18:29
But if I now do make hi, it does compile ./hi and it still prints out the exact
1:18:34
same thing. But what's going on inside of the computer's memory when I use a string called s instead of three chars, well,
1:18:42
you can think of the string as taking up at least three bytes, H, I, exclamation point.
1:18:47
But it's not three separate variables, it's one variable. But what does this really look like now, especially
1:18:53
if I add back the yellow lines? s is really just an array of characters.
1:19:00
So we called it a string last week, and I claim today that this is an abstraction in the CS50 library that's giving us this string,
1:19:10
but it's really just an array of size at least 3 here where s, bracket, 0 presumably gives me the H, s, bracket,
1:19:16
1 is the I, s, bracket, 2 is the exclamation point. But just by saying string, all of that happens automatically.
1:19:22
I don't even need to tell the computer how many chars are going to be in this string all at once.
1:19:27
So in fact, let me go over to maybe a variant of this program and we can see this syntactically.
1:19:33
So instead of printing out the whole string with %s, let me actually be a little curious and print out %c, %c, %c,
1:19:43
and then change s to s, bracket, 0, s, bracket, 1, s, bracket, 2. Which is not better in any sense.
1:19:49
This is way more tedious now, but it does demonstrate that I can treat here in week 2
1:19:54
as though it's an array, which means even in week 1 it was an array, we just didn't know it. We didn't have the syntax with which to express that.
1:20:01
So if I now do make hi, still compiles ./hi. Same exact output, but I'm now just kind of manipulating
1:20:09
the string in these different ways because I a string is just an array of characters, so I can treat with the square bracket notation.
1:20:16
But how do I know-- how does the computer know where hi ends? And this is where strings get a little dangerous.
1:20:23
Like a char is 1 byte no matter what. 1 char, 1 character, that's it. But a string, recall my question mark from earlier,
1:20:31
could be null bytes if it's-- you would think could be 0 bytes if you have nothing in it inside the quotes.
1:20:37
It could be one character, two, 10, 100 like I claimed, but how does the computer know where strings end?
1:20:44
Like how does the computer not know that the string is not the whole row of memory here?
1:20:49
How does it know that it ends here? Well, it turns out, all this time, when we've been using, quote-unquote,
1:20:54
string and using get_string from the CS50 library, there's actually a special sentinel value
1:21:00
at the end of every string in a computer's memory that tells the computer string, stops here.
1:21:06
And the sentinel value-- and by sentinel, I just mean special value that the world decided on decades ago, is all 0 bits.
1:21:13
If you have a byte with all 0 bits in it, that means string ends here.
1:21:20
So the implication is that the computer now, using a loop or something, can print out char, char, char-- oh, done,
1:21:26
because it sees this special value. If it didn't have that, it might blindly go char, char, char, char char--
1:21:32
printing out values of memory that don't belong to that given string. So I was correcting myself verbally a moment ago
1:21:39
because I said that this string is of length 3, it's 3 bytes, but it's not. Every string in the world, both last week and now, this
1:21:47
is actually n plus 1 bytes where n is the actual human length that you care about, H-I, exclamation point, or 3,
1:21:54
but it's always going to use one extra byte for this so-called zero value at the end.
1:21:59
And this 0 value is very tedious to write a 0-- as 8 0 bits. So we would actually typically just write it as a 0.
1:22:07
But you don't want to confuse a 0 on the screen-- it's actually being like the number 0 on the keyboard.
1:22:12
And so we would actually typically write this symbol with a backslash 0. So this is the char-based representation of 0.
1:22:19
So it means the exact same thing, this is just C notation that indicates that this is 8 0 bits,
1:22:26
but just makes clear that it's not literally the number 0 that you want to see on the screen, it's a sentinel value
1:22:32
that is terminating this here string. So now what can I do once I know this information?
1:22:38
Well, I can actually even see this let me go back to this code here in VS Code. Let me change these %c's to %i's just like before.
1:22:46
And now, we'll see again those same numbers, make hi, ./hi, there are the three.
1:22:51
I can technically poke around a little bit further, %i one more, and let's look at s, bracket, 3.
1:22:58
I was not exaggerating earlier when I said, in general, if you go past the end of an array, bad things can happen.
1:23:06
But in this case, I know that there is one more thing at the end of this array because this is how strings are built. This is not a CS50 thing,
1:23:13
this is a thing in C. Every string in the world in double quotes ends with a backslash 0-- that is 8 0 bits.
1:23:20
So if I really want, I can see this by printing out s, bracket, 3, which is the fourth and final location.
1:23:26
If I recompile my code now, make hi ./hi, I should see 72, 73, 33, and 0.
1:23:34
That's always been there. So I'm always using 4 bytes, somewhat wastefully, but somewhat necessarily
1:23:40
so that the computer actually knows where that string ends. So if we go back to the memory representation of this here,
1:23:48
it's just as though you have an array of integers being stored contiguously back to back to back, the last one of which means this is the end of the array
1:23:56
of characters, but because I'm using, quote-unquote, "string," because I'm using %s and %c, I'm not seeing these numbers by default,
1:24:04
I'm seeing H-I, exclamation point unless I explicitly tell printf, no, no, no, no, show me with %i these actual integers.
1:24:13
This, then, is how you can think about the string. Like you don't really need to think about it as being individual characters.
1:24:18
This is just s, and it has some length here, but it does not necessarily an array that you yourself have to create,
1:24:26
you get it automatically just by using a string. Now there's just-- not to add on to the jargon.
1:24:32
This backslash 0, these 8 0 bits, there's actually a technical term for them. You can call them NUL.
1:24:38
It's typically written in all caps like this, confusingly. In a couple of weeks, we're going to see another word pronounced null,
1:24:44
but spelled N-U-L-L. Left hand wasn't talking to right hand years ago, but N-U-L means this is the 0 byte that terminates strings,
1:24:54
that indicate the end of a string. And fun fact, you've actually seen this before even though we glossed over it.
1:25:00
Here's that ASCII chart from last time. If I focus on the leftmost column, guess what is the 0 ASCII character?
1:25:08
NUL. You never see null on the screen, it's just how you pronounce 8 0 bits.
1:25:14
Whew! questions on this representation of strings? Yeah? AUDIENCE: Are strings [INAUDIBLE]?
1:25:20
DAVID MALAN: Are string structured differently in other languages? Yes. They are more powerful in other languages. In C, you have to build them yourself in this way.
1:25:28
More on that when we get to Python. Other questions. Yeah? AUDIENCE: [INAUDIBLE]
1:25:41
DAVID MALAN: A really good question. Does that mean we don't have a function to get the length of a string? Do we have to create it?
1:25:47
Short answer, there is a function, but you have to-- someone had to write code for it. You can't just ask the string itself like you can in JavaScript or Java.
1:25:56
What is the-- AUDIENCE: [INAUDIBLE] DAVID MALAN: Yeah, you can. It's actually more similar to Python than it is to JavaScript or Java,
1:26:04
but we'll see that in just a few minutes, in fact. So let's introduce maybe a couple of strings.
1:26:09
So here's two strings in the abstract called s and t, and I've initialized them arbitrarily to "HI!" and "BYE!"
1:26:15
just so we can explore what's going to actually happen underneath the hood. So let me go back to VS Code.
1:26:20
Let me just completely change this program to be that instead. So string equals, quote-unquote, "HI!"
1:26:26
String t equals, quote-unquote, "BYE!" in all caps. And then let's print them both out very simply. %s backslash n, s.
1:26:34
Print out %s backslash n, t just so we can see what's going on. If I do make hi ./hi, I should, of course, see these two strings.
1:26:44
But what's going on inside of the computer's memory? Well, in this computer's memory, assuming these are the only two variables involved and assuming the computer
1:26:51
is just doing things top to bottom, "HI!" is probably going to be stored somewhere like this on my canvas of memory,
1:26:58
"BYE!" is probably going to be stored there. And it's wrapping around, but that's just an artist's representation. But notice that it is now really important
1:27:05
that there is this NUL byte at the end of each string because that's how the computer is going to know where "HI!"
1:27:11
ends and where "BYE!" begins, otherwise you might see "HI!" "BYE!" all on the screen at once if there weren't the sentinel value indicating
1:27:20
to printf, stop at this character. But that's all that's going on in your program
1:27:26
when you have two variables in this way. And in fact, what's really going on and things get a little more interesting
1:27:32
here, if I were to want two of these things,
1:27:37
notice that I could refer to them two as arrays. So s, bracket, 0, 1, 2, and even 3.
1:27:43
t, bracket, 0, 1, 2, and even 3 and 4. But if I want to actually really blend some ideas,
1:27:51
just playing around with these basic principles now, notice what I can do in this version. If I know I've got two arrays in VS Code,
1:27:59
I don't strictly need to do string s and t and u and v. That's devolving back into the scores1, scores2, scores3 mantra where
1:28:08
I had multiple variables almost the same name even though I'm using different letters of the alphabet. What if I want--
1:28:13
what if I do this? string words, and if I want to store two words in the computer's memory, fine.
1:28:19
Create an array of two strings. But what is a string? A string is an array of characters, so it's getting a little bit trippy here,
1:28:28
but the ideas are still going to be the same. words, bracket, 0 could certainly equal "HI!"
1:28:34
words, bracket, 1 can certainly equal "BYE!" just like the scores example. And then if I want to print these things with %s, I can print out words,
1:28:42
bracket, 0. And then I can print out %s backslash n words bracket 1.
1:28:48
And the example is not going to be any different in terms of its output, but I've now avoided s and t, I now just have one variable called words
1:28:58
containing both of these here things. And if I really want to poke around, here's where things get even more visually overwhelming,
1:29:06
but just the logical extension of these same ideas. Right now is the previous version where I had two variables, s and t.
1:29:13
If I now use this new version where I have one variable called words, just like this here, the picture should follow logically like this.
1:29:22
words, bracket, 0 is this string; words, bracket, 1 is this string; but what is each string?
1:29:27
It's an array of characters. And so you can also think of it like this, where this H is words, bracket,
1:29:36
0, bracket, 0. So the 0-th character of the 0-th word. And this is words, bracket, 0, 1; words, bracket, 0, 2; words, bracket, 0, 3.
1:29:45
And then words, bracket, 1, 0. So it's kind of like a two-dimensional array, almost.
1:29:52
And you can think about it that way if helpful. But for now, it's just applying the same principles to the code.
1:29:58
So if I go to my code here and I've got my "HI!" and my "BYE!"-- this is going to look a little stupid, but let me change this %s to %c, %c,
1:30:07
%c, and print out words, bracket, 0. words, bracket, 0, bracket 1. words, bracket, 0, bracket, 2 to print out that three-letter word.
1:30:16
And now down here, let me print out %c, %c, %c, %c because it's four letters in BYE, exclamation point.
1:30:24
This is words, bracket, 1, but the first character; words, bracket, 1, the second character; words, bracket, 1, the third character;
1:30:32
and words, bracket, 1, the fourth character. It's hard to say when you're typing a different number, but that's what we get by using zero indexing, so to speak.
1:30:40
make hi. Whew! No mistakes. "HI!" Says the same thing. So again, there's no magic.
1:30:46
Like you are fully in control over what's going on inside of the computer's memory. And now that we have this array syntax with square brackets,
1:30:54
you can both create these things and then manipulate them or access them however you so choose.
1:31:01
Whew! Questions on arrays or strings in this way?
1:31:08
Yeah, over here. AUDIENCE: Can you have any array that has multiple data types in it? DAVID MALAN: Good question.
1:31:13
Can you have an array with multiple different data types? Short answer, no; longer answer, sort of,
1:31:19
but not in nearly the same user-friendly way as with languages like Python or JavaScript or others.
1:31:25
So assume for now arrays should be the same type in C. Other questions?
1:31:30
Yeah, over here. AUDIENCE: When you talk about [INAUDIBLE]??
1:31:47
DAVID MALAN: Oh, a really good question. It will-- so for those who couldn't hear, if you were to look past the end of one array,
1:31:54
would you start to see the beginning of the second? In this case, maybe the word "BYE!" Could depend on the particulars of your code in the computer.
1:32:01
Let's try this. So let's get a little greedy here and go one past H-I, exclamation point,
1:32:07
null character by looking at words, bracket, 0, 3, which should actually be our null character, so that's going to be there.
1:32:16
And actually, let's see. Let's go ahead and do this. Make hi ./hi.
1:32:21
Still works as expected, but let me change this to integer, integer so we can actually see what's going on.
1:32:27
Integer. And now, if I recompile make hi, I should see the same thing,
1:32:32
but numerically. And now what I think you're proposing is let's get a little crazy and go even past that to what could be location 4,
1:32:41
but we know semantically doesn't exist, but maybe is bumping up against "BYE!" So make hi ./hi.
1:32:49
And guess what 66 is. Well, just the B, but yes.
1:32:54
66, recall, is capital B because in week 0, capital A was 65.
1:32:59
So indeed, now we're really poking around. And you can get crazy. Like, what's 400 characters away and see what's going on there.
1:33:05
Eventually your program will probably crash, and so don't poke around too much, but more on that in the coming days, too.

## [String Length](https://youtu.be/4vU4aEFmTSo?t=5592)

1:33:12
All right, well how about some other revelations and problem-solving? Now coming back to the question about strings length earlier,
1:33:18
and we'll see if we can then tie this all together to something like cryptography in the end and manipulating strings
1:33:24
for the purpose of sending them securely. So let me propose that we go into VS Code here again in a moment.
1:33:30
And I'm going to create a program called length. Let's actually figure out ourselves the length of a string initially.
1:33:36
So I'm going to go ahead and code length.c. I'm going to go ahead and include cs50.h.
1:33:42
I'm going to include stdio.h, int main void. And then inside of main, I'm going to prompt the user for their name.
1:33:49
get_string, quote-unquote, "Name." And then I'm going to go ahead and I want
1:33:55
to count the length of this string. But I know what a string is now. It's char, char, char, char, and then eventually the null character.
1:34:01
So I can look for that. And I can write this in a few different ways. I know a bunch of different types of loops now, but I'm going to go with a while loop by first declaring a variable n,
1:34:10
for number of characters, set it equal to 0. It's like starting to count with your fingers all down, and I want to do the equivalent of this, counting each of the letters
1:34:17
that I type in. So I can do that as follows. While the name variable at location n does not equal,
1:34:29
quote-unquote, backslash 0, which looks weird, but it's just asking the question, is the character
1:34:35
at that location equal to the so-called null character? Which is written with single quotes and backslash 0 by convention.
1:34:43
And what I want to do, while that is true, is just add 1 to n. And then at the very bottom here, let's just go ahead and print out with %i
1:34:52
the value of n because presumably if I type in HI, exclamation point,
1:34:57
I'm starting at 0 and I'm going to have H, I, exclamation point, null character so I don't increment n a fourth time.
1:35:05
So let's go ahead and run down here. make length ./length, Enter.
1:35:12
Well, I guess I'm asking for name, so I'll do my name for real. David, five characters, and I indeed get 5.
1:35:18
If I used a for loop, I could do something similar, but I think this while loop approach, much like our counter from the past,
1:35:26
is fairly straightforward. But what if I want to do this? What if I want to make another function for this? Well, I could do that.
1:35:32
Let me-- All right, let's do this. Let's write a quick function called string_length. It's going to take a string called s or whatever as input.
1:35:40
And then you know what? Let's just do this in that function. I'm going to borrow my code from a moment ago.
1:35:45
I'm going to paste it into this function. But I'm not going to print out the length, I'm going to return the length n.
1:35:51
So I have a helper function of sorts that's going to hand me back the length of the string, and that's why this returns an int, but takes a string as its argument.
1:36:00
How do I use this? Well, first, I do need to copy the prototype so I don't get into trouble as before.
1:36:06
Semicolon. And then in my main function, what I think I can do now is something like this.
1:36:11
I can do int length equals the string length of the name variable
1:36:17
that was just typed in. And now using printf %i, print out length, semicolon.
1:36:23
So exact same logic. The only thing I've done that's different this time is I've added a helper function just to demonstrate
1:36:30
how I can take some pretty basic functionality, find the length of a string, and modularize it into a function abstract it away so I never again have
1:36:38
to copy-paste that for loop. I now have a function called string_length that will solve this problem for me.
1:36:43
Whoops, wrong program. make length. Huh. Use of undeclared identifier 'name.'
1:36:51
What did I do wrong? Apparently on line 16 of length.c, what did I do wrong here?
1:36:59
Yeah, in front. AUDIENCE: [INAUDIBLE]
1:37:06
DAVID MALAN: Good. AUDIENCE: [INAUDIBLE] DAVID MALAN: Good. Perfect terminology. So name is local to main.
1:37:12
The scope of name is main, though sounds similar, but different words. And so I'm actually should be calling this
1:37:19
s because s is the name of the local variable being passed in even though it
1:37:24
happens to be 1 and the same as name because on line 9, I'm indeed passing in name as the argument.
1:37:32
All right. So this is where, again, copy-paste can sometimes get you into trouble. Let's try to make length again. Now it works. ./length, D-A-V-I-D, and now we have a function that seems to be
1:37:42
working. But this is such like commodity functionality. Like my God, like surely someone before us
1:37:47
has written a function to get the length of a string before, and indeed, other people have.
1:37:53
So it turns out that in C, just as you have the stdio library, you also have a string library whose header file is called, appropriately,
1:38:00
string.h. In fact CS50 has documentation, therefore, in its own manual pages, so to speak, along with some sample usage thereof.
1:38:08
But it turns out, in the string library, there is a very popular function analogous to the Python one
1:38:13
that you asked about earlier called strlen where strlen, one word, no underscores, just
1:38:19
figures out the length of a string. And honestly, I've never looked at its source code, but it probably uses a while loop, maybe it uses a for loop,
1:38:26
but it certainly uses the same idea of just iterating-- that is, walking from left to right over a variable
1:38:33
in order to figure out what the length of a given string is. So how do we use this? Well if I go back to VS Code here, I can throw away
1:38:42
the entirety of my string length function, I can throw away the prototype, therefore,
1:38:47
and I can include a third header file, string.h, inside of which I claim now is this function called strlen
1:38:55
that I can just now use out of the box for free because someone else wrote this function for me.
1:39:00
And string.h will teach the compiler that it exists. So if I now do make length and ./length, now I have a similarly working program
1:39:10
that doesn't bother having me write unnecessary code. So this is another example of a library.
1:39:16
The string library is just going to make our lives easier by not having to--
1:39:22
for us not having to reinvent some wheel. All right, well where else does this get interesting?
1:39:27
How about something like this? Let me go back into VS Code here. Let's create a program called string.c--
1:39:35
we'll play around with our own strings-- that's going to start similarly. So let's include cs50.h, let's include stdio.h,
1:39:44
let's include string.h so we can use that same strlen function. int main void.
1:39:50
And inside of this, let's do this. Let's get a string s and prompt the user for any old string as input.
1:39:57
All right. And then let's go ahead and maybe print out, quote-unquote, "Output."
1:40:04
And I'm just going to line up my spaces just right because these words are slightly different lengths, but we'll see why I'm doing this.
1:40:09
It's just for aesthetics' sake in a moment. And let's go ahead now and do this. If I want to print out every character in a string, how can I now do this?
1:40:17
Well, this is actually a pretty common task even though this version, thereof, will seem pointless. for int i gets 0,
1:40:23
i is less than the length of s. i++ is just the conventional way to start a loop that iterates from left
1:40:31
to right over a string of that length. And then let's go ahead and print out each character, %c,
1:40:38
printing out the string at location i using our fancy new array syntax.
1:40:43
And at the very end of this program, let's just print out a new line character just to move the cursor to the bottom
1:40:48
like we've done in the past. So this is kind of a stupid program like I am reinventing the wheel that is
1:40:54
the %s format code. I already know that printf can print out a whole string. Suppose it didn't.
1:40:59
Suppose I forgot about %s and I only knew about %c, these lines of code here collectively will print out the entirety of a string
1:41:09
character by character based on its length. So if I compile this program, make string ./string and type in my name--
1:41:17
for instance, David, the output is D-A-V-I-D, and here's why I hit the spacebar an extra time,
1:41:22
because I wanted input and output to line up nicely so we could see that they're, in fact, the same length. So let me just stipulate.
1:41:28
This code is correct, but there is an inefficiency with this line of code.
1:41:35
Let's talk about design instinctively. What is maybe bad about this line of code 9--
1:41:42
line 9 that I've highlighted? This one is subtle. Let's go over here.
1:41:47
AUDIENCE: [INAUDIBLE] DAVID MALAN: Yeah.
1:41:54
I'm calling strlen inside of the loop again and again and again. Why?
1:41:59
Well, recall how for loops worked. When we walked through it last week, that middle part of for loop in between the semicolons keeps getting checked, keeps getting checked,
1:42:07
keeps getting checked. And so if you put a function call there, which is totally fine syntactically, you're asking the same damn question again and again and again.
1:42:14
And the length of David, D-A-V-I-D, is never changing. So strlen, implemented decades ago by some other human,
1:42:21
has some kind of loop in it, and you're literally making that code run again and again and again just
1:42:26
to get the same answer 5 again and again. So I think your instinct is right. I could come up with another variable outside of the loop.
1:42:33
I could do something like this. int length equals strlen of s, and then I could just plug that in.
1:42:40
But there's a slightly more elegant way. If you like doing things with slightly less code, this is correct as I've now written it.
1:42:46
It's less efficient-- it's more efficient because I'm only calling strlen once now on this new line 9,
1:42:53
but a more common way to write this would typically be to do something like this. After initializing i, you can also initialize something else like length.
1:43:02
And you can set length equal to strlen of s, then your semicolon, and now you can say while i is less than that length.
1:43:10
Or I can tighten this up further. If it's just a number and it's a super short loop, might as well just call it n.
1:43:16
So this now would be a canonical way of implementing the exact same idea, but without the inefficiency because now you're
1:43:23
calling strlen in the initialization part of for loop, not inside of the Boolean expression that gets checked and executed
1:43:32
again and again. Yeah? AUDIENCE: [INAUDIBLE]
1:43:38
DAVID MALAN: Correct. Well, I'm declaring i as an int, but by way of the comma, I am also declaring n as an int.
1:43:45
So they've got to be the same type for this trick to work. Good observation. Other questions on this one here?
1:43:54
No? All right. Well, let's play around further here. Let me propose that there's other libraries and header files
1:44:01
as well that you might find useful. There's also something called ctype, which relates to types and c's that's got a bunch of useful functions
1:44:08
that we can actually see if we visit the documentation here. But before we get there, let me actually whip up
1:44:14
a program that maybe does something a little bit fun, albeit low level, like forcing some string to uppercase if the human types it in lowercase.
1:44:21
So let me go ahead and write a program called uppercase.c. Let me go ahead and give myself the same header files.
1:44:27
Include cs50.h, include stdio.h. And for now, let's include string.h for the length.

## [uppercase.c](https://youtu.be/4vU4aEFmTSo?t=6274)

1:44:34
And let's go ahead and have int main void as before. And inside of main, let's give myself a string
1:44:40
s equaling get_string "Before," just so I know what the string is initially.
1:44:46
Now I'm going to print out proactively "After" with two spaces just so that things line up aesthetically on the screen
1:44:53
because "After" is one character shorter. And now I'm going to do the same technique as before. for int i equals 0, n equals the string length of s, i is less than n, i++.
1:45:07
And then inside of this loop, what do I want to do logically? I want to force these characters to uppercase if they are, in fact,
1:45:15
lowercase. And so how might I do this? Well, there's a bunch of ways to express this, but I'm going to do it maybe the most straightforward way
1:45:22
even if you've not seen this before. If the current letter in the string at location i,
1:45:28
because I'm in a loop starting from 0 all the way up to, but not through the string length, is greater than
1:45:34
or equal to a lowercase a, in single quotes, and that letter is less than
1:45:42
or equal to a lowercase z. What does this mean in English? Well, this essentially means if lowercase--
1:45:48
logically, if it's greater than or equal to little a and less than or equal to little z, it's somewhere between and z in lowercase.
1:45:55
What do I want to do? Well, I want to force it to uppercase. So I want to print out a character without a new line yet
1:46:03
that prints out the current character, but force it to uppercase. Well, how can I do this?
1:46:09
Well, this is where this gets into some low-level hacking, but notice the same ASCII chart.
1:46:14
Here's our uppercase letters from last time. Here's our lowercase characters, and let me highlight those.
1:46:20
Does anyone notice a relationship between capital A and lowercase a that happens to be the same for capital B and lowercase b?
1:46:29
AUDIENCE: Capital A [INAUDIBLE]. DAVID MALAN: Yeah. Like this pattern is true.
1:46:35
So 97 minus 65 is 32, and that's true for every lowercase and uppercase letter respectively.
1:46:41
So I can leverage that. And this is not a CS50 thing. Like this is ASCII. This is, in turn, Unicode. This is how modern computers work.
1:46:47
So if I go back to VS Code here, you know what I could do. Let's just literally subtract 32. But because I'm displaying this as a char, not as an int,
1:46:55
I'm going to see the lowercase letter seemingly become an uppercase instead.
1:47:01
Else, if it's not lowercase-- maybe it's already uppercase, maybe it is punctuation, let's just go ahead and print out with %c
1:47:09
the original character unaltered. And then at the very end of this program, let's print a new line just to move the cursor to the next line.
1:47:17
All right, so let's do make uppercase. And let me type ./uppercase. And I'll type in D-A-V-I-D, all lowercase, and now,
1:47:26
you'll see it's in all caps. If, though, I type in maybe my last name but capitalized M, that's OK,
1:47:31
the rest of it will still be capitalized for me. Now I don't love this technique. It's a little bit fragile because I had to do some math.
1:47:40
I had to check my reference sheet and then incorporate it into my program. Even though it will be correct, I could be a little more clever.
1:47:45
I could actually do something like this. Well, whatever the value of lowercase is-- lowercase a is minus whatever the value of capital A is,
1:47:53
and I could actually do it arithmetically even though that, too, is somewhat inefficient in that it's asking the same question again
1:47:59
and again, but the compiler is probably smart enough to optimize that. And frankly, for those more comfortable, a good compiler
1:48:05
will also notice, no, no, no, no, you don't want to call strlen again and again. The compiler can do some of these optimizations for you,
1:48:13
but it's still good practice to get into yourself. But there's probably a better way. Instead of rolling this solution ourselves
1:48:19
and subtracting 32 or doing any arithmetic, let's use that ctype library.
1:48:24
Let me go back up to my header files. Let's additionally include ctype.h.
1:48:29
Let's pretend like I read the documentation in advance, which I did, in fact. And let's instead of doing any math here,
1:48:37
let's use a function that exists in that library called toupper and pass to it whatever the current character is in s at location i.
1:48:47
Otherwise, I still print out the unchanged character. And let me go ahead and do make uppercase ./uppercase.
1:48:54
And now without any math, no subtracting 32, that, too, also works.
1:49:00
But it gets better. If you read the documentation for toupper, it turns out its documentation tells you, if C is already uppercase,
1:49:07
it just passes it through for you. So you don't even need to ask this conditional question. I can actually cut this to my clipboard, get rid of all of this,
1:49:17
and just replace that one line only and just let toupper handle the situation for me because again, its documentation
1:49:25
has assured me that if it's already uppercase, it's just going to return the original value.
1:49:30
So if I make uppercase, this time, ./uppercase, now it works and now things are getting kind of fun.
1:49:36
I mean, these are mundane tasks, admittedly, but at least I'm standing on the shoulders of smart people who came before me who implemented the string library, the ctype library--
1:49:45
heck, even the CS50 Library so I don't need to reinvent any of those wheels.
1:49:51
Questions on any of these library techniques?
1:49:57
It's all still arrays, it's all still strings and chars, but now we're leveraging libraries to solve some of our problems for us.

## [Command-line Arguments](https://youtu.be/4vU4aEFmTSo?t=6605)

1:50:05
All right. So let's come full circle to where we began, where and I mentioned that some programs include
1:50:10
support for command line arguments. Like Clang takes command line arguments words after the word clang.
1:50:18
CD, which you've used in Linux, takes command line arguments. If you type cd, space, pset1 or cd, space,
1:50:24
mario in order to change directories into another folder. If you do rm like I did earlier, you can remove a file
1:50:31
by using a command line argument, a second word that tells the computer what to remove. Well, it turns out that you, too, can write
1:50:38
code that takes words at the command prompt and uses them as input. Up until now, you and I have only gotten user input via get_string, get_int,
1:50:47
get_float, and functions like that. You, too, can write code that take command line arguments which,
1:50:52
frankly, just save the human time. They can type their entire thought at the command line, hit Enter, and boom,
1:50:57
the program can complete without prompting them and re-prompting them again. So here's where we can now start to take off some more training wheels.
1:51:05
Up until now, we've just put void inside of the parentheses here any time we implement main.
1:51:11
It turns out that you can put something else in parentheses when using C. It's a mouthful, but you can replace void
1:51:18
with this bigger expression. But it's two things.
1:51:25
int, called argc by convention, and a string, but not a string, actually an array of strings called argv.
1:51:32
And these terms are a little arcane, but argc means argument count-- how many words did the human type at the prompt?
1:51:38
Argv stands for argument vector, which is generally another term for an array-- you've heard it perhaps from mathematics.
1:51:44
It's like a list of values, or in this case, a list of command line arguments. So C is special.
1:51:49
If you declare main as not taking void inside of parentheses, but rather, an int and an array of strings, C will figure out
1:51:58
whatever the human typed at the prompt and hand it to you as an array and the length thereof.
1:52:03
So if I want to leverage this, I can start to implement some programs of my own that actually incorporate command line
1:52:10
arguments. For instance, let me go back in a moment here to VS Code. Let me create a program, for instance, called greet.c
1:52:19
that's just going to greet the user in a few different ways. So let me first do it the old way. cs50.h.
1:52:24
Let me include stdio.h. Let me do int main void still.
1:52:29
So the old way. And if I want to greet myself or Carter or Yulie or anyone else, I could do, old fashioned now, get the answer from the user, get_string.
1:52:39
Let's prompt for "What's your name?" question mark, just like we did in Scratch. And then do printf, "Hello," comma, %s backslash n, answer.
1:52:49
So we've done this many times now this week and last. This is the old school way now of getting command line--
1:52:56
of getting user input by prompting them for it. So if I do make greet /greet, there's no command line arguments at the prompt,
1:53:04
I'm literally just running the program's name. If I hit Enter, though, now get_string kicks in, asks me for my name,
1:53:10
and the program then greets me. But I can do-- otherwise, I could do something like this instead.
1:53:17
First, answer's a little generic, so let's first change this back to name and back to name, but that's a minor improvement there
1:53:23
just stylistically. Let's, though, introduce now a command line argument so that I can just greet myself by running the program, hitting Enter,
1:53:31
and being done, no more get_string. So I'm going to go ahead and change void to int argc, string
1:53:39
argv with square brackets. string means-- the square brackets means it's an array;
1:53:45
string means it's an array of strings; and argc, again, is just an integer of the number of words typed.
1:53:51
Now I'm going to somewhat dangerously going to do this. I'm going to get rid of my use of get_string altogether, and I'm going to change this line to be not name, which no longer exists,
1:54:01
but I'm going to go into this array called argv and I'm going to go into location 1.
1:54:08
So I'm doing this on faith. I haven't explained what I'm doing yet, but I'm going to do make greet ./greet,
1:54:15
and now I'm going to type my name at the command line just like with rm, with clang, with cd.
1:54:20
With any of the commands you've written with multiple words, I'm going to greet literally David. So I hit Enter, and voila, I've somehow gotten access
1:54:29
to what I typed at the prompt by accessing this special parameter called
1:54:34
argv. Technically you could call it anything you want, but the convention is argv and argc from right to left here.
1:54:41
Just a guess, then. What if I change this to print out bracket 0 and recompile the code?
1:54:47
And I run ./greet David? What might it say instinctively?
1:54:54
Any hunches? Yeah. So it's going to say hello, ./greet.
1:54:59
So it turns out, you get one for free. Whatever the name of your program is always accessible in argv at location 0.
1:55:07
That's just because. It's a handy feature. In case there's an error or you need to tell the user how to use the program,
1:55:12
you know what the command is that they ran, but at location 1, maybe 2, maybe 3 are the additional words
1:55:18
that the human might have typed in. Well, let's do something a little smarter than this. Let me go back to version 1.
1:55:25
Let me recompile it, make greet. Let me rerun ./greet David, and this seems to work fine.
1:55:31
What if I get a little curious and print out location 2? Let me recompile the code, make greet ./greet David, Enter, OK, there's null.
1:55:41
And I mentioned we'd see N-U-L-L, and here's one incarnation thereof, but this is clearly wrong.
1:55:47
So I probably don't want to even let the user do this because I don't want them to see bogus output. Like this is arguably the a bug in the code
1:55:53
that it even bothered to show this by default. So what could I do instead? Well, what if I do this?
1:55:59
If argc equals equals 2, then go ahead and comfortably
1:56:07
say printf "hello," argv, bracket, 1. Else, if the human did not give exactly two arguments at the prompt,
1:56:15
let's just print out some default value like "hello, world" like from last week. In other words now I'm doing this error checking with a conditional,
1:56:23
making sure with this Boolean expression only if argc equals equals 2, and therefore has two words in argv
1:56:29
do you want to proceed. And so now if I do make greet again, ./greet David, this now works.
1:56:35
But if I don't cooperate and I just run greet, what should it say? Just hello, world.
1:56:41
If I run David Malan as two words, what should it say? hello, world, because that's not exactly equal to 2.
1:56:49
Again, the first word in argv is always the program's name. The second word is whatever the human, then, has typed.
1:56:56
Now if we don't even know in advance how many words they're going to be, we can combine today's ideas. This is going to look a little weird, but it's the same thing as before.
1:57:04
for int i gets 0, i is less than--
1:57:09
how about argc i++? And then inside of this loop, I can print out %s, maybe backslash n, comma,
1:57:19
and then print out argv, bracket, i. So I can have a loop that iterates argc number of times,
1:57:27
once for every word at the prompt. I can print out argv, bracket, i, which is the i-th word in that array
1:57:34
from left to right. And so if I now run make greet and I do ./greet alone,
1:57:40
I just see the program's name. If I do ./greet David, I see, those two, one after the other.
1:57:47
If I do David Malan, I get those three words. If I keep going, I'll get more and more words.
1:57:52
So using just the length of the array and the name of the array, I can actually do quite a bit there.

## [Cowsay](https://youtu.be/4vU4aEFmTSo?t=7078)

1:57:58
Now there's actually some fun things you can do with this, and this is sort of beside the point, but there's this thing in the world called ASCII art, which
1:58:04
is making pictures and beautiful things just using ASCII or maybe nowadays Unicode characters, but without using emoji.
1:58:09
Like emoji kind of make this a little too easy. But if all you have are traditional largely English letters
1:58:15
and punctuation, you can actually do some interesting things. On Linux systems-- for instance, if I go back to VS Code here,
1:58:21
let me increase the size of my terminal window here. And it turns out that we've pre-installed-- really,
1:58:27
for no compelling reason, but just for fun, a program called cowsay, which has a cow say something.
1:58:34
So if I want to have a cow say "moo" in ASCII art, I can do this, and you get an adorable cow saying something like "moo" on the screen.
1:58:41
But moo is a command line argument that is clearly modifying the output of this program because I could also
1:58:46
change it to say hello, comma, world, and now the cow is going to say that instead. So it takes multiple command line arguments, if you will.
1:58:53
But it also takes what are called flags or switches whereby any command line argument that starts with a dash is usually like a special configuration
1:59:01
option that you would only know exists by reading the documentation or seeing a demonstration. And if I have my syntax right, if I do cowsay -f, and maybe I'll do--
1:59:12
let's see. Instead of this cow say, how about I'll do -f for file,
1:59:18
and I'm going to change it into duck mode. And I'm going to have this version of the ASCII art say quack.
1:59:23
So it's a tiny little duck there, but it's saying quack. And you can kind of waste a lot of time doing this. I can do cowsay -f dragon and say something like, RAWR,
1:59:33
and this is just amazing. Again, not really academically compelling, but it does demonstrate, again, command line arguments, which are everywhere,
1:59:41
and you've indeed been using them already. But there's one other feature we wanted to introduce you to today, which will be a useful building block, which will also

## [Exit Status](https://youtu.be/4vU4aEFmTSo?t=7190)

1:59:50
reveal one other thing about the code that we've been writing. It turns out that all of the programs we've been writing thus far, eventually
1:59:58
obviously exit because you see your prompt again unless you have an infinite loop such that it never ends. But eventually they exit.
2:00:03
And secretly, every program we've written thus far actually has what's called an exit status.
2:00:09
It's like a special return value from the program itself that by default is always 0.
2:00:14
0 as a number in the world generally means everything's OK. The flip side of that is because the world tends to use integers
2:00:21
and you've got four billion possibilities, like every other number in the world when it comes to our program's exit
2:00:27
status is bad. If it's 1, it's probably bad. If it's negative 1, it's bad.
2:00:32
And in fact, you've probably seen this in the real world. If you've ever had like a random error message on the screen--
2:00:37
here's a screenshot of Zoom, for instance. And that screenshot, somewhat confusingly or unknowingly,
2:00:43
has an error code like 1132, that probably means that the Zoom software that some other humans wrote incorrectly somehow
2:00:52
had an error and it did not exit with status 0, it exited with status 1132.
2:00:58
And somewhere at Zoom, there's probably a file or a book that tells the programmers what this error code actually means.
2:01:04
This is not useful for you and me. There's some programmer at Zoom who would probably be like, oh, I know what I did or my colleague did wrong in this case.
2:01:10
You've seen this elsewhere even though this is not quite the same thing, but we'll talk about this in a few weeks. If you've ever seen 404, like numbers are everywhere, and on the web,
2:01:19
404 means like file not found. It means you made a typo, the web server deleted a file, or something like that,
2:01:26
but this is just to say numbers are so often used to signify or represent errors. Even though that's not an exit status, per se,
2:01:33
that's an HTTP status code, which we'll soon see. But you have access to exit statuses as it relates
2:01:40
to command line software already. Up until now, this is how we've been writing main, now
2:01:46
with command line arguments, but we've also been writing main with an int return value.
2:01:51
And you've never used this-- we didn't talk about this last week. I just ask that you trust me and just keep copying and pasting this.
2:01:57
But that int means that even your programs can return values which can be useful even if you don't use command line
2:02:05
arguments and we just go back to the original version like void. So for instance, if I go ahead and open up, for instance, VS Code again,
2:02:15
I'll get rid of the dragon. And let's do one other program here called status just to play around with the idea of these so-called exit statuses.
2:02:23
Let me just demonstrate the idea with an include cs50.h, include stdio.h, int main, and here I'll do int argc, string argv.
2:02:36
And then inside of main, let's do a similar program to before like the hello, world. So printf "hello," comma, %s backslash n.
2:02:44
Then let's print out argv 1. But I only want to execute that line if the human gave me a command line
2:02:52
argument. Otherwise I don't want to even say some default like hello, world. I just want to abort early and just exit the program, no output whatsoever.
2:03:00
So I could do this. If argc does not equal 2--
2:03:05
and it's a single equals, but it's a bang, an exclamation point, means not equal. So this is the opposite of equals equals.
2:03:11
Then previously I would have just printed hello, world, but now I want to print out an error message
2:03:16
like, "Missing command-line argument" just to explain to the user why the program is about to terminate, and then I can return 1.
2:03:26
It's kind of arbitrary. I could also return 1132, but why start there? This is the only possible error that could go wrong in my program.
2:03:34
So I'm going to start at 1. Zoom clearly has 1,000-plus possible things that can go wrong in their source code, which is why the number got as big as 1132,
2:03:42
but I'm just going to arbitrarily, but conventionally return 1. But if everything is OK and I do-- it is not the case that argc does not equal 2
2:03:52
and I actually get to line 11, I'm going to return 0 because 0, again, I claim,
2:03:57
signifies success. And all of this time, every program we've written-- you've written
2:04:03
has secretly exited with 0 by default. But now that our programs are getting more sophisticated,
2:04:09
when something goes wrong, it turns out it's useful to have the power to just return some other value even
2:04:15
though the user is not going to see it. Even though the Zoom user shouldn't see it, it's still there. It's diagnostically useful to you, or in the case of a class,
2:04:22
to your TF or TA or CA. So if I do make status now to compile this program and run ./status and type
2:04:30
my first name I think this is a success. It should say hello, David and secretly exit with 0.
2:04:37
If you really want to see the 0, there's this arcane command you can type. You can literally type at your prompt echo $?.
2:04:45
It's weird symbology, but it's what the humans chose decades ago. This will just show you what did the most recently-run program secretly exit
2:04:53
with. So if I do this in VS Code, I can do exit $?, Enter,
2:04:58
and there's that secret 0. I could have been doing this week and last week, it's just not that interesting. But it is interesting, or at least marginally so, if I rerun status
2:05:08
and maybe I don't provide a command line argument or I provide too many. So argc does not equal 2.
2:05:14
And I hit Enter, I get yelled at with the error message, but I can see the secret status code, which is, indeed, 1.
2:05:21
And so now if you're ever in the habit in either a class like this or in the real world where you're automatically testing your code,
2:05:27
be it with check50 or in the real world, things called unit tests and other third-party software, those tests can actually detect these status code-- exit statuses
2:05:36
and know that your code succeed or fail, 0 or 1. And if there's different types of failures it can detect--
2:05:42
status 2, status 3, status 1132, it's just one other tool in your toolkit.

## [Cryptography](https://youtu.be/4vU4aEFmTSo?t=7548)

2:05:48
But all of that is terribly low level, and really, the goal of this week-- and really, today, and really, code more generally,
2:05:54
is to solve problems. So let's consider an increasingly important one, which is the ability to send information securely,
2:06:01
whether it is in file format, wirelessly, or any other. Cryptography is the art and the science of encrypting.
2:06:08
Scrambling information. So that even if I write a secret message to you and I send it through this open audience with so many nosey eyes
2:06:16
who could look at the message, if I've encrypted this message, none of them should be able to read it, only you, whoever you are,
2:06:22
to whom I intended that message. In the world of cryptography, then encryption means scrambling the information so that only you and the recipient
2:06:30
can receive it. So if we consider our black box like in week 0 and 1, here is the problem to be solved.
2:06:36
And let me propose a couple of pieces of vocabulary. Plaintext is any message written in English or any human language
2:06:42
that you want to send and write yourself. Ciphertext is what you want to convert it to before you just hand it off to a bunch of random strangers
2:06:49
in the audience or a bunch of servers on the internet, any one of whom could look at your message. So in the black box is what we're going to call
2:06:56
a cipher, an algorithm for encrypting or scrambling information
2:07:02
in a reversible way. It doesn't suffice to just scramble the information randomly, otherwise the recipient can't do anything with it.
2:07:07
It's an algorithm, a cipher that encrypts it in such a way that someone else can decrypt it.
2:07:13
And here's a common way. Most ciphers take as input not only the plaintext message in English
2:07:20
or whatever else, but also a key. And it's metaphorically like a key to open a lock, but it's technically generally a number, like a really big number made up
2:07:29
of lots of bits. And not even 32, not even 64, sometimes 1,024 bits, which is crazy
2:07:35
unpronounceable large, but the probability that someone is going to guess your key is just so, so small
2:07:40
that for all intents and purposes, you are, in fact, secure. So what's an example of this, for instance?
2:07:46
Suppose the secret message I want to send is innocuously just "HI!" Well, it'd be pretty stupid to write "HI!" on a piece of paper,
2:07:52
hand it to someone in the audience, and expect it to get all the way to the back without someone like glancing at it and obviously seeing and reading the plaintext.
2:08:00
So what if I, though, agree with someone in back, for instance, that our secret is going to be 1?
2:08:05
And we have to agree upon that secret in advance, but 1 just means that is my key. And let me propose that according to one popular cipher,
2:08:13
if I want to send "HI!", change the H to an I and the I to a J-- that is,
2:08:19
increment effectively every letter of the alphabet by one, and if you get to a Z, wrap back around to A, for instance.
2:08:25
So shift the alphabet by one place in this case and send this message now instead.
2:08:31
So is that secure? Well, if one of you kind of nosily looks at this sheet of paper, you won't see "HI!"
2:08:36
You will see some information leak in this algorithm. You'll see an exclamation point, so I'm enthusiastically saying something,
2:08:42
but you won't know what the message is unless you decrypt it. Now that said, is this very secure, really, in practice?
2:08:50
I mean, not really. Like, if you know I'm just using a key and I'm using the English alphabet, you could probably brute force your way to a solution
2:08:58
by just trying 1, trying 2, trying 3, trying 25, go through all the possibilities tediously,
2:09:03
but eventually it's probably going to pop out. This is actually known, though, as the Caesar cipher. And back in the day, before anyone else knew about or had invented encryption,
2:09:12
Caesar, Julius Caesar, was known to use a cipher like this using a key of three, literally.
2:09:17
And I guess it works OK if you're literally the first human in the world by lore to have thought of this idea, but of course, anyone who intercepts it
2:09:25
could attack it nonetheless and figure things out a bit mathematically. 13 is more common.
2:09:31
This is called ROT13 on the internet for rotate the letters of the alphabet 13. That changes "HI!" to "UV!"
2:09:38
You might think what's better than 13? Well, let's double the security. ROT26. Why is this stupid?
2:09:45
I mean, there's like 26 letters in the alphabet, so like A becomes A. So that doesn't really help-- oh, wait. Oh, I'm pointing at something that's not on the screen, dammit.
2:09:53
Suppose the message is more lovingly, "I LOVE YOU," instead of just "HI!"
2:09:58
Same exact approach, whether or not there's punctuation, "I LOVE YOU," with an input of 13 might now become this.
2:10:03
And now it's getting a little less obvious what the ciphertext actually represents. And now, what's twice as secure is 13?
2:10:10
Well, 26 is surely better, but of course, if you rotate 26 places, that, of course, just gives you the same thing.
2:10:17
So there's a limit to this, but again, that just speaks to the cipher being used, which is very simple.
2:10:22
There is much, much better, more sophisticated mathematical ciphers that are used. We're just starting with something simple here.
2:10:29
As for decryption, if I'm using a key of 1, how do I reverse the process?
2:10:34
Yeah, so I just minus 1. So B becomes A, C becomes B, A becomes Z. And if it's 13,
2:10:41
I subtract 13 instead or whatever the key is, so long as sender and receiver actually know it.
2:10:46
So in this case here, this is actually the message with which we began class. If we have this message here and I used a key of 1 to encrypt it,
2:10:53
well, decrypting, it might involve doing something like this. Here's those same letters on the screen, and I think in a moment
2:11:00
before we adjourn, I'll mention too that we might have encrypted a message in eight characters this whole day, so if any of you took the time
2:11:06
and procrastinated and figured out what the light bulb spelled and they didn't seem to spell anything in English, well, here now is the solution for cracking it.
2:11:13
This, if I subtract 1, becomes what? U becomes T. And this is obviously-- see where we're going with this?
2:11:22
And if we keep going, subtracting 1-- so indeed, we're at the end of class now because this was CS50. And the last thing we have to say is we have hundreds of ducks waiting for you
2:11:30
outside. So on the way out, grab your own rubber duck. [APPLAUSE] [MUSIC PLAYING]
