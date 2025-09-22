---
link: https://youtu.be/3LPJfIKxwWc
related_files:
  - week-0-notes.md
  - problemset/week-0-problemset.md
  - problemset/week-0-scratch.md
title: "Lecture 0: Week 0 - Scratch"
type: transcription
week/lecture: "0"
---

# [Lecture 0: Week 0 - Scratch](https://youtu.be/3LPJfIKxwWc)

TABLE OF CONTENTS:

0:00 - Introduction
1:30 - AI Instructor
2:15 - This is CS50
12:29 - Computer Science
13:56 - Binary
28:03 - ASCII
37:36 - Unicode
46:43 - Color
48:11 - Representation
51:36 - Algorithms
1:00:11 - Pseudocode
1:05:16 - Thank you
1:06:16 - Artificial Intelligence
1:15:52 - cs50.dev
1:16:19 - Scratch
1:19:03 - Hello, World
1:22:06 - Hello, You
1:29:23 - Meow
1:32:10 - Abstraction
1:36:22 - Conditionals
1:43:50 - Oscartime
1:50:33 - Ivy's Hardest Game
2:00:03 - The Harvard Krokodiloes and The Radcliffe Pitches

## [Introduction](https://youtu.be/3LPJfIKxwWc?t=0)

0:00
[MUSIC PLAYING]

## [AI Instructor](https://youtu.be/3LPJfIKxwWc?t=90)

1:30
[AUDIENCE EXCLAIMING] [APPLAUSE]
1:38
SPOT: Hello, world.
1:44
This is CS50, Harvard University's introduction to the intellectual enterprises of computer science
1:50
and the art of programming. Woof, woof. [LAUGHTER]
1:57
2:08
I'm sorry, Dave. [PINK, "WHAT ABOUT US"] What about us?

## [This is CS50](https://youtu.be/3LPJfIKxwWc?t=135)

2:15
What about us? La-da-da-da-da-da-da. La-da-da-da-da-da-da. We are searchlights.
2:21
We can see in the dark.
2:27
We are rockets pointed up at the stars.
2:34
We are billions of beautiful hearts.
2:41
And you sold us down the river too far.
2:49
What about us? What about all the times you said you had the answers?
2:57
What about us? What about all the broken happy ever-afters?
3:05
What about us? What about all the plans that ended in disaster?
3:12
What about love? What about trust? What about us?
3:18
La-da-da-da-da-da-da.
3:24
La-da-da-da-da-da-da. La-da-da-da-da-da-da.
3:30
La-da-da-da-da-da-da.
3:55
DAVID J. MALAN: All right. So-- [APPLAUSE, CHEERING]
4:00
This is CS50, Harvard University's introduction
4:05
to the intellectual enterprises of computer science and the art of programming. And this is Spot.
4:11
And our thanks to our friends at 3D Cowboys for bringing him by class today. Perhaps a round of applause for our special Professor [INAUDIBLE]..
4:18
[APPLAUSE] My name is David Malan. And I actually took this class, CS50, myself, some years ago.
4:26
But I almost didn't. And I didn't because when I got to campus, as a first-year, I really gravitated toward things already familiar, things
4:33
with which I was already comfortable, specifically, government. And I came in here thinking I was going to major or concentrate in government.
4:38
And it was only once I got to sophomore year, fall semester, that some friends of mine were coming to this class called
4:44
CS50 that was very much to beware at the time, in that it was an unfamiliar field to so many of us, myself included.
4:50
But I got up the nerve to go over the threshold, sit in on the first class, just shop it, so to speak.
4:56
And I was hooked. I found that homework was, for the first time, fun. And this was after having enrolled only because the professor let
5:03
me enroll pass/fail or [INAUDIBLE] because I didn't really think I could even cut it. But fast forward to five Mondays later in the semester,
5:10
I actually switched to a letter grade, deciding, wow, this is actually something for me. And I say this because computer science, what
5:17
I didn't realize about it at the time, really is this very general purpose way of thinking and way of solving problems.
5:23
And even if this is the only CS class you ever take, even if this is the only formal training you have in programming
5:29
as a practical skill, it's just so darn applicable to so many other fields-- the arts, humanities, social sciences,
5:35
natural sciences, and beyond, and certainly within the STEM fields, themselves. That said, it's going to often feel a little something like this.
5:43
This is from our friends at MIT, down the road, which is one of their hacks whereby they connected a fire hydrant to a drinking fountain,
5:51
with a little sign up there that says, "GETTING AN EDUCATION FROM MIT IS LIKE DRINKING FROM A FIRE HOSE," which is to say that it's
5:57
going to feel, quite often, in this class, too, that there's just a lot of information. And you can't possibly absorb it all, but realize
6:03
that's to be expected, especially in an introductory class. The whole point is for so much of it to feel new, but with practice, with time,
6:11
with years, even, looking back, will you get all the more comfortable with the material. But you're not meant to feel comfortable along the way.
6:18
And so let me encourage you, invite you, expect you to get comfortable feeling uncomfortable along the way,
6:23
whether you have or have not prior computer science or programming experience. Now, back in my day, the class' syllabus was a little bit different.
6:32
And, really, when I and all of my classmates exited the class, we would say to friends that we learned how
6:37
to program in C, which is a language that we, ourselves, will still learn in this class. But that was it for languages.
6:44
But nowadays, as you'll see, we'll explore not just this older language called C, but a more modern language
6:49
called Python that's very much in vogue for data science, and web applications, and much more. But we'll also introduce you, along the way,
6:56
to another language called S-Q-L or SQL, which is specifically for databases. And SQL is a different type of programming language
7:03
that's just going to give you different ways of solving problems, different building blocks with which to express problems you want to solve.
7:09
We'll introduce you, toward the end of the semester, yet another language, JavaScript, often used with markup languages called HTML and CSS, with which maybe you
7:17
have some experience if you've made websites. But we'll do this because so many of today's actual real-world software
7:23
is web-based. Or it's phone-based, mobile-based, but even then, it's using these same languages, like JavaScript.
7:30
And so by the end of CS50, in particular, you won't know how to program in X, or Y, or Z, per se.
7:35
But, period, you'll learn how to program. And, indeed, among the goals of this class
7:41
is to equip you with enough of a set of concepts, enough practical skills and experience that after CS50, again, if you never take another CS class,
7:49
you can teach yourself new languages. And you won't feel-- you won't have been reliant on a class to, indeed,
7:55
introduce you to each and one of those ideas. And what are we going to do, then, in this class? And, really, what are we going to start doing today?
8:01
Well, we're going to learn how to solve problems. And that's really what computer science is all about. We'll, very specifically, today, knock off a few to-dos.
8:09
We'll learn how to represent simple things, like numbers. We'll learn how to represent letters of an alphabet, like English.
8:14
We'll learn how to represent colors-- red, green, blue, and everything in between. We'll learn how to represent, more interestingly,
8:20
full-fledged images that you might see on the web or your phone. We'll talk about representing videos and even audio files.
8:26
So, by the end of today, alone, you will exit here with a newfound mental model for how you can
8:31
represent all of today's media and multimedia that we take for granted and use most every day.
8:37
But we'll also focus today, ultimately, on how to write algorithms, like step-by-step instructions for solving
8:43
some problem, specifically, implementing algorithms with code. And that's what we'll find. An algorithm is just something you can express
8:50
in English or any human language, but code is a translation of that to, presumably, the 0's and 1's that you've probably heard
8:57
is all that computers ultimately speak. And if you're feeling like that's a lot for today, if you're feeling like that's a lot for the whole semester,
9:04
realize and take comfort in knowing that -thirds of you have never taken a CS course before.
9:09
So even if you think, like I did all those years ago, that, surely, my friends, the kids I didn't even in the class,
9:15
must know more than I, have been programming since they were six years old. That's just not the case. You're in very much good company.
9:21
And within the class will you find different tracks, by way of the homework assignments, called "problem sets,"
9:26
by way of the sections or recitations. There will be different tracks for those of you less comfortable, more comfortable, somewhere in between.
9:32
And if you really don't know why you are here today, we'll even have sections for those least comfortable, where you just
9:37
don't necessarily feel ready to dive into CS or maybe STEM, more generally. But we'll get you there by way of the course's support structure.
9:44
And it's very much grounded in this mindset. What ultimately matters in this class is not so much
9:50
where you end up relative to your classmates, but where you end up relative to yourself, when you began. So whether you have or have not prior programming or CSS experience,
9:58
it's not going to matter when it comes to evaluation, when it comes to the output, be it a grade, or a satisfactory mark, or the like.
10:04
It's going to depend on, really, where you are today, in this, what we call week zero, versus the very end of the semester, when
10:11
you will have built something grand, of your very own, in software. But CS50 is also characterized, fairly uniquely,
10:17
by its community, its culture. And along the way, you'll see that your experience is punctuated by a lot of social and academic events alike.
10:24
CS50 lunches, most every Friday, we'll gather at a nearby restaurant called Changsho where we'll have Chinese lunch together.
10:30
And as many of you as might want to attend that week will be able to join us, sit down, and chat casually with me, the course's teaching staff, friends of ours, alumni from industry, as well.
10:39
CS50 Puzzle Day, coming up this weekend, will be an opportunity, even if you have no prior CS experience, just to solve problems,
10:46
not jigsaw puzzles, but puzzles in the logical sense. We'll hand you a packet of puzzles--
10:52
logic problems, or riddles, or the like-- that you, as teams, can solve together. And at the very end, we'll walk you through.
10:57
And along the way, there'll be not only these puzzles, but pizza, and prizes, and so much more, as well.
11:02
Towards the end of the semester, we'll have a CS50 Hackathon whereby we'll get together around 7:00 PM, at the start of reading period,
11:09
and we'll finish up around 7:00 AM the next morning. And it will be this opportunity to really bond
11:15
with your classmates, your project partners, if you work in a team, on your very own final project, which is meant
11:20
to be a capstone of the course, something you build, yourselves, that we don't hand you a specification for.
11:25
But it's your final offboarding, so that when you exit CS50, you don't need CS50 anymore.
11:31
You don't need me. You don't need your TF. You can actually write code and solve problems on your own. So this picture here is one of our past photos from earlier in the evening.
11:39
Things get a little quieter as we then, around 5:00 AM, drive anyone who's still awake and energetic to a nearby IHOP
11:46
for pancakes, around then. But here is how most of the evenings tend to end for at least some
11:51
of your classmates prior. But at the very end of the class is the so-called CS50 Fair, an exhibition of all of your final projects for friends, faculty,
11:59
students, and staff across campus, whereby you'll be invited to a space like this. Bring your laptop. Bring your phone, whatever it is you have built and created.
12:06
And we'll just show it off for a bit of the afternoon, complete with music, and friends from industry, and candy, and all what makes gathering together at term's end fond.
12:16
And you'll wear, ultimately, very proudly, we hope, your very own "I took CS50," stating, very matter of factly,
12:21
what I did some years ago; that, indeed, this was a course I, myself, took. So, today, let's focus, then, on computer science, like what is it.

## [Computer Science](https://youtu.be/3LPJfIKxwWc?t=749)

12:29
Well, it's really the study of information. But, really, it's, more specifically, about solving problems,
12:34
using certain ideas and techniques, all of which you'll exit the course with. So, as such, problem solving is a goal that we'll
12:43
approach by way of something called "computational thinking." So computational thinking, you can oversimplistically think about it
12:49
as thinking like a computer. But it's really the application of ideas that we'll dive into today
12:55
and we'll finish some weeks from now, that you can apply to problems from this field or most any other, but in a computational,
13:01
that is, a very methodical, very careful way. And that's what CS really did for me and does for a lot of people.
13:07
It helps clean up your thought processes. Even if you go off into the real world and do nothing in tech,
13:12
you have an ability, after classes like this, to express yourself a little more correctly, more
13:18
precisely and, generally, having better command of your own ideas and your language. So what's problem solving?
13:24
Let me propose that this is it. This is as simple as we can make today's goals and the semester's goals. Problems to be solved look like this.
13:30
You've got some input, the problem to be solved. You've got a goal being the output, like the solution there, too. And then somewhere in the middle is the secret sauce,
13:38
where we'll spend the next several weeks figuring out how we can convert these inputs to outputs. But before we can do that, we all just have
13:44
to agree on how to represent these inputs and outputs, whether it's with English or, really, any type of language.
13:51
But, as I spoiled earlier, you probably came in here already with a general sense that, yeah, computers somehow

## [Binary](https://youtu.be/3LPJfIKxwWc?t=836)

