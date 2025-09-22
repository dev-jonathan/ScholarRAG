---
link: https://youtu.be/jZzyERW7h1A
related_files:
  - week-3-notes.md
  - problemset/week-3-plurality.md
  - problemset/week-3-problemset.md
  - problemset/week-3-runoff.md
  - problemset/week-3-sort.md
  - problemset/week-3-tideman.md
title: "Lecture 3: Week 3 - Algorithms"
type: transcription
week/lecture: "3"
---

# [Lecture 3: Week 3 - Algorithms](https://youtu.be/jZzyERW7h1A)

TABLE OF CONTENTS:

0:00 - Introduction
1:01 - Overview
3:02 - Attendance
9:43 - Linear Search
25:03 - Binary Search
28:28 - Running Time
38:14 - search.c
51:33 - phonebook.c
53:49 - Structs
1:05:26 - Sorting
1:12:46 - Selection Sort
1:24:53 - Bubble Sort
1:33:13 - Recursion
1:46:31 - Merge Sort
2:00:23 - Sort Race

## [Introduction](https://youtu.be/jZzyERW7h1A?t=0)

0:00
[MUSIC PLAYING]

## [Overview](https://youtu.be/jZzyERW7h1A?t=61)

1:01
DAVID MALAN: All right, this is CS50. And this is week 3. And as promised, we thought we'd take a bit of a break on new syntax this week
1:09
and focus a lot more on algorithms and implementation thereof because over the past few weeks, besides Scratch, we've now had C.
1:15
And you have a lot of vocabulary now. Even if it might not seem yet that you fully grasp all of the functionality of this particular language, with practice,
1:23
it'll get easier and easier. But today, we'd focus instead on ideas and ultimately on this, how to think algorithmically, and so to take problems in the real world
1:32
and try to quantize them in a way that you can map those puzzle pieces from week 0 or all of this new syntax from weeks 1 and 2
1:39
on to actually writing code to solve those problems. To contextualize this, though, we thought we'd remind you of this here chart from week zero.
1:46
And recall that in week zero, we painted this picture where on the x-axis on the horizontal was the size of the problem.
1:52
And the number of phone book pages increased as you went from left to right. And then on the vertical axis or y-axis, we had time to solve.
1:59
So this was like how many seconds, how many page turns, how many units of measure-- whatever you're using.
2:05
We might actually describe the solution there too. And the first algorithm we had in week 0 for the phone book
2:10
was, like, one page at a time. So we plotted it with this 1 to 1 slope. The second algorithm, we started doing two pages
2:16
at a time, which did risk a bug. I might have to double back one page. But it was still going for the most part twice as fast.
2:23
So it was still a slow but sort of a 2 to 1 slope instead of 1 to 1. But the third and final algorithm, recall,
2:29
was sort of fundamentally different. And it was this logarithmic curve, so to speak, whereby it kept increasing, increasing, increasing but very, very slowly.
2:38
So even if you, like, doubled the size of the phone book, as by having Cambridge and Allston here in Massachusetts merge, no big deal.
2:44
It was just one more page turn, not another 500 or another 1,000. So think back today on that particular idea of how we began to divide
2:54
and conquer the problem. And that sort of gave us a fundamentally better advantage. So we thought we'd see if we can apply this lesson learned as follows.

## [Attendance](https://youtu.be/jZzyERW7h1A?t=182)

3:02
If I were to take, like, attendance today sort of here on stage, I could do it old school, like, 1, 2, 3, 4, 5, 6, 7, 8, and so
3:10
forth, so one step at a time. I could also double the speed-- 2, 4, 6, 8, 10, 12, 14, 16, and so forth.
3:18
But I dare say we can learn a bit from week zero. And if you'll indulge me right in place, could everyone
3:24
stand up and think of the number one. So right where you are, just stand up if you could.
3:32
Stand up. And think of the number one. So at this point, hopefully, everyone's literally thinking of the number one.
3:38
And the second step of this algorithm, which I claim ultimately theoretically should be much faster than either my one person at a time
3:45
or two people at a time, step two is this. Pair off with someone standing. And add their number to yours.
3:51
And remember the sum.
3:59
Person can be in front of, behind, left, or right of you.
4:06
All right most likely most everyone in the room assuming you found someone is thinking of the number two
4:13
now unless you're sort of an odd person out in the row. And that's fine. If you're still one, that's fine. But most of you are probably two.
4:19
Next step is that one of you in those pairs should sit down.
4:29
OK, so many of you tried to sit down as quickly as possible we noticed. But so next step now, at this point, rather, most of you
4:37
are thinking of the number two. A few of you are thinking of the number one. And that's OK. The next step, and notice we're about to induce a loop, so the rest of this
4:45
is on you, if still standing, go back to step two.
4:53
[INTERPOSING VOICES]
5:18
DAVID MALAN: If still standing, notice that this is a loop. So keep going. Keep going if still standing.
5:24
[INTERPOSING VOICES] DAVID MALAN: There?
5:30
How about there? [INTERPOSING VOICES] DAVID MALAN: That's OK.
5:36
But now keep going. Keep going. Keep pairing off, so maybe you two.
5:42
All right, a few more seconds. [INTERPOSING VOICES]
5:48
DAVID MALAN: So step two, still.
5:55
All right, keep pairing if you're standing. [INTERPOSING VOICES]
6:03
6:08
DAVID MALAN: All right. All right, so theoretically, there's only one person standing left.
6:16
But clearly, that's not the case. That's fine. I will help with the pairing because some of you are far away.
6:22
So let's see. What's your number here? Sorry? What's your number?
6:27
Eight. OK, go ahead and sit down. How about in back? What's your number? 46. Nice.
6:32
OK, go ahead and sit down. Who else is standing? Over here, what's your number?
6:38
You're 16? OK, so go ahead and sit down. And behind you? 48.
6:44
OK, go ahead and sit down. Is anyone still standing? Yeah? 32.
6:50
Nice. Still standing over here. 43. OK, nice. Sit down.
6:55
Sit down. And anyone else still standing here? 22. Go ahead and sit down.
7:01
Is anyone still standing and participating? Yeah, where-- oh, yeah.
7:07 16. OK, go ahead and sit down. Anyone else still standing? OK, so theoretically, everyone's paired off.
7:14
You were the last person standing. So when I hit Enter here, having just greased the wheels
7:19
to do all of the remaining additions myself, we should have the total count of people in the room.
7:24
And recognize that unlike my algorithm, which would have required pointing at each and every person
7:29
or my second algorithm, which would mean pointing at every two people twice as fast, theoretically, the algorithm you all just executed,
7:38
I daresay, should've been fundamentally faster. Why? Because no matter how many people in the room-- maybe, like,
7:43
if there were 1,000 people in the room, there would then have been 500, just as there would be 500 pages in week zero.
7:50
Then from 500, there'd be 250-- 125. Why? Because on each step of the algorithm, half of you
7:55
theoretically were sitting down, sitting down, sitting down, dividing and conquering that problem.
8:00
So the total number of people in the room as of now according to your count is 231.
8:08
As a backup, though, Carter kindly did it the old-fashioned way, one person at a time. And Carter, the actual number of people in the room is?
8:16
[LAUGHS] OK, so our first real world bug to be fair. So theoretically, that should have worked.
8:23
But clearly, we lost some numbers along the way, so a bug that we can fix today. But remember that really, this is just similar in spirit
8:31
to that algorithm we indeed did in week zero. It's the same as the phone book example. It went off the rails in this case.
8:37
But it's the same idea, ultimately dividing and conquering. And any time you have this halving, halving, halving,
8:44
there's going to be a logarithm involved there, even if you're a little rusty on your math. And that's fundamentally faster than just doing something n times
8:51
or even n divided by 2 times where n is the number of people in the room or in week zero, the number of pages in the phone book.
8:57
So even when you're using your iPhone or Android device later today, like, if you search for a contact using autocomplete,
9:04
it is that so-called divide and conquer algorithm that's finding people in your address book.
9:10
It's not starting top to bottom or bottom up. It's probably going roughly to the middle and then doing the top half or the bottom half, repeating again and again.
9:19
So these ideas are everywhere. And hopefully, you end up finding just the one person you're looking for or in your case,
9:25
the one person last standing who should have theoretically had the count of everyone because if each of you started by representing 1,
9:32
effectively handed off your number, handed off your number, handed off your number, it theoretically should have coalesced
9:38
in that final person standing. So let's consider the connection now between this idea

## [Linear Search](https://youtu.be/jZzyERW7h1A?t=583)