13:56
only speak or know 0's and 1's, the so-called binary system. But that's just one way of representing information.
14:02
Even simpler than binary is unary. So if you've ever, at this age or any prior age, counted on your fingers,
14:10
this is unary notation, whereby each of your digits, your fingers literally represent some piece of information;
14:17
taking attendance, like 1, 2, 3, 4, 5. But on your one human hand, how high can you count in this unary notation?
14:25
AUDIENCE: Five. AUDIENCE: Five. DAVID J. MALAN: Five, I'm hearing five. Six, I heard one six.
14:31
But I'm going to go further and say the answer, if you're clever about it, is actually-- AUDIENCE: 40?
14:37
DAVID J. MALAN: Not quite 40. You overbid, but-- AUDIENCE: 31. DAVID J. MALAN: 31 is as high as I can actually count.
14:43
And that's because if I actually-- and if you're thinking this is weirdly painful now, it will be, but this
14:49
is my hand representing the number 0. Normally, in unary, this is 1, 2, 3, 4, 5, of course, obviously.
14:55
But what if I take into account the order in which I'm putting my fingers up and down? So maybe this is still 0. Maybe this is still 1.
15:02
But maybe this is now 2, where it's just the single second finger up, not two of them, total.
15:08
Maybe this is now 3. Maybe this is now-- often offensive, with just the middle finger up.
15:14
This is now [LAUGHS] 5. This is now 6. This is now 7.
15:21
And my hand just hurts too much if I try to count higher than seven. But, theoretically, because each of my fingers can be down or up
15:27
and I've got five of them, that's actually 32 possible permutations, up and down.
15:32
But wait a minute. We said, 31, but if you start at 0. You have to subtract 1 from the biggest possible value.
15:38
So this is to say you and I have been using unary because it's just simple, and it gets the job done. But if we just think about representation a little more cleverly,
15:46
we can do exactly what computers do, using not what mathematicians call "base-1," where the finger is either there or it's not, but base-2.
15:54
And in base-2, we just need two digits at our disposal. And we could call these digits 1 and 2, A and B, black or white.
16:02
We just need two words to describe two pieces of information. Computers keep it simple. And just like we humans start counting 0, 1, 2, 3 on up,
16:10
computers use 0 and 1, and that's it. But that's by convention. But why do they do that?
16:16
Well, it turns out, when you use base-2, otherwise known as binary, well, it just maps really readily to the real world.
16:24
Because, at the end of the day, what do we all do, if you've got a laptop, or a phone, or any device? You plug it into the wall because it needs electricity at some point.
16:32
And what if you have electricity or not? Well, there's your two possible values.
16:38
Either it's there, or it's not. And because computers are electrical devices, this is why binary is just useful.
16:43
It's nice and simple. Either electricity is there, or it's not. So when you plug this device in and you've
16:48
got all these electrons or whatever flowing, maybe if we just hang on to some of that electricity, we can represent what we'll call a 1.
16:55
And maybe if we let it dissipate or go away, that's a 0. So on and off maps very readily to this idea of just 0's and 1's.
17:02
And if you've ever thought of this, now, as binary digits-- "bi" implying 2, 0 and 1-- well, if you've ever heard this term now,
17:10
"bit," it just means binary digit. A single bit is just a 0 or 1. But we could have called these things anything we want.
17:16
Now how does this map to be clear to the real world? Well, we can't see the tiny little switches inside of our Macs,
17:23
PCs, and our phones that are actually turning the electricity on or off, storing electricity or not.
17:28
But they're called transistors. They've got millions of them in today's hardware. And they're just on or off, like a switch or a light bulb.
17:35
So, for instance, if there's no electricity, the switch is off, we would call this, by convention, a 0.
17:40
If, though, you throw the switch and it actually turns on, we would call this-- AUDIENCE: On.
17:45
DAVID J. MALAN: --an "on," exactly, a 1. We could have reversed it. But this is just the way the world decided to standardize.
17:51
And that's it. So you've either got something on or off, a 1 or a 0. And this, then, is this thing we know now as a binary digit or a bit.
18:00
So once we've got these values, what about how-- how can we go about, perhaps, representing things?
18:07
Well, you know what? It turns out we've got a lot of light bulbs right here. Let me grab-- thanks. Excuse me, spot. Let me grab the little music stand here.
18:16
Let me borrow a couple of these bulbs and see if we can't make clearer than my hand, alone, what's going on here.
18:22
So I'm going to go ahead and grab two of these. And I'll just put them here. And I can turn these things on or off now.
18:28
So if I've got two bits, two switches, two transistors, if you will, well, if I go ahead and turn on this one, I'm representing what number in binary,
18:38
perhaps? AUDIENCE: 1. DAVID J. MALAN: So just 1. Now, if I'm using unary, I would turn this one on and be done with it.
18:45
And that's 2, but not in binary. Binary, it's the permutations, which ones are on and off, that matters.
18:51
So what, now, am I representing here, perhaps? AUDIENCE: 2. DAVID J. MALAN: 2. So this is when I put my single pointer finger up.
18:58
But then when I did this, in my human hand, this was like representing the number 3.
19:03
How do I represent the number 4. Yeah, I need another light bulb, so I need more hardware, so to speak.
19:11
So if I turn-- if I leave this one-- if I turn this one on, this one off, this one off,
19:19
now I have the number 4. And someone tell me, saying the words "on"
19:24
and "on" and "on," or "on," or "off," or "on," using combinations of "on," "off" and-- "on" and "off," how do I represent 5, from your left to your right?
19:32
How about over here? AUDIENCE: On, off, on. DAVID J. MALAN: "On, off, on," I heard. And that's exactly right.
19:38
And how do I represent, maybe, 6? Over here? AUDIENCE: Off, on, on. DAVID J. MALAN: Off, on, on, not quite.
19:45
From left to right? AUDIENCE: Off-- the other way. DAVID J. MALAN: The-- [LAUGHS] OK, so from right to left. So I think we leave this one on.
19:50
This one, I'm going to claim, represents, now, 6 and 7.
19:58
AUDIENCE: On, off. DAVID J. MALAN: I'm just going to-- it's actually going to be "on, on, on." Now, if you're wondering, where are these people coming up
20:04
with these combinations, there's actually a system here. It's actually hard for me to do it backwards.
20:09
But it turns out there's actually a system that's not all that unfamiliar. In fact, let me propose this.
20:15
Let me propose that we consider what you and I all learned in grade school, which was something like the base-10 system, 10
20:23
meaning that you use 10 different digits, not two, 10. So 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, that's the base-10 system, otherwise known
20:30
as decimal, "dec" implying 10. So that's what you and I use every day. Well, let's think about how we represent numbers in decimal,
20:37
in the normal human way. Well, here is a number. It's what number, of course? AUDIENCE: 123.
20:42
DAVID J. MALAN: 123. So we all just have an intuition for that, obviously. But it's not necessarily 123.
20:48
You're just assigning meaning to the positions of these digits. This is really the pattern 1-2-3.
20:54
But you immediately jump, mathematically, to 123, but why? Well, odds are, in grade school, you learned that the rightmost digit is
21:00
the ones place or the ones column. This is the tens place or the tens column. This is the hundreds place.
21:06
And so why is this relevant? Well, this is like doing 100 times 1 plus 10 times 2 plus 1 times 3 or, if we multiply that out, 100 plus 20 plus 3,
21:16
ergo, the number, now, that we just take for granted is 123. But that's in base-10, the so-called decimal system,
21:24
whereby each of these digits is in a different column. And those columns are, again, ones place, tens, hundreds.
21:31
If we keep going, thousand, ten thousand, and so forth. But where did these come from? Well, here's the base. If you remember exponents and all of that,
21:37
this is just 10 to the 0, 10 to the 1, 10 to the 2, ad infinitum. And so, now, what if we just changed the base from 10, 0 through 9,
21:46
to just two digits, 0 and 1? Well, now the math is fundamentally the same. But it's 2 to the 0, 2 to the 1, 2 to the 2,
21:52
which gives us the ones place, twos place, and fours place. Now, why is this relevant?
21:58
If you've got three light bulbs or three bits that are off, off, off, what have I done?
22:03
4 times 0 plus 2 times 0 plus 1 times 0 is, obviously, the number you and I know, in decimal, as 0.
22:09
This, though, represents the number you and I know as-- AUDIENCE: 1 DAVID J. MALAN: This represents-- AUDIENCE: 2.
22:15
DAVID J. MALAN: --3, 4. And just to be clear, this is why, when I grabbed the additional light bulb,
22:21
we claimed that this now was 4. Because we had "on, off, off," "on, off, off."
22:29
This now is 5. This now is 6. This now is 7. And if I wanted to count higher, what would the pattern of 0's and 1's be
22:36
for the number 8? AUDIENCE: 1, 0-- DAVID J. MALAN: 1, 0, 0, 0. So we just need more hardware, more bits.
22:42
So it wasn't arbitrary, even if it was non-obvious, what I was actually doing with turning these light bulbs on and off.
22:49
Now, it turns out here we are talking about how to represent information, like numbers, but we could also use bits, 0's and 1's, light bulbs
22:59
to represent instructions, as well. Because, at the end of the day, that's all computers do. They process data, information of some sort, whether it's files,
23:07
or numbers, or images, or videos, or the like. And you do things with those files.
23:13
You open them. You print them. You edit them and the like. So there's this notion of instructions, what the computer can actually do.
23:18
And I bet we could come up with some pattern of 0's and 1's or, equivalently, light bulbs that tell even Spot what to do.
23:26
Maybe, go up, or down, or left, or right. And it could certainly do this autonomously by using various sensors.
23:33
We need to keep things safe today. We're using Wi-Fi in sending Spot these very instructions. But what's happening, wirelessly, with our friend Andrew, here, is,
23:41
essentially, he's sending Spot instructions just encoded, wirelessly, somehow, as patterns of 0's and 1's.
23:47
And the folks at Boston Dynamics, who built this robot, programmed Spot to recognize certain patterns as meaning "up,"
23:54
a certain pattern as meaning "down," "left," "right," and any number of other things. So, in fact, Spot, come on over here, if you could.
24:00
Come on, Spot. [FOOTSTEPS] OK.
24:05
So Spot, for instance, may very well have a pattern of 0's and 1's that represents shake.
24:11
Shake, Spot. So he could do that and any number of other movements, as well.
24:16
And maybe, especially with sensors here and also a little human help over here, for today, what if we went ahead and did something-- maybe
24:22
ask Spot some questions? So let's go ahead, and we'll start simple. Spot, here we have some bits, "off, off, on."
24:31
Spot, what [LAUGHS]-- OK. Spot, what is this representing, "off, off, on"?
24:41
[SPOT TAPS STAGE] Correct? I think so. Very horse-like, OK.
24:46
Thank you. All right, so a round of applause for Spot here. [APPLAUSE] All right. So, Spot, what if we [LAUGHS] turn--
24:54
OK. We'll turn that one off here. How about if we turn this one on? So it's "off, on, off." Spot, what's this number?
25:02
[SPOT TAPPING STAGE] Is that correct? Nice. OK. [APPLAUSE]
25:07
[LAUGHS] How about one final flourish? How about, Spot, instead of "off, on, off," let's go ahead and do "off, on, on"?
25:16
So think, in your mind's eye, what the answer should be. All right, Spot, "off, on, on."
25:24
[SPOT LANDING ON THE STAGE] OK. And a round of applause for, Spot, as well.
25:30
[LAUGHS] [APPLAUSE] So this is to say, no matter how--
25:36
thank you, Spot. No matter how fancy today's hardware or software is, it really just boils down to representing
25:42
information and instructions. And computers, and phones, and the like really are just operating on those same pieces of information,
25:51
whether implemented in 0's and 1's or with, really, anything else. All right. So, where can we take this, once we have this agreed-upon system
25:59
for representing [LAUGHS] information? Well, it turns out that using three bits, three 0's and 1's, at a time,
26:06
isn't actually all that useful. And you and I, even in conversation, don't often say the word "bit."
26:12
We say the word "byte." And what is a byte, if familiar? Yeah? AUDIENCE: It's eight bits. DAVID J. MALAN: So it's just eight bits.
26:18
It's just a more useful unit of measure. And it happens to be a power of 2, 2 to the third, which just makes math work out cleanly.
26:24
But it's just a convention, to have more interesting units of measure than individual bits. So a byte is eight bits.
26:30
So, for instance, this represents, using eight bits, eight light bulbs, the number you and I know is 0.
26:36
And this byte of all 1 bits-- now you've got to do some quick math-- represents what number, instead?
26:46
So it's all 1's; eight of them, total. How about over here, on the end? AUDIENCE: 255.
26:51
DAVID J. MALAN: So it's, indeed, 255. Now, that's not the kind of math that you need to do in your head for a class like this, but you could.
26:57
This is the ones place, twos, fours, eight, 16, 32, 64, 128.
27:04
And because they're all 1, you just have to add up all of those columns' values. And you get 255.
27:10
But a little mental trick, too, is that, if you've got eight bits and each of them can be two possible values, 0 or 1,
27:17
that's like 2 possibilities here times 2 times 2 times 2 times 2, eight times. So that's 2 to the eighth, so that is maybe a little easier to do.
27:25
That's 256. Or easier, in the sense that you get used to seeing these numbers in CS. That's 256.
27:31
But wait a minute. How do I reconcile this with your 255? Because you start at 0.
27:36
So you lose one on the high end because we started counting and representing the number, like 0.
27:42
All right. Questions on how we've represented just numbers or, for instance, instructions to Spot, thus far?
27:51
Any questions on binary, unary, or the like?
27:57
No? All right, so seeing none, let's let things escalate a bit. So how do you represent letters because, obviously, this

## [ASCII](https://youtu.be/3LPJfIKxwWc?t=1683)