9:43
and what we introduced last week, which was this idea of very simple data structures in your computer's memory-- like, actually using this memory as
9:52
though it's kind of a grid of bytes. Each one of these squares, recall, represents 1 byte or 8 bits.
9:58
And we can get rid of the hardware and sort of abstract it away as just this grid of memory or this canvas.
10:03
And then we introduced arrays last week. And what was the key definition of an array? How would you describe an array?
10:11
What is it, anyone? What's an array? Yeah, in the middle.
10:18
A collection. A collection. And I don't love data types only because in C, it tends to be the same type.
10:24
So a collection of data. I do like that. But there's one other key characteristic. Do you want to be more precise? It's not just a collection--
10:32
something about where it is. Potentially strings. But strings are just an example of putting char, char, char, char.
10:39
It could certainly be integers or floating point values. Another characteristic? Sorry?
10:45
It's not necessarily ordered. Actually, we'll come back to that today. It could be in any order. And certainly a string isn't necessarily in sorted order.
10:52
It's in whatever the word is. It's a list in concept. But there was something key about where we put things in memory.
10:59
Yeah? Consecutive-- the memory is consecutive, a.k.a., contiguous.
11:05
An array is important in C because, yes, it's a list of values. Yes, it's a collection of values. But the real key distinction in an array in C is that it's contiguous.
11:15
The bytes are back to back to back somewhere in the computer's memory, at least for any given data type, be it an int, a float, a bigger string.
11:23
All of the characters are back to back to back in the computer's memory, not spread all out, even if you have space elsewhere.
11:30
So with that said, we can actually start to solve problems with that mindset.
11:35
And for instance, if I kind of pare this down to just an abstract array of size 1, 2, 3, 4, 5, 6, 7, for instance, suppose
11:42
that there are these numbers inside of this array of memory. So here are seven integers or ints in C. I have in this case
11:51
sorted them just to make the numbers pop out as obviously smallest to largest. But the catch with C is that if I were to ask you
11:58
or if you were to ask the computer through code to find you the number 50, well, obviously, every human in this room
12:03
just found it obviously right there because we kind of have this bird's eye view of the whole memory at once.
12:10
But the computer ironically does not have that bird's eye view of its own memory. It can only look at each location one at a time.
12:18
So if you really were to do this like a computer, you would kind of have to, like, shield your eye and only look at one number at a time from left
12:26
to right, from right to left, or in any order in order to find is the 50 actually there.
12:31
You can't just take a step back. And boom, it pops out at you. So this is kind of analogous, this array,
12:37
to being like a set of gym lockers or school lockers like this where the doors are actually closed by default.
12:42
The numbers are in there. But the doors are closed, which is to say the computer and we can't actually look. So we couldn't find yellow lockers.
12:49
But we did find red lockers here. And so I propose that you think of these lockers on the stage here of which there are seven as well as representing an array.
12:57
And just so we have some terminology, notice that I've labeled these bracket 0, bracket 1, bracket 2, 3, 4, 5 and 6.
13:05
And the bracket notation recalls the new syntax from last week that lets you index into--
13:10
go to a specific spot inside of an array. And notice that even though there are seven lockers,
13:15
I only counted as high as six. But again, that's just a side effect of our generally counting from 0.
13:20
So 0 through 6 or 0 through n minus 1 because if there are n equal 7 lockers,
13:27
n minus 1 is 6. So that's the left bound and the right bound respectively. So suppose that we were to use these lockers as representing a problem,
13:37
like we want to find an actual number behind these doors. So this is actually a very common problem in the real world.
13:42
And you and I take for granted every day that big companies like Google and Microsoft and others, like, do this for us
13:49
constantly, not to mention AI doing something similar nowadays, searching for information.
13:54
And we'll focus on some basics first that will lead us to more sophisticated algorithms ultimately.
13:59
But all we're going to talk about fundamentally is this same picture from week zero and from week one and from week two
14:05
where here is a problem to be solved. So if for instance, the input to this problem is an array of numbers--
14:11
an array of seven numbers-- I can't see them all at once-- but I'm looking for something like the number 50--
14:16
ultimately, I want to get back out. I claim true or false. Like, the number 50 is there.
14:21
Or it is not. That's one way of thinking about the search problem. Find me some piece of data if it's there.
14:27
Otherwise, tell me that it's not-- true or false, respectively. So the algorithm inside of this black box,
14:33
though, is where we're going to actually have to do some thinking and actually figure out how best to find the number or the data we care about.
14:41
And even though we'll use numbers to keep things simple today, you could certainly generalize this to web pages or contacts
14:47
or any other type of information that are in some computer or database more generally.
14:52
So maybe to keep things interesting, could we get-- how about two volunteers?
14:59
Wow, that was fast. OK, come on down. And how about one other volunteer? I'll go over here.
15:04
OK, how about you? Come on down. Sure, round of applause for our volunteers. [APPLAUSE]
15:10
OK, welcome. Come on over. Do you want to introduce yourself to the group?
15:15
AUDIENCE: [INAUDIBLE]. DAVID MALAN: Like a few seconds is fine. AUDIENCE: Hi, I'm Sam. I am not a CS concentration.
15:21
DAVID MALAN: [LAUGHS] So what are you? Do you know yet? AUDIENCE: Applied math. DAVID MALAN: OK.
15:27
Nice. Nice to meet you. Welcome. And? AUDIENCE: Hi, I'm Louis. I'm from first year, Matthews.
15:32
And I'm going to do Econ with Stats. DAVID MALAN: Oh, you're in Matthews too? OK. [CHUCKLES] I was in Matthews too, so Matthews South?
15:40
Oh, wow. Oh, my god. I was room 201. AUDIENCE: 103. DAVID MALAN: Fifth floor--
15:46
all right, so anyhow. And so we have Louis and your name? AUDIENCE: Sam. DAVID MALAN: Sam. Louis and Sam.
15:51
So Louis and I are going to step off to the side for just a moment because Sam, we have a problem for you to solve. This feels a little bit like Price Is Right.
15:57
But behind you are these seven lockers. And we'd like you to just find us the number 50.
16:03
That's all the information you get. But we'd like you to then explain how you go about finding it. AUDIENCE: Wait, are they in order or anything?
16:10
Or [INAUDIBLE] it just kind of [INAUDIBLE]?? DAVID MALAN: Find us the number 50.
16:15
And then tell us how you found it.
16:20
OK, what was in there, just so the audience knows. AUDIENCE: [INAUDIBLE] DAVID MALAN: Yes. [LAUGHTER] AUDIENCE: It was $10, a very, very big $10 bill.
16:28
DAVID MALAN: OK. AUDIENCE: Fake money. DAVID MALAN: OK.
16:33
AUDIENCE: That was $100.
16:39
$1. $5. OK, I'm not lucky.
16:45
Oh, I found it. DAVID MALAN: Nice. Take it out and so people can believe. All right, wonderful.
16:50
So you found the 50. [APPLAUSE] And now if you could explain. I'll take that.
16:55
If you could explain, what was your algorithm? What was the step-by-step approach you took? AUDIENCE: I didn't really have one.
17:03
I just started on one end. And I went down because it wasn't in order or anything. So I just kept going until I found it.
17:09
DAVID MALAN: OK, so that's actually pretty fair. And in fact, let's step forward here. Carter's going to very secretly kind of shuffle the numbers
17:14
in a particular new arrangement here. And so you really went from right to left. And I dare say maybe going from left to right might be equivalent.
17:22
But could she have done better? Could she have done better, because that took 1, 2, 3, 4, 5 steps?
17:29
Could Sam have done better? Sure. How?
17:35
OK, so you got lucky. You could have found the number in one step. Although, luck isn't really an algorithm.
17:40
It really isn't a step-by-step approach. So another thought? AUDIENCE: [INAUDIBLE] dollar bills--
17:46
sort them in order? DAVID MALAN: Oh, interesting. So you could have taken out all of the dollar bills, sorted them,
17:54
put them back in, and then you probably could have done something like the divide and conquer approach. AUDIENCE: I didn't know I was allowed to do that.
18:00
DAVID MALAN: No, you weren't allowed to. So that's fine. AUDIENCE: [INAUDIBLE] DAVID MALAN: But that would be a valid algorithm. Although, it sounds very inefficient to do all this work just
18:07
to find the number 50 because in doing that work, she would've found the 50 once. But that might actually be a reasonable solution
18:13
if she plans to search again and again and again, not just for seven numbers but maybe a lot of numbers.
18:18
Maybe you do want to incur some cost up front and all the data so as to find it faster. But let's do this a little more methodically.
18:24
We'll step off to the side once more. And just by convention, if you want to go ahead and-- do we need this? OK.
18:29
AUDIENCE: Got it. DAVID MALAN: OK, let's go from left to right. Yep. And go ahead and show everyone the numbers just
18:34
to prove that there's no funny business here. AUDIENCE: 20. DAVID MALAN: [LAUGHS]
18:41
AUDIENCE: Oh, OK. 500. DAVID MALAN: Nice.
18:48
AUDIENCE: 10. DAVID MALAN: Mm-hm. So it doesn't sound like it's sorted, either, this time.
18:54
AUDIENCE: Five. DAVID MALAN: Nice. And?
18:59
AUDIENCE: 100. DAVID MALAN: Oh, so close.
19:05
AUDIENCE: [INAUDIBLE] DAVID MALAN: I know. Now we're just messing with you. AUDIENCE: 1. DAVID MALAN: OK, and lastly?
19:10
AUDIENCE: [GASPS] 50. DAVID MALAN: Very well done. OK, so nicely done. [APPLAUSE] And so thank you.
19:17
So this is a say whether she goes from left to right or right to left, like, the performance of that algorithm just going linearly
19:24
from side to side really depends on where the number ends up being. And it kind of does boil down to luck. And so that was kind of the best you could do because I dare say,
19:31
had you gone linearly from right to left-- and go ahead to reset-- had you gone from right to left, that time you would have gotten lucky.
19:37
So on average, it might just kind of work out. And so half the time, it takes you maybe half as many steps--
19:43
half the number of lockers to find it on average because sometimes it's in the one end. Sometimes it's on the other end. Sometimes it's smack dab in the middle.
19:49
But we're going to give you the option now, Louis, of knowing that it's sorted. So we're going to take away the microphone from you.
19:56
But stay on up here with us. And you are now given the assumption that the numbers are this time sorted from smallest to largest, left to right.
20:03
And might you want to take more of a divide and conquer approach here? Wait a minute.
20:09
AUDIENCE: [LAUGHS] DAVID MALAN: What might you do as your algorithm, Louis? AUDIENCE: Well, I think I know all the numbers, right?
20:16
It's 1, 5-- DAVID MALAN: Oh, damn it. AUDIENCE: 10, 20, 50. DAVID MALAN: OK, so Louis has some memory, as we'll say. OK.
20:22
AUDIENCE: But assuming if I didn't have memory. DAVID MALAN: OK, assuming if you didn't have memory, where would you start first? AUDIENCE: I would probably start in the middle.
20:27
DAVID MALAN: OK, go ahead. Go in the middle. And what do you see? AUDIENCE: 20. DAVID MALAN: 20.
20:32
OK, what does that mean now for you? AUDIENCE: So now that means that since4 I know there's some numbers bigger, I'll go to the right.
20:38
DAVID MALAN: Good. So you can tear the problem in half, so to speak. As per week zero, skip all of the lockers on the left.
20:43
And now go where relative to these three? AUDIENCE: Relative to the middle. DAVID MALAN: OK. AUDIENCE: So maybe [? you ?] don't know what's on the right-hand side.
20:48
And so now it's 100. DAVID MALAN: OK, nice. AUDIENCE: So the 50 must be between 20 and 100.
20:54
So it must be this one. DAVID MALAN: Indeed. So a round of applause for Louis for getting this right this time.
21:00
[APPLAUSE] We have some lovely parting gifts, since we're using monopoly money. So it's not actual money.
21:06
But this is the Cambridge edition Harvard Square and all for both of you. So welcome.
21:11
Thank you so much. [APPLAUSE]
21:17
So Louis was actually getting particularly clever there when his first instinct was to just remember what were all the numbers and then sort of deduce
21:23
where the 50 must obviously be. So that's on us. Like, ideally, we would have completely changed the dollar amount so
21:29
that he couldn't use that information. But it turns out Louie's instinct there to figure out where the number should
21:34
be and jump right there-- index into that exact location-- is actually a technique. And it's a technique we'll talk about in future classes
21:42
where you actually do take into account the information and go right where you want. It's an example of what we'll eventually call hashing, so to speak,
21:50
in a concept called hash tables. But for now, let's try to formalize the algorithms that both of these volunteers kind of intuitively
21:58
came up with, first and second. And we'll slap some names on them. So the first, and I've hinted at this, is what we would call linear search.
22:05
Anytime you search from left to right or from right to left, it's generally called linear search.
22:10
Why? Because you're kind of walking in a line, no matter which direction you're going. But now for today's purposes, let's see if we can't truly
22:17
formalize what our volunteers' algorithms were by translating them, not necessarily to code yet, but pseudocode.
22:24
See if we can't map it to English-like syntax that gets the ideas across. So I dare say, the first algorithm, even though she went from right to left,
22:32
then from left to right, might look like this. For each door from left to right, she checked if 50 is behind the door
22:39
as by looking at it. If it was behind the door, then she returned true. Like, yes, this is the 50.
22:45
That didn't happen on the first iteration, though. So she moved on again and again.
22:51
And now notice the indentation here is just as important as it was in week zero. Notice that only at the very bottom of this algorithm
22:59
do I propose returning false. But it's not indented inside of this pseudocode. Why? Well, because if I had changed it to be this,
23:06
what would be the logical bug in this version of that algorithm? Yeah?
23:17
Exactly. If she had opened the first door, found it to be the wrong number if it says else-- if it's not behind the door, then return false--
23:24
that would erroneously conclude the 50's not there, even though it could certainly be among those other doors.
23:29
So this first version of the code where the return false is sort of left indented, so to speak, and the very last thing
23:35
you do if you don't previously return true, that just makes sure that we're handling all possible cases.
23:42
But let's make this maybe a little more technical. This is how a computer scientist or a programmer
23:47
would likely express this instead. Instead of just drawing it in broad strokes, it's actually fine to kind of steal some of the syntax from languages like C
23:56
and actually use some of the indices or indexes like 0, 1, 2, 3, 4, 5, 6,
24:01
to represent the pieces of data we care about. So this is a little more precise. For i-- like a variable i-- from the value 0 to n minus 1,
24:12
so in the case of seven doors, this is like saying, for i starting at 0, going up to 6, do the following.
24:19
If the number 50 is behind the doors array-- so I'm using array syntax, even though this is technically still pseudocode--
24:27
if the ith location of my doors array has the number 50, return true.
24:32
Otherwise, if you do that again and again and again-- n total times-- and you still don't find it, you want to return false.
24:39
So we introduced this. This is just an example of how you can start to borrow ideas from actual code to paint the picture even more precisely of what
24:47
it is you want a colleague to do, what it is you want your code to do, ultimately, by sort
24:53
of borrowing these ideas from code and incorporating it into our pseudocode. But what about the second algorithm here,

## [Binary Search](https://youtu.be/jZzyERW7h1A?t=1503)

25:03
the second algorithm, whereby he took a divide and conquer approach, starting in the middle and then going right and then going left.
25:10
Well, it turns out this is generally called binary search. Bi implying two, because you're either going with the left half or the right half again and again.
25:17
This is literally what we've been talking about since week zero when I searched the phone book. That too was binary search, dividing and dividing and dividing in half and half.
25:25
So if we were to draw some pseudocode for this, I would propose that we could do something like this. If 50 is behind the middle door, then we got lucky.
25:34
Just return true. Else if the 50 is less than the value at the middle door--
25:40
so if it's smaller than the middle door-- I want to search to the left. So I can say search left half. Else if 50 is greater than the middle door, I want to search to the right.
25:50
And I think that's almost everything, right? Is there a fourth possible case?
25:57
What else could happen?
26:03
Good. So taking into account that if there are no doors left or no doors to begin with, we better handle that case
26:09
so that we don't induce one of those spinning beach balls, so that the computer doesn't freeze or crash. There's really four possible scenarios in searching for information.
26:17
It's either in the middle or to the left or to the right. Or it's just not there at all. And so I sort of slip that in at the end because technically, that's a question
26:24
you should ask first because if there's no doors, there's no work to be done. But logically, this is the juicy part-- the other three questions
26:31
that you might ask yourself. So this then might be the pseudocode for binary search. And we could make it more technical.
26:37
And this is where it kind of escalates quickly syntactically. But I'm just using the same kind of syntax. If doors in my pseudocode represents an array of doors,
26:45
well, then doors bracket middle is just a pseudocode-like way of saying go to the middle door in that array.
26:51
And then notice, else if 50 is less than-- that middle value-- then search doors bracket 0, so the leftmost one--
26:59
through doors middle minus 1. So you don't need to waste time researching the middle door.
27:05
So I say middle minus 1 so that I scooch over slightly to the left, so to speak. Else if 50 is greater than the value at the middle door,
27:13
then you want to search 1 over to the right, so middle plus 1 among those doors, through the last door, which is not n,
27:21
because we start counting at 0, but n minus 1. And the rest of the algorithm is the same. This is just a little more precise.
27:27
And I dare say, when writing a program in C or any language, like, honestly, starting in pseudocode like this will generally make it
27:36
much easier to write the actual code. So in fact, in this and future problem sets, do get into the habit,
27:41
especially if you're struggling getting started-- just write things out in English and maybe high level English a little more like this.
27:47
Then as a version two, go in with your keyboard or paper, pencil. And make it a little more precise using some code-like syntax.
27:56
And then I dare say in version 3, you can now translate this pretty much verbatim to C code.
28:01
The only headache is going to be rounding issues with integers because if you divide an integer and you a fraction,
28:06
it's going to truncate, so all that kind of headache. But you can work through that by just thinking through what's going to get truncated when
28:12
you round down or up as a solution. Any questions, though, on this pseudocode
28:17
for either linear or binary search as we've defined them--
28:23
linear or binary search-- no? All right, well, let's consider then a bit more

## [Running Time](https://youtu.be/jZzyERW7h1A?t=1708)