28:03
makes our devices more useful, whether it's in English or any other human language. How could we go about representing the letter A, for instance?
28:10
If, at the end of the day, all our computers, all our phones have access to is electricity; or, equivalently,
28:17
switches; or, metaphorically, tiny little light bulbs inside of them that can be on and off-- that's it.
28:23
There's no more building blocks to give you. How could we represent something like the letter A?
28:30
Yeah, how about here? Yeah? AUDIENCE: You could assign a number. DAVID J. MALAN: Perfect. So we could just assign every letter a number.
28:37
And we could do this super simply. Maybe 0 is A, and 1 is B. Or maybe 1 is A,
28:42
and 2 is B. It doesn't really matter, so long as we all agree and we all use the same types of computers, in some sense, ultimately.
28:48
Well, for various reasons, the humans that designed this system, they went with the number 65. So, nowadays, anytime your computer is showing you the capital letter
28:57
A on the screen, underneath the hood, so to speak, it's actually storing a pattern of 0's and 1's that represents the number 65.
29:06
And it tends to use seven bits or, typically, eight bits, total, even if it doesn't need all of those bits in total.
29:12
So how do we get there? Well, here, for instance, is that same pattern. Here is that pattern of bits that represents 65.
29:19
And why? Well, quick check here. This is the ones place, twos, fours, eights, 16, 32, 64's place.
29:29
OK, so 64 plus 1 gives me 65. So that is to say here's how a computer, using some light switches, so to speak,
29:36
would represent the number 65. And our Macs, our PCs, our phones just all know this. So whenever they see that in their memory, so to speak,
29:44
they show a capital letter A on the screen. So that's it. That's the system known as ASCII, the American Standard
29:51
Code for Information Interchange. And the A is actually operative there because we're only talking, thus far,
29:57
about English letters in our alphabet. And, in fact, I claimed, a moment ago, that we only use
30:02
seven, maybe eight bits to represent letters of an alphabet. So, just to come back to you, if I may, how many
30:08
possible letters of the alphabet could-- how many possible letters of any alphabet could we represent with eight bits?
30:14
AUDIENCE: 256. DAVID J. MALAN: 256, the numbers 0 through 255. Now, that's more than enough for English because we've
30:20
got A through Z, uppercase, lowercase, a bunch of numbers, a bunch of punctuation symbols. But in a lot of languages, with accented characters, a lot of Asian characters,
30:28
this is not nearly enough memory or bits with which to represent all of those possible values.
30:34
So we need to do a little better than ASCII, but we can build on top of what they did years ago. So here is a chart of ASCII codes.
30:41
It's just a bunch of columns showing us the mapping between letters and numbers. So, for instance, up here is the capital letter A, 65; capital B, 66;
30:49
capital C, 67; dot, dot, dot. 72 is H. 73 is I and so forth.
30:56
There's some weird things over here, like special symbols, that we'll learn about over time. But there's a mapping between every English letter
31:02
of the alphabet and some number, just as you'd propose, both for uppercase and lowercase. So, for instance, if we highlight just a few of these for now
31:10
and I say that I've just received a text message or an email that, underneath the hood, so to speak, if I have the ability
31:17
to look at what switches are on and off, I received this message here.
31:22
Well, first-- and this is not what CS is about, but just fun fact. Does anyone know what number this would represent in decimal,
31:29
if this is the binary pattern, like ones place, twos place?
31:34
AUDIENCE: 72? DAVID J. MALAN: 72 is correct. And again, not, intellectually, all that interesting
31:39
and this is not the kind of math that we spend all day as CS-- a computer scientist doing. But it's just following the same darn pattern, which
31:45
is to say it might look cryptic, but, conceptually, intellectually, it ultimately is exactly as we did before.
31:50
So, yes, I'll spoil the rest of the math. It's 72, 73, 33. Now, anyone remember, in your mind's eye, what message we just spelled?
31:58
AUDIENCE: Hi. AUDIENCE: Hi. DAVID J. MALAN: Yeah, so it is, in fact, "Hi!" Though, no one really said that excitedly. What's the 33, if you noticed?
32:04
AUDIENCE: Exclamation point. DAVID J. MALAN: OK, so a lot of people noticed. Yes, it's an exclamation point. And that's, indeed, noticeable right here.
32:11
33 is the exclamation point. And that's just something, eventually, that might sink in. But, for the most part, if you remember capital A is 65,
32:18
you can figure out at least 25 other answers to these kinds of questions because they're all contiguous like that.
32:24
So there's the exclamation point. But at the end of the day, we might just have this mapping known as ASCII.
32:30
And it's how our phones, and computers, and devices, more generally, actually store information. So we thought we'd make--
32:37
maybe take a little pressure off of me here. And could we maybe flip things around? How about we try applying this newfound knowledge--
32:44
if it's, indeed, new to you-- with seven volunteers, seven bits, if we could? OK. I saw your hand first.
32:49
Come on down. Maybe your hand, there. OK, three, come on down over here.
32:54
How about four and five? Yep, come on down. Yep, in the black shirt, yep. How about let me go farther back?
33:00
How about in the green, over there? And how about you, seven, over here? All right. Come on down. [CHATTER]
33:05
Come on down. So a round of applause for our brave volunteers. [APPLAUSE]
33:12
All right. So if you'd like to stand, roughly, side by side, here in the middle of the stage.
33:17
First of all, thank you. Let's see.
33:23
1, 2, 3, 4, 5, 6, 7, perfect. OK. And let's go all the way over to this place, here.
33:29
If you would like to introduce yourself to the class. RACHEL RICHEY: I'm Rachel Richey. DAVID J. MALAN: OK.
33:35
And what year? Anything about you? RACHEL RICHEY: Oh, first year, concentrating in CS. DAVID J. MALAN: OK. Welcome to the stage.
33:40
Next. SPEAKER: Hi. I'm [? Kang. ?] Also a first-year concentrating in CS.
33:46
SPEAKER: Hello. My name is [? Lam. ?] I'm a [INAUDIBLE] student from education department.
33:52
DAVID J. MALAN: Nice. OK. Next. JORDAN MITTLER: Hi. I'm Jordan Mittler, concentrating in economics and maybe some CS.
33:59
SPEAKER: So, hi. I'm [? Natalia. ?] First year, and I want to do CS. SPEAKER: Hi. I'm [? Khadija. ?] I'm a first-year, and I want to do CS.
34:05
DAVID J. MALAN: [LAUGHS]. SPEAKER: Hello. I'm [? Caleb. ?] And, once again, first year, concentrating in CS.
34:11
DAVID J. MALAN: OK. Wonderful. A pattern, yes. Thank you. Thank you. [APPLAUSE] So, if you haven't guessed already, each of these volunteers
34:20
is going to represent a bit, from left to right, or right to left, in this case. So let's see. If you want to represent-- how about the twos place?
34:27
How about the fours place, the eighths place, 16ths place, 32's, 64, and 128?
34:37
Although, wait a-- I think I screwed up. We needed one-- eighth volunteer. I think you know-- well, I think--
34:42
[CLEARS THROAT] Spot? OK. Come on over. If you guys could step forward a little bit, and then scooch this way,
34:49
just to give Spot some room. [FOOTSTEPS] So Spot will represent the ones place.
34:55
Now, what our volunteers have on the back of their sheets of paper are little instructions. We're going to spell out a three-letter word in English by using three bytes,
35:05
from left to right, because now we have eight volunteers. I'm going to propose that you raise your hand, if you're
35:10
supposed to represent a 1. Or you just stand there, without raising your hand, if you're meant to represent a 0.
35:15
And what we'll have the audience do is do the quick math to figure out-- one, two, three-- each letter, what number is it.
35:22
What letter is it? And we'll see what word that we have finally spelled. All right. So, in round one--
35:28
you have instructions on your back of your sheet that will tell you to-- what your number is. If you're 0, stand there.
35:33
If you're a 1, raise your hand. [PAPER RUSTLING]
35:40
What number do these guys seem to be representing? AUDIENCE: 68. DAVID J. MALAN: 66, I think.
35:46
64 plus 2, so 66, which is the letter-- AUDIENCE: B. DAVID J. MALAN: OK, so, B. OK, so, B. All right.
35:52
Hands down. Second letter is going to be spelled how?
36:01
[SPOT LANDS ON THE STAGE] AUDIENCE: Whoa. AUDIENCE: Whoa. AUDIENCE: Whoa. DAVID J. MALAN: [LAUGHS] All right.
36:07
What are we spelling now? [INDISTINCT CHATTER] I think-- psst, yep, OK.
36:15
Yeah, I think you're one. [LAUGHTER] OK.
36:20
Now what number are we spelling? AUDIENCE: 79 DAVID J. MALAN: 79, I heard, which is the letter?
36:26
AUDIENCE: O. DAVID J. MALAN: O. OK. So hands down. Thank you, Spot. One final flourish. So we've spelled B-O--
36:33
third letter, go ahead. [SPOT LANDS ON THE STAGE]
36:40
What number, now, is this? AUDIENCE: 87. AUDIENCE: 87. DAVID J. MALAN: I heard it here, 80--
36:45
AUDIENCE: Seven. DAVID J. MALAN: --seven, which is? AUDIENCE: W. DAVID J. MALAN: W, which, of course, spells "bow." So if our volunteers could take a bow, Spot included.
36:53
[APPLAUSE] So this will make more sense in week one,
37:01
when we have an assignment involving a certain someone from the Nintendo World. But we have a lovely parting gift for each of you.
37:06
SPEAKER: Thank you. [LAUGHS] DAVID J. MALAN: Thank you for volunteering. SPEAKER: Thanks. DAVID J. MALAN: You might need to share it with the folks next to you.
37:11
[CHATTER]
37:18
Oop, here we go. There we go. Thank you-- SPEAKER: Thank you. RACHEL RICHEY: Thank you. DAVID J. MALAN: --so much. One more round of applause, if we could, for our volunteers. Thank you.
37:23
[APPLAUSE] Did you lose something? OK. All right. So, [LAUGHS] Spot's had it.
37:31
So let's see, then, if we've solved, now, the problem of representing English letters of the alphabet,

## [Unicode](https://youtu.be/3LPJfIKxwWc?t=2256)

37:36
being able to spell out words like "bow," B-O-W. What if we actually do have accented characters? What if we do have other glyphs that we want to represent?
37:43
Well, here, of course, is a standard US English keyboard, which a lot of you might have. But there's also characters that you can type much more
37:50
easily if you have a foreign keyboard, relative to the US, or with certain keystrokes on your own Mac, PC, and phone.
37:55
But, nowadays, too, there's this menu that, probably, you've used in the past hour or two to actually send some emoji.
38:03
An emoji, even though they look like pictures and they actually are pictures on the screen, they're, technically, just characters, characters of an emoji alphabet
38:13
that happened to use a certain pattern of 0's and 1's to represent each of these faces, each of these people, and places, and things.
38:19
And it turns out that one of the reasons that we have just so many [LAUGHS] such characters nowadays is because we now
38:29
use Unicode instead of ASCII. So Unicode is a superset, so to speak, of ASCII,
38:34
which is to say that we, humans, realized, some time ago, that just using eight bits to represent letters of the alphabet
38:40
certainly isn't very good when we want to represent other, non-English languages. So Unicode doesn't just use eight bits.
38:47
It sometimes uses 16 bits per character, sometimes 24 bits per character,
38:52
and sometimes even 32 bits per character. Now, why those numbers? That's just one byte, two bytes, three bytes, or four bytes.
39:00
And that gives us-- does anyone know? That gives us the ability to represent as many as 4
39:06
billion possible characters. Because if the longest one is 32 bits, that's 2 to the 32,
39:12
which, if you do out the math, trust me, is roughly 4 billion. So that's a lot of characters. And we've got a lot of room, then, for these emoji.
39:19
But it's not just about having fun, pictorially, on the screen. Unicode's mission really is to represent and to preserve all human languages
39:27
digitally, both past, present, and future. So it is really about capturing the entirety of human knowledge,
39:35
as we've expressed it in language, but also giving this newfound ability that's been used centuries ago, too-- in writings,
39:42
on walls, and the like-- pictograms via which we can still communicate, even independently of our own human language.
39:48
So we'll reduce it, today, to just patterns of 0's and 1's, but the problem being solved is much greater and well-beyond CS, itself, there.
39:56
So here is a pattern of 0's and 1's using Unicode, so more than eight bits, that represents a very popular emoji, which
40:04
might be a bit of a hint. This is the most popular emoji, as of last year, at least, statistically, internationally.
40:10
[INTERPOSING VOICES] DAVID J. MALAN: Does this help? It's, roughly, this number here.
40:16
No? It's this one here. So this is the most popular emoji, by most measures, as of last year.
40:23
But it doesn't always look like this. Those of you who have a Mac or an iPhone recognize this symbol, perhaps, immediately.
40:28
Those of you with Android devices or other platforms might notice that it's the same idea, but it's a little bit different.
40:35
And this is because, too, emojis, at the end of the day, just represent character, but those characters can be drawn,
40:41
can be painted in different ways. And reasonable people will interpret differently this emoji, whose official name is "face with tears of joy."
40:49
And, indeed, Google interprets it a little differently from Apple, versus Microsoft, versus Meta, versus other companies, as well.
40:55
So you can almost think of those different companies as having different fonts for emoji. And that really starts to connect things to the world of text and characters.
41:04
So, just so you've seen it. More on this, another time. It turns out that emoji and, really, characters, in general,
41:10
we don't use binary 0's and 1's to represent them because no one, myself included, is going to recognize what's what. It's just too much math.
41:16
It's not interesting. And even decimal numbers-- that was 4 billion or some-- I don't remember which number is which.
41:22
So we represent things a little more compactly. And this, too, admittedly, still looks cryptic, but this is a Unicode code point that uses another system, mathematically,
41:30
called base-16 or hexadecimal. More on that, another time. But it's just a way of representing numbers even more succinctly,
41:38
writing less on the screen, because you're using not just 0 through 9, as in decimal. But you're using A through F, as well, so a few letters
41:46
of the English alphabet come into play. But, for now, that's just a little easier to remember, too, for people who care, that that is the number that
41:53
represents "face with tears of joy." But what if we want a customized emoji? And this, increasingly, is the case.
41:59
Here, for instance, are the five skin tones that phones, and laptops, and desktops, nowadays, support. It's based on something called the "Fitzpatrick scale," which essentially
42:07
categorizes human skin tone into six or, in this case, five different categories, from lighter to darker. But this suggests that, wow, if we want to represent people
42:17
with five different skin tones, like this, that could significantly increase how many unique patterns of 0's and 1's we
42:25
need for every possible face. But if we think about it from an engineering perspective, we can actually just think of skin tone as modifying some default
42:33
color, for better or for worse. And yellow is the de facto default, Simpson style. But to modify it to look more genuinely human-like, from lighter to darker,
42:41
well, maybe we just use the same pattern of bits to represent a human thumb, for instance, thumbs up or thumbs down.
42:47
And we just, then, modify that character to be displayed with a different skin tone. So, for instance, here, then, is the "thumbs up"
42:53
that you might use on various platforms. And let me just stipulate that this is the Unicode code point.
42:59
That is the number that Macs, PCs, and phones use underneath the hood to represent the default yellow "thumbs up."
43:05
But if you want to give it a medium skin tone, you still use that same number, that same pattern of 0's and 1's,
43:12
or switches, underneath the hood. But you use a few more switches that the computer or phone
43:17
will interpret as, "Oh, you don't want to see the default in yellow because of this second number that's in the computer's memory somewhere.
43:23
You want me to adjust it to be the medium skin tone or any of the other values, instead."
43:29
So that's the engineering solution to this problem of just trying to represent different ranges of emoji here.
43:35
Well, what about something like this? There's a lot more combinatorics, nowadays, on your keyboard for relationships, for instance.
43:40
So here is a "couple with heart" here. So the couple, here, of course, is represented with, apparently,
43:46
this number here. But that's it. But if you want to be more specific-- like man and woman, or man-man, woman-woman-- it's the same idea,
43:53
but we just need to express ourselves a little-- with a little more information. So, for instance, the way the Unicode folks came up with,
44:00
years ago, to represent, for instance, a woman with a heart and a man, from left to right, would be using these values.
44:06
So things just escalated quickly, but only in the sense that we're using more bits, more 0's and 1's, to represent,
44:12
more expressively, this particular combination. So this happens to be the number in Unicode
44:18
that represents the woman at left. This is the number that represents the man at right. And this is the pair of numbers that represents
44:25
the heart in the middle, sometimes red, sometimes pink, displayed here as pink. But if we want to change the combination, for instance, to be,
44:32
say, woman-- if we want to change the combination to be woman-woman, notice that, now, the left and the rightmost numbers match.
44:39
Or if we flip it back to man-man, it's just using different numbers on the tail end again. And meanwhile, if I rewind, there's these two identical values here.
44:48
These are called zero-width joiners or ZWNJ characters. It just is a special number that humans reserve to say,
44:55
glue the emoji at the left to the emoji on the right and so forth. So it connects ideas in this way.
45:02
So there's actually a lot of emojis, nowadays, that are a combination of different things. "Heart on fire" is one that's, technically,
45:09
the combination of a heart emoji, the fire emoji, joined together, numerically, in this way.
45:16
So computer scientists who come up with these things are just reducing things to representations.
45:21
All we have at our disposal are 0's and 1's. So we all just need to agree, ultimately-- whether we're Google, Microsoft, or the like-- how we're going to standardize
45:28
these kinds of things as information. Questions, then, on how characters are represented in a computer,
45:36
be it English or any other language? Yeah. AUDIENCE: How is the plus a number? DAVID J. MALAN: How is the what?
45:41
AUDIENCE: The plus, the U+. DAVID J. MALAN: Oh, the U+ is just a convention, really. So U+ represents a special Unicode character,
45:49
which is a U with a plus in the middle. And this is just the convention for saying, hey, everyone, here comes a number that represents a Unicode code point.
45:58
The U and the 1 have no-- sorry. The U and the plus have no mathematical significance. It's just a visual clue to folks.
46:05
Other questions on representing text in this way? All right.
46:10
So what about colors? We've already started looking at pictures. Well, how are those pictures, be it emojis or anything else, represented?
46:17
One of the most common ways is just with RGB-- red, green, and blue. It turns out that if we just keep track of how much red should
46:24
be on the screen, and how much green, and how much blue, combined together, that gives us every color of the rainbow,
46:29
from white to black and everything in between. So how do we represent an amount of red, and green, and blue?
46:35
Well, frankly, just with three different numbers. And this is how computers typically represent colors. Every one of the dots on your computer screen or your phone screen

## [Color](https://youtu.be/3LPJfIKxwWc?t=2803)

46:43
is called a pixel. And every single dot underneath the hood has three numbers associated with it,
46:50
so three numbers, three numbers, three numbers for every little dot. And those three numbers, together, say how much red, green, and blue
46:56
should the device display at that location. So, for instance, if you had a dot on your screen
47:02
that said, "use this much red, this much green this much blue," because each
47:07
of these numbers, I'll tell you, are one byte or eight bits, which means the total possible values is 0 to 255--
47:15
let me just ballpark that the 72, it feels like a medium amount of red because it's in between 0 and 255.
47:21
73 is a medium amount of green, and 33 of blue is just a little bit. So if you combine a medium amount of red, green, and a little bit of blue,
47:29
anyone want to guess what color of the rainbow this is? AUDIENCE: Brown. DAVID J. MALAN: Sorry? AUDIENCE: Brown.
47:35
DAVID J. MALAN: Brown? So, close. It's a little more yellow than it is brown. But if we combine them, it looks a little something like this.
47:41
This is just CS trivia, not something that even I would be able to eyeball, unless I came up with that particular example.
47:46
But wait a minute. We've seen these numbers before. 72, 73, 33 represented what-- AUDIENCE: Hi!
47:52
DAVID J. MALAN: --a few minutes ago? So it meant "Hi!" but here I am, claiming, no, no, no, no, that means yellow. How do you reconcile this?
47:58
Well, at the end of the day, this is all we have, 0's and 1's, whether you think of them as numbers,
48:04
or letters, or even colors now. But it depends on the context. So if you've received a text message or an email,