28:28
formally a question that we'll come back to in the future in future classes as well. What is the running time of these algorithms?
28:35
What is, that is to say, the efficiency of these algorithms? And how do we actually measure the efficiency of an algorithm?
28:41
Is it with a stopwatch or with some other mechanism? Well, I propose that we think back to this picture here, whereby this, again, was representative of both the phone book
28:50
example from week zero and theoretically, bug aside, the attendance counting algorithm from earlier today, whereby
28:57
this same green line theoretically represents how much time it should have taken us as a group to count ourselves.
29:04
Why? Because if maybe another class comes in and doubles the size of the number of humans in this room, no big deal.
29:11
That's just one more step or one more iteration of the loop because half of the people would anyway sit down.
29:17
So this green algorithm still represents the faster theoretical algorithm today. And so recall that we described these things more mathematically as n.
29:26
So this was one page at a time or one person at a time. This was two people or two pages at a time.
29:33
So it's twice as fast, so if n is the number of people or pages and divided by 2 is the total number of steps.
29:38
And then this one got a little mathy, but log base 2 of n. And log base 2 of n just means what is the value when you take n and divide it
29:47
in two by 2 again and again and again and again until you're left with just one page or one person standing.
29:54
But in the world of running times, it turns out that being this precise is not that intellectually interesting.
30:00
And it sort of devolves into lower level math. It's just not necessary when having discussions about the efficiency of an algorithm or even code that you've written.
30:07
So generally, a computer scientist, when asked what's the running time of your algorithm or what's the efficiency of your algorithm or more
30:13
generally how good or bad is your algorithm, they'll talk about it being on the order of some number of steps.
30:20
This is a phrase you'll hear increasingly in computer science where you can kind of wave your hand at it. Like, oh, the lower level details don't matter that much.
30:27
All you care about in broad strokes are certain numbers that will add up the most.
30:32
And in fact, when computer scientists talk about the efficiency of algorithms, they tend to throw away constant factors, so literally, numbers like 2
30:43
that might be dividing here or a base here. So for instance, these two algorithms to a computer scientist
30:49
would sort be the same. Like, yeah, it's technically twice as fast. But look at the lines. I mean, they're practically the same and this one here too, log base 2-- sure.
30:57
But if you remember from math class, you can change the base of any logarithm from one number to another pretty easily.
31:03
So ah, let's just generalize it as log of n. It doesn't really matter fundamentally what the numbers actually are.
31:09
And honestly, if we zoom out slightly so that the y-axis and the x-axis
31:14
get even bigger, honestly, these first two algorithms really do start to resemble each other closer and closer.
31:21
And I daresay in your mind's eye, imagine zooming further and further and further out. Like, that red and yellow line are pretty much-- once n is large enough--
31:29
going to be functionally the same. Like, they're practically the same algorithm. But this one is still doing amazingly because it's
31:35
a fundamentally different shape. So this is to say when a computer scientist talks about, thinks about the efficiency of algorithms, we just throw away the constant terms
31:43
that when n gets really large just don't seem to matter as much. They don't add up as much or fundamentally
31:49
change the picture in a case like this. So what I'm describing here with this capital letter O has a technical term.
31:55
This is called big O notation. And this is omnipresent in computer science and often rears its head even in programming,
32:02
specifically when talking about the design of some algorithm. And this is a little cheat sheet here on the screen now.
32:07
Very often, algorithms that you write or you use will be describable as being on the order of one of these running times.
32:17
So n is just representative of the number of things-- number of people, number of pages-- whatever it is you're actually doing in code.
32:25
So the mathematical formulas inside of the parentheses describe as a function of the size of that input
32:33
how fast or slow the algorithm's going to be. So this algorithm in the middle here, big O of n, so to speak,
32:40
means that it takes linear time, in other words. So my first algorithm-- 1, 2, 3, 4--
32:47
or my first algorithm in week zero-- 1, 2, 3, 4. That was a linear search.
32:53
The number of steps it takes is on the order of n because if there's n pages, in the worst case, like, John Harvard's all the way at the end of the phone
33:00
book, so it takes me n steps. In this case, it's always going to take me n steps to count you all because if I want to point at each and every one of you,
33:06
that is always going to take me n steps. So big O represents an upper bound on the number of steps
33:13
that you might be counting. And so we often use it to consider the worst case and the worst case, John Harvard, or whoever might be all the way at the end of the phone
33:20
book. So that linear search is on the order of n. But what about n squared?
33:25
This means n people doing n things. So for instance, and we won't do this today,
33:30
but if we were to ask you again to stand up and shake everyone's hand in the room--
33:36
not good for health nowadays-- but shake everyone's hand in the room, how many handshakes would there be?
33:42
Well, if there's n of you and you've got to shake everyone else's hand, that's technically n times n minus 1.
33:48
Let's throw away the minus 1. That's n times n or n squared handshakes. That's a lot of handshakes.
33:54
And so the running time of shaking everyone's hand in the room to introduce yourself would be on the order of n squared.
34:00
At the other end of the spectrum, the faster end, big O of 1 doesn't mean that the algorithm takes literally one step.
34:07
It could take two steps or three or even 1,000 steps. But what it means is it's a constant number of steps.
34:14
So it doesn't matter how many people are in the room, this describes something taking just one step total
34:21
or a constant number of steps total. So for instance, earlier when everyone stood up at the same time,
34:26
that was constant time because if we had twice as many people come into the room, it's not going to take us twice as long to stand up
34:32
if everyone stands up at the same time. That would be a constant time algorithm. So this is linear.
34:38
This is constant. If you want to get fancy, this is quadratic. This is logarithmic. And this is n log n.
34:44
Or there's other fancier terms we can give it as well, but for now, just a common list of running times that we might apply to certain algorithms.
34:53
So linear search, I claim, is in big O of n because it's going to take in the worst case n steps.
34:58
What about binary search? How many steps does binary search take on the order of
35:05
according to this chart? Yeah? AUDIENCE: Log n. DAVID MALAN: Log n. Yeah, because no matter what with binary search, you're dividing in half,
35:14
half, half. But in the worst case, it might be in the last door you check.
35:19
But you only took log n steps to get there. But it still might be the last one you check. So binary search indeed would be on the order of log n.
35:26
But sometimes, you do get lucky. And we saw with our volunteers that sometimes you can get lucky and just find things quicker.
35:32
So we don't always want to talk about things in terms of an upper bound, like how many steps in the worst case might this algorithm take.
35:38
Sometimes it's useful to know in the best case how few steps might an algorithm take. So for that, we have this capital Greek omega, which
35:46
is another symbol in computer science. And whereas big O represents upper bound, omega represents lower bound.
35:53
And it's the exact same idea. It's just a different symbol to represent a different idea, the opposite, in this case.
35:58
So here's a similar cheat sheet here. But when you use the omega symbol, that just means that this algorithm might take as few as this many steps,
36:07
for instance, in the very best case. So by that logic, if I ask about linear search,
36:12
our first demonstration with the lockers, let's consider the best case. How many steps might it take to search n lockers
36:19
using linear search in the best case? You get lucky. So I heard it. Yeah, just one step.
36:24
So we could say that linear search is an omega of 1, so to speak. What about binary search?
36:30
If you've got n lockers, in the best case, though, how few steps might it take us?
36:35
Again, one, because we might just get lucky. And boom, it happens to be right there in the middle. So you could say that both linear search and binary search are an omega of 1.
36:46
Now, by contrast, my attendance algorithm, the first one I proposed-- 1, 2, 3, 4, 5, 6, 7, I claimed a moment ago that that's in big O of n
36:55
because if there's n people in the room, I've got to point at everyone. But equivalently, if there's n people in the room and I have to point at everyone, what's the fewest number of steps
37:03
it could take me to take attendance using this linear approach?
37:08
So still n, right, unless I guess, which is not an algorithm. Like, unless I guess, I'm not going to get the right answer,
37:14
so I kind of have to point at everyone. So in both the best case and the worst case, some algorithms still take n steps.
37:20
And for this, we have what we'll call theta notation, whereby if big O and omega happen to be the same, which is not always the case
37:28
but can be, then you can say that algorithm is in theta of such and such.
37:33
So my attendance-taking algorithm, the very first, 1, 2, 3, 4, all the way on up to n would be in theta of n
37:40
because in both the best case and the worst case, it takes the same number of steps as per my big O and omega analysis.
37:48
Now, there is a more formal mathematical definition for both of these. And if you take higher level computer science, you'll go more into the weeds of these ideas.
37:54
But for now, big O, upper bound. Omega, lower bound. Questions on this symbology?
38:03
It'll be a tool in our tool kit. No? OK, so with that said, let's see how we might translate this to actual code

## [search.c](https://youtu.be/jZzyERW7h1A?t=2294)

38:14
in something that makes sense now using C and not so much new syntax but applications of similar ideas from last time.
38:20
So for instance, let me actually go over to search dot C. And in search dot C, I'm going to go ahead and implement the idea of linear search,
38:27
very simply, using integers initially. So to do this, let me go ahead and give myself the familiar CS50 dot h
38:34
so that I can ask the human what number to search for. Then let me go ahead and include standard io.h
38:40
so that I can use printf and the like. Then I'm going to go ahead and do int main void without any command line
38:45
arguments because I'm not going to need any for this particular demonstration. And someone asked about this a while back.
38:50
If I want to declare an array of values but I know in advance what the values are, there is a special syntax I can use,
38:57
which is this. If I want a whole bunch of numbers but I want those numbers to be stored in an array, I can store them in--
39:04
using these curly braces. And I'm going to use the same numbers as the monopoly denominations that we've been playing with.
39:10
And I'm just going to put them in sort of random order. But I'm going to deliberately put the 50 all the way at the end just so that I know that it's going to try all possible steps, so big O of n,
39:19
ultimately. Now let's go ahead and ask the user for a value n. And we'll use get int.
39:24
And just ask the user for a number to search for, be it 50 or something else. And then here's how I might implement in code now linear search,
39:32
translating effectively the pseudocode from last time. For int i equals 0.
39:38
i is less than 7. i plus plus. And then inside of this loop, I can ask a question.
39:43
If the ith number in the numbers array-- so numbers bracket i-- equals, equals the number n
39:51
that I care about, well, this is where I could just declare return true or return false. Here, I'm going to go ahead and just use a printf statement.
39:58
And I'm going to say found, backslash n, just to know visually that I found the number. And else I might do something like this.
40:06
Else if that's not the case, I'll go ahead and print out not found backslash n.
40:13
All right, so let me zoom out for just a moment. Here's all of my code. Any concerns with this implementation of what I claim is now linear search?
40:25
Any concerns with what I claim is linear search? Yeah? AUDIENCE: [INAUDIBLE]
40:32
DAVID MALAN: Exactly. If I search the first number and it's not found, it's going to say not found.
40:37
But it's going to keep saying not found, not found, not found, which might be fine. But it's a little stupid. I probably want to know if it's found or not.
40:44
So I've made that same mistake that I called out earlier. Like, the else is not the alternative to not finding
40:49
the number in that first location. It's the final decision to make when I haven't actually found the value.
40:55
So I think what I want to do is get rid of this else clause. And then at the outside of this loop, I think
41:01
I want to conclude printf not found. But here too there's a new bug that's arisen.
41:08
There's a new bug, even though I fixed the logical error you just described. What symptom are we still going to see?
41:15
Yeah, now it's going to always print not found,
41:20
even when I have found it because even once I've found it and I finished going through the array, it's still going
41:26
to assume that I got to the bottom. And therefore, it's not found. So I need to somehow exit out of main prematurely, if you will.
41:32
And recall that last week, we also introduced the idea that main all this time does actually return a value, an integer.
41:39
By default, it's secretly been zero. Anytime a program exits, it just returns zero, an exit status of zero.
41:46
But we do now have control over that. And so a convention in C would be that when you want your main function to end prematurely if so,
41:54
you can literally just return a value. And even though this feels a little backwards, this is just the way it is.
41:59
You return zero to indicate success. And you return any other integer to indicate failure.
42:06
So by convention, people go to 1 and then 2 and then 3. They don't think too hard about what numbers to use.
42:11
But in this case, I'm going to go ahead and return 1 if I do get to the bottom of this file.
42:16
So now if I open back up my terminal window, I run make search. No syntax errors-- dot slash search.
42:23
I'm going to be prompted for a number. Let's go ahead and search for the number 50. And I should see found.
42:28
Meanwhile, if I run it again-- dot slash search-- I search for the number 13, that should be not found.
42:34
So I claim that this is now a correct implementation of linear search that's gone from left to right, looking for a number that may or may not
42:43
be there. Any questions on this version of the code here? Yeah?
42:49
AUDIENCE: [INAUDIBLE] DAVID MALAN: Return zero indicates success
42:55
when doing it from main in particular. And that's backwards only in the sense that generally 0 is false.
43:02
And 1 is true. But the logic here is that if the program works correctly, that's zero.
43:09
But there's an infinite number of things that can go wrong. And that's why we need 1 and 2 and 3 and 4 and all the way up.
43:15
Other questions? AUDIENCE: [INAUDIBLE] DAVID MALAN: Yes.
43:21
AUDIENCE: [INAUDIBLE] DAVID MALAN: Correct. When you return zero or return any value from main wherever it is in your code,
43:31
the program will effectively terminate right then and there. No additional code will get executed at the bottom of the function.
43:37
You'll effectively exit out. Just like in a normal function that isn't main, when you return a value,
43:43
it immediately exits that function and hands back the value. Yeah? AUDIENCE: [INAUDIBLE]
43:49
DAVID MALAN: So return 1 is just me being pedantic at this point because I'm frankly not going to really care what
43:56
the exit status is of this program. But once I've introduced the idea of manually returning 0 on this line 14
44:03
to indicate success, it stands to reason that I should also return a different value when I want to indicate failure.
44:10
And so even though this does not functionally change the program-- it will still work-- it will still print the same things correctly-- it's a lower level detail
44:19
that programmers, teaching assistants, testing software, might appreciate, knowing what actually happened
44:24
in the program underneath the hood. All right, so what about strings?
44:30
So it turns out with strings, we're going to have to think a little harder about how best to do this.
44:35
So let me actually go ahead and do this. Let me go ahead and get rid of much of this code but transition
44:41
to a different type of array, this time an array of strings. And I'm going to call the array strings itself plural, just to make clear
44:47
what's in it instead of numbers. I'm going to use the square bracket notation, which just means I don't know at the moment how many elements it's going to have.
44:54
But the compiler can figure it out for me. And in the spirit of Monopoly, let's go ahead in our curly braces, do something like this.
45:00
Battleship is going to be one of the strings. Boot is going to be another. Cannon is going to be a third.
45:07
Iron is going to be the fourth. Thimble-- and if you've ever played Monopoly, you know where these are coming from-- and top hat, for instance.
45:14
So this gives me 1, 2, 3, 4, 5, 6. I could write the number 6 here. And the compiler would appreciate it.
45:20
But it doesn't matter. The compiler can figure it out on its own just based on the number of commas. And this also ensures that I don't write one number to the left
45:28
and then miscount on the right. So omitting it is probably in everyone's benefit. Now let's do this.
45:33
Let's ask the user for a string using get string instead of get int for some string to search for.
45:40
Then let's go ahead and do the exact same thing. For i int i equals 0.
45:46
i is less than 6, which is technically a magic number. But let's focus on the searching algorithm for now.
45:53
i plus plus. And then inside of this loop, let's do this. If strings bracket i equals equals, s, then let's go ahead
46:04
and print out just as before, quote, unquote, found-- backslash n-- and proactively return zero this time.
46:10
And if we don't find it anywhere in the loop, let's go ahead and return 1 at the very bottom, before which we will print not found backslash n.
46:17
So it's the exact same logic at the moment, even though I've changed my ints to strings.
46:23
Let me go ahead and open up my terminal window now. Do make search again and see, OK, so far, so good.
46:30
Let me now go ahead and do dot slash search. And let's go ahead and search for-- how about top hat.
46:37
So we should see found. Huh. All right, not found. All right, well, let's do dot slash search again.
46:43
How about thimble? Maybe it's because it's just two words. No, thimble's not found, either.
46:50
Dot slash search-- let's search for the first one, battleship. Enter-- still not found.
46:55
Let's search for something else like cat. Not found. What is going on because I'm pretty sure the logic is exactly the same?
47:03
Well, it turns out in C, this line here, currently line 11,
47:09
is not how you compare strings. If you want to compare strings in C, you don't do it like you did integers.
47:15
You actually need another technique altogether. And for that, we're going to need to revisit one of our friends, which
47:21
is string.h, which is one of the header files for the string library that we introduced last week that has in addition to functions
47:27
like strlen, which gives you the length of a string, it also gives us, as per the documentation here, another function that we'll
47:34
start to find useful here, succinctly named strcmp, for string compare. And string compare will actually tell us if two strings are the same or not.
47:44
It will indeed compare them. And if I use this now, let me go back to my code
47:49
here and see what I might do differently if I go back into my code here and change this value.
47:55
Instead of using strings bracket i equals, equals s, let's do str compare. And I read the documentation earlier.
48:01
So I know that it takes two arguments, the first and the second string that you want to compare, so strings bracket i and then s,
48:09
which is the string that the human typed in. But somewhat weirdly, what I want to check for
48:15
is that str compare returns zero. So if str compare when given two strings is input, strings bracket i and s,
48:24
returns an integer 0, that actually means the strings are the same.
48:30
So let's try this. Let me do make search again. Huh. What did I do wrong here?
48:36
A whole bunch of errors popped out. What did I do wrong? Yeah?
48:41
Yeah, so I didn't include the very header file we're talking about. So again, it doesn't necessarily mean a logical error. It just means a stupid error on my part.
48:47
I didn't actually include the header file. So let me go back and actually do that. Up at the top in addition to cs50.h and standard io,
48:54
let's also include string.h. Let me clear my terminal and do make search again.
48:59
Crossing my fingers. That time it worked. And now if I do dot slash search and search for top hat like before,
49:06
now, thankfully, it is, in fact, found. If I do it once more and search for battleship, now it's, in fact, found.
49:12
If I do it once more and search for cat, which should not be in there, that is not, in fact, found.
49:17
So now just intuitively, even if you've never done this before, why might it be valuable for this function called strcmp
49:25
to return zero if the strings are equal as opposed to a simple Boolean like true or false, which might have been your intuition?
49:34
When you compare two strings, what are the possible takeaways
49:40
you might have from comparing two strings? It's not just that they're equal or not.
49:45
AUDIENCE: [INAUDIBLE] DAVID MALAN: OK, so maybe if the ASCII values are the same, that
49:51
might imply, indeed, literal equality. But something else. AUDIENCE: [INAUDIBLE] about how similar these things are [INAUDIBLE]..
49:58
DAVID MALAN: Ah, nice. Like, you and I in English, certainly, are very much in the habit of sorting information, whether it's in a dictionary, in our contacts, in a phone book, in any such technology.
50:06
And so it's often useful to be able to know, does this string equal another? Sure.
50:11
But does this string come before another alphabetically or maybe after another alphabetically?
50:17
So sometimes, you want functions to give you back three answers. But equals, equals alone can only give you true or false, yes or no.
50:24
And that might not be useful enough when you're trying to solve some problem involving strings. So it turns out str compare actually compares the two strings for equality
50:34
but also for what's called, playfully, ASCII-betical order. So not alphabetical order, per se, but ASCII-betical order
50:41
where it actually compares the integer values of the letters. So if you're comparing the letter A, It's going to compare 65 against some other letter's integer value-- hence
50:51
ASCII-betical value. So we're not doing any form of sorting here. So it's sort of immaterial. But as per the documentation, I do know that str compare
50:59
returns zero if two strings are equal. And a little teaser for next week, it turns out when I was only using equals,
51:06
equals to compare strings bracket i and s, I was not comparing the strings in the way that you might have thought.
51:13
And if you have programmed in Java or Python before, equals, equals is actually doing something different in those languages
51:20
than it is actually doing in C. But more on that next week. For now, just take on faith that str compare is indeed
51:26
how you compare two strings. So let's actually put this into play with some actual additional code.

## [phonebook.c](https://youtu.be/jZzyERW7h1A?t=3093)

51:33
Let me propose that we implement a very simplistic phone book, for instance. Let me go ahead and implement here--
51:40
how about in a new file. Instead of search dot C, let's actually do phone book dot c.
51:46
And in this phone book, I'm going to go ahead and include the same header file, so cs50.h, so I can get input--
51:52
standard io.h, so I can use printf-- string.h so that I can use str compare.
51:58
Let me give myself a main function again without command line arguments for now. And let me go ahead now and store a proper phone book, which
52:05
has some names and some actual numbers. So let's store the names first. So string-- names is going to be the name of my array.
52:12
And let's go ahead and store Carter's name, how about my name, and maybe John Harvard for phone book throwback.
52:18
Then let's go ahead and give me another array called numbers wherein I'll put our phone number, so 617-495-1000 for Carter--
52:27
617-495-1000 for me-- technically, directory assistance here. And then for John, we'll give him an actual one.
52:34
So it's actually going to be 949-468-2750.
52:40
You're welcome to text or call John when you want. Whoops. And just for good measure, let's go ahead and put our country codes
52:46
in here plus 1, even though at the end of the day, these are strings. So indeed notice I'm not using an integer for these values.
52:54
I kind of sort of should. But here's where data types in C and programming more generally might sometimes mislead you.
53:01
Even though we call it, obviously, a phone number. It's probably best to represent it generally as strings, in fact,
53:08
so that you can have the pluses-- you can have the dashes so that it doesn't get too big and overflow an integer.
53:14
Maybe it's an international number for which there's even more digits. You don't want to risk overflowing a value. And in general, the rule of thumb in programming
53:20
is even if in English we call something a number, if you wouldn't do math on it ever, you should probably be storing it
53:26
as a string, not as an integer. And it makes no logical sense to do math on phone numbers, per se.
53:33
So those are best instinctively left as strings. And in this case, even more simply, this ensures that we have pluses and dashes stored inside of the string.
53:41
All right, so now that I have these two arrays in parallel, if you will. Like, I'm assuming that Carter's name is first.

## [Structs](https://youtu.be/jZzyERW7h1A?t=3229)

53:49
So his number is first. David's name is second. So his number is second. John's is third and thus third.
53:54
So let's actually search this. Let's ask the user for-- how about a name using get string.
54:01
And this will be a name to search for in the phone book just like we did in week zero. Let's do for int i equals 0, i less than 3.
54:09
Again, the 3 is bad practice. I should probably store that in a constant. But let's keep the focus for today on the algorithm alone--
54:15
i plus, plus. Then in here, let's do if-- how about names bracket i equals, equals name typed in.
54:27
But wait a minute. I'm screwing this up again. What should I be using here? str compare again-- so let's do str compare, names bracket i comma,
54:37
name, which came from the user. And if that return value is zero, then let's go ahead
54:42
and print out, just like before, found backslash n. But you know what? We can do something more interesting.
54:48
Let's actually print out the number. So I didn't just find something. I found the name. So let's actually plug in that person's corresponding number.
54:55
So now it's a more useful phonebook or contacts app where I'm going to show the human not just found but found this specific number.
55:02
Then I'm going to go ahead as before and return 0 to indicate success. And if we get all the way down here, I'm going to go ahead and say not found
55:09
and not print out any number because I obviously haven't found one, and return one by convention to indicate failure.
55:15
So let me open my terminal window. Let me do make phone book-- enter. So far, so good-- dot slash phone book.
55:23
Let's search for Carter-- enter-- found his number. Let's do it again. Dot slash phone book--
55:28
David-- found it. Let's do it one more time for John-- found it. And just for good measure, let's do one other here like Eli--
55:38
enter-- not found in this case. All right, so it seems to be working based on this example here.
55:43
But now we've actually implemented the idea of, like, a proper phone book. But does any aspect of the design of this code,
55:51
even if you've never programmed before CS50, does anything rub you wrong about how we're storing our data--
55:58
the phone book itself-- these names and numbers? Does anything rub you the wrong way?
56:04
Yeah, in back. AUDIENCE: [INAUDIBLE]
56:09
DAVID MALAN: Yeah, really good observation. I'm separating the names and the numbers,
56:15
which indeed, it looks a little bit weird. And there's actually this technical term in the world of programming,
56:20
which is code smell, where, like-- [SNIFFING]---- something smells a little off about this code in the sense that, like, this probably doesn't end well, right?
56:27
If I add a fourth name, a fourth number, a fifth name, a fiftieth name and number, like, at some point, they're probably
56:33
going to get out of sync, right? So, like, there's something awry about this design that I shouldn't decouple the names from the numbers.
56:39
So something kind of smells about this code, so to speak. And any time you perceive that in your code, it's probably an opportunity to go about improving it somehow.
56:48
But to do that, we actually need another tool in the toolkit. And that is, again, this term that I've used a couple of times--
56:53
data structures. Like, arrays have been the first of our data structures. And they're so simplistic. It just means storing things back to back to back contiguously in memory.
57:01
But it turns out C-- and a little bit of new syntax-- but it's not a lot of new syntax today--
57:06
a little bit of new syntax today will allow us to create our own data structures, our own types of variables,
57:13
largely using syntax we've seen thus far. So to do this, let me propose that in order
57:19
to represent a person in a phone book-- well, let's not just implement them as a list of names and a list of numbers.
57:26
Wouldn't it be nice if C had a data type actually called person? Because if it did, then I could go about creating an array called--
57:34
using the pluralized form-- people-- containing my people in my phone book.
57:40
And maybe a person has both a name and a number. And therefore, we can kind of keep everything together.
57:46
So how can I do this? Well, what is a person? Well, a person, really, in this story is a person has a name.
57:52
And a person has a number. So can we create a new data type that maybe has both of these together?
57:58
Well, we actually can by using one piece of new syntax today, which is just this here.
58:05
Using what's called a struct, we can create our own data structure that actually has some structure in it.
58:11
It's not just one thing like a string or an int. Maybe it's two strings. Maybe it's two ints. Maybe it's one of each.
58:16
So a structure can be a variable that contains any number of other variables,
58:21
so to speak. And typedef is a cryptic keyword that just means define the following type-- invent the following data type for me.
58:28
And the syntax is a little weird. But you say typedef struct curly brace. Inside of the curly braces, you put all of the types
58:35
of variables you want to associate with this new data type. And then after the curly brace, you invent the name
58:40
that you want to give it. And this will create a new data type in C called person, even though no one thought of this decades
58:47
ago when C was created alongside of the ints and the floats and so forth. So how can I actually use this?
58:55
Well, it turns out that once you have this building block of creating your very own data structures, I can go back into my code
59:03
and improve it as follows in direct response to your concern about it seeming not ideal that we're decoupling the names and the numbers.
59:10
Now, it's going to look a little more complicated at first. But it will scale better over time. So within my code here, I'm going to go ahead
59:17
and essentially type out exactly that same data type. So define a structure that has inside of it a string called name and a string
59:27
called number. And let's call this thing a person. So these new lines copied and pasted from the slide a moment ago just
59:34
invent the data type called person. So the only thing we need today is the syntax via which we can set a person's name and number-- like, how can we access those values.
59:43
So to do this, I'm going to go ahead and erase the hard-coded arrays that I had before.
59:49
And I'm going to give myself one array of type person called people with room for three people.
59:55
So this seems like a bit of a mouthful. But the new data type is called person. The array name is called people, which in English is weird.
1:00:02
I mean, it could call it persons to make it a little more parallel. But we call them people, generally. And I want three such people in my phone book.
1:00:09
Now, how do I actually initialize those people? Well, previously, I did something like this-- names, bracket, 0.
1:00:16
And then I did numbers, bracket, 0. Well, it's a similar idea. I do people, bracket, 0.
1:00:22
But if I want to set this person's name, the one new piece of syntax today is a period, a literal dot operator, that says go inside of this person
1:00:32
and access their name field or their name attribute. And set it equal to, quote, unquote, "Carter."
1:00:39
Then go into that same person. But go into their number field. And set that equal to plus 1, 617-495-1000.
1:00:48
Then-- and I'll just separate it with white space for readability-- go into people bracket 1.
1:00:53
Set their name into mine, David. Let's go into people bracket 1 number. Set that equal to the same, since we're both available through the directory,
1:01:02
so 617-495-1000. And then lastly, let's go ahead and do people bracket 2 dot name equals,
1:01:10
quote, unquote, "John," and then people bracket 2 dot number equals, quote, unquote, "plus 1, 949-468-2750--
1:01:21
let me fix my dash-- semicolon. And now I think I can mostly keep the rest of the code the same
1:01:29
because if I'm searching for this person's name, I think the only thing I want to change is this because I don't have a names
1:01:35
array anymore. So what should I change this highlighted phrase to in order
1:01:40
to search the ith person's name? What should this be?
1:01:45
Yeah? People bracket i dash name because the whole point of this loop
1:01:51
is to iterate over each of these people one at a time. So people bracket i gives me the ith person-- first [INAUDIBLE] people 0,
1:01:57
people 1, people 2. But if on each iteration, I want to check that person's name and compare it against whatever the human typed in,
1:02:04
now I can do exactly that. But I have to change the output to be people bracket i dot number,
1:02:12
in this case. So I've added a little bit of complexity. And granted, this is not going to be the way long term you create a phone book.
1:02:19
Odds are, we're going to get the phone book with a loop of some sort. We're going to use a constant, so I know how many people I have room for.
1:02:24
For demonstration sake, I'm just typing everything out manually. But I think logically now, we've achieved the same thing.
1:02:30
So let me do make phone book for this new version-- no syntax errors-- dot slash phone book. Let's search for Carter-- enter.
1:02:36
And there indeed is his number. Let's go ahead and search for David. There's my number. And lastly, let's search for John--
1:02:42
his number. And again, we'll search for someone we know is not there-- Eli. And Eli is not found.
1:02:47
So what we've done is try to solve this problem of introducing a brand new data type that allows us to represent this custom data that you and I just
1:02:57
created. And that is by using the struct keyword to cluster these things together and the typedef keyword to give it a brand new name that we might like.
1:03:05
Now, as an aside, when it comes to styling your code, you'll actually see that style50 and similar tools will actually
1:03:11
put the name of the data type on the same line as the closing curly brace, just sort of a curiosity. That's fine.
1:03:16
Even though I wrote it the first way for consistency with Scratch and our prior examples, this is the right way in styling it.
1:03:23
Any questions now on this data type? Yeah?
1:03:29
AUDIENCE: [INAUDIBLE]
1:03:34
DAVID MALAN: The question is, do you have to assign both the name and the number when creating a person? Or can you only get away with assigning one of them?
1:03:42
You can. But that's going to be one of those so-called garbage values, typically. And so there's just going to be some bogus data there.
1:03:48
And unless you are so careful as to never touch that field thereafter, you probably run the risk of some kind of bug, even a crash in your code,
1:03:56
if you try to access that value later, even though you've never initialized it. So yes, it's possible. But no, do not do that.
1:04:02
Other questions? No? All right, well, now that we have the ability
1:04:08
to sort of represent more interesting structures, up until now, we've sort of assumed that in order to get to binary search,
1:04:14
we have a phone book that someone already sorted for us. For our second demonstration with our volunteers,
1:04:19
we assumed that someone, Carter in that case, had already sorted the information for us. It was proposed by the audience that, well,
1:04:26
what if we sort the information first and then go find the number 50? That invited the question even early on-- well, how expensive is it to sort?
1:04:33
How much time and money and inefficiency do Google and Microsoft and others spend to keep their data and our data sorted?
1:04:41
Well, let's consider what the problem really is. If this is how we represent any problem, the unsorted data
1:04:47
that we might consume by typing things in randomly to a search engine or crawling the internet or just adding context in any old order to our phone
1:04:54
is arguably unsorted. It's certainly not alphabetically sorted by default. But we want to get it sorted.
1:04:59
And so somewhere in here in this black box, we need a set of algorithms for actually sorting information as well.
1:05:05
For instance, if we have these integers here unsorted-- 72541603-- effectively random, the problem of sorting, of course,
1:05:14
is to turn it into 01234567 instead. And there's a bunch of different ways to do this.
1:05:20
But before we do that, I think it's probably time for some brownies. So let's go ahead and take a 10-minute break. And we'll see you in 10.