## [Representation](https://youtu.be/3LPJfIKxwWc?t=2891)

48:11
odds are the pattern of 0's and 1's that the computer is showing you are going to be interpreted as text because that's
48:17
the whole point of a text message or an email. If, though, you opened up MacOS's or iOS's or Windows's or Android's
48:23
calculator app, the same pattern of 0's and 1's might be interpreted as numbers for some addition, or subtraction, or whatever.
48:30
If you open the same pattern of 0's and 1's in Photoshop, like a graphics program, they're going to be interpreted, in that context,
48:37
as colors. So context matters. And, indeed, as soon as next week, when you start writing code in that language called C,
48:43
the onus will be on you, the programmer, to tell the computer, interpret the following sequence of bits as a number, or a letter, or something else.
48:52
And you won't have to even worry about what the 0's and 1's are, but you need to give the computer a hint as to what type of file
48:58
or piece of data you're representing. So that gives us bits. And you can actually see these dots, these pixels on the screen.
49:05
Let me zoom in, zoom in. And here we have it, just with this emoji, which, at the end of the day, is a picture that someone at Apple, in this case, drew.
49:13
And you can see-- if you really zoom in, or take your phone or TV and really put it close to your face, you'll see all of these dots,
49:19
depending on the hardware. And each of these dots, these squares, is storing 24 bits or three bytes, 24 bits, 24 bits, 24 bits.
49:28
And that's whey, dot, dot, dot, if you've got a photograph, for instance, that's three megabytes, which
49:35
is 3 million bytes, well, odds are there's 1 million pixels therein
49:42
because you're using three bytes per pixel to represent each of those colors. That's a bit of an oversimplification, but that's
49:48
why images and photos are getting bigger and bigger nowadays. Because we're throwing even more pixels into the file.
49:56
Music-- [MUSIC PLAYING] --how could you represent music, digitally, using just 0's and 1's, or numbers, really?
50:03
Any instinct, whether a musician or not? Yeah. AUDIENCE: The notes could be represented by a number.
50:11
DAVID J. MALAN: Yeah, so we can just represent notes by a number. So A is some number, and B. And maybe sharp or flat is some other number.
50:17
But note might not be quite enough for some-- yeah? AUDIENCE: [INAUDIBLE].
50:22
DAVID J. MALAN: Ah, OK. So one note-- one number to represent the note, itself, the sound or the pitch; one other number to represent the duration.
50:30
In the context of piano, how long is the human holding the key down? And maybe I can think of a third, the loudness.
50:37
How hard has the person played that note? So, minimally, with three numbers, you could imagine representing music, as well.
50:43
And, indeed, that's very well might be what computers are doing when you listen to sound. What about video?
50:48
How could you represent videos, as well? Yeah? AUDIENCE: Through many images. DAVID J. MALAN: Yeah, many images.
50:54
So if you've ever produced a film or looked at some of the fine print, 30 frames per second, FPS, or 29 frames per second
51:02
is just how many pictures are flying across the screen. But that's really all a video file is on a computer, lots of pictures moving so quickly in front of us that you and I, our brains,
51:10
interpolate that as being actual motion. And, in fact, from yesteryear, motion pictures,
51:15
it's like pictures that are giving the illusion of motion, even though there's only 30 or so of them flying across the screen.
51:21
So we have a way, now, to represent information, both as input and output, whether it's numbers, letters, images, anything else.
51:29
Let's now focus on what's inside of that black box, so to speak, wherein we have algorithms, step-by-step instructions

## [Algorithms](https://youtu.be/3LPJfIKxwWc?t=3096)

51:36
for solving some problem. Now, what do I mean by "algorithms" or "step-by-step instructions"?
51:41
Well, maybe, if we were to turn this into code-- and that's how we'll connect the dots, ultimately, today.
51:47
Code is just the implementation, in computers, of algorithms. An algorithm can be something we do in the physical world.
51:53
Code is how we implement that exact same idea, in the context of a computer, instead. And here, for instance, is a very common application inside of a computer,
52:02
for your context. This is the iOS version of the icon. And, typically, if you click on that icon, you'll see something like all of your contacts here,
52:09
typically, alphabetical, by first name or last name. And your phone or your computer lets you often search for someone's name
52:17
at the very top. And it will autocomplete, and it'll be pretty darn fast. But it'll be pretty darn fast because the programmers who
52:23
implemented that application are looking for someone quickly for you. Now, I can do this old school style, whereby we have one of these things
52:33
from yesteryear, an actual phone book. So, in a physical phone book like this, you might have 1,000 pages.
52:39
And on every page are a bunch of names and a bunch of numbers. And as I flip through this, I could look for someone specific.
52:45
So suppose I want to call John Harvard, who's-- the first name, of course, starts with a J. Well, I could just turn, page by page,
52:52
looking for John Harvard. And if he's not there, I keep turning and turning. So this is an algorithm.
52:58
I'm stepping through the phone book, one page at a time. Is it correct, this algorithm, assuming I'm looking down?
53:04
So, yeah. I mean, it's stupidly slow because why am I wasting my time with the A's, and the B's, and the so forth?
53:10
I could probably take bigger bites out of it. But it is correct. And that's going to be one of the goals of writing code, is to, of course,
53:16
solve the problem you care about correctly. So correctness goes without saying, or else what's the point of writing the code or solving-- or implementing
53:23
the algorithm? All right. Well, let me at least speed things up. So, instead of one page at a time, so, two, four, six, eight--
53:29
no, ignore that-- 10, 12, 14, 16, and so forth. It's a little hard to do, physically, but it sounded faster.
53:35
It was twice as fast, theoretically, but is it correct? AUDIENCE: No. DAVID J. MALAN: So, no. Why?
53:41
Yeah? AUDIENCE: Yeah, you might [INAUDIBLE]. DAVID J. MALAN: Yeah, I might miss John Harvard because, just by accident,
53:46
he might get sandwiched between two pages. But do I have to throw the algorithm out altogether?
53:52
Probably not. Once I reach the K section, which is past the J section, I could double back at least one page, at least, [PATS TELEPHONE BOOK]
53:58
and just make sure I didn't blow past him completely. So that is twice as fast, because I'm going two pages
54:04
at a time, plus one extra step. So it's still an improvement. So the first algorithm, worst case, if it's not John, but someone whose name starts with Z,
54:10
that might take me a full 1,000 steps. The second algorithm is just 500 steps because I'm
54:16
going two pages at a time plus one, in case I have to double back, but that's in the worst case. But most of us in the-- in yesteryear, and what Apple, and Google, and others
54:26
are actually doing is, in software or here, physically, we're typically going, roughly, to the middle.
54:31
Especially if there's no cheat sheet on the side, like A through Z, I'm just going to go to, roughly, the middle. And, oh, here I am, not surprisingly, in the M section.
54:38
But what do I now know. If this is the M section, where is John Harvard? So, clearly, to the left, alphabetically.
54:46
And so here is where we can take a much bigger bite out of the problem. We can really divide and conquer this problem
54:52
by tearing [TEARS BOOK] the problem in half, throwing half of it away, 500 pages away, leaving me with a smaller problem,
55:01
half as big, that I can really just now repeat. So I go, roughly, here, and now I'm in the E section.
55:07
So I went a little too far back. But what do I now know? If this is the E pages, where's John? AUDIENCE: To the right.
55:12
DAVID J. MALAN: So now he's to the right. So I can-- again, hopefully, he's not on that page. I can tear the problem in half again, throw that 250 pages away.
55:20
And now I've gone from 1,000 to 500 to 250 pages. Now I'm moving because the first algorithm was one page at a time,
55:26
second was two. This is hundreds of pages at a time. And if I go, roughly, again, to the middle; roughly,
55:31
to the middle; roughly, to the middle, hopefully, I'll find John Harvard on one final page. Can only do this once, but one final page.
55:39
So that invites the question, I would think, if the phone book does have 1,000 or so pages,
55:44
how many times can I divide the problem in half to get down to one last page?
55:50
So it's, roughly, 10. And the quick math is 1,000 goes to 500 to 250 to 125 to 67 something.
55:56
So we have to deal with rounding issues, eventually. But assuming we work out the math, it's, roughly, 10 page tears.
56:01
And that's crazy faster than 1,000 pages and still faster than 500 pages.
56:07
So it's fundamentally better. And, indeed, if I finally get to that final page, in the software world,
56:13
you'd see something like this, John Harvard and his number, which you're welcome to call or text. But that's how we now have our answer, much like the single page there.
56:22
But let's consider just how efficient that actually is. So here's a very rough, broad-- with broad strokes, a chart.
56:30
So here's an xy plot. So here, on the horizontal, is going to be the size of the problem. And, by that, I mean, how many pages are we trying to go through?
56:38
This would be zero pages. This would be a lot of pages. How much time does it take to solve the problem?
56:43
How long does it take to find John Harvard or anyone else? This means no time. This means a lot of time.
56:48
So what's the relationship among these algorithms? Well, the first one is actually just a straight line. If there's n pages in the phone book, well, I
56:57
claim that it's a one-to-one relationship. Because if Verizon or the phone company adds another page next year,
57:04
that just means I might have one more step next year, as well, to find John Harvard or anyone else.
57:09
But the second algorithm, it's also a straight line, but it's lower, even though it might not look obvious.
57:15
And what do I mean by that? Well, let me just draw some temporary lines. If this is how many pages are in the phone book-- dot,
57:20
dot, dot-- notice that it takes this much time, on the red line, to solve the problem. But if I, instead, use the second algorithm,
57:28
it takes me half as much time. So, even though they're both straight lines, one is strictly lower than the other, which means it's faster.
57:34
It's better. But the third algorithm is a fundamentally different shape, and it looks a little something like this.
57:40
And it looks like it's going to flatten, flatten, flatten out, but it never does. It just rises ever so slowly.
57:46
And what this means is that if maybe Cambridge and Allston, here in Massachusetts, merge next year, so we go from 1,000 page phone book
57:53
to a 2,000 page phone book, that means, if we're here this year,
57:58
we're over here next year. It's not all that much higher. But it would be much higher if we were using the first two algorithms.
58:04
Why? It'd be an extra 1,000 steps to find someone in that combined phone book or maybe another 500 steps.
58:09
But, to be clear, if we're using my third and final algorithm, how many more steps will it take me next year,
58:15
when Cambridge and Allston merge into one 2,000-page phone book?
58:20
Just one more step, no big deal. It's one more page tear. And this is what we mean, ultimately, about not just writing
58:26
code or implementing algorithms that are correct, but, now, that are well-designed or efficient, specifically.
58:33
And this is what makes someone a better programmer, perhaps, than someone else, or a better problem-solver than someone else,
58:38
is acquiring, over time, these skills. So that, sure, you could solve the problem quickly and dirtily,
58:43
so to speak, but if you're going to have a lot of data eventually, be it in your phone book or maybe your Google website index,
58:49
if you're searching the web, you're going to want to try to think about how to design algorithms that look like this.
58:54
Mathematically, this is called a logarithm. And it's log base 2 because I'm halving, halving, halving, again and again. But, for now, just know that it's a fundamentally faster and different
59:03
shape. So, among our goals in CS50, ultimately, is not just to write and solve problems correctly, but, ultimately, ever more efficiently,
59:12
as well. Any questions, then, on these ideas of efficiency and design?
59:20
Any questions here? Yeah, in back? AUDIENCE: [INAUDIBLE]. DAVID J. MALAN: A good question. Just to repeat it, can a graph like this capture the accuracy of the algorithm?
59:27
Short answer, no. For instance, if I drew a straight line that is super low on this graph, which would imply that the algorithm takes
59:35
the same amount of time, no matter how many pages there are, my algorithm might actually be to just pull a random page from the phone
59:41
book, one step, and say, here it is. But that's not necessarily going to be accurate, unless I get really, really lucky.
59:47
So the graph really only speaks to efficiency and the design of the algorithm, not the correctness of it.
59:52
To analyze the correctness, you need to use another mechanism altogether, namely, logic.
59:58
Other questions now, on efficiency, in this way? No? All right.
1:00:03
So, with that in mind, let's begin to translate this to some actual code. And, in fact, before we look at, today, one actual programming language,

## [Pseudocode](https://youtu.be/3LPJfIKxwWc?t=3611)

1:00:11
albeit a graphical one, let's consider something called pseudocode. So pseudocode has no formal meaning. Generally, you write it in English or whatever your own human language is.
1:00:19
But you write your thoughts down tersely, succinct, but precisely.
1:00:25
You try to really convey your thoughts, not with a wave of the hand, metaphorically, but step by step, precisely.
1:00:31
So what do I mean by this? Here might be some representative pseudocode via which I describe that third and final algorithm in a way
1:00:39
that I could hand it to you and you could do the same at home. Or I could hand it to someone at Google, and they could implement it in Android.
1:00:45
Or I could hand it to someone at Apple, and they could implement it in iOS. So, step one, I claimed, was "Pick up phone book."
1:00:51
Step two was "Open to the middle of the phone book." Step three, "Look at the page," as I did.
1:00:57
And now things get a little more interesting. Step four, "If person is on page," I have to make a decision.
1:01:03
Presumably, what should I do if John Harvard is on the page I'm looking at? So stop and probably make the call, or email, or whatever the goal might be.
1:01:12
And so I'm going to actually indent this, visually, by a few spaces, just to make clear that you should only do line five if the answer to line four
1:01:19
is yes. Otherwise, you don't bother. The next thing I'm going to do, line six, is consider another possibility.
1:01:26
"If the person I'm looking for is earlier in the book," what do I want to do? Well, I could write--
1:01:31
I could describe this in a bunch of ways. I'm going to do this tersely, as follows. "Open to the middle of the left half of the book,
1:01:38
so it's open to the middle of the left half of the book. And then, what am I going to do? Well, I've just divided the problem into something smaller.
1:01:46
But it's fundamentally the same problem. It's just a fewer number of pages. So I'm just going to go back to line three and do it again
1:01:54
because the problem is just getting smaller and smaller, presumably. Else, if the person I'm looking for is later in the book,
1:01:59
open to the middle of the right half of the book, and, also, "Go back to line 3."
1:02:04
But there's a fourth possibility and its failure to realize, sometimes, that there's other possible outcomes that
1:02:11
make computers crash, or spinning beach balls, or the like, if a programmer doesn't anticipate some situation.
1:02:17
What's the fourth possible situation, when looking for John Harvard? AUDIENCE: If they're not in the book. DAVID J. MALAN: If they're not in the book, at all.
1:02:24
And, indeed, I might get to the very last page and John Harvard's not even on that one. I'd better handle that and say, else, as a catchall, just quit altogether.
1:02:33
And, truly, often, in your Macs, PCs, phones, when they freeze, or, again, spinning beach ball, or the like, and just weird things happen, that's just
1:02:39
because some human made a dumb mistake. And they didn't realize that you could somehow get your phone or your laptop into a configuration that they didn't anticipate.
1:02:47
So we're going to try to handle that here. Now this is just one way of writing pseudocode. There's no one way to do this.
1:02:52
All of us in this room could come up with slightly different pseudocode. But I think you'll find characteristic are certain building
1:02:59
blocks in all of our answers. Here, in yellow, are what, as of today, we're
1:03:04
going to start calling "functions," technically speaking. These are like actions or verbs that literally, in this case, tell me
1:03:10
what to do. Next, we're going to have these things, conditionals, forks in the road, so to speak, that take me down this path or another,
1:03:20
metaphorically. So I do this thing or something else. But how do I decide if I want to go this way, or this way, or this way, or this way?
1:03:26
I need to ask a question. And in programming, we'll typically use what are called Boolean expressions, named after a mathematician, Boole.
1:03:33
And a Boolean expression is essentially just a question with a yes/no answer, a true or false answer, a 1 or 0 answer.
1:03:42
It doesn't matter how you think about it, but it's got two possible answers. And so you can think of these as being expressions with question marks,
1:03:49
even though I didn't draw such. Person on page, person earlier in book, person later in book,
1:03:54
those are Boolean expressions. And they tell me whether I should go down one fork in the road or another.
1:04:00
And, lastly, there's this, "Go back to line 3," in two different places. That represents what we call a "loop," some kind of cycle that's
1:04:06
doing something again and again. Now these are just a few building blocks here-- functions, conditionals, Boolean expressions, loops.
1:04:12
But you'll find that they're characteristic of so many different languages, one of which we'll look at today, another of which
1:04:18
we'll look at next week. And those include, indeed, C, and Python, and other languages still. And so this is why we focus on these basics
1:04:25
and fundamentals in these early days because we're going to see them again and again. So even if you feel like that fire hose is hitting you sometime,
1:04:31
we'll give you, today, ultimately, more visuals by which you can hang onto, so as to actually write code, ultimately,
1:04:38
in different languages and solve all sorts of problems. Now, we'd be remiss in not bringing up what's behind characters like Spot,
1:04:46
and ChatGPT, and other software, artificial intelligence. And it turns out, to get to the point of AI,
1:04:51
we're actually going to need more building blocks than just functions, and loops, and conditionals. It's not going to be quite that simple.
1:04:57
But this has been a lot, so far. Let's go ahead, here, and take a five-minute break. And when we resume, we'll take a look not only at AI,
1:05:03
but also a specific language called Scratch. So no cake, just yet, but we'll come back in five.
1:05:09
Before we dive back in, I just wanted to call out a special guest that we have here today, beyond Spot, someone

## [Thank you](https://youtu.be/3LPJfIKxwWc?t=3916)

1:05:16
who's come from even farther away. And, in fact, if any of you have taken CS50x, the OpenCourseWare version
1:05:22
of the class, or dabbled in it over the past few years in some of CS50's online social communities, you might have had your questions answered
1:05:29
by a certain human from New Zealand. And she's come all this way, today, to spend this lecture with us.
1:05:35
This is CS50's own Brenda Anderson. If you might come up for acknowledgment from all of us here.
1:05:41
[APPLAUSE]
1:05:47
It's not much, but just a little token of our thanks. Brenda has helped, truly, thousands of students online
1:05:53
for the past many years. And, in fact, her own daughter has been the artist behind the duck that's about to loom large in CS50 this year and beyond.
1:06:03
So, thank you to Brenda. [APPLAUSE]
1:06:11
All right. So it's hard to escape a discussion of artificial intelligence, nowadays,

## [Artificial Intelligence](https://youtu.be/3LPJfIKxwWc?t=3976)

1:06:16
but we thought we'd use this as an opportunity to connect some of these dots. Because, indeed, over the course of the semester,
1:06:22
we'll be-- not only be talking about artificial intelligence or AI, but really using it all the more constructively
1:06:28
to help you solve problems, help you get unblocked when you hit a wall, cognitively or syntactically, when writing code.
1:06:35
And, indeed, it's no accident that we have this duck here, looming large, which is really the embodiment of the sort of AI
1:06:42
that you'll experience within CS50, itself, this year. So let's talk about the so-called chatbots that
1:06:48
inspired some of those headlines with which we began class, that weren't quite on the nose. So the class will still be taught by us humans,
1:06:54
but helped by this CS50 duck, a chatbot of sorts. Now what do I mean by this?
1:07:00
Well, it turns out that, when it comes to implementing something like an artificial intelligence, we don't quite
1:07:06
have all of the building blocks yet, certainly after just today's week zero, to implement something like that.
1:07:12
But I think we can skate in that direction, intellectually. So, for instance, if we were to take a stab at implementing our own chatbot--
1:07:19
some interactive text-based program that talks to us, and answers questions, and the like-- we could
1:07:24
try borrowing some of today's ideas already, those functions, conditionals, loops, and more.
1:07:30
And I could write something like this. If I am writing code or pseudocode for a chatbot, I could program the chatbot to do something like this.
1:07:37
If the student says, hello, to the chatbot, then the chatbot should say, hello, back. Else, if the student says, goodbye, well, the chatbot
1:07:44
should say, goodbye, back. Else, if the student asks how you are, the chat bot should say that it's well.
1:07:51
But things get a little harder when you start asking more interesting questions, like, else,
1:07:57
if the student asks why 111 in binary is 7 in decimal. Now, you could imagine that we just have a conditional,
1:08:03
with this Boolean expression, that programs the chatbot to just give you the answer and explain, in an English sentence, why that, in fact, is.
1:08:12
But what if you, the student, asks why 110 is 6 in decimal or why 010 is 2?
1:08:20
I mean, you can just imagine the explosion in the amount of code that we would have to write to just anticipate every darn question that you
1:08:28
might ask about today and every other class, not to mention all of the knowledge in the universe. So, surely, there are other ways to implement algorithms
1:08:36
that allow something like a chatbot or AI, more generally, to be fed input, still, like all of the internet, all
1:08:43
of the worldwide web, all of the pages and textual content therein, but to let it just figure out how to answer our questions based
1:08:51
on those kinds of inputs, assuming the inputs, themselves, are accurate. So "large language models" is a term you might
1:08:56
have heard bandied about over the past several months, or LLMs. And a large language model really is an implementation, in software,
1:09:04
of code that actually takes, as input, lots and lots of language-- like the text of lots and lots of web pages, dictionaries, encyclopedias,
1:09:13
Wikipedias, and the like-- and infers, from the patterns of English words or any human language,
1:09:19
what a typical human might actually say when asked a question. And some of these questions are easy, right?
1:09:24
Probably, on the internet, alone, not to mention everyday life, if someone extends their hand and says, "Hi. How are you," odds are, with 90% probability, you're going to say,
1:09:33
"Good. Thanks. How are you?" So I bet we could write software that just infers what it should say, probabilistically, statistically, based
1:09:41
on those kinds of patterns online. And that's, indeed, where the world is starting to go, when it comes to the most sophisticated
1:09:47
of algorithms, where you and I, the humans, we don't try to anticipate every possible input. Rather, we give it a more general purpose
1:09:54
input, like all human knowledge, and ideally just let it figure things out. Now, we're not quite there, yet. And odds are you've heard of hallucinations or just mistakes
1:10:02
that these large language models make. But their inputs are imperfect. And sometimes there's a bit of randomness sprinkled
1:10:07
in because you don't want the thing to always say the exact same thing. Even you and I might say, "Eh, I'm not that great today" 10% of the time.
1:10:14
So you need to perturb the output in some way. But within CS50 and within this world of large language models,
1:10:20
we do have these tools like ChatGPT, and Bing, chat, and others. And we'll stipulate that, for CS50's purposes,
1:10:26
the direction we're going this year is that this is what's in the syllabus, dot, dot, dot; that it will not be allowed, it will be considered
1:10:32
not reasonable to use AI-based software, other than CS50's own. So the goal here is not to simply take away
1:10:39
tools that are clearly inevitable, in my view, and clearly helpful and productivity savers.
1:10:44
But we'd like there to be some guardrails, intellectually, on just how helpful these chatbots are. Because as you've probably seen, if you ask it a question,
1:10:52
these chatbots are already pretty good at not just helping you finish your current thought, but it'll hand you your second and your third thought and do the assignment for you.
1:10:59
But I think, through prompting, so to speak, we'll be able to coax some of our own tools, being computer scientists, ourself, in a direction
1:11:07
that you actually find to be the right balance, akin to having a good tutor by your side 24/7, who doesn't just hand you answers,
1:11:14
but, indeed, tries to lead you to the same. So you actually get something out of the experience, and, ideally, three-plus months from now,
1:11:20
those training wheels can come off, too. And you're able to still stand on your own. So it will be reasonable to use CS50's own AI-based software which
1:11:28
will actually take the form of a CS50 duck, which is actually available now-- and we'll use it throughout the term-- at CS50.ai, a web-based application
1:11:37
that's quite similar to ChatGPT, but that has the personality of a CS50 teaching fellow or TF, or teaching assistant,
1:11:44
TA, that also happens to think of itself as a duck. And for reasons we'll get to in a couple of weeks time,
1:11:49
but rubber ducks, in particular, are a thing in programming. But more on that, before long, as you can even see from the one
1:11:56
there on my desk. With that said, too, well, I'm going to call out CS50's own Brenda Anderson, whose daughter, Sophie, kindly not only created
1:12:05
the first incarnation, digitally, of this duck, but also, most recently, once it actually did more than quack a random number
1:12:11
of times in response to questions, has now been virtually brought to life, too. So, all that and more, over the coming weeks, but you'll find, ultimately,
1:12:18
that the goal is to really bring to life the availability of an AI-based tutor that you have access to, a friend in your--
1:12:26
next to you, that will help guide you through a lot of the course's challenges along the way.
1:12:31
And we actually rolled it out this past summer, already, with some of your predecessors, through the Harvard Summer School. One student wrote, at summer's end, that this duck
1:12:38
"felt like having a personal tutor-- I love how AI bots will answer questions without ego and without judgment
1:12:44
generally entertaining even the stupidest of questions without treating them like they're stupid.
1:12:49
It has, as one could expect, an inhuman level of patience." So there's actually something really there because as many teachers
1:12:56
as there are in CS50-- myself, the course's preceptors, teaching fellows, teaching assistants, and course assistants-- there's only so many of us.
1:13:03
And we're only awake so many hours of the day. And I think you'll find, too, that we're on the cusp of something
1:13:08
pretty remarkable, in the coming years, where it's going to get a lot more enabling, now, to learn material
1:13:14
not only within the confines of a class, but on your own, ultimately, as well. And as one other student put it, at summer's end, with respect to the duck,
1:13:22
"Love love loved the duck. We're friends now." So that, too, awaits. But, first, we're going to need to start with the basics.
1:13:28
And we started today by talking about binary. And darn it, here it is again. So we can't actually get to the point of using, or solving, or implementing AI
1:13:37
until we understand this. And odds are most of you won't know, at a glance, what this piece of software
1:13:42
does. But these are the 0's and 1's that represent, perhaps, the first program that any programmer writes, which is now a clue to some
1:13:50
of you who have dabbled in code before. What does this pattern of 0's and 1's tell a typical computer to do?
1:13:56
Might someone guess? AUDIENCE: "Hello, world." DAVID J. MALAN: It's going to have it say, "hello, world," which is one of the very first programmer-- programs
1:14:02
that most any programmer writes. Should you be able to recognize these 0's and 1's? Do I recognize these 0's and 1's?
1:14:08
No, not at all. I just happen to know that they are the same. And that was a leading question. But they are representing data and instructions, ultimately,
1:14:17
data like H-E-L-L-O, comma, W-O-R-L-D and an instruction like,
1:14:22
"Print that data to the screen." As for what these patterns of 0's and 1's are, this is not something that a computer scientist or programmer worries about.
1:14:30
We just stipulate that, OK, someone, somewhere knows how to do this. And it's probably someone like Intel, who makes
1:14:36
the hardware inside of the computers. But you and I, starting now, already, in week zero,
1:14:41
can start to view binary more abstractly. We don't care about the 0's and 1's.
1:14:46
We only care that you can use 0's and 1's to represent more useful quantities, like numbers,
1:14:52
and letters, colors, and more. So this, next week, is going to be the code we actually start writing at a keyboard.
1:14:58
And this is that language called C. It's the same language I, myself, learned years ago, when taking CS50, when all we learned at the time was C.
1:15:05
But this, too, has some crypticness to it. And if you've never programmed before, you can probably wrap your mind around,
1:15:11
OK, I'm guessing the "printf" prints out the "hello, world." But what's with the semicolon, the quotes, the backslash,
1:15:16
and the curly braces, the #include, and all of this stupid syntax? A lot of this, in the beginning of any class, is really a distraction.
1:15:23
It is not intellectually interesting. But it's the stupid kind of stuff that's going to trip you up quite often.
1:15:29
And so, today, what we'll do is focus not on syntax, characters on the keyboard, but ideas
1:15:35
because what really matters in this program is that "printf" is a function here for our purposes.
1:15:40
And that function is to display information on the screen. Everything else, as we'll soon see, has value
1:15:46
and will be understood by you, before long, but for now, it's a distraction. Let's focus on those building blocks.

## [cs50.dev](https://youtu.be/3LPJfIKxwWc?t=4552)

1:15:52
When it comes time to write code, though, for the curious, especially if you've programmed before, we'll use a very popular free and open-source tool
1:15:58
called Visual Studio Code, or VS Code. We'll use a cloud-based version of it that we pre-install everything
1:16:06
you need in the cloud for you so you don't have to deal with headaches like getting your Mac or PC to work. You'll use instead this URL, cs50.dev, but more
1:16:13
on that in next week, week one. For now, we'll use another cloud-based editor called Scratch.

## [Scratch](https://youtu.be/3LPJfIKxwWc?t=4579)

1:16:19
And odds are some number of you use this probably as early as like middle school or the like. And that was fine to create your own animations, games,
1:16:27
interactive art, or the like. But we'll use it today for just a bit. And we'll use it in the course's first homework,
1:16:32
AKA problem set 0, to explore now some of these same ideas. And among the goals today for the remainder of today
1:16:39
is not to focus so much on Scratch and the particulars because this is not a language that you're going to use often but to give you very visual representations of ideas
1:16:50
so that when things do escalate next week to C, to the more cryptic, it's the same ideas just typed out instead of dragged and dropped.
1:16:57
So by that, I mean this. I'm going to go ahead and share in just a moment the user interface of Scratch.
1:17:03
But what's nice about Scratch is that this is how we're going to implement that same program today.
1:17:08
These are two blocks or puzzle pieces on the screen, and they've been interconnected to tell the computer to say "hello, world"
1:17:15
on the screen. The user interface that we're about to use will look generally something like this. It's a web-based editor that you can also
1:17:22
download it locally to use offline. And you'll see that at the left here are a whole bunch of puzzle pieces
1:17:28
or blocks. They're categorized by color, and the blue ones tend to relate to motion, for instance.
1:17:33
The purple ones represent looks. The pink one represents sounds. The yellow one represents events.
1:17:40
More on that soon. The orange ones represent control, and then there's operators, variables, my blocks, and even some extensions
1:17:46
we can install as well. So it just categorizes things visually and colorfully so that you
1:17:51
can find what you're looking for. But we're going to use these puzzle pieces to drag and drop them onto this area here.
1:17:58
And we're going to connect them when we want them to do something. What can they do? Well, by default, Scratch comes with this cat here, otherwise known
1:18:06
as a sprite, which is a character in a game or in a graphics context. And this cat lives in this two-dimensional world in which
1:18:12
the cat can go up, down, left, right. And you can actually change the cat's costume to be a dog, a bird, or anything else.
1:18:18
It really is more of an idea than it is a specific animal in this case. But the world that Scratch lives in looks a little something like this.
1:18:26
It's like a Cartesian plane with x-coordinates and y-coordinates. And the numbers don't so much matter fundamentally,
1:18:32
except that when you want the cat or any character to go up, down, left, or right by some amount, it's
1:18:37
useful to know, for instance, that 0, 0 is the middle, 0 comma 0 for x comma y.
1:18:42
All the way up is a y value of 180. All the way down is -180. All the way to the left is -240.
1:18:50
All the way to the right is 240. And generally, you're not going to have to worry about numbers. You're going to use these relatively-- go right, go left, go up, or down.
1:18:58
But that's just the world that Scratch itself lives in here. So let's go about using Scratch here.