## [Sorting](https://youtu.be/jZzyERW7h1A?t=3926)

1:05:26
All right, we are back. And where we left off was this cliffhanger. We've got some unsorted numbers.
1:05:32
We want to make them sorted. How do we do this? And at the risk of one too many volunteers,
1:05:37
could we get eight more volunteers? Wow, OK, overwhelming. OK, how about 1, 2, 3, 4.
1:05:45
How about all three of you? OK, 5, 6, 7--
1:05:51
OK, 8. Come on. All right, one from each section-- all right, come on down. [INTERPOSING VOICES]
1:06:00
DAVID MALAN: All right, come on down.
1:06:05
Thank you. And if you all could grab a number here.
1:06:10
So you'll be 7. Stand on the left there if you could. All right, you'll be number 2. Stand to his left.
1:06:17
OK, keep coming. OK, yeah. OK, here we go.
1:06:24
There you go. OK, [INAUDIBLE] 0 and 3. OK, so let's just make sure they match what we've got there.
1:06:31
Good so far. OK, so we have eight volunteers here, an array of volunteers, if you would. This time, we've used eight rather than seven.
1:06:38
We deliberately had seven lockers just so that the divide by 2 math worked out. That was very deliberate that there was always a [INAUDIBLE] a middle,
1:06:44
a middle, a middle. In this case, it doesn't matter because we're going to focus on sorting. But first, how about some introductions from each group?
1:06:51
AUDIENCE: I'm Rebecca. I'm a first year in Pennypacker. And I'm thinking about studying environmental science
1:06:56
and public policy. [CHEERING] DAVID MALAN: Nice. [APPLAUSE] AUDIENCE: I'm [? Mariella. ?] I'm also in Pennypacker.
1:07:02
I'm a first year. And I'm thinking of studying bioengineering. DAVID MALAN: Wonderful. AUDIENCE: My name's [? Haron ?] [? Li. ?] I'm a freshman in Matthews.
1:07:09
I'm planning on studying applied mathematics. DAVID MALAN: Nice-- Matthews. AUDIENCE: My name is Emily. I'm a first year in Canada.
1:07:15
And I'm still deciding what to study. DAVID MALAN: Fair. AUDIENCE: My name's [? Tanai. ?] I'm a first year from Toronto.
1:07:21
And I'm planning on studying ECON and CS. DAVID MALAN: Nice. AUDIENCE: My name is Teddy.
1:07:26
I'm a first year in Hurlbut. And I'm planning on concentrating in computer science with linguistics. DAVID MALAN: Nice.
1:07:31
AUDIENCE: Yeah! DAVID MALAN: Nice. [APPLAUSE] AUDIENCE: My name's [? Lenny. ?] I'm a first year in Matthews.
1:07:36
And I'm planning on concentrating in gov and CS. DAVID MALAN: Ah, nice. [CHEERING] [APPLAUSE] And?
1:07:41
AUDIENCE: My name is Eli. I'm a first year in Hollis. And I plan on concentrating in CS. DAVID MALAN: Eli, we keep looking for you today.
1:07:47
OK, so if you guys could scooch a little bit this way just to be a little more centered. Notice that this array of volunteers is entirely unsorted.
1:07:54
So we thought we'd do three passes at this. Could you all sort yourselves from smallest to largest?
1:08:00
Go.
1:08:06
All right, that was very good. So yes, so, sure. OK. [CHEERING] [APPLAUSE]
1:08:12
And let's see. What was your algorithm? AUDIENCE: I just kind of found the person that
1:08:19
was, like, one lower or one higher. So I looked at him. He had 2. So I knew I had to be on his left. And then she had 3.
1:08:25
So I told her to come to my right. And then I knew he had 5. DAVID MALAN: OK, nice-- pretty clever. And how about your algorithm?
1:08:31
AUDIENCE: Same thing-- looked for the number that was lower and higher and found the middle. DAVID MALAN: OK, interesting, because I think from the outside view,
1:08:38
it all seemed very organic. And things just kind of worked themselves out, which is fine. But I dare say what you guys did was probably a little hard for me
1:08:44
to translate into code. So let me propose that we take two passes at this. If you could reset yourselves to be in that order from left
1:08:51
to right, which is just the exact same sequence, just so that we're starting from the same point each time.
1:08:58
[INAUDIBLE] Very good. All right, so let me propose this. We can approach sorting in a couple of different ways.
1:09:04
But it needs to be methodical. Like, it needs to translate ideally to pseudocode and eventually code.
1:09:09
So as much as we can quantize things to be step by step, I think the better this will scale overall,
1:09:15
especially when there's not eight people but maybe there's 80 people or 800. Because I dare say that if we had everyone in the room sort themselves--
1:09:22
if they were all handling a number-- like, that probably wouldn't have worked out very well. It probably would have taken forever because there's just so much more data.
1:09:29
So let's be a little more methodical. So for instance, I don't have a bird's eye view of the numbers just as before because even though we don't
1:09:35
have doors in front of our volunteers, they're effectively lockers too. And the computer or the human in my case can only look at one door at a time.
1:09:42
So if I want to find the smallest number and put it where it should go on the left, I can't just take a step back and be like, OK, obviously, there's the one.
1:09:49
I have to do it more methodically. So I'm going to check here-- 7. At the moment, this is actually the smallest number I've seen.
1:09:55
So I'm going to make mental note of it. OK, 2 I see now. I can forget about the 7 because 2 is clearly smaller.
1:10:01
5-- I don't need to remember it. 4-- I don't need to remember it. 1-- OK, that's clearly smaller.
1:10:06
Have I found my smallest number? Not even because there actually is a 0. So I should go through the whole list.
1:10:11
But I will remember that my smallest element is now 1. 6 is not smaller-- oh, 0 is smaller, so I'll remember this.
1:10:18
3 is not smaller. And so now, our volunteer for 0-- what was your name? AUDIENCE: [INAUDIBLE]. DAVID MALAN: Mariana, and where should we put you clearly?
1:10:26
So there. But what's your name again? AUDIENCE: [INAUDIBLE] DAVID MALAN: Eli's in the way. So we could have Mary Ellen?
1:10:31
AUDIENCE: [INAUDIBLE] DAVID MALAN: [? Mariella ?] just go to the right of Eli. But that's kind of cheating, right?
1:10:37
Because if this is an array, recall that they are contiguous. But there could be other stuff in memory to the left and to the right.
1:10:43
So that's not quite fair. We can't just have the luxury of putting things wherever we want. But Eli, you're not even in the right order, anyway.
1:10:49
So why don't we just swap you two. So [? Mariella ?] and Eli swap. But now I've taken one bite out of this problem.
1:10:55
I've coincidentally made it a little better by moving Eli closer to where he is. But you know what?
1:11:01
He was in a random location, anyway. So I don't think I made the problem any worse, fundamentally. Now I can do this again.
1:11:06
And I can shave a little bit of time off of it because I don't need to revisit [? Mariella ?] because if she was the smaller and I've already selected her from the array,
1:11:14
I can just move on and take one fewer bites this time around. So 2 is the smallest number, not 5, not 4.
1:11:20
OK, 1 is the smallest number. So I'm going to remember that as with a mental variable- 6, 7, 3.
1:11:27
OK, 1 is the smallest. So let me select number 1. And we're going to have to evict you, which is making the problem slightly worse.
1:11:34
But I think it'll average out. And now 0 and 1 are in the right place. So now let me do this again but faster.
1:11:40
So 5-- OK, 4-- 2 is the smallest-- 6, 7, 3. OK, 2, let's put you where you belong, evicting 5.
1:11:48
Now I can skip all three of these volunteers. OK, 4, is the smallest. Nope. Nope. Nope.
1:11:53
3, you're the smallest. Let me evict 4. All right, and now let me move in front of these volunteers.
1:11:59
5, 6, 7, 4, come on back. All right, and now let's select 6, 7, 5.
1:12:04
OK, come on back. Oh, no, no cheating, Eli. OK, and then let's see. 5, 7, 6-- OK, 6, come on back.
1:12:13
OK, now you have to move. OK, and now we've selected in turn all of the numbers from left to right.
1:12:18
And even though that did feel slower-- I was doing it a little more verbally as I stepped through it-- but I dare say we could translate that probably more to code.
1:12:25
Why? Because there's a lot of, like, looping through it and probably a lot of conditionals just asking the question, is this number smaller than this one or conversely greater than this other one.
1:12:34
All right, let's do this one more time. If you guys could reset yourselves to this ordering.
1:12:41
All right, so we again have 72541603.

## [Selection Sort](https://youtu.be/jZzyERW7h1A?t=4366)