## [Hello, World](https://youtu.be/3LPJfIKxwWc?t=4743)

1:19:03
I'm going to change over to my cloud-based editor here, where I've gone to scratch.mit.edu.
1:19:10
And I've clicked Create in order to create a project. And that gives me this blank canvas here. And I'm going to do these somewhat quickly because I kind of know
1:19:17
what I'm looking for. But part of the process with problem set zero is going to be clicking, and dragging, and sort of scrolling around
1:19:23
to see what building blocks exist. But I know under Events there's this puzzle piece here
1:19:29
when green flag clicked. Why is that germane? Well, if I zoom out, and go back to Scratch's world at the right here,
1:19:35
notice that above Scratch's world there's a green flag, which is going to mean go, and a red stop sign, which,
1:19:40
of course, is going to mean stop. So if I drag this puzzle piece anywhere into the middle,
1:19:46
it's just going to plop where I put it. But what that means semantically is when someone clicks that green flag,
1:19:53
I want Scratch the cat to do this other thing. Well, what do I want it to do? Well, let me go under Looks.
1:19:59
And looks here in purple have some puzzle pieces like this. Well, I can say hello for some number of seconds,
1:20:06
or I can just go ahead and say hello. So let's do that. I'm going to drag this say block.
1:20:11
And notice that as soon as I get close enough, it's going to magnetically want to connect. So I can let go, and they snap together automatically
1:20:17
because they're the right shape. I don't have to say hello, exclamation point. I can change it to the more canonical, hello comma world.
1:20:23
So anything in this white oval is editable that you can change as just text there. If I now zoom out, let me go ahead and click the green flag.
1:20:31
And voila-- this should be my first program in Scratch. Hello, world.
1:20:37
Without any of the distractions of syntax or weird characters on the screen, it's just done what I want it to do. All right.
1:20:42
Let me go ahead and click Stop there. And let me make it a little more connected to what we've discussed thus far.
1:20:48
So this puzzle piece here, say hello, world, represents what type of building block using the vocabulary of today?
1:20:56
So it's a function. So these purple blocks are functions, say, hello, world. And let me give you another piece of terminology.
1:21:02
These white ovals that take textual input-- in general, those are called parameters or arguments.
1:21:08
And they customize the behavior of a function. So a parameter or an argument customizes,
1:21:14
modifies the default behavior of a function, like in this case, say. Similarly, in the C code from earlier that we'll see next week,
1:21:20
the printf function took a quoted phrase like, hello, world, similarly as input.
1:21:27
But more on that in the future. So how does this connect to the mental model we presented earlier?
1:21:32
Well, here's problem-solving as I described it earlier, inputs to outputs with algorithms or code in the middle.
1:21:39
Well, what we've got here really is an input of, hello, world, the white oval. The function or algorithm that it's going into as input is the say block.
1:21:48
And what is the output of using this say block, the say function? It's the visual effect of having the cat have the little speech bubble appear
1:21:55
above its head, saying, hello, world. So everything we do, in fact, can be mapped back
1:22:00
to that very simple idea of inputs and outputs. Well, let's make it a little more interesting, though.

## [Hello, You](https://youtu.be/3LPJfIKxwWc?t=4926)

1:22:06
It's a little boring to just say "hello, world" all the time. Let me go ahead and drag this away. And if you just drag it to the left and let go, it gets automatically deleted.
1:22:15
Let me go under Sensing in light blue here. And you'll see there's a bunch of blocks, one of which
1:22:20
is an ask block, an ask function, which is going to prompt the human, me, for some input.
1:22:26
So let me go ahead and drag that over here, and it snaps together. I could change the question, but I'm OK with that question.
1:22:32
We'll use what's your name. But notice that this block, ask, is a little special. It is not just going to display like a speech bubble on the screen.
1:22:40
It's actually going to return a value, and this is another term of art today and onward. A return value is some value that can be handed back to you conceptually
1:22:48
from a function so that you can do something with it. It's as though the ask function asks someone for their name,
1:22:55
writes it down on a piece of paper, and hands you the piece of paper. You can do anything now that you want with that name.
1:23:00
And here is how you access the name in this special block called answer, which, again, will start calling a return value.
1:23:07
So if I want to say "hello" to someone specific, I'm going to do this. Let me zoom out. Let me go back to Looks, and let me go back to Say.
1:23:15
And I'm going to change the say block here to "hello, comma." Then I'm going to zoom out.
1:23:21
Well, I need two inputs, I think. So I'm going to grab another say block, and I'm going to put it below.
1:23:26
And I could just type "David," but this is going to defeat the whole point of asking me for the name.
1:23:31
And it will only work for me. So I don't want to do that. So let me go back to Sensing, and notice the shape is important here.
1:23:38
Even if it's not quite the same size, the shape matters. And I can actually drag this and change the input of this say function
1:23:45
to be whatever that return value is, that piece of paper that has the person's name on it. And it grows to fill, but now we have a program
1:23:53
that I think when I click the green flag-- watch-- is going to prompt me. What's your name? And now I have room to type down here.
1:23:59
So I'm going to type D-A-V-I-D. I'm going to hit Enter, and it should say "hello, Dave." Wait. Hmm.
1:24:06
Huh. Maybe it was-- didn't work. D-A-V-I-D. Here we go.
1:24:11
Hello, David. Hmm. It's missing the hello, but I'm quite sure we have a hello right there.
1:24:19
So what explains this bug or mistake? Yeah. AUDIENCE: [INAUDIBLE].
1:24:26
So they overlap. DAVID J. MALAN: Exactly. Put another way, my Mac, my PC, it's just so darn
1:24:33
fast that it did exactly what it was supposed to. But it said "hello, David" so fast that we didn't even see, we being the human,
1:24:40
the slowest part of the puzzle, see the actual hello. So there's a few different ways to fix this, as you know. We could have it say "hello" for some number of seconds.
1:24:48
So I could kind of do that. So let me do this. I can decouple these by just dragging and letting it go so that they're magnetically far apart.
1:24:55
Let me go ahead and drag this one, say hello for two seconds. I'm going to change the grammar here to be hello comma again.
1:25:02
I'm going to go ahead and disconnect these two. I'm going to throw away the old one that I don't want to use.
1:25:08
And I'm going to reconnect this so that now-- OK. It's going to say hello for two seconds and then my name, hopefully.
1:25:14
So let me click Stop and Start. D-A-V-I-D. Enter.
1:25:20
OK. So it's better, but it's kind of poorly implemented. Like, come on.
1:25:26
I just wanted to say hello comma David. Why is that hard? Well, maybe we can actually combine these a little differently.
1:25:31
And let me propose this. Let me actually get rid of these blocks again. And let me go ahead and just say one thing.
1:25:38
But can I somehow combine this to say hello comma David all in one breath?
1:25:43
Well, it turns out if I go under Operators, I know from having played with this before that there's this puzzle
1:25:49
piece down here called join. It's an oval. It's a little big, but, again, it will grow to fill.
1:25:54
And by default, it wants to join two words, "apple" and "banana." But those are just placeholders.
1:25:59
So let me go ahead and drag this over the default hello. Let me change "apple" to hello comma space and then banana.
1:26:08
Let me go back to Sensing. Let me grab answer and drag and drop that. So now notice that I'm kind of layering my ideas.
1:26:16
And put another way, the output of this join block is presumably going to join two things together,
1:26:22
apple and banana or hello comma David. And then the output of join is going to become the input to say.
1:26:29
So aesthetically, it just looks better. It's still correct, but it's just better. So if I type "David," and hit Enter, hello, David.
1:26:36
This is what a normal program would presumably do, not show you part of the phrase and then the rest of the phrase.
1:26:42
Like, it's just better in this way. So let's connect this now to this same puzzle piece and this methodology.
1:26:48
So here's that same puzzle piece, ask. How do we fit it into this input and output flow with algorithms?
1:26:53
Well, the input to that puzzle piece is something like, what's your name, question mark. Then the algorithm or the code implementation thereof
1:27:01
is this ask block and wait so the human has a moment to type their response in. The output of that function recall is a return value.
1:27:09
You don't see anything on the screen by default because we've not used say yet, but we get this return value.
1:27:14
And let me scooch everything over now so that we can now join those inputs together.
1:27:20
So here's this puzzle piece. Let me go ahead and propose that the inputs now to the join block are two arguments or two parameters, so to speak, hello and answer.
1:27:30
They go into that join puzzle piece, whose purpose in life is to return one joined version thereof.
1:27:36
Let me slide this all over logically now so that now that output becomes the input to the say block
1:27:42
and now is why the cat has the speech bubble saying all at once, hello comma David. So what we've done here is kind of composed the output
1:27:51
and from one function into the input of another. And you can think of this in a couple of different ways, left to right, as I did there, or kind of
1:27:58
like stacking these things on top of one another. But at the end of the day, even as programming gets more and more powerful for us, it's just inputs and outputs, inputs
1:28:07
and outputs. And thankfully, with built-in functionality from our friends at MIT who designed Scratch, I can even do something playful like this.
1:28:14
I can go to that Extensions button at the bottom. And there's a lot of fancy things I can add here, like text-to-speech.
1:28:20
So let me go ahead and choose text-to-speech. And let me go ahead here and change the say block in purple.
1:28:28
Let me get rid of the say block, and let me borrow this. Let me get the speak block like this.
1:28:33
And now let me drag and drop this oval. It's going to grow to fill. And I think it's just about to be a little more interesting.
1:28:38
Let me click Play now, and hopefully this isn't too loud. D-A-V-I-D. Enter.
1:28:44
SPEAKER: Hello, David. DAVID J. MALAN: OK. [APPLAUSE] Thank you.
1:28:50
Thank you. That's a low bar. [CHUCKLES] Let me go ahead and set the voice too. And you might now remember how we began class, where
1:28:56
we had a robotic, computerized voice. Well, we didn't use Scratch at the time, but we could change this in Scratch
1:29:03
alone to be a little different. So D-A-V-I-D. SPEAKER: Hello, David. DAVID J. MALAN: OK. Little creepy, but we can play all day long with that.
1:29:10
But the point is that these functions are just now doing something a little different. But it's just these inputs and outputs.
1:29:15
Well, let's make the cat more like a cat. Let me go ahead and throw away all of this asking question stuff. Let me go up to Sound, and let me go ahead

## [Meow](https://youtu.be/3LPJfIKxwWc?t=5363)

1:29:23
and drag the play sound meow until done. And here too it comes with meow. You can add your own sounds as well.
1:29:31
But I'm just going to use the default meow and here too. Hopefully, this won't be too loud. Let's make the cat meow by clicking Play.
1:29:37
[MEOWING] OK. It's a little piercing, but it's cute. And if I want the cat to meow twice, I could just play the game twice.
1:29:45
[MEOWING] All right. But it would be nice to just get it to meow automatically two, or three,
1:29:52
or more times. So you know what I could do? I could just drag a second one of these. Actually, you know what?
1:29:57
I could even just right-click or Control-click and duplicate them. But I'll just keep dragging and dropping. There's different ways to solve problems.
1:30:03
And now let me click Play. [MEOWING] OK. Cat does not sound particularly happy.
1:30:09
So we could go under-- how about Control? We could wait one second.
1:30:15
Now, there's no room, but it will sort of expand to give room for me. So let me try this. And now it's going to wait one second in between meows.
1:30:22
[MEOWING] OK. Let me stipulate that is correct.
1:30:28
If my goal is to get the cat to meow three times, it meowed three times. But per our discussion earlier of algorithms and the design thereof,
1:30:36
this is not the best design. [MEOWING] OK? [LAUGHTER] Thank you for playing along at home.
1:30:42
Yeah. In what sense is this arguably not well-designed?
1:30:47
Yeah. AUDIENCE: You repeated yourself. DAVID J. MALAN: I repeated myself, which actually in programming tends not to be a good thing.
1:30:53
Now, it was easy. I almost resorted to copy-paste, which saves me time upfront. But just imagine a contrived scenario.
1:30:59
Now, what if I want it to wait like two seconds in between? All right. It's not that big a deal. I change it here, and I change it here.
1:31:05
But what if the program is meant to meow 10 times? Then I have to change it here, and here, and here, and here, and here.
1:31:10
And eventually I'm going to screw up. Humans are fallible. I'm going to overlook one of them. One time, it's going to be one second.
1:31:16
Another is going to be two, and just stupid things will happen. You're setting yourself up for failure if you design things poorly.
1:31:23
And so I would propose that we use another type of building block to solve this instead. Yeah.
1:31:28
AUDIENCE: [INAUDIBLE] DAVID J. MALAN: Yeah. So we could use a loop and just write minimal code but to accomplish even more functionality.
1:31:35
So let me throw away most of these blocks. And let's go and grab this repeat block, which we haven't used yet,
1:31:40
but it's right there. And as the name suggests, this will allow me to repeat something some number of times. Let me put these two puzzle pieces inside.
1:31:48
It'll grow to fill. Let me reconnect it to the green flag. I'll change the default 10 to a 3.
1:31:53
And now-- [MEOWING]
1:31:58
It's just sort of better because if now you want it to meow more times, you change it one place. If you want it to slow down, you change it in one place.
1:32:05
There's no room for error. And that's generally a good thing. But this is silly.

## [Abstraction](https://youtu.be/3LPJfIKxwWc?t=5530)