1:12:46
Good. So how about this? I liked the intuition that they originally had, funny enough, whereby they just kind of organically
1:12:53
looked to the person to the left and to the right and kind of fixed the problem. So if they were out of order, they just kind of swapped locally adjacent
1:12:59
to each other. So let's try this. So 7 and 2, you're clearly out of order. So let's swap just you two.
1:13:05
7 and 5, you're out of order. Let's swap you two. 7 and 4, let's swap you two. 7 and 1, let's swap you two.
1:13:12
7 and 6, let's swap you two. 7 and 0, swap you two. 7 and 3, swap you two.
1:13:18
OK, that was a lot of swapping. But notice what happened. I'm not done, clearly. It's not sorted yet.
1:13:24
But I have improved the situation. How? Who is now definitely in the right place?
1:13:29
So, 7-- or Eli has wonderfully bubbled all the way up to the top of the list, so to speak.
1:13:35
Now I can actually skip him moving forward. So that takes one bite out of the problem. Let's do this again. 2 and 5 are OK.
1:13:40
5 and 4, let's swap. No, over there. [LAUGHS] Thank you. 5 and 1, let's swap.
1:13:46
5 and 6 are good. 6 and 0, let's swap. 6 and 3, let's swap.
1:13:52
And we don't have to worry about Eli. And now, what's your name again? AUDIENCE: [? Haron. ?] DAVID MALAN: [? Haron-- ?] we don't have to worry about him either as well.
1:13:57
So now I can go back to the beginning. And even though it feels like I'm going back and forth a lot, that's OK because the problem's still getting better and better.
1:14:05
I'm taking a bite out of it each time. 2 and 4 are good. 4 and 1, let's swap. 4 and 5 are good.
1:14:11
5 and 0, swap. 5 and 3, swap. And now these three are in the right place. Let's do it again.
1:14:16
2 and 1-- ah, here we go. Let's swap. 2 and 4 are OK. 4 and 0, swap. 4 and 3, swap.
1:14:22
Now, these four are OK. 1 and 2, you're good. 2 and 0, swap. 2 and 3, you're good.
1:14:27
You're good. OK, now 1 and 0, swap-- 1 and 2 and now 0 and 1.
1:14:33
A round of applause if we could for our volunteers. [APPLAUSE] [CHEERING]
1:14:38
So if you want to put your numbers on the tray there, we have some lovely Super Mario Oreos today, which
1:14:44
maybe drives a lot of the volunteerism. But here we go. Thank you all so much.
1:14:51
And maybe, Carter, if you can help with the reset? All right, here we go. [INAUDIBLE] yes, all set.
1:14:57
Thank you very much. Thank you. Thank you, guys. Thank you, yes.
1:15:04
To recap, let's actually formalize a little more algorithmically what we did.
1:15:09
And I deliberately kind of orchestrated things there to show two fundamentally different approaches, one where I kind of selected the element I wanted again and again
1:15:18
on the basis of how small it was. I looked for the smallest, then the next smallest, and so forth. The second time around, I took a different approach
1:15:24
by just fixing local problems. But I did it again and again and again until I fixed all of the minor problems.
1:15:30
And frankly, what they did organically at the beginning was probably closer to the second algorithm than the first,
1:15:36
even though I'm not sure they would write down the same pseudocode for it. The first algorithm we executed is actually called selection sort.
1:15:43
And I deliberately used that vernacular of selecting the smallest element again and again to evoke this name of the algorithm.
1:15:50
So for instance, when we had these numbers here initially unsorted, I kept looking again and again and again for the smallest element.
1:15:58
And I don't know a priori what the smallest number is until I go through the list at least once.
1:16:04
Then I can pluck out the 0. I then go through the list a second time to pluck out the 1, a third time
1:16:10
to pluck out the 2. Now, this assumes that I don't have an infinite amount of memory because even though I kept repeating myself looking for the next smallest
1:16:17
element, next smallest element, I propose that I only keep track of one number at a time, one variable in my mind, which
1:16:25
was the smallest element I have seen thus far. If I used more memory, I could probably remember from the first pass
1:16:32
where the 2 is, where the 3 is. But that's a different algorithm. And it would take more space, more memory.
1:16:37
I was confining myself to just one variable in my approach. So here might be the pseudocode for what we'd call selection
1:16:44
sort, the very first algorithm that we all did together, not organically, but more methodically as a group.
1:16:50
I would propose that we use some syntax from C when we talk about the loop and say for i from 0 to n minus 1.
1:16:57
Now, why is that? Well, if there were n people or 8, 0 through 7
1:17:02
are the indexes or indices of those humans on stage from left to right. So what did I have myself do?
1:17:08
Find the smallest number between numbers bracket i and numbers bracket
1:17:15
n minus 1. So when the loop starts at 0, this is literally
1:17:20
saying between numbers bracket 0 and numbers bracket n minus 1.
1:17:25
So from the far left to the far right, find me the smallest number. Then swap that number with numbers bracket i.
1:17:34
So that's why we evicted the person all the way over to the right or your left the very first time,
1:17:39
and then the next person, and the next person, and so forth. So this is an algorithm that has us go back and forth, back and forth,
1:17:46
iteratively selecting the smallest element. So if we generalize this now, not away from eight people to, like, n people,
1:17:53
you can think of them as representing an array, a.k.a. doors like this where the leftmost one is 0, the rightmost one is n minus 1,
1:18:01
second to last is n minus 2, and so forth if we don't know or care what n specifically is.
1:18:06
So how many total steps does selection sort perhaps take?
1:18:11
And let's make this a little more real here. Let me actually open up, for instance, a quick visualization here.
1:18:17
And on the screen here, you'll just see now an artist's rendition of an array of values whereby tall purple bars
1:18:24
represent big integers. And short purple bars represent small integers. So the idea of any sorting algorithm here as visualized
1:18:31
is to get the small bars on the left and the big bars on the right. And this is a nice handy tool that lets you play around with different algorithms.
1:18:37
So here is selection sort that I've just clicked. In pink again and again is the equivalent
1:18:42
of me walking through the volunteers looking for the next smallest element. And as soon as I found them, I swapped them into their leftmost location,
1:18:50
evicting whoever's there in order to gradually sort this list from left to right.
1:18:56
And so as you can see here, it holds very briefly in pink whatever the currently smallest element it has found is.
1:19:03
That's the analog of, like, me pointing to my head whereby it's constantly comparing, comparing, comparing,
1:19:09
looking for the next smallest element. Now, I'm kind of stalling because I'm running out of intelligent words
1:19:15
to say. But that is to say, this algorithm feels kind of slow. Like, it seems to be doing a lot of work.
1:19:20
Where is the work coming in? Like, what is it doing a lot of specifically?
1:19:26
Yeah? Yeah, it keeps going back and forth and back and forth. And even though it's shaving a little bit of time,
1:19:31
right, because it doesn't have to stupidly go all the way back to the beginning, and I was saving myself a few steps, like, it's a lot of cyclicity again and again and again.
1:19:38
And put another way, it's a lot of comparisons again and again. And some of those comparisons you're doing multiple times
1:19:44
because I only remembered one element at a time in my head. So I have to kind of remind myself on every pass which
1:19:50
is smallest, which is smallest. So this invites the question how fast or how slow or equivalently
1:19:57
how efficient or inefficient is something like bubble-- selection sort.
1:20:03
Well, let's actually consider how we could analyze this as follows. So if we have n numbers that we want to sort,
1:20:12
how many comparisons do we do the first time? Well, if there's n numbers, you can only make n minus 1 comparisons.
1:20:19
Why? Because if we have eight people here and we started with whoever's all the way over here, we compare this person against seven others-- n minus 1 if n is 8.
1:20:27
So the first pass through the list, I made n minus 1 comparisons. But that put the smallest number 0 in place.
1:20:34
The second time I walked across our eight volunteers, I didn't need to walk in front of all eight. I could shave off a little bit and do seven of them,
1:20:41
then six, then five, then four. So if I were to write this out roughly mathematically, I could do this-- n minus 1 plus n minus 2 plus n minus 3 plus
1:20:50
dot, dot, dot, all the way down to my very last comparison at the end of the list. Now, this is the kind of thing that typically in high school
1:20:57
you'd look at the back of the math book or physics book that's got a little cheat sheet for all of the formulas that add up.
1:21:02
This series here, let me just stipulate, adds up to this-- n times n minus 1 divided by 2.
1:21:09
So no matter what n is, this formula captures that series, that summation of all of those values.
1:21:14
So that is how many steps I took again and again and again when implementing selection sort for eight people.
1:21:22
So of course, let's multiply this out. So this is like n squared minus n all divided by 2. Let's do it out a little bit more.
1:21:28
That's n squared divided by 2 minus n over 2. And now we're back into the territory of running times.
1:21:34
Like, how many steps does this algorithm take? How many comparisons are we making? Now, n squared seems like the biggest term.
1:21:42
It's the dominant term. In other words, as n gets large-- not eight but 80 or 800
1:21:48
or 8,000 or 8 million-- squaring that is going to make a way bigger difference than just doing, like, n divided by 2 and subtracting that off.
1:21:55
Similarly, just dividing even this quadratic formula by 2, like, yes, it's going to halve it literally.
1:22:01
But that's kind of a drop in the bucket. As n gets larger and larger and larger, it's still going to be a crazy big number.
1:22:07
So computer scientists would typically wrap this in some big O notation and say, OK, OK, selection sort is on the order of n squared.
1:22:16
That's not a precise measurement. But it's on the order of n squared because it's making so many darn comparisons, not unlike everyone shaking everyone else's
1:22:23
hand like I proposed verbally earlier. It's a lot of work to get that done. So selection sort is on the order of n squared steps.
1:22:30
And that's kind of a slow one. That's what was at the top of my cheat sheet earlier when I proposed a ranking of some common running times.
1:22:37
There's an infinite number of them. But those are some of the common ones. So can we do actually better?
1:22:42
Well, if bubble sort then is in big O-- sorry. Sorry-- spoiler.
1:22:49
If selection sort is in the order of n squared, could we maybe get lucky sometimes?
1:22:55
Like, with selection sort, what would the best case scenario be? Well, the best case would be, like, everyone is already sorted,
1:23:00
0 through 7. And we just get lucky. But does bubble sort-- [SIGHS]---- does selection sort appreciate that?
1:23:10
Does selection sort take into account whether the list is already sorted? Not necessarily, because if you look at the pseudocode even,
1:23:18
there's no special conditional in here that says, if it's already sorted, exit early.
1:23:23
It's just going to blindly do this this many times. And you can actually see pseudocode-wise the n squared.
1:23:30
Notice that this line of pseudocode here is essentially telling me to do what? Do something n times from 0 to n minus 1,
1:23:37
or equivalently, if you prefer the real world, from 1 to n. That's n times total.
1:23:42
But what are you doing inside of this loop? Well, every time you're inside of this loop, you're looking for the smallest element, looking for the smallest element.
1:23:49
And that might take you as many as n steps. So another way to think about the running time of this algorithm
1:23:55
selection sort is this loop is telling you to do something n times. This line is telling you to do something n times as well.
1:24:02
And that's roughly n times n or n squared. It's not precise. But it's on the order of n squared.
1:24:07
Unfortunately, if you're just blindly doing that much work always, even if you have any number of doors, this
1:24:14
is going to end up being in omega of n squared as well,
1:24:19
because even in the best case where all of the numbers are already sorted, there is nothing about the algorithm called selection sort or even
1:24:26
my implementation thereof that would have said, wait a minute-- like, I'm done, and exit prematurely.
1:24:31
So selection sort is in big O of and omega of n squared as we've designed it.
1:24:39
And by coincidence, because those boundaries are the same, you can also say that it's in theta of n squared.
1:24:45
No matter what, you're going to spend n squared steps or n squared comparisons. But that second algorithm that I keep teasing called bubble sort,

## [Bubble Sort](https://youtu.be/jZzyERW7h1A?t=5093)

1:24:53
and I deliberately used the word bubble in my description of what was happening because Eli, I think was our first volunteer, who
1:24:58
kind of bubbled his way up all the way to the end of the list. Then number 6 did, then 5, then 4, then 3, then 2, then 1.
1:25:05
All of the numbers kind of bubbled their way up being the bigger values to the right. So bubble sort just does something again and again
1:25:11
by comparing adjacencies, comparing, comparing, comparing. And then it does it again and again and again.
1:25:17
So let's analyze bubble sort. If, for instance, this was the original array that we tried sorting before-- same exact numbers--
1:25:24
I was doing things like flipping the 7 and the 2, and then the 7 and the 5, and then the 7 and the 4.
1:25:29
But that would only fix minimally one number. I then had to repeat again and again and again.
1:25:37
So that one too felt like it was taking some time. So here's one way of thinking about bubble sort. Bubble sort pseudocode could say this.
1:25:43
Repeat the following n times. And that's why I kept going through the list again and again--
1:25:48
for i from 0 to n minus 2. Now, this is a little weird, but we'll get back to this-- from i
1:25:56
from 0 to n minus 2. If the number at location i and the number at location i plus 1
1:26:02
are out of order, swap them. And then just repeat, repeat, repeat.
1:26:08
But we've never seen n minus 2 in pseudocode before. Why is it n minus 2 and not the usual n minus 1?
1:26:14
Yeah? AUDIENCE: [INAUDIBLE]
1:26:20
DAVID MALAN: Exactly, because we're taking a number and comparing it to the next one. So you better not go all the way to the end
1:26:26
and expect there to be a next one at the end of the list. So if we use these same numbers here, even though they're
1:26:31
in a different order, if this is location 0, and this is location n minus 1 always, if you think
1:26:38
of i as being my left hand, it's pointing from 0 to 1 to 2 to 3 to 4 to 5 to 6 to 7.
1:26:44
If you get to the end, you don't want to look at i plus 1 because that's pointing to no man's land over here. And you can't go beyond the boundaries of your array.
1:26:51
But n minus 2 would be the second to last element, as you know. And that makes sure that my left hand and right
1:26:56
hand stay within the boundaries of the array if left hand represents i and right hand represents i plus 1.
1:27:02
So it's just to make sure we don't screw up and go too far past the boundary of the array. But as implemented here, this too does not take into account whether or not
1:27:10
the array is already sorted. So technically, we can actually do this n minus 1 times
1:27:16
because the last one you get for free. It ends up being in place. But even still, let's do a quick analysis here.
1:27:22
If we've got n doors in total from 0 on up to n minus 1,
1:27:27
bubble sort's analysis looks a little bit like this. Do the following-- n minus 1 times n minus 1 times.
1:27:35
Well, how did we get from that? Let me back up to the pseudocode. If this is the pseudocode as I originally put it,
1:27:40
I then propose verbally a refinement. You don't need to repeat yourself n times again and again because again, the last one bubbles up.
1:27:46
But by process of elimination, it's in the right place. So you can think of it as just n minus 1 times.
1:27:52
How many times can you compare i and i plus 1?
1:27:57
Well, you're iterating from 0 to n minus 2. And this is where the math is going to get weird.
1:28:03
But that is n minus 1 steps also. Why? Because if you do it in the real world starting at one,
1:28:09
this is saying from i from 1 to n minus 1. And then maybe it pops a little more obviously.
1:28:15
This inner loop is repeating n minus 1 times. So outer loop says do the following n minus 1 times.
1:28:20
Inner loop says do this now n minus 1 times. Mathematically, then, that's n minus 1 times n minus 1.
1:28:27
Now we've got our old FOIL method. So n squared minus n minus n plus 1. Combine like terms gives us n squared minus 2n plus 1.
1:28:35
But now let's think like a computer scientist. When n gets really large, we definitely don't care about the plus 1.
1:28:41
When n gets really large, we probably don't even care about the minus 2n. It will make a mathematical difference but a drop in the bucket
1:28:48
once n gets to be in the millions or billions. So this would be on the order of what, similarly?
1:28:54
On the order of n squared as well. So algorithmically, and actually, we'll use a different term
1:28:59
now-- asymptotically-- asymptotic notation is the fancy term to describe big O and omega and theta notation-- asymptotically bubble
1:29:08
sort is, quote, unquote, "the same" as selection sort in terms of its upper bound. It's not 100% exactly the same.
1:29:15
If we get into the weeds of the math, there are obviously different formulas. But when n gets really large and you plot the pictures on a chart,
1:29:22
they're going to look almost the same because they're going to be fundamentally the same shape. So in our cheat sheet here, bubble sort now is in big O of n squared.
1:29:33
But let me propose that we make an improvement. Here's our pseudocode earlier.
1:29:38
When might it make sense to abort bubble sort early? Like, when could you logically conclude that I do not need
1:29:47
to make another pass again and again? And remember what I did from left to right over our volunteers.
1:29:54
I was comparing, comparing, comparing, comparing and maybe swapping people who were out of order. So what could I do to short circuit this?
1:30:03
AUDIENCE: [INAUDIBLE] DAVID MALAN: Perfect. If I compare through the whole list left to right and I make no swaps,
1:30:10
it stands to reason that they're already ordered. Otherwise, I would have swapped them. And therefore, I would be crazy to do that again and again and again.
1:30:17
Because if I didn't swap them the first time around, why would I swap them the second time around if no one's moving. So I can terminate the algorithm early.
1:30:25
So in pseudocode, I could say something like this. If no swaps, quit. And I can do that inside of the inner loop.
1:30:31
So once I make a pass through the people and I say, hm, did I make any swaps? If no, just quit because they're not going
1:30:38
to move any further if they didn't just move already. So bubble sort then might arguably be an omega of what?
1:30:45
In the best case, how few steps could we get away with with bubble sort?
1:30:51
OK, it's not one. But it is n. Why? Because I minimally need to go through the whole list to decide,
1:30:56
did I make any swaps. And logically-- and this will come up a lot in the analysis of algorithms--
1:31:03
any question like, is this list sorted, cannot possibly take only one step if you've got n elements.
1:31:09
Why? Because then you're just guessing. Like, if you don't at least take the time to look at every element,
1:31:14
how in the world can you conclude logically that they're sorted or not? Like, you minimally have to meet us halfway and check every element.
1:31:21
So it's minimally in omega of n. Constant time wouldn't even give you time to look at the whole list
1:31:27
if there's n elements. So that's the intuition there. So we can't say anything about theta notation for bubble sort because it's different, upper and lower bounds.
1:31:34
But we seem to have done better asymptotically than selection sort.
1:31:39
In the worst case, they're just as bad. They're super slow. But in the best case, bubble sort with that tweak--
1:31:45
that conditional about swapping-- might actually be faster for us. And you'd want Google, Microsoft, your phone, to use that kind of algorithm.
1:31:52
Let me go back to the sorting demonstration earlier. Let me re-randomize the array. Small bars is small number.
1:31:58
Big bars is big number. And let me click bubble sort this time. And you'll see again, the pink represents comparisons.
1:32:04
But now the comparisons are always adjacent from left to right. So this is pretty much doing with more bars what I did with eight people here.
1:32:12
And you'll see that the biggest elements, Eli being the first one of the humans, bubbled up
1:32:18
all the way to the right, followed by the next largest, next largest, next largest. But here again you can visually see.
1:32:25
And with the number of words I'm using to kind of stall here, you can [? hear ?] that this is kind of slow
1:32:31
because you're doing a lot of comparisons again and again and again. And you're making improvements. So you're taking bites out of the problem
1:32:37
but really only one bite at a time. So I kind of feel this is going to be like holding in a sneeze
1:32:43
if we don't finish this. So I feel like we should give you emotional closure with getting this to finish.
1:32:49
Any questions in the meantime because there's going to be no surprise. It's going to be sorted. This is bubble sort.
1:32:57
No? All right, we're almost there. It's going faster because the list is effectively getting shorter.
1:33:02
And-- oh, OK, so that then was bubble sort.
1:33:08
But both of these, I claim now, are actually pretty inefficient. They're pretty slow.