1:32:10
Like, Scratch comes with a cat. Why didn't MIT give us a puzzle piece called "meow?" Like, why am I implementing the idea of meowing myself?
1:32:18
Like, that took me what? 1, 2, 3, 4 puzzle pieces. Why isn't there just one puzzle piece that meows for me?
1:32:24
This too we can do in code, be it in Scratch, or C, or other languages too. I'm going to go down to these pink my blocks here,
1:32:32
where I can create my own puzzle piece. And I'm going to call this literally "meow." And I'm going to go ahead and just click OK.
1:32:39
And notice that it's given me this new type of start connector. It's a start puzzle piece that nothing goes above it.
1:32:44
But you can put anything you want below it. And I'm going to go ahead and cheat here. I'm just going to grab my existing code, so to speak.
1:32:51
This is code I'm writing, even though it's puzzle pieces. And now let me just claim, and I'll move this aside.
1:32:57
Here is now an implementation of my own function, my own block called "meow," whose purpose in life
1:33:03
is to meow until done and then wait one second. But what's powerful now is notice at top left, now that I've made the block,
1:33:10
I can use it any number of times. So I can grab this meow block, drag it over here, and you know what?
1:33:17
Now that "meow" exists as an idea, I can abstract that away. And I'm just going to arbitrarily drag it way to the bottom.
1:33:24
I'm not deleting it. I'm just putting it out of sight, out of mind so that we can focus now on this idea. And I claim that this implementation of meowing
1:33:31
is sort of better because it's more compact, it does what it says, and I don't care about the implementation details of "meow."
1:33:38
So this idea of abstraction, something we're going to use frequently. To abstract something away is to simplify.
1:33:44
Don't think about the underlying implementation details. Just care about what it does or what it's called.
1:33:50
Someone has to care about the implementation details, like me 30 seconds ago. But here on out, I don't need to care.
1:33:56
And so in fact, you and I are using the abstraction that is Scratch because I don't know how to put a speech bubble on the screen.
1:34:02
I don't know how to create that sound, meow. MIT did that, and they abstracted those pieces of functionality away already for us by just giving us
1:34:10
these puzzle pieces we see here. So the code will work the exact same. [MEOWING]
1:34:17
But it's sort of better designed now because now I've abstracted away the idea of meowing.
1:34:23
But I bet I can improve this further. Can I get rid of the repeat block altogether? And let me just tell the meow block how many times to meow.
1:34:31
Well, let me go down to the bottom and look at the implementation details. I'm going to right-click or Control-click on this,
1:34:37
and I'm going to edit it. So I'm going to make a change. And I didn't do this before, but I'm going to call it "meow," as before.
1:34:42
I'm going to add an input. And just so I know what it says what it does, I'm going to add the word "times" here.
1:34:49
And I'm going to change this placeholder to n. n for "number" is the go-to placeholder any time
1:34:54
we want to talk about a number in CS. So now notice the puzzle piece looks a little different.
1:35:00
It takes an argument or a parameter called n, which represents the number of times you want the thing to meow.
1:35:05
Now, that doesn't do that yet. So let me go back to my other code. Let me just decouple these temporarily.
1:35:13
I'm going to move my loop into my implementation of meowing. But I don't want to hard code, that is literally write the number 3 anymore.
1:35:21
I'm going to grab this oval and put it there. So now I've generalized the function.
1:35:27
So now it will meow any number of times, 0 on up, by executing that loop
1:35:33
and now more powerfully. Out of sight, out of mind. Notice that my code just became so darn simple.
1:35:40
Like, my function is called "meow." It meows some number of times. All I have to do is type a number there, and it just works.
1:35:46
And I don't care any more about those lower-level, so to speak, implementation details.
1:35:52
So here, no surprise. If I type in the number 3, zoom out, and hit Play-- [MEOWING]
1:36:00
--it still works just fine. So any questions on what we've just done here?
1:36:05
It's still just meowing, but that's besides the point. It's this creation of our own functions, this modularity,
1:36:11
this abstraction that's going to be the idea that keeps coming back to us. No? All right.
1:36:16
So let's make this a little more cat-like. Let me throw away all of this code. And let me go ahead--

## [Conditionals](https://youtu.be/3LPJfIKxwWc?t=5782)

1:36:22
oops-- let me throw away this code first and then the rest of this code. And let me go ahead and give myself another green flag block.
1:36:28
And let me go ahead, and let's create a cat that allows us to pet it by moving my cursor over the cat.
1:36:34
And maybe it likes that, so it'll meow when I do that. So let me go under Control, and let me grab this if conditional,
1:36:42
which we talked about as a building block earlier. Let me go to Sensing, and we haven't used this before.
1:36:47
But here is a weird sort of diagonal shape that says touching mouse pointer question mark.
1:36:52
So that's a Boolean expression. So I'm going to drag that, and it's definitely the wrong size. But it is the right shape, so it will grow to fill.
1:36:59
And the question I want to ask is if the cat is touching the mouse pointer, then go ahead and meow happily.
1:37:05
So let me grab the meow sound, put it in there. And so I think when I click the green flag to start the program,
1:37:12
and now I let the mouse pointer touch the cat, we should hear--
1:37:19
huh. huh. Doesn't seem to be working. There's a bug or a mistake in this program too.
1:37:27
What did I do wrong? Yeah. AUDIENCE: You didn't specify the sprite [INAUDIBLE].. DAVID J. MALAN: I don't need to specify the sprite explicitly
1:37:33
because a detail I didn't discuss earlier. In the bottom right of the screen, notice that the cat is already selected.
1:37:39
So this code relates to that cat. So your instinct is good if we had two or more sprites,
1:37:45
but I just have one, so I'm covered there. Other thoughts. Yeah. AUDIENCE: It only checks once.
1:37:50
DAVID J. MALAN: It only checks? AUDIENCE: Once. DAVID J. MALAN: Once. So I click the green flag. The computer did what I told it to do.
1:37:57
The mouse pointer was not touching the cat at that moment because it was touching the green flag. So, of course, it didn't meow.
1:38:03
So what maybe is the fix here? What puzzle piece can we add? AUDIENCE: After the green flag is [INAUDIBLE]..
1:38:09
DAVID J. MALAN: OK. OK. Interesting solution. So let me go ahead, and under Control let me grab a-- wait one second.
1:38:17
I'm going to change the 1 to 5, and now I'm going to click the green flag. So here we go. 1, 2, 3, 4, 5.
1:38:28
Damn it. [MEOWING] OK. That was yours, not mine. [LAUGHTER] It didn't work.
1:38:33
AUDIENCE: [INAUDIBLE] DAVID J. MALAN: Sorry? AUDIENCE: [INAUDIBLE] DAVID J. MALAN: Oh, maybe forever. So your approach would work, but it's very much a hack, if you will.
1:38:42
Like, I would have to time it perfectly so that the mouse pointer is touching it, or, conversely, I have to drag it there and just
1:38:49
leave it there for five seconds. And that's a little weird because you don't just touch a cat and then five seconds later it meows at you.
1:38:54
Like, presumably, we want it to be more interactive. So I like this idea of a loop. Right? Why don't we just tell the cat to forever listen for the cursor
1:39:04
as by using not repeat but forever? Let me move this in here. So now the cat's going to be told when the green flag is clicked just forever,
1:39:11
if touching, if touching, if touching. Oh, meow when actually touched. So now if I zoom out and hit Play, nothing's happening.
1:39:19
I don't have to wait any number of seconds. But when I do touch the cat-- [MEOWING] [APPLAUSE] [CHUCKLES] Fan section here.
1:39:26
Thank you. [MEOWING] So now it's actually working quite well. So there we have sort of a logical bug.
1:39:33
But it does make sense if you think about what it was you told the computer to actually do. Well, let's make things even more interesting
1:39:39
by using one of these extensions. In this bottom left corner, this is how I got to text-to-speech earlier. Let me go to Video Sensing over here too.
1:39:47
And I can actually-- there we go-- literally, the video has come on. Let me go ahead and do this. Get rid of this code, and let me step out of the frame.
1:39:55
When video motion is greater than-- well, this is CS50, so let's just type in 50, which is just a measure of motion.
1:40:02
Let me go and play sound meow.
1:40:07
OK. And let me stop and restart. All right. So there's the cat.
1:40:13
1:40:18
[MEOWING] OK. It worked. The cat's a little insensitive.
1:40:24
[MEOWING] There we go. Actually, you know what? Maybe it's just-- let me put-- let's change it.
1:40:30 20. Oh, my God. Oh, that's OK. [MEOWING] There we go. All right.
1:40:35
There we go. So now it's a little more sensitive to the petting by using the camera. Now, this is kind of a weird example.
1:40:41
And if I just start moving around crazily, like, it's just going to meow incessantly, which was what was happening-- [MEOWING] Stop.
1:40:48
[LAUGHTER] OK. When in doubt, this is when you reload the page. [LAUGHTER] All right.
1:40:53
So now we're back to where we wanted to be. But where can we now use these kinds of building blocks? Like, we were doing such tiny little programs.
1:41:00
But even that we could turn into a whole game, I bet. Could we get like one volunteer to come on up?
1:41:07
One volunteer? Everyone's looking down. OK. On the end here. Come on down. Yeah. All right.
1:41:12
Round of applause for our one brave volunteer here. [APPLAUSE]
1:41:18
All right. These Super Mario cookies are on the line for you, depending on how this goes.
1:41:23
So I'm going to have you come over here. And in advance on Scratch's website, we have some pre-made games,
1:41:28
one of them written by one of your predecessors, a former student, that they implemented this sort of "Whac-A-Mole" game.
1:41:36
So what you're about to see is the camera turn on on you. And you're going to see four moles above, below, left, and right.
1:41:43
And using only your head-- up, down, left, right-- the goal is to whack a mole to get a point every time your head touches one of these sprites.
1:41:51
So you're about to see things get very interesting very quickly. But using these building blocks, just those simple
1:41:57
blocks but have four sprites, not four cats but four moles in this case. We can actually turn these into actual games.
1:42:03
[MUSIC PLAYING] So here we go. Click Beginner. OK. And we just need you to center your head first.
1:42:10
[MUSIC PLAYING]
1:42:20
[INDISTINCT CHATTER] [CHUCKLES] [MUSIC PLAYING]
1:42:28
Nice. Ten seconds. [MUSIC PLAYING]
1:42:36
Nice. Two seconds.
1:42:42
AUDIENCE: [LAUGHS] DAVID J. MALAN: All right. A round of applause. [APPLAUSE] Thank you.
1:42:48
You want to introduce yourself? AUDIENCE: Hi, everybody. My name is [? Vanilla. ?] I'm a first year,
1:42:53
and I'm going to be majoring in computer science and economics. DAVID J. MALAN: Nice to meet you. Here we go. Thank you.
1:42:59
AUDIENCE: Nice to meet you. [APPLAUSE, CHEERING] DAVID J. MALAN: So we won't look at the code for that actual game. It was written by one of your predecessors.
1:43:05
And you can see it online if you're curious. But you can think about now with our functions, conditionals,
1:43:10
Boolean expressions, loops how you could kind of compose that kind of program. So odds are there was a loop that was just constantly listening
1:43:17
for that kind of connectivity, or it was one of those extensions that was waiting for motion to go
1:43:22
touch one of those sprites. Notice that there's these numbers up here. And we haven't talked about this yet. But just like in math, where you can have variables x, y, and z,
1:43:30
in programming, you can create variables using other puzzle pieces in Scratch that just keep track of how many seconds are left,
1:43:36
that keeps track of how many times her head hit one of the moles. And so you can implement the mechanics of games using very simple building
1:43:43
blocks. But how do you go about building something that's more interesting and interactive like that? Let me go ahead and bring up, for instance,

## [Oscartime](https://youtu.be/3LPJfIKxwWc?t=6230)

1:43:50
one of the very first things I wrote years ago when I was in graduate school and Scratch had just come out. I was taking a class at MIT's Media Lab.
1:43:57
And they invited us to beta test-- that is, try out the software before it then became part of the world.
1:44:03
And the game I made was this one here. Let me find the right version of "Oscartime."
1:44:10
So "Oscartime" is a game that took me tens of hours probably in the end.
1:44:15
It was a little bit addictive, but let me go ahead and full-screen it. And I won't play the whole game. But it looked a little something like this.
1:44:23
OSCAR: (SINGS) Oh, I love-- DAVID J. MALAN: Where trash is falling from the sky. And I can click on it and drag it.
1:44:30
And notice as I get close, the lid opens up like this. And if I let it keep falling, it goes in, and Oscar gives me a point.
1:44:37
And I can do this again. OSCAR: If you really want to see something trashy-- DAVID J. MALAN: All right. Here comes something else.
1:44:42
OSCAR: I have here a sneaker that-- DAVID J. MALAN: So now there's two pieces of trash. OSCAR: It's all full of holes, and the laces are--
1:44:49
DAVID J. MALAN: And it just keeps going, and going, and going. And if we can lower the volume for just a moment, we'll let more trash fall.
1:44:55
But to your comment earlier about one sprite or more sprites, that's what we're seeing here. Even though our examples thus far are just one cat, one or two puzzle
1:45:03
pieces, or a few puzzle pieces. Here is, I claim, a sprite. Here is another sprite. Here is another sprite.
1:45:09
And by toggling among them in that bottom right-hand corner, I can just associate different puzzle pieces with each of these sprites.
1:45:15
Now, I didn't start off by implementing this whole game. And in just a moment, if we can raise the volume a little bit,
1:45:20
we'll see even more trash is falling. So this is what-- I hate this song now, like 10 plus hours listening to this song on loop
1:45:26
just to get the timing right. But it brings to life all of these different sprites. And if you play it again and again, it's always a little bit different
1:45:34
because I'm using some randomness. So this newspaper doesn't always fall from there. Sometimes it's here.
1:45:39
Sometimes it's here. And so here, again, we have mechanics of a game where things are being perturbed a little, randomized a little bit
1:45:45
to keep things more interesting. And let me go ahead. OSCAR: (SINGS) I love trash. DAVID J. MALAN: There we go.
1:45:51
How. about raise a little volume? One more piece of trash. So a clock. It just goes on forever, this kind of game.
1:45:57
But let's go ahead and consider. Let me close that. Let me go ahead and consider. How I went about implementing that from the get-go.
1:46:04
So I will stipulate-- let me open a few of these versions here-- that the very first thing I did
1:46:11
was pretty much just implement the stage. Right? I was kind of procrastinating, so I poked around. I found the Sesame Street lamppost, and I dragged it into the world.
1:46:18
And done. Version one is done. It didn't do anything, but at least I had the world sort of laid out.
1:46:23
That is to say I took a baby step toward my goal. Then I started thinking about, all right, how do I bring the trash to life, even if it doesn't do much of anything else?
1:46:31
And so I created another sprite by clicking the appropriate button in that bottom right-hand corner. And I thought about, well, what do I want this trash to do?
1:46:38
I want it to just kind of fall from the sky. And so what I did here was the following.
1:46:44
If I go to this trash piece here or-- actually, sorry. Out of order. What I actually did first was I didn't even have the trash fall.
1:46:51
If I play this game, the trash just stays there in the air. But I can do this.
1:46:57
I can drag it, and as before, as I touch the other sprite, I get the trash can lid to go up.
1:47:03
So how do I do that? Well, let me click on Oscar down there, my first sprite. And here are the puzzle pieces via which I implemented this idea.
1:47:10
I changed Oscar's costume, his appearance, to be just number one, which was one of the images I imported into the program.
1:47:17
And then I forever did this. If Oscar is touching the mouse pointer, then change Oscar's costume to number two, otherwise change it back to one.
1:47:26
So it's super simple animation. I'm just toggling between lid up, lid down, lid up, lid down,
1:47:31
but it kind of feels interactive. And if I wanted to really make this pretty, I could have 30 different costumes where the lid is ever so slightly higher.
1:47:40
Then it would look even more like a movie or fluid motion. But this was enough to get the job done, which
1:47:46
is to say I didn't try to implement all of "Oscartime" together. I just took a second baby step toward my goal.
1:47:52
And then my next version of "Oscartime" might have looked a little something like this, where now the trash--
1:47:57
there's more going on here. Let's look at two of these blocks of code. The first thing I did was I enabled drag mode to draggable,
1:48:04
and I had to Google to figure this out because otherwise it didn't let me drag the trash while playing the game. But once I figured that out, I tell the trash
1:48:12
to go to a random x-coordinate between 0 and 240 from left to right and then the y location 180
1:48:19
because I always want the trash falling from the sky. And then what do I do? I told the trash to forever change its y-coordinate, its vertical coordinate,
1:48:27
by negative 1, negative 1, negative 1, one pixel at a time, which creates the illusion of it falling from the sky.
1:48:34
But I needed to do one other thing, and let me scroll up. Each of your sprites can have multiple programs, multiple scripts,
1:48:41
so to speak, that are not attached to one another. They will happen in parallel for you. The second one is saying this.
1:48:47
Forever if the trash is touching Oscar, what should it do?
1:48:52
Go to a completely different x and y location at the very top. Why?
1:48:57
Well, as soon as I drag the trash over the Oscar, I want it to disappear as though it's going into the can.
1:49:03
And I then want it to reappear at the top so more trash falls. So I just thought about what would it mean
1:49:08
for the trash to go into the trash can. Well, who cares? What really matters to the human user is that it just
1:49:14
disappears and teleports elsewhere. And so that's the idea I implemented here.
1:49:19
So if you can reduce intuitive ideas to just basic building blocks like this,
1:49:24
you can start to make things much more interactive. And lastly, if I look at this version here,
1:49:29
you'll see that we've combined these. And so indeed, if I actually go ahead and play this now,
1:49:35
not only is it falling. I can let it fall right on top of Oscar and watch it disappear.
1:49:41
But notice Oscar doesn't pop out yet because that was the fourth version and then the fifth version. And then I added the annoying music and so forth but sort of
1:49:48
composed this program step by step by step so as to accomplish my larger goal. And this is going to be true of all of the code you write,
1:49:55
be it in Scratch, or C, or Python, or in the like, trying to come up with--
1:50:00
or rather, trying to reduce your ideas, your grand vision to just baby steps, building blocks so that you start with version one,
1:50:07
and maybe you submit version 10 or 20. But you don't try to implement version 10 or 20 at the get-go.
1:50:13
You take those incremental steps. All right. How about one other? Well, let me propose this.
1:50:19
Let me go ahead and open three games that represent one that your predecessors also implemented, which looks a little something
1:50:27
like this in version zero. Suppose I wanted to implement a game that simply has these kinds of mechanics.

## [Ivy's Hardest Game](https://youtu.be/3LPJfIKxwWc?t=6633)

1:50:33
I'm touching my arrow keys on my keyboard-- up, down, left, and right. And I'm moving the Harvard logo. Let me zoom in a bit.
1:50:39
So if I hit the up arrow, the Harvard shield goes up. If I hit the down arrow, the shield goes down.
1:50:44
If I go all the way to the left, it goes left until it hits the wall and same thing on the right. So this is like the beginnings of a game or a beginning
1:50:51
of a maze, something like that. Well, how might I implement this? Well, let me look inside this one.
1:50:57
And there's a lot going on, but, again, I sort of took simple steps. Notice that I've got three sprites--
1:51:02
a left wall, which is just a straight line, the right wall, which is a straight line. And just intuitively, why did I implement those as sprites?
1:51:10
Why do they need to exist as entities themselves? Yeah, in front.
1:51:16
AUDIENCE: [INAUDIBLE] DAVID J. MALAN: Yeah. I want it to interact with the shield. So I need to be able to ask that Boolean expression, like,
1:51:21
not touching mouse pointer but touching shield, for instance, a different type of yes/no question.
1:51:26
And so what is the code for the shield actually doing? Well, there's a lot of duplication, and let me focus on the abstraction first.
1:51:32
Notice that I've got this one green flag clicked. I want the shield to go dead center, 0 comma 0,
1:51:38
and then forever listen for the human's keyboard, and feel for the wall. So I decided to implement my own pink puzzle pieces that
1:51:45
implement the two separate ideas. One, just listen for the keyboard-- up, down, left, right-- and then do something. And then feel for walls is this idea of whenever I go up,
1:51:53
down, left, or right, if I touch a wall, I need to stop doing whatever the keystrokes are telling me to do.
1:52:00
So now if we dive into those implementation details, listen and feel are abstractions, custom puzzle pieces.
1:52:07
Let's look at the implementation details. Well, here's the keyboard. If the key arrow up is pressed, change y by 1.
1:52:15
If key down arrow is pressed, change y by negative 1. And you can probably see where this is going.
1:52:21
Right arrow is x by 1. Left arrow is x by negative 1, and that's sort of all that's involved with up, down, left, right.
1:52:29
But wait a minute. Why is there no loop in this listen for keyboard puzzle piece?
1:52:35
I needed a loop last time so it constantly works. AUDIENCE: [INAUDIBLE] DAVID J. MALAN: Exactly.
1:52:41
I put the loop in my main part of my program up top so something is telling me to keep listening again and again.
1:52:48
So it's got to be somewhere, but it doesn't have to be in the actual implementation. And lastly, how about this feel for walls?
1:52:53
Well, if touching left wall, which is just another sprite, change x by 1. So that is to say if I'm touching the left wall,
1:53:00
I want to bounce it back the other direction and same thing on the right wall. If I'm touching the right wall, I want to bounce it
1:53:06
back to the left, which effectively means that even if the human's hitting the key, it's like fighting with this code,
1:53:11
but it's never going to go through the wall based on that math. It's going to stop it right there.
1:53:16
All right. Let's add something else to the mix. Suppose I want the game to change to be a little something like this, where Yale is some kind of block in between me and the exit.
1:53:25
So some dramatic race here. OK. I just got by, but the Yale logo doesn't seem to be doing all that much except bouncing.
1:53:32
So I'm guessing there's a loop, maybe a conditional checking for those walls too. So let's go ahead and zoom out, see inside.
1:53:38
Let's not worry about Harvard because it's pretty much the same. Let's look at the Yale puzzle pieces. And sure enough, go to the middle.
1:53:45
0 comma zero. Point in direction 90, so point horizontally on the grid.
1:53:50
And then if touching left wall or touching right wall-- I'm kind of cheating this time, but cleverly, just spin around and do 180
1:53:58
so you effectively bounce off the wall. This just tightened up my code. I don't need to do the negative 1 or the plus 1.
1:54:03
I just say bounce in this form of code, otherwise just constantly move one step. Now, if this is a game where Yale is supposed to be better and faster,
1:54:12
well, let's change the 1 to 5. Move 5 pixels at a time. Let's move it 10 back and forth.
1:54:17
Let's maybe 100. Uh-oh. So what just happened? That is a bug, which we can avoid by just not doing that.
1:54:25
But why did it break out of the wall? Yeah. AUDIENCE: [INAUDIBLE]. At first it was [INAUDIBLE].
1:54:30
DAVID J. MALAN: Exactly. Because I'm doing 100 steps at a time, I'm never actually touching the other sprite because I'm
1:54:36
sort of stepping way over it. So there's never a moment where they're actually touching. So previously, I was just getting lucky by doing fewer steps because it's
1:54:44
gradually going over the wall, which gives me just enough time to detect as much. So I would have to kind of tinker, and he'll
1:54:50
handle this a little bit differently. So it's a bug if it's too fast. But at least if I keep it slow and reasonable
1:54:55
the math actually does work out, so long as it starts again in the middle. Well, let's do one final flourish here, whereby let's bring MIT into the mix.
1:55:04
Right? They're super smart, so maybe they can kind of track us and follow wherever I'm going.
1:55:11
So how might this work? All right. So nothing happens yet because we haven't finished composing the game.
1:55:16
And notice here-- OK. Now MIT is struggling. It's kind of twitching there because it's going just above, and below,
1:55:21
and then above, and below. So we could fix that too if we want. But that's just a function of my math, one pixel at a time.
1:55:28
Let me open up this one, see inside, and click on MIT.
1:55:33
And it doesn't take much to implement MIT, it seems. So go to random position, forever point towards the Harvard logo outline,
1:55:43
AKA the shield, and then move one step. So if I wanted to make MIT even smarter, even faster, what do I change here?
1:55:50
AUDIENCE: [INAUDIBLE] DAVID J. MALAN: Yeah. Change one step to two steps to double their speed or five steps, 10 steps,
1:55:56
or 100 steps. And the game is going to be over like that. But that's all it takes to now make these kinds of elements. So if you are a game player on your phone, or consoles,
1:56:03
or computer, or whatever, if you think about almost any game, you can probably now start to think about how they implemented
1:56:08
those mechanics because it's just being reduced to functions, conditionals, loops, variables, and the like in this case.
1:56:15
So let's go ahead here and have maybe one final volunteer. We've got one more bag of Oreos here.
1:56:22
OK. That was super fast. Do you want to come on up? All right. Brave volunteer. Come on up. [APPLAUSE]
1:56:30
All right. Let me find the full-fledged version of this that one of your predecessors
1:56:36
made. And let me get the right one. OK. Here we go.
1:56:41
We'll see some instructions on the screen in just a moment. And when we hit Play, you'll see that the mechanics are all combined now
1:56:50
into one full-fledged game. But first, an introduction. It's on.
1:56:55
SAM: Hi, everyone. I'm Sam. I live in [INAUDIBLE]. I'm a freshman, and I'm from Nepal. DAVID J. MALAN: All right.
1:57:01
Welcome to the stage. [APPLAUSE] SAM: Thank you. DAVID J. MALAN: All right. So here we go. Yep. Go ahead and click the green flag.
1:57:08
[MUSIC PLAYING] [MC HAMMER, "U CAN'T TOUCH THIS"] You can't touch this.
1:57:14
DAVID J. MALAN: You see the grid is just bigger this time. (SINGING) You can't touch this.
1:57:19
DAVID J. MALAN: Nice. Now there's that Yale element. (SINGING) You can't touch this. My, my, my my music hits me so hard.
1:57:27
Makes me say, oh, my Lord. Thank you for blessing me with a mind to rhyme and two hyped feet. It feels good when you know you're down, a super dope homeboy from the Oaktown.
1:57:35
DAVID J. MALAN: OK. Third Yale. All started at slightly different positions.
1:57:41
(SINGING) I told you, homeboy. You can't touch this. DAVID J. MALAN: Nice. All right. There's MIT. (SINGING) And ya know you can't touch this.
1:57:47
[CHEERING, APPLAUSE] DAVID J. MALAN: Oh. (SINGING) You can't touch this. Yo.
1:57:53
Let me bust the funky lyrics. DAVID J. MALAN: Gotta go fast. Oh.
1:57:59
No.
1:58:05
Oh. [CHUCKLES] (SINGING) Cold on a mission, so fall on back. Let them know that you're too much, and this is a beat they can't touch.
1:58:13
DAVID J. MALAN: Nice. [EXCLAIMING] (SINGING) You can't touch this. DAVID J. MALAN: No more walls but two MITs.
1:58:20
(SINGING) Yo, sound the bell. School's in, sucker. DAVID J. MALAN: Princeton now. (SINGING) Give me a song or rhythm.
1:58:25
Making them sweat, that's what I'm giving them. Now, they know you talk about the Hammer when you're talkin'
1:58:31
'bout a show that's hyped and tight. Singers are sweatin', so pass them a wipe or a tape to learn.
1:58:36
DAVID J. MALAN: Second to last level. (SINGING) The chart's legit. Either work hard, or you might as well quit.
1:58:41
That's word because you know you can't touch this.
1:58:48
You can't touch this. Break it down. DAVID J. MALAN: All right.
1:58:53
Clear. There we go. Nice. Oh, oh.
1:58:59
Oh. Few more lives. Oh.
1:59:05
(SINGING) Stop. Hammer time. DAVID J. MALAN: Here we go. There we go. [EXCLAIMING] All right. Couple more tries.
1:59:12
Yes! Oh, no. (SINGING) This is it for a winner. Dance to this, and you're gonna get thinner.
1:59:17
Now move, slide your rump. DAVID J. MALAN: Starts getting stressful. (SINGING) Just for a minute, let's all do the bump. Bump, bump, bump.
1:59:23
Yeah. You can't touch this. Look, man. You can't touch this.
1:59:29
You'll probably get hyped, boy. DAVID J. MALAN: One more try. (SINGING) You can't touch this. Ring the bell. School's back in.
1:59:34
DAVID J. MALAN: All right. A round of applause, nonetheless. [APPLAUSE] Nicely done. Thank you.
1:59:42
So as you might have noticed if your eyes started to wander to the light bulbs here, there's
1:59:48
actually 64 of these light bulbs. And I'm wondering if you divide 64 by 8, that's 8 bytes of light bulbs.
1:59:55
And we now have some Unicode in our vocabulary. So might very well be the case that we've been spelling something out on the stage here for you all of this time.

## [The Harvard Krokodiloes and The Radcliffe Pitches](https://youtu.be/3LPJfIKxwWc?t=7203)

2:00:03
But before we adjourn for cake to be served in the Transept, allow me to introduce some of CS50's human friends,
2:00:11
the Harvard Krokodiloes and the Radcliffe Pitches,
2:00:17
to give us this exciting ending, "This is CS50."
2:00:23
[APPLAUSE, CHEERING]
2:00:36
[HARMONICA NOTE] [VOCALIZING] SPEAKER: (SINGING) There's a certain someone who I'm indebted to.
2:00:50
And since the old [? BNC ?] has 50, I have this friend for you.
2:01:00
A two, three, four. [VOCALIZING]
2:01:08
Oh, rubber ducky, you're the one. You make [INAUDIBLE] so much fun.
2:01:14
Rubber ducky, I'm awfully fond of you. [SCATTING] Rubber ducky, you make me smile, and you help my code compile.
2:01:25
Rubber ducky, you're my very best friend. It's true. When I'm at a standstill, your debugging abilities stun me.
2:01:33
When I'm at the end of my rope, you just snap, and my code's up and running.
2:01:40
Rubber ducky, you're so fine, and I'm lucky that you're mine. Rubber ducky, you're my very best friend.
2:01:47
It's true. You're my best friend. It's true.
2:01:52
Rubber ducky, I'm awfully fond of you.
2:02:02
[CHEERING, APPLAUSE]
2:02:08
SPEAKER: Good afternoon, CS50. We are the Harvard Krokodiloes, Harvard's oldest a cappella group, founded way back in 1946 at the historic Hasty Pudding Club.
2:02:16
We'd love to make a big thank you to CS50 staff and to David Malan for having us perform here at Sanders Theater.
2:02:21
And you enjoyed this performance, please come audition for us this weekend at Farkas Hall.
2:02:26
[CHEERING, APPLAUSE]
2:02:36
SPEAKER: Hello, everyone. We are some of the Radcliffe Pitches, and we are also hosting auditions this weekend.
2:02:41
You can find more information at our Instagram, @radcliffepitches. Now, let me tell you a little bit about just about a year ago
2:02:48
today, when I was sitting in your very seats on my first day of CS50 lecture. And this is just about how I was feeling.
2:02:55
[HARMONICA NOTE] [VOCALIZING]
2:03:03
(SINGING) It's the first day of class, and I'm brand new to code.
2:03:11
Is this for me? So many people around. Can I get through the workload?
2:03:18
But it's my dream. I tend to stick to English, not science.
2:03:25
But my [INAUDIBLE] friends told me to try this. Hey, dancing robot dog, you kind of look like you have your life together,
2:03:32
I guess. I really need some advice. (ALL SINGING) We know you're feeling unsure,
2:03:37
but this is really the right call. In CS50, you'll meet new friends, get free food.
2:03:44
You'll be all set for this fall in CS50.
2:03:50
You have a thousand TAs who will help you. You'll get cupcakes, duckies, Chinese food.
2:03:58
And you can always take this class and set aside.
2:04:03
SPEAKER: This is CS50. Fist bump.
2:04:10
[LAUGHTER] [APPLAUSE, CHEERING]
2:04:16
DAVID J. MALAN: Thank you to the Kroks. Thank you to the Pitches. Cake is now served. Come on up to say hi if you'd like or meet Spot.
2:04:23
See you next time. [APPLAUSE, CHEERING] [MUSIC PLAYING]