## [Recursion](https://youtu.be/jZzyERW7h1A?t=5593)

1:33:13
And my god, that was only eight humans on the stage. That was only, like, what, 40 or 50 bars on the screen.
1:33:19
What if we start talking about hundreds or thousands or millions of inputs? Like, those algorithms are probably going to take crazy
1:33:25
long because n squared gets really big. So can we do better than n squared? Well, we can.
1:33:31
But let me propose that we introduce a new problem-solving technique that we've actually been using already, just not by name.
1:33:38
In programming and in mathematics, there's this idea of recursion. And recursion is a description for a function that calls itself.
1:33:48
A function that calls itself is recursive. So what do we mean by this? Well, we've actually seen this already.
1:33:54
Here's the same pseudocode for binary search earlier. And binary search-- bi implying two-- went
1:34:01
either left or right or left or right, halving each time. So that was the division and conquering.
1:34:06
So this is the same pseudocode. But notice that in my pseudocode earlier,
1:34:12
I literally used the keyword search inside of my definition of search. So this is sort of one of those, like, circular definitions.
1:34:19
Like, if this is a search algorithm, how am I getting away with using the word search in the definition of search?
1:34:24
It's kind of when you get reprimanded for using a word to define a vocabulary word. This is kind of like that because this algorithm is calling itself.
1:34:32
This search function is calling itself. Now, normally, if you were to have a function call itself,
1:34:38
call itself, call itself, call itself, it would just do that infinitely. And presumably, it would go on forever.
1:34:43
Or the program or computer would probably crash because out of memory or something like that-- more on that next week. But there's a key detail, a key characteristic
1:34:50
about this algorithm that makes sure that doing the same thing again and again is not crazy.
1:34:56
It's actually going to lead us to a solution. Even though I'm using search here or search here,
1:35:02
what's happening to the size of the problem for each of these lines?
1:35:08
What's happening? Yeah? It's being cut in half. So even though I'm doing the exact same thing algorithmically again and again,
1:35:15
I'm doing it on a smaller, smaller, smaller input-- fewer, fewer, fewer doors-- fewer, fewer, fewer people.
1:35:21
And so even though I'm doing it again and again, so long as I have this so-called base case, as we'll call it, that just makes sure if there's no doors-- you're done--
1:35:29
I can break out of what would otherwise be an infinite loop of sorts.
1:35:34
All right, so those two lines we've already kind of seen. And actually, we saw this in week zero. So this is the pseudocode for the phone book example from week zero.
1:35:42
And you might recall that we had these lines of code here. And this is very procedural or iterative where I literally
1:35:48
told you go back to line 3. And we did that today when we took attendance, so to speak. With that third algorithm, you went back to step 2 again and again.
1:35:55
That's a very iterative loop-based approach. But you know what? I could be a little more clever here too in week zero. We just didn't want to get too far ahead of ourselves.
1:36:03
Let me actually change these highlighted lines to be more, succinctly, search left half book, search right half of book.
1:36:10
I can now tighten the code up. So it's kind of a shorter algorithm. But it's the exact same idea. But on week zero, I very methodically told you what I want you to do next.
1:36:20
But here, I'm sort of recognizing that, wait a minute, I just spent the past six lines telling you how to search.
1:36:25
So go do more of that. You have all of the logic you need. So this too is recursive in the sense that if this is a search algorithm,
1:36:33
the search algorithm is using a search algorithm inside of it. But here too, the phone book was getting divided and divided
1:36:39
and divided in half again and again. So recursion doesn't just describe mathematical formulas.
1:36:45
It doesn't just describe pseudocode or code-- even physical structures. So we deliberately brought back these bricks here today,
1:36:51
which are reminiscent, of course, from Mario and Super Mario Brothers. That pyramid, especially if we get rid of the distractions
1:36:56
of the ground and the mountains and so forth, is itself recursive as a structure.
1:37:01
Now, why is that? Well, here you can kind of play verbal games. If this is a pyramid of height 4--
1:37:07
and ask the question, well, what is that-- what is a pyramid of height 4-- I could kind of be difficult and say, well, it's just
1:37:13
a pyramid of height 3 plus 1 other row. All right, well, what's a pyramid of height 3?
1:37:18
You could be difficult and say, well, it's just a pyramid of height 2 plus 1 more row. What's a pyramid of height 2? Well, it's this plus 1 more row.
1:37:27
I might have skipped a step there. What's a pyramid of height 2? Well, it's a pyramid of height 1 plus 1 more row.
1:37:33
What's a pyramid of height 1? Well, it's nothing plus 1 more row. Or at this point, you can just say it's a single brick.
1:37:39
You can have a base case that just says, like, the buck stops here. Stop asking me these questions. I can special case or hard code my answer to the very tiniest of problems.
1:37:48
So even those bricks then are sort of-- the pyramid is recursively defined. And we can actually implement this even in code
1:37:54
if we want in a couple of different ways to make this clear. So let me go back over to VS Code here.
1:37:59
And let me propose that we do one old-school iterative example with this-- code iteration dot C.
1:38:06
And iteration just means to loop again and again. An iteration is a pass through the code. And let me go ahead and whip this up as follows.
1:38:13
Let's include the CS50 library. So we have our get int function.
1:38:18
Let's include standard io so that we have printf. Let's go ahead and create main with no command line arguments today.
1:38:27
Let's go ahead and create a variable of type int set equal to the return value of get int asking
1:38:33
the user for the height of the pyramid. And then let me assume for the sake of discussion that there is a function now that will draw a pyramid of that height.
1:38:41
All right, now let's actually implement that function as a helper function, so to speak. So if I have a function called draw, it's going to clearly take an integer.
1:38:49
And I'll call it, maybe, n as input. And it doesn't need to return anything. So I'm going to say that this is a void function.
1:38:55
It doesn't return a value. It just has a side effect of printing bricks on the screen. How can I go about doing a pyramid of height n?
1:39:02
Well, I'm going to do this one, which looks like this-- one at a time,
1:39:07
then two, then three, then four. And this is a little easier, for instance, than problem set one, which had the pyramid flipped around the other way.
1:39:14
So this one's a little easier to do deliberately. So if I go back to my code, I could say something like this-- for int i gets 0.
1:39:21
i is less than, let's say, n, which is the height-- i plus, plus. That's going to essentially iterate over every row of the pyramid top to bottom.
1:39:30
This might feel similar-- reminiscent-- to problem set one. Then in my inner loop, I'm going to do four.
1:39:36
int j gets 0. j is less than i plus 1 j plus, plus.
1:39:42
And we'll see why this works in a moment. And then let's go ahead and print out a single hash, no new line.
1:39:47
But at the very bottom of this row, let's print out just a new line to move the cursor down a line.
1:39:54
Now, I'm not done yet. Let me hide my terminal for a second. I need the prototype. So I'm going to copy this, paste it up here with a semicolon.
1:40:02
And I think now the code is correct. Now, why is this correct? Because on my outer loop, I'm iterating n times starting at 0.
1:40:11
My inner loop-- realize I want to have at least one hash, then two, then three, then four.
1:40:18
So I can't start my number of hashes at 0. And that's why I'm doing j all the way up to i plus 1 so that when i is 0,
1:40:26
I'm actually still printing one hash, and then two hashes, and then three. Otherwise, I would start with 0, which is not my goal.
1:40:32
Let me go in and do make iteration to compile this-- dot slash iteration. And let me go ahead and make my terminal bigger--
1:40:39
enter. The height will be, for instance, 4. And indeed, it's not quite to scale because these are a little more
1:40:45
vertical than they are horizontal. But it essentially looks like that pyramid. And I can do this even larger.
1:40:50
Let's do this again after clearing my screen. Let's do like 10 of these. And it gets bigger. Let's do, like, 50 of these.
1:40:56
And it gets even bigger. It doesn't even fit on the screen. But it works. And that's an iterative approach, 100% correct,
1:41:02
and similar to what you might have done already for something like week zero or week one.
1:41:08
But it turns out if we leverage recursion, we can be a little more clever, in fact. Let me go ahead and do this.
1:41:13
Let me minimize my terminal window. And let me go back into my code here. And let me propose to implement the exact same program recursively instead.
1:41:23
And let me go ahead and do this. I'm going to leave main--
1:41:31
let's see-- exactly as is. And I'm going to go ahead and change my draw function to work as follows.
1:41:39
Let me delete all of these loops because loops are sort of an indication of using iteration. And I'm instead going to do this.
1:41:45
What is a pyramid of height 4? I said it's a pyramid of height 3 plus 1 more row.
1:41:52
So let's take that literally. If a pyramid of height n needs to be drawn, let's first draw a pyramid of n minus 1.
1:42:01
And then how do I go about drawing one more row? Well, this, I can use a bit of iteration. But I don't need a doubly-nested loop anymore.
1:42:08
I can set i equal to 0, i less than n, i plus, plus.
1:42:13
And this block of code is simply going to print one simple row of hashes again and again followed by a new line just
1:42:23
to move the cursor down. So notice this line here. And I'll add some comments-- print pyramid of height n minus 1,
1:42:33
print one more row. So I'm kind of taking a bite out of the problem by printing one row.
1:42:39
But I'm deferring to, weirdly, myself, to print the rest of the pyramid. Now I'm going to go ahead and try compiling this-- make--
1:42:47
oh. And this is no longer iteration. So I'm actually going to do this-- code recursion dot c.
1:42:53
I'm going to paste that same code into this new version, just so we have a different file without breaking the old one.
1:42:59
And now I'm going to do make recursion. All right, interesting. So Clang is yelling at me with this error.
1:43:05
All paths through this function will call itself. So Clang is actually smart enough to notice in my code
1:43:11
that no matter what, the draw function is going to call the draw function. And the draw function is going to call the draw function.
1:43:16
And the draw function's going to call the draw function. Now, to be fair, n, the input to draw, is getting smaller and smaller.
1:43:23
But what's going to happen eventually to the input of draw as I've written this code right now?
1:43:28
Yeah, in the back? AUDIENCE: [INAUDIBLE] DAVID MALAN: Exactly. Remember that integers are signed by default.
1:43:35
They can be both positive or 0 or negative. And so here, if I just keep blindly subtracting 1,
1:43:41
it's going to do that seemingly forever until I technically underflow. But that's going to be like 2 billion rows of pyramids later.
1:43:47
So I think what I actually need to do is something like this. I need to ask the question, if n equals 0--
1:43:56
or heck, just to be super safe, let's say if n is less than or equal to 0, just to make sure it never goes negative, let's just go ahead
1:44:04
and return without doing anything. So I'm going to comment this as, like, if nothing to draw, well, then
1:44:10
don't blindly call draw again. So this is that so-called base case. This is analogous to saying, like, if John Harvard not in phone book
1:44:16
or if no lockers or doors left, then just exit or return in this case.
1:44:22
So now I'll never call draw a negative number of times or zero number of times.
1:44:28
I will only do it so long as n is positive. So now if I make my terminal bigger, make recursion again does compile fine.
1:44:36
Dot slash recursion-- let's do the same input for. And I get the exact same number of bricks.
1:44:42
Let's go ahead and do it again with maybe 10. That seems to work too. Let's do it again with 50.
1:44:48
That seems to work too. And I can go a little crazy. I can do, like, 5,000. This is still going to work. It's just not going to fit on my screen.
1:44:55
But it is doing a valiant attempt to print all of those out. Now, it turns out that could get us in trouble
1:45:00
if we start poking around in the-- now, maybe not 5,000 but 500,000 or 5 million or beyond.
1:45:07
But for now, we'll just assume that this is just a slow process at that. But if we go back to the goal, which was to print this thing here,
1:45:14
this too is a recursive structure that we're just now translating the ideas of recursive code to.
1:45:19
And actually, if you've never discovered this, we would be remiss in not doing this for you. If I go into a browser here.
1:45:27
And suppose that I'm not using any AI fancy technology. I'm just going to Google.com. And I search for recursion because I'm curious to see what it means.
1:45:35
Google for years has had this little Easter egg for computer scientists.
1:45:43
It's not a typo. Get it? Ha, ha, kind of funny. Yeah? OK, like, see?
1:45:49
Recursion-- so if you click recursion, OK, now we're in night mode for some reason. But OK, like, so it just does this endlessly.
1:45:57
OK, so programmers with too much free time or too much control over Google's own servers to do that. So it turns out, yes, if you search for recursion on Google,
1:46:05
this is a long-standing Easter egg in this case. But the point of introducing recursion is that, one, it's actually going to be a very powerful problem-solving technique
1:46:12
because honestly, it, one, we've seen in pseudocode already, it kind of tightens up the amount of code or the amount of lines
1:46:18
that you need to write to convey an algorithm. And two, it will actually allow us to solve problems in a fundamentally different way
1:46:24
by using computer's memory in an interesting way. And so toward that end, we wanted to introduce one final sort today, which

## [Merge Sort](https://youtu.be/jZzyERW7h1A?t=6391)

1:46:31
we won't use humans to demonstrate but just numbers instead, namely something called merge sort. And merge sort is an algorithm for sorting n numbers that I claim
1:46:40
is going to be better than selection sort and bubble sort. It's got to be better because that n squared was killing us.
1:46:46
We want to get something lower than n squared. So merge sort's pseudocode essentially looks like this.
1:46:51
And this is it. Merge sort says, if you've got n numbers or an array of numbers,
1:46:58
sort the left half of them, sort the right half of them. And then merge the sorted halves. And we'll see what this means in just a moment.
1:47:05
But if there's only one number, just quit. So this is my base case because this is recursive. Because if this is a sorting algorithm called merge sort,
1:47:12
I'm kind of cheating by using the verb sort in the sorting algorithm. But that just makes it recursive. It doesn't make it wrong.
1:47:18
So what do I mean by merging? Just to make this clear, here among these numbers are two lists of size 4.
1:47:25
And I'm going to scooch them over to the left and the right just to make clear that on the left is one half that is sorted--
1:47:32
1346 from smallest to largest. On the right is a second half that's also sorted 0257.
1:47:40
So for the sake of discussion, suppose that I'm partway through this algorithm called merge sort.
1:47:46
And I've sorted the left half already, clearly. I've sorted the right half already, clearly. Now I need to merge the sorted halves.
1:47:52
What do we mean by that? Well, that means to essentially, conceptually, point your left hand at the first at the left half.
1:48:00
Point your right hand at the right half. And then decide which of these numbers should come first
1:48:05
in order to merge or kind of stitch these two lists together in sorted order. Well, which is smaller?
1:48:11
Obviously, 0. So that last step, merge sorted halves, would have me take this number
1:48:16
and put it in an extra empty array up here. Now I move my right hand to the next number in the right half.
1:48:22
And I compare the 1 and the 2. Obviously, 1 comes next. So I put this now up here. Now I compare the 3 and the 2.
1:48:28
Obviously, the 2 comes next. And so I put this up here-- 3 and 5-- obviously, 3--
1:48:34
4 and 5-- obviously, 4--
1:48:40
6 and 5-- obviously, 5-- and 6 and 7-- obviously, 6.
1:48:46
And I didn't leave quite enough room for 7, perhaps, and lastly, 7. So that's all we mean by merging two lists together.
1:48:53
If they're already sorted, you just kind of stitch them together by plucking from one or the other the next number
1:48:59
that you actually want. And that's it. And even though I picked up partway through this algorithm, those three steps alone would seem to work.
1:49:05
So long as you can sort the left half and sort the right half, you can surely then merge the sorted halves.
1:49:10
Now I'll go ahead and do this digitally rather than use the physical numbers because clearly, it's a little involved moving them up and down.
1:49:16
But this rack here, this shelving, essentially represents one array with maybe a second array here.
1:49:22
And heck, if I really want it, a third and a fourth array. It turns out that with selection sort and bubble sort, we've really been tying our hands because I only
1:49:30
allowed myself a constant amount of memory, just one variable in my head, for instance, with selection sort that let me keep
1:49:35
track of who was the smallest element. And when we did bubble sort, the only number I kept in mind was i, like i and i plus 1.
1:49:42
I didn't allow myself any additional memory. But it turns out in programming and in CS, you
1:49:47
can trade off one resource for another. So if you want to spend less time solving a problem,
1:49:53
you've got to throw space at it. You've got to spend more space, spend more money, in order to give yourself more space to reduce your time.
1:50:00
Conversely, if you're fine with things being slow in terms of time, then you can get away with very little space.
1:50:06
So it's kind of like this balance whereby you have to decide which is more important to you, which
1:50:11
is more expensive for you, or the like. So let's go ahead then and consider exactly this algorithm as follows.
1:50:20
So suppose that these are the numbers in question. So here is our array.
1:50:26
It's clearly unsorted. I'd like to sort this. I could use selection sort. But selection sort was not great because it's big O of n squared.
1:50:33
And it's omega of n squared, so sort of damned if you do. Damned if you don't. Bubble sort was a little better.
1:50:38
It was still big O of n squared. But sometimes, we could get lucky and shave some time off. So it was omega of only n.
1:50:44
Let's see if merge sort is fundamentally better. And let's do so by trying to reduce the number of comparisons-- no more looping
1:50:51
back and forth and back and forth and back and forth endlessly. So here's how we can draw inspiration from the idea of recursion and divide
1:50:58
and conquer as per week zero. Let's first think of these numbers as indeed in an array contiguously from left to right.
1:51:04
Let's then go ahead and sort the left half. Because again, the pseudocode that you have
1:51:10
to remember throughout this whole algorithm has just three real steps. Sort the left half. Sort the right half.
1:51:16
Merge the sorted halves. And then this is sort of a one-off thing. But it's important. But this is the juicy part. Sort left half.
1:51:22
Sort right half. Merge the sorted halves. So if we go back to this array on the top shelf, here's the original array.
1:51:27
Let's go ahead and sort the left half. And I'm going to do so by sort of stealing some more memory,
1:51:32
so I can sort of work on a second shelf with just these numbers. So 6341 is now an array of size 4, essentially.
1:51:39
How do I sort an array of size 4? Well, I've got an algorithm for that-- selection sort. But we decided that's slow.
1:51:45
Bubble sort-- that's slow. Wait a minute. I'm in the middle of defining merge sort. Let's recursively use the same algorithm by just
1:51:52
sorting the left half of the left half. So if you've got an array of size 4, it's only three steps to solve it.
1:51:58
Sort left half. Sort right half. Merge. So let's do that. Let's sort the left half.
1:52:03
OK, wait a minute. How do you sort an array of size 2? I've got an algorithm for that. Sort the left half.
1:52:08
Sort the right half. Merge the two halves. All right, let's sort the left half.
1:52:14
What now? So 6 is a list of size 1. What was that special base case then?
1:52:19
So it was quit or just return. Like, I'm already done. So this list of size 1 is sort of weirdly already sorted.
1:52:26
So I'm making progress. Meanwhile, what's the next step after sorting this left half? Sort the right half.
1:52:32
Done. This is already sorted. But here's the magic. What's the third step for these numbers?
1:52:38
Merge them. So this is like the left hand, right hand thing. Which one comes first? Obviously, 3 and then 6.
1:52:45
And now we are making progress because now the list of size 2 is sorted.
1:52:50
So what have I just done? I've just finished sorting the left half of the left half.
1:52:56
So after I've sorted the left half, what comes next if you rewind in time?
1:53:01
Sort the right half of that left half. So now I take the right half.
1:53:06
And how do I sort this right half of size 2? Well, sort its left half. Done. Sort its right half.
1:53:12
Done. Now merge them together. And obviously, the 1 comes first, then the 4.
1:53:17
Now where are we? We're at the point in the story where we have a left left half sorted and a right left half sorted.
1:53:26
So what comes next now narratively? Merge the two together, so left hand, right hand, so 1346.
1:53:35
And where are we now in the story? We're sort of at the beginning because I've now sorted the left half.
1:53:41
And you recall the demo I did physically, this is how I had the left half was already sorted on the second shelf.
1:53:46
But now that I've sorted the left half of the original array, what's the original second step?
1:53:53
Sort the right half. So it's the same idea. So I'm borrowing some extra memory here. And now I've got an array of size 4.
1:53:59
How do I sort an array of size 4? Sort the left half. All right, how do I sort an array of size 2? Sort the left half.
1:54:05
Done. Sort the right half. Done. Now what? Merge the two together. And of course, it's 2 and 5.
1:54:12
Now what do I do? I've sorted the left half of the right half. So now I sort the right half of the right half.
1:54:19
How do I sort a list of size 2? Well, sort the left half. Done. Sort the right half. Done. Merge them together-- 0 and 7.
1:54:27
Where am I in the story? I've sorted the left half and the right half of the original right half.
1:54:33
So I merge these two together-- 0 and then 2 and then 5 and then 7.
1:54:38
Whew. Where are we? We're at exactly the point in the story where we had the numbers originally on the second shelf.
1:54:44
We had a list that's sorted on the left, a list that's sorted on the right. And what I demoed physically was merging those two together.
1:54:52
So what happens now? 01234567.
1:55:00
And it seems kind of magical and kind of weird in that I kind of cheated. And when I had these leaves--
1:55:05
these leaf nodes, so to speak-- these singletons-- I was, like, sorted. I wasn't really doing anything. But it's that merging that seems to really be doing
1:55:12
the magic of sorting things for us. So that felt like a mouthful. And recursion in general is the kind of thing
1:55:19
that will, like, bend your brain a little bit. And if that went over your head, like, that's fine. It takes time and time and time and practice.
1:55:25
But what there was not a lot of with this algorithm was again and again and again and again.
1:55:31
I was kind of only doing things once. And then once I fixed a number, I moved on to the next.
1:55:38
And that's sort of the essence of this algorithm here. If it helps you to see it in another visual way,
1:55:43
let me go back to our previous visualization here. Let me re-randomize the array and click merge sort.
1:55:48
And this time, notice that merge sort is using more space. Technically, I was using 1, 2, 3 shelves.
1:55:54
But you can actually be slightly more intelligent about it and actually just go back and forth and back and forth between two shelves
1:56:00
just to save a little space. So you're still using twice as much space. But you don't need four times as much space as the diagrams
1:56:06
or as the shelves might imply. So here is merge sort. And you'll notice that we're sort of working in halves-- sometimes
1:56:13
big halves, sometimes smaller halves. But you can see as the two halves are merged,
1:56:18
things seem to happen very quickly. And so notice that this is the same number of bars as before.
1:56:23
But that was way faster, right? I don't need to stall nearly as much as I have in the past.
1:56:29
So why is that? Well, if we go back to the diagram in question, here's the array that's already sorted.
1:56:35
And if we consider now exactly how much work is done, I'll stipulate already it's not n squared. n squared was slow.
1:56:41
And merge sort is actually much better than that. Let's see how much better it is. So here is the original list--
1:56:48 63415270. And here are all of the remnants of that algorithm, all of the states
1:56:54
that we were in at some point-- sort of leaving a whole bunch of breadcrumbs. How many pieces of work did I do?
1:57:01
Well, like, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
1:57:08
20, 21, 22, 23, 24. So I moved things around, like, 24 times, it seems.
1:57:15
And how do I actually reason about that? Well, these are the numbers. This is like my temporary workspace here.
1:57:21
And 24 is the literal number. But let's see if we can't do things a little more generically. Log base 2 of n, recall, is what refers to anything
1:57:27
that we're doing in half-- dividing, dividing, dividing. And that's kind of what I was doing here. I took a list of size 8-- divide it into two of size 4, then four of size 2,
1:57:36
then eight of size 1. Well, how many times can you do this if you start with eight numbers?
1:57:41
Well, that's log base 2 of 8. And if we do some fancy math, that's just log base 2 of 2 to the third.
1:57:46
And remember, the base and the number here can cancel out. So that's actually 3. So log base 2 of 8 is 3, which means that's how many times you
1:57:55
can divide a problem of size 8 in half, in half, in half. But every time we did that per this chart, I had to take the numbers
1:58:03
and merge them together, merge them together, merge them together. And so on every row of this postmortem of the algorithm,
1:58:12
there are n steps, n steps, n steps. So laterally, there's n steps because I had to merge all of those things
1:58:19
back together. But what is the height of these yellow remnants? Well, it's 3, which is log base 2 of 8, which is 3.
1:58:26
So this is technically three times 8, ergo 24 steps.
1:58:32
But more generally, this is log n height and n width, so to speak.
1:58:39
So the total running time I claim is actually n log n, which it's OK if that doesn't quite gel immediately in your mind,
1:58:46
especially if you're rusty on algorithms. But and we can throw away the base because that's just a constant factor and with a wave of our hand when we talk about big O notation, merge sort,
1:58:54
I claim is in big O of n log n-- that is, n times log n.
1:59:01
Unfortunately, it is also in omega of n log n, which means that, frankly, bubble sort might sometimes outperform it,
1:59:09
at least when the inputs are already sorted or certainly relatively small. But that's probably OK because in general,
1:59:16
data that we're sorting probably isn't very sorted. And honestly, we could even half merge sort to just do one pass to check initially, is the whole thing sorted,
1:59:24
and then maybe terminate early. So we can maybe massage the algorithm a little better to be a little smarter. But fundamentally, merge sort is in theta of n log n,
1:59:34
is how you would say it. It's on the order of n times log n steps. Now, in terms of that chart, it's strictly higher than linear.
1:59:42
But it's strictly lower than quadratic-- n and n squared, respectively. So it clearly seems to be faster.
1:59:49
So it's not as good as linear search. And it's definitely not as good as binary search. But it's way better than selection sort or bubble sort actually were.
1:59:58
So with that said, we thought we'd conclude by showing you a final film that's just about a minute long that compares these actual algorithms and shows them as follows.
2:00:08
You'll see on the top, the middle, and the bottom, three different algorithms. On the top, you will see selection sort.
2:00:14
On the bottom, you will see bubble sort. And in the middle, you will see and hear an appreciation of what n log n is--

## [Sort Race](https://youtu.be/jZzyERW7h1A?t=7223)

2:00:23
a.k.a., merge sort today. So if we could dim the lights dramatically, this is n log n vis a vis n squared.
2:00:31
[VIDEO PLAYBACK] [MUSIC PLAYING]
2:01:37
[END PLAYBACK] All right, that's it for CS50. We'll see you next time. [APPLAUSE] [MUSIC PLAYING]
