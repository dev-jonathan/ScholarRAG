---
link: https://youtu.be/0euvEdPwQnQ
related_files:
  - week-5-notes.md
  - problemset/week-5-inheritance.md
  - problemset/week-5-problemset.md
  - problemset/week-5-speller.md
title: "Lecture 5: Week 5 - Data Structures"
type: transcription
week/lecture: "5"
---

# [Lecture 5: Week 5 - Data Structures](https://youtu.be/0euvEdPwQnQ)

TABLE OF CONTENTS:

0:00 - Introduction
1:02 - Stacks and Queues
9:56 - Jack Learns the Facts
12:05 - Resizing Arrays
30:33 - Linked Lists
1:16:11 - Trees
1:30:38 - Dictionaries
1:34:31 - Hashing and Hash Tables
1:52:41 - Tries

## [Introduction](https://youtu.be/0euvEdPwQnQ?t=0)

0:00
[MUSIC PLAYING]

## [Stacks and Queues](https://youtu.be/0euvEdPwQnQ?t=62)

1:02
DAVID J. MALAN: All right, this is CS50. And this is week 5.
1:07
And among our goals for today are to revisit some topics from past weeks but to focus all the more on design possibilities, particularly
1:16
by way of data structures. So data structures, again, is this way via which you can structure your data. But more specifically in C, It's how you can
1:23
use your computer's memory in interesting and, daresay, clever ways to actually solve problems more effectively.
1:29
But we're going to see today that there's actually different types of data structures. And we'll make the distinction between abstractions,
1:35
like high-level descriptions of these structures and the lower-level implementation details so to speak.
1:41
So in particular, we'll talk first today about what we call abstract data types. So an abstract data type is like a data structure.
1:48
But it offers certain properties, certain characteristics. And it's actually up to the programmer how
1:53
to implement the underlying implementation details. So, for instance, there's actually this abstract data type that's
1:58
common in computing known as a queue. And from the real world, most of us are presumably familiar with queues,
2:04
otherwise known in the US typically as lines or forming lines. In fact, I have here three bags of cookies.
2:12
Could I get three volunteers to come up on stage and queue up? OK, I saw your hand first. How about your hand second?
2:17
And in the blue. OK, come on down, just you three.
2:22
Come on over. And if you want to queue up over here if you could.
2:29
Come on down. Thank you. As we begin, do you want to introduce yourselves first? NAFTALI HOROWITZ: Hi. My name is Naftali Horowitz.
2:34
I'm a first year studying computer science and economics. And I sleep at Hurlbut Hall.
2:41
DAVID J. MALAN: All right, next. CATHERINE: Hi, everyone, my name is Catherine. I'm planning on studying engineering. I'm not sure mechanical or electrical yet but one of the two.
2:49
And I'm currently in Kennedy. DAVID J. MALAN: Nice. Nice to meet. ISABELLA: Hi, everyone. I'm Isabella. I'm in Strauss.
2:54
And I plan on majoring in computer science. DAVID J. MALAN: Wonderful. Well, welcome to all three of you. And I think this will be pretty straightforward.
3:00
I have here these three bags of cookies. You formed nicely this line or this queue. So if you'd like to come up first and take your cookies, thank you.
3:07
And right that way, that's all there is to this demonstration. Your cookies as well. Right this way.
3:12
And your cookies. Right this way. Wonderfully well done. Thank you to our volunteers. The point is actually sincere, though, simple as that demonstration was.
3:21
And as easy as it was to get those cookies, queues actually manifest a property that actually
3:26
is germane to a lot of problem solving and computing and the real world. Specifically, queues offer this characteristic, FIFO, first in first
3:34
out. And indeed as our volunteers just noticed, as they queued up on stage, 1, 2, 3, that is the order in which I
3:41
handed them their cookies. And daresay it's a very equitable approach. It's very fair. First come, first served might be a more casual way
3:47
of describing FIFO, first in, first out. Now, structures like these actually offer specific operations
3:53
that make sense. And in the context of queues, we generally describe these operations as enqueueing and dequeueing
3:58
So when our first three volunteers came up, they enqueued. And as I handed them each a bag of cookies,
4:03
they dequeued and exited in that same order. Now, how could you go about implementing a queue in code, specifically in C?
4:11
Well, we can actually implement it in bunches of different ways. But perhaps the most obvious is to borrow our old friend, namely arrays.
4:17
And we could use a data structure that looks a little something like this, whereby we specify the total capacity of this data structure.
4:26
For instance, we might store a total of 50 people or just 3 in this case. We might define our structure then as containing those people
4:33
as simply an array. And if a person is a data type that we've defined in week past, you could imagine each of our volunteers is indeed a person.
4:40
And we've stored them one after the other contiguously in memory by way of this actual array.
4:47
But we do need to keep track inside of a queue using one other piece of data-- namely, we need to keep track of an integer,
4:53
like the size, like how many people are actually in the queue at this moment. Because if we have a total capacity of 50,
5:00
I'd like to if I only have three volunteers. Then I can do some quick arithmetic and know that I could have fit another 47 people in this same queue.
5:08
But it's finite. Of course, if we had 50 volunteers all wanting cookies, that's as many people as we could actually handle.
5:14
So there is this upper bound then on how many we could fit. But there's yet other ways for storing data inside of a computer's memory.
5:21
And there's this other abstract data type known as a stack. And stacks are actually omnipresent as well even though it's not necessarily the system
5:29
you would want when you line up on stage. For instance, could we get three more volunteers? OK, I saw a hand here, right here, and right here.
5:37
Come on down. We'll have the orchestra come up this time. All right, come on over.
5:43
And if you wouldn't mind, come on over. We'll do introductions first. This will be almost as easy as the last one if you want to introduce yourself.
5:50
And let me just stack you against the lectern this time. So if you could go there. And if you could come over here. And if you could come over here, we'll stack all three of you.
5:58
So you were first. So you're first in the stack. SPEAKER: Hi. I'm [INAUDIBLE]. I have no idea what I'm studying. And I live in Strauss.
6:03
DAVID J. MALAN: Wonderful. And next? SPEAKER: Hi. I'm [? Tanai. ?] I'm studying econ and CS. And I live in Canada.
6:09
CLARA: Hi. I'm Clara. I want to study applied math. And I'm in Wigglesworth. DAVID J. MALAN: Wonderful. Welcome, to all three of you. And if I may, let me just advance a bit more information about stacks.
6:18
The catch is that stacks actually support what's known as LIFO, so last in, first out, which
6:24
is sort of the opposite really of a queue or a line. So in fact you were last in line. So here we have your cookies.
6:29
Thank you so much. And if you'd like to exit that way, we have your cookies here. Thank you so much. We'd you to exit this way.
6:35
And even though you were first, LIFO doesn't really give you any cookies because you're first in, not last in.
6:43
So, yeah, OK, point's made. We'll give you the cookies. All right, so thank you to all three of our volunteers.
6:50
But LIFO, suffice to say, doesn't offer the same fairness
6:55
guarantees as a queue or a line more traditionally. And imagine just lining up in any store or the dining hall or the like.
7:01
Ideally, you want the people running the place to adhere to that queue, to that line so that FIFO is preserved if you indeed care about being first,
7:10
whereas there are contexts in which LIFO does actually make sense. In fact, if you think about Gmail, your inbox, or Outlook,
7:18
typically you're viewing your inbox as a stack right. Because when you get new mail, where does it end up?
7:23
It actually ends up in the top. And if you're like me, odds are which emails do you tend to first?
7:30
I mean, probably the ones on the top, the ones that came in last, most recently that is and that might actually
7:36
be to the detriment of people who emailed you earlier today or yesterday. Because once they sort of fall off the bottom of your screen,
7:42
frankly, unless you click next, you may never see those emails again. But stacks are indeed one way of storing data.
7:48
And Google and Microsoft presumably made the judgment call that, in general, we users want to see the most recent data first.
7:55
The last information might be the first we want out. Now, just in terms of nomenclature, the two operations
8:01
that are analogous to enqueueing and dequeueing but with this property of LIFO are instead called push and pop.
8:07
So when our first volunteer came up on stage, so to speak, I pushed him onto the stack against the lectern there.
8:12
Second person was pushed. Third person was pushed. And then when it was time to hand out the cookies, we popped them, so to speak, one after the other but preserving that LIFO
8:21
property. But here's where things are a little interesting in terms of implementation details. A stack could be implemented almost identically underneath the hood
8:30
to a queue because what do you need? You need an array of people, which we could use our person data
8:36
type for past classes. We have to keep track of how many people are in the stack so that even if we have a capacity of like 50,
8:43
we know at least that we can store 3 plus maybe 47 others.
8:48
Now, there's still going to be a change in the underlying implementation details because not pictured here is the actual C code that actually pushes
8:55
and pops or enqueues and dequeues. So whatever loops you're using, whatever code you're using,
9:01
odds are that's where those properties are going to be implemented. FIFO versus LIFO, you're going to implement maybe the loop
9:06
in this direction instead of this one or some such distinction. But at the end of the day, stacks and queues
9:12
are just abstract data types in the sense that we can implement them in bunches of ways, two of them
9:17
among them here thus far on the screen. But that array is going to come back to bite us. Because if you only have a capacity of 50,
9:24
what happens if 51 people want cookies next time? You just don't have room for them even though, clearly, we have
9:30
enough room for the people themselves. We have enough memory. So it seems a little shortsighted to limit just how much data
9:36
can fit in our data structures. So with that said, a friend of ours, Shannon Duvall at Elon University,
9:41
kindly put together a visualization of the same. And allow me to introduce you to two fellows known as Jack and Lou.
9:50
If we could dim the lights for this video. [VIDEO PLAYBACK] [MUSIC PLAYING]

## [Jack Learns the Facts](https://youtu.be/0euvEdPwQnQ?t=596)

9:56

- Once upon a time, there was a guy named Jack. When it came to making friends, Jack did not have the knack.
  10:04
  So Jack went to talk to the most popular guy he knew. He went up to Lou and asked what do I do?
  10:09
  Lou saw that his friend was really distressed. Well, Lou began, just look how you're dressed.
  10:15
  Don't you have any clothes with a different look? Yes, said Jack. I sure do. Come to my house and I'll show them to you.
  10:22
  So they went off to Jack's. And Jack showed Lou the box where he kept all his shirts and his pants and his socks.
  10:28
  Lou said, I see you have all your clothes in a pile. Why don't you wear some others once in a while?
  10:33
  Jack said, well, when I remove clothes and socks, I wash them and put them away in the box.
  10:39
  Then comes the next morning, and up I hop. I go to the box and get my clothes off the top.
  10:45
  Lou quickly realized the problem with Jack. He kept clothes, CDs, and books in a stack.
  10:51
  When he reached for something to read or to wear, he chose the top book or underwear. Then when he was done, he would put it right back.
  10:58
  Back it would go on top of the stack. I know the solution, said the triumphant Lou. You need to learn to start using a queue.
  11:06
  Lou took Jack's clothes and hung them in a closet. And when he had emptied the box, he just tossed it.
  11:11
  Then he said now, Jack, at the end of the day, put your clothes on the left when you put them away.
  11:17
  Then tomorrow morning when you see the sun shine, get your clothes from the right from the end of the line.
  11:22
  Don't you see, said Lou? It will be so nice. You'll wear everything once before you wear something twice.
  11:28
  And with everything in queues in his closet and shelf, Jack started to feel quite sure of himself all thanks
  11:34
  to Lou and his wonderful queue. [END PLAYBACK]
  11:40
  DAVID J. MALAN: So the same-- wonderful, thanks to Shannon-- so you might have noticed I wear black all the time
  11:46
  so we could make a similar gag about here's what my stack of clothes at home looks. Even though I might own a blue and a red sweatshirt,
  11:52
  it doesn't really work if you're popping everything from a stack every time, cleaning it, replenishing the blacks sweaters before the red or the blue
  11:59
  even get popped themselves. But we're going to focus today not just on stacks and queues which for us are really meant to motivate

## [Resizing Arrays](https://youtu.be/0euvEdPwQnQ?t=725)

12:05
different ways of designing data even though the implementation details might differ. But we're going to start focusing on solving some problems
12:12
that invariably we'd be bumping up against anyway as we develop more and more real world software, not just
12:17
smaller programs as in class. And arrays, recall, are what? What's the key characteristic or definition
12:22
of an array with respect to your computer's memory and storing things in it? Yeah? AUDIENCE: It stores the data contiguously.
12:28
DAVID J. MALAN: Perfect. So it stores the data contiguously back to back to back. And as we've seen thus far, when you allocate space for an array,
12:36
you typically do it with square brackets. You specify a number in those brackets or maybe a constant, like capacity, like I just did.
12:42
And that fixates just how much data you can actually store in there. We did see last week, though, that we could
12:48
start to use malloc to allocate an equivalent number of bytes. But even that, when you call it just once,
12:54
gives you back a specific finite number of bytes. So you're similarly deciding in advance how much memory you
12:59
can store in an array. So let's consider what kinds of problems this could get us into. So here's an array of size three.
13:04
And suppose for the sake of discussion we've already put three numbers into it 1, 2, and 3 literally.
13:10
Suppose now we want to add a fourth number to that array. Well, where does it go? Intuitively and pictorially, you'd like to think it could go there.
13:18
But remember the context we introduced last week when we talked about computers' memories. There's lots of stuff going on.
13:24
And if you only ask the computer, the operating system, room for three integers, who knows what's here and here and here,
13:32
not to mention everywhere else on the screen? So if we zoom out for instance, we might like to put the number four there.
13:38
But we can't if in that greater context there's a lot more stuff going on. So for instance, suppose that elsewhere in my same program or function
13:46
I've already created a string like H-E-L-L-O, comma, space, world, backslash 0.
13:52
Just by bad luck, that could be allocated right next to my 1, 2, 3. Why? Well, if I ask the operating system for space for three numbers,
13:59
then I ask the operating system for space for a string, it's pretty reasonable for the computer to put those things back to back,
14:06
because it's not going to anticipate for us that, well, maybe they actually want four numbers eventually or five numbers or more.
14:13
Now, as for all of these Oscars the Grouch, that's just meant to represent pictorially here the notion of garbage values.
14:19
There's clearly other bytes there and available. I don't know what it is. And I don't care what it is.
14:24
But I do care that I can't just presume to put something right where I want in the computer's memory unless I preemptively ask it for more memory.
14:33
Now, if all of those are garbage values, which is to say that who cares what they are-- it's just junk left over
14:38
from previous runs of the function or the like-- there's clearly plenty of room for a fourth number.
14:44
I could put the number four here or here or here or down here or here or here. But why would I not want to just plop the four wherever
14:51
there is a garbage value currently? Yeah? AUDIENCE: Because you want it to be next to your array of 1, 2, 3.
14:57
DAVID J. MALAN: Exactly, I want it to be next to my array of 1, 2, 3 because, again, arrays must be and must remain contiguous.
15:03
Now, that's not a deal breaker because where else could I put maybe the entire array?
15:09
Well, there's room up here for four numbers. There's room down here for four numbers. So that's fine. And that could be a solution to the problem.
15:15
If you've run out of space in your fixed size array, well maybe I just abstract everything else away,
15:20
and I just move my array to a different location that's a little bit bigger. But there is going to be a downside.
15:26
Even though this is a solution, even though I can certainly copy the 1, the 2, the 3-- and now I can plop the 4 there.
15:32
And, heck, I can then let go of the old memory in some way and give it back to the operating system to be reused later.
15:38
This is successful. But why intuitively might we not want this
15:44
to be our solution of creating a new array that's a little bigger, copying the old into the new, and getting rid of the old?
15:51
Good, yeah, I think I had one more step.
15:57
Suppose I want to add a fifth number, a sixth number. That's a lot of work. And, in fact, what's the expensive part or what's the slow part of that story?
16:04
Yeah? AUDIENCE: It takes a lot of time. DAVID J. MALAN: It takes a lot of time. But specifically, what's taking time if we can put our finger on it?
16:10
Yeah, in the back? AUDIENCE: You're using twice as much. DAVID J. MALAN: OK, for a period of time,
16:16
I'm using twice as much memory, which certainly seems wasteful because even though I don't eventually need it, it is going to mushroom
16:22
and then shrink back down, which seems like an inefficient use of resources. But what specifically is slow about this process too?
16:28
Yeah, in the middle. AUDIENCE: You're iterating through the original array to copy it over. DAVID J. MALAN: Yeah, good choice of words.
16:34
You're iterating over the array to copy it over using a for loop, a while loop. So it's probably like big O of n steps just
16:41
to copy the array and technically big O of n plus 1 if we had one more. But that's still big O of n. So it's the copying, the moving of the data, so to speak,
16:48
that's certainly correct. But maybe it's not the best design. Wouldn't it be better if we could do something otherwise?
16:55
Well, let's consider what this might actually translate into in code and what the implications then might be.
17:00
Let me switch over here to VS Code. Let me propose to open up a file called list.c brand new.
17:07
And let's create this list of numbers and then add to it over time and see when and where we actually bump up against these problems.
17:13
So let me include standard io.h in order to simply be able to print things out ultimately, int main void, so no need
17:21
for command line arguments here. Let me give myself an array called list just of size 3
17:27
for consistency with the picture thus far. And now let me go ahead and just manually make it look like in memory what it did on the screen.
17:34
So list bracket 0 is going to equal to number 1. List bracket 1 is going to equal the number 2.
17:40
And list bracket 2 equals number three. So even though the array is, of course, zero indexed, I'm using more familiar 1, 2, 3 as my digits here.
17:48
Now, suppose I want to print these things out. Let's just do something as a simple exercise. So for int i equals 0, i is less than 3 i plus plus.
17:58
Inside of this loop, I'm going to do something simple like print out iteratively, as you note, backslash n list bracket i.
18:07
So very simple program. It's not the best design because I've got this magic number there. I'm hard coding the 3.
18:12
But the point is just to go through the motions of demonstrating how this code works.
18:19
Good, you got it in before I hit compile. So wait. Thank you.
18:25
All right. Maybe round of applause. Thank you. [APPLAUSE]
18:30
All right. All right, so this is going to get aggressive, though, eventually. So let me add the semicolon.
18:36
Let me recompile this list. Seems to compile OK. And if I do ./list, I should see, of course, 1, 2, 3.
18:44
So the code works. There's no memory constraints here because I'm not trying to actually add some values. But let me consider how I could go about implementing this idea of copying
18:54
everything from the old array to the new array, frankly, just to see how annoying it is, how painful it is.
18:59
So you're about to see the code escalate quickly. And it will be helpful to try to wrap your mind around each individual step
19:06
even though if you take a step back, it's going to look like a crazy amount of code to solve a simple idea. But that's the point.
19:12
We're going to get to a place, particularly in week 6 where all of what we're about to do reduces to one line of code.
19:18
So hang in there for now. So let me go ahead and do this. If I want to create a version of this code that can grow to fit more numbers,
19:28
for instance, how can I go about doing this or at least demonstrate as much? Well, I cannot use an array in this traditional way of using square
19:37
brackets because that makes list, the variable, forever of size 3.
19:42
I can't free it. Remember free you can only use with malloc. So you can't give it back and then recreate it using this syntax.
19:48
But I can use this trick from last time, whereby, if I know there is this function called malloc, whose purpose in life
19:53
is to give me memory, I could, for instance re-declare list to be a pointer so to speak that is the address of a chunk of memory.
20:01
And I could ask malloc for a chunk of memory namely of size 3 but not 3
20:07
per se, three integers for good measure. So technically that's three times the size of whatever an int is.
20:14
Now, for our purposes today, that's technically 3 times 4 or 12. But I'm trying to do this very generally in case we use it
20:20
on an old computer or maybe a future computer, where the size of an int might very well change.
20:25
That's why I'm using size of int. It will tell me always the correct answer for my computer. So to use malloc--
20:31
not going to catch me on this one-- what header file do I need to add? Standard?
20:37
AUDIENCE: Standard lib.h. DAVID J. MALAN: Standard lib.h. So I'm going to go ahead and include standard lib.h, which
20:42
gives me access to malloc. And what I'm going to additionally do is practice what I preach last week, whereby in extreme cases malloc can return not the address
20:51
of an actual chunk of memory. What else can malloc return in cases of error? Yeah?
20:57
AUDIENCE: Null. DAVID J. MALAN: Null, N-U-L-L in all caps, which represents technically address 0.
21:02
But you're never supposed to use address 0. So it's a special sentinel value that just means something went wrong. Do not proceed.
21:08
So it's going to add some bulk to my code. But it is good practice. So if list at this point actually equals equals null,
21:14
there's no more work to be done here. I've got to abort the demo altogether. So I'm going to return 1 just arbitrarily
21:19
to say we're done with this exercise. It's not going to be germane for class. We can surely find room for three integers but best practice
21:25
whenever using malloc. Now, this code here does not need to change because list is now still
21:33
a chunk of memory of size 12, I can actually get away with still using square bracket notation
21:38
and treating this chunk of memory as though it's an array. And this is a bit subtle. But recall from last time, we talked briefly about pointer arithmetic,
21:47
whereby the computer can do some arithmetic, some addition, subtraction on the actual addresses to get from one location to the other.
21:54
And that's what the computer is going to do here. Because it says list bracket 0, that's essentially
21:59
just going to put the number 1 literally at the beginning of that chunk of memory.
22:05
And because this is a modern computer, it's going to take four bytes in total. But I don't want to put the number 4 here to shift it over myself.
22:12
Because I'm using square brackets and because the computer knows that this chunk of memory is being treated
22:19
as a chunk of addresses of integers, pointer arithmetic magically kicks in.
22:24
So what the computer is going to do for me is put this 1 at location 0. It's going to put this number 2 at location 1 times size of int, so 4.
22:34
And it's going to put this number 3 at location 2 times size of int, which gives me 8.
22:40
So in other words, you don't have to think about how big that chunk of memory is if you already gave the compiler a clue as
22:46
to the size. For our purposes today, don't worry too much about that. The bigger takeaway is that when you allocate space using malloc,
22:52
you can certainly treat it as though it's an array using week 2 notation, which is arguably simpler than using
22:59
dots and stars and all of that. But this isn't quite enough now because let me stipulate that for the sake of discussion,
23:05
at this point in time here on line 16, where the cursor is blinking, suppose I realize just for the sake of discussion,
23:13
oh, I should have allocated space for four integers instead of three. Now, obviously, if I were writing this for real,
23:19
I should just go fix the code now and recompile it altogether? But let's just pretend for the sake of discussion that somewhere in your program you want to dynamically allocate more space
23:28
and free up the old in order to implement this idea of copying from old to new memory.
23:34
So how could I do that? Well, let me go ahead and temporarily give myself another chunk of memory.
23:39
And I'm going to literally call it tmp for short, which is a common convention, tmp. I'm going to set that equal to the amount of space
23:46
that I actually do now want. So I'm to say four times the size of an int. So technically it'll give me 16 but space for four integers this time.
23:54
And what that's doing for me in code is essentially trying to find me space for four integers elsewhere
24:02
that might very well be garbage values now. But I can, therefore, reuse them. So once I've done this, something could still go wrong.
24:09
And I could check if temp equals equals null, then actually I should exit altogether and finish up.
24:15
But there's a subtlety here. And you don't need to dwell too much on this for today. But there is technically a bug right now.
24:22
Why based on week 4, last week, might it not be correct technically
24:28
to immediately return 1 and abort the program altogether at this point? AUDIENCE: I think when you allocate memory sometimes it has garbage values.
24:36
DAVID J. MALAN: OK, so when you allocate memory, sometimes there might be garbage values there that is true. But that is to say that those 16 bytes might be garbage values,
24:45
have Oscar the grouch's all on the screen. But tmp itself will literally be the return value of malloc.
24:51
And malloc will always return to you the address of a valid chunk of memory. Or it will return null.
24:56
So this line is actually OK. What I don't love is that I'm returning 1 immediately.
25:02
AUDIENCE: I think [INAUDIBLE]. DAVID J. MALAN: Yes, so this is where it's subtle.
25:07
It's not quite right to just abort right now and return 1. Why? Because up here, remember, a few moments ago
25:14
we used malloc presumably successfully. Because if we got all the way down here, we did not abort on line 9.
25:21
So we kept going. But that means we've allocated three times size event, so 12 bytes earlier.
25:26
So frankly, if you compile this code, run it, and then ask Valgrind, it's going to identify a memory leak of size 12 because, as you know,
25:34
we did not free the original memory. So this is where frankly C does get a little annoying because you and I as the programmers have to remember all of these details.
25:41
So what I really want to do here, before I return 1, to be best practice, I want to free the original list.
25:48
So I give back those bytes to the operating system. Now, as an aside, technically when any program quits, all of the memory
25:54
is going to be given back to the operating system. But practicing what I'm preaching now will get you into better situations
26:00
later. Because if you don't free up memory, you will have leaks. And that's when our own Macs and PCs tend
26:06
to start to slow down and use up more memory than they should. But let's avoid discussion of more error checking there.
26:13
Let's just assume that now I'm on line 23 of this program, whereby I have presumably successfully allocated
26:19
enough space. So the next step after allocating these four bytes is to, as you noted earlier,
26:24
iteratively copy the old numbers into the new space. So this is actually pretty straightforward.
26:30
I'm going to go ahead. And for int i gets 0, i is less than 3 i plus plus just
26:36
like I was printing last time. I'm going to go ahead and set the i-th location of temp
26:41
equal to the i-th location of list, semicolon. And that's it. I'm just copying into the temporary array whatever was in the old array.
26:51
But that still leaves me with this fourth byte, of course-- or, sorry, this fourth location, where I want to put the number 4.
26:58
But if I'm going to do that for the sake of discussion even though this isn't really a compelling real world program,
27:03
I'm going to just manually go into the last location in tmp, a.k.a.
27:08
tmp bracket 3 and set that equal to my fourth number. So that's all.
27:13
The whole point here is to mimic in code what it was we wanted to do here. But now there's one more step.
27:20
What was the next step after copying the 1, the 2, the 3, and adding the 4? What do I want to do?
27:25
Now, I can safely free the list. Now I want to go ahead and get rid of the original memory or at least hand it back to the operating system.
27:32
So here is where I can free the list, not in the case of an error but actually deliberately free the original list because I
27:40
don't need those 12 bytes anymore. But now if I want to really have quote, unquote list
27:46
point at this new chunk of memory, well, then I could also do this, list equals temp.
27:53
So this is a little weird. But recall that list has just now been freed. So even though list technically contains the address of a chunk of memory,
28:00
it's no longer valid because, again, it was freed. So, yes, it's still technically there. But it's effectively garbage values now.
28:06
So I'm certainly free-- no pun intended. I'm certainly allowed to update the value of list.
28:11
And I want list to now point to the new chunk of memory. So sort of metaphorically, if list was originally
28:17
pointing at a chunk of memory there, maybe now I want it to point over here. So I'm just updating the value of list ultimately.
28:24
All right, now that I've got this all done, I think I can just use this same loop as before. I could change the 3 to a 4 because I now have four numbers.
28:32
At the very bottom of this program though, also subtle, I should probably now at the very end free this list.
28:38
And for good measure, let me go ahead and return 0. But now I think I have a complete program that, again,
28:44
to be clear is not how you would write this in the real world because you would not allocate three integers then
28:52
decide you want to allocate four then fix all of this. But we could probably borrow, copy and paste some of this code into production code eventually, whereby this would
28:59
solve some actual problems dynamically. So let me cross my fingers, make list. So far so good, ./list.
29:06
And I should see 1, 2, 3, 4. So long story short, it's a lot of work just to get from the original array
29:14
to the second. So ideally, we would not do any of this in the first place. Ideally, what could we do instead?
29:21
Well, maybe we should just allocate more memory from the get go in order to avoid this problem altogether.
29:27
So how might I do that? Well, instead of having allocated an array of size 3, let alone an array
29:33
of size 4, why don't I just proactively from the beginning of my program allocate an array of size 30 or heck 300 or 3,000
29:41
and then just keep track of how much of it I'm using? That would be correct. It would solve the problem of not painting yourself into a corner
29:50
so quickly. But what remains as an issue? AUDIENCE: You're using a lot of memory. DAVID J. MALAN: I'm using a bunch more memory.
29:56
Especially if this program's only going to ever manage a few numbers, why are you wasting 100 times more memory than you might actually?
30:03
And there's an another corner case that could still arise even though this solves the problem. AUDIENCE: If you add another list, you'll run out of memory.
30:10
DAVID J. MALAN: Exactly, we can eventually still run into the exact same problem because if I want to put 301 numbers in the list or 3,001, well,
30:17
I'm still going to have to jump through all of these hoops and reallocate all of that space. And, honestly, now per year concern about the looping, iterating 300 times
30:26
3,000 times is certainly eventually going to start to add up if we're doing it a lot in terms of speed and slowdown.

## [Linked Lists](https://youtu.be/0euvEdPwQnQ?t=1833)

30:33
So maybe there's a better way altogether than doing this. And indeed there is if we start to treat our computer's memory as a canvas
30:41
that we can start to use to design data structures more generally. Arrays are a data structure, arguably.
30:46
They're super simple. They're contiguous chunks of memory. But we could use memory a little more cleverly, especially now per last week
30:53
that we have pointers, which is painful as they might be to wrap your mind around sometimes. They really just let us point to different places in memory.
31:01
And so we can start to stitch things together in an interesting way. So the only syntax we'll really need to do that to stitch things together
31:11
in memory and build more interesting structures are these things, struct, which allows us to represent structs already.
31:17
And we did this with persons. And we played with this last time as well. And we saw it already for queues and stacks.
31:23
The dot operator, we haven't used it that much. But recall that whenever you have a struct, you can go inside of it using the dot operator.
31:30
And we did that for a person, person.name and person.number when we were implementing a very simple address book.
31:36
The star was new last week. And it can mean different things in different contexts. You use it when declaring a pointer.
31:43
But you also use it when dereferencing a pointer, to go there. But just so you've seen it before, it actually
31:49
tends to be a little annoying, a little confusing to use star and dot together. You might remember one example last week where in parentheses I
31:56
put star something. And then I used a dot operator to go there and then go inside the structure.
32:02
Long story short, we'll see today that you can combine simultaneous use of star and dot
32:07
into something that actually looks like an arrow, something that vaguely looks like a foam finger that might be pointing from one place
32:14
to another. So we'll see that actually in some code. So where can we take this?
32:20
Well, let's implement the first of these ideas, namely something that's very canonical in computing known as a linked list.
32:28
And let's see if we can maybe do this. How about Scully, could we get you to come on up and volunteer here?
32:35
So our friend Scully-- there's some cookies in this for you. So Scully has come prepared with a whole bunch of balloons
32:41
to represent chunks of memory because we'd like to paint a picture here of what's involved in actually allocating space that's not necessarily
32:48
contiguous and might be over there or over here or over here in the computer's memory. So, for instance, if I want to start allocating space
32:56
one at a time for a list of numbers, Scully, could you go ahead and malloc one balloon for me?
33:01
And in this balloon I'll store for instance, the number one ultimately. So we have a balloon here.
33:07
We rehearsed this before. And these balloons are actually really hard to blow up and tie off quickly. So thank you. So here we have a chunk of memory.
33:13
And I could certainly for instance go in here and store if I might the--
33:19
here we go. I could certainly go ahead here and store in this balloon, for instance, the number one.
33:24
But in the world of an array, it would just be back to back to back. And actually, frankly, why do we need the balloons even?
33:30
I could just use these numbers, 1, 2, 3. But the problem doesn't indeed arise note, that when we want to put a fourth number, well where does it go?
33:37
Well, again, just to paint a picture, ideally I might allocate space for four.
33:42
But if this is my array of size 3 like where does it go? This is the point. We can't just put it next to the 3.
33:49
Maybe there's room for the 4 over here. But we have to somehow connect these from one to the other.
33:54
So, in fact, let's act that out. So if I instead use this balloon metaphor of just allocating space from wherever it is, can you go ahead and allocate
34:01
like another chunk of memory for me? And here is where I'll now have a chunk of memory in which I can store
34:07
the number computers a little slow. So in here, the second balloon I'll have a separate chunk of memory.
34:15
AUDIENCE: Oh my gosh. DAVID J. MALAN: There we go. OK, good. Second chunk of memory, thank you, Scully.
34:24
Now, I can certainly-- Thank you. I can certainly now store the number two in this chunk of memory.
34:33
But it's not necessarily contiguous. This chunk came from over here as per Scully's position originally. This chunk obviously is coming from over here.
34:39
And if you don't mind holding that for a moment, this is breaking the metaphor of an array, which was indeed contiguous.
34:45
And even though I as the human can certainly go over and walk next to her, that's the equivalent of copying values from one place to another.
34:51
What if we're a little more clever, though? And if Scully found space for this number one over here, let's just leave this balloon here.
34:57
And if she found space for the number 2 over there, let's leave that balloon there. But we do somehow have to connect these numbers together.
35:05
And here is where to-- I'll try to do this on the fly. Maybe I could do something like this. I can take this balloon here.
35:11
And I can actually tie a string to it so that if I want to connect one to the other, we can link these, if you will, together.
35:20
And so here now I have a linked list that is not necessarily contiguous. There's a whole bunch of memory that may very well have real values,
35:27
may very well have garbage values. But I've somehow now linked these two together. And maybe just as a final flourish, if we could blow up one more balloon
35:35
to represent more space-- and now she's finding room for that balloon over there.
35:41
Nice. This one is a Yale chunk of memory. So now I'll need one more link, if you will.
35:51
And if I actually connect these two in this way, let me go ahead and tie this off here.
35:58
Now I can go ahead and connect these two. If you never see this demonstration again in next year's videos,
36:05
it's because this did not go very well. Here now we have the number one where we first malloced it,
36:11
the number two roughly where we malloced it, and the number three-- OK, so maybe we'll fix this some other year.
36:17
Now, we'll have the number 3 allocated there. But the whole point of this silly exercise is that we can certainly use the computer's memory as more of a Canvas,
36:25
put things wherever we want, wherever is available so long as we somehow
36:31
connect the dots, so to speak and can make our way from one chunk of memory to the next to the next, thereby literally linking them together.
36:39
But, of course, we're using balloons for this metaphor. But at the end of the day, this is just memory. So how could we encode one chunk to another chunk to a third chunk
36:49
might you think? What's the trick? Yeah? AUDIENCE: Pointers. DAVID J. MALAN: Using pointers. That's why we introduced pointers last week.
36:55
Because as simple as an idea as it is, as hard as it is to write sometimes in code, it's literally just a pointer, a foam finger pointing to another chunk of memory.
37:04
And so these pointers really are metaphorically being implemented now in with these pieces of string. So we'll have to debrief later and decide if we ever do this demo again.
37:12
But thank you to Scully for participating.
37:17
OK, we have plenty of-- OK, fair's fair.
37:23
There we go. Thank you Scully. So let's now actually translate this to something a little more concrete
37:28
and then get to the point where we can actually solve this problem in code. So here's that same canvas of memory.
37:34
And if in this canvas of memory now I actually want to implement this idea of the number 1, the number 2, the number 3,
37:40
let's stop tying our hands in terms of expecting our memory to be contiguous back to back and start to move away from using arrays.
37:47
So, for instance, suppose I want a malloc space for the number 1 just as I first asked of Scully.
37:53
Suppose it ends up over there on the board. The important thing for discussion here is that that number one, wherever it ends up, is surely located at some address.
38:01
And for the sake of discussion as in the past, suppose the number one just ends up at location 0x, 1, 2, 3.
38:07
So 0x, 1 2, 3 is where Scully was originally standing right here. Then we asked for malloc for another chunk of memory.
38:13
Suppose that it ends up over here at address 0x, 4, 5, 6. So that's maybe roughly here when Scully was standing in her second position.
38:21
Lastly, we allocate the number 3. Maybe it ends up at location 0x, 7, 8, 9, which was again per Scully's third malloc roughly over here on stage.
38:30
Now, this picture alone doesn't seem to lend itself to an implementation of the string, metaphorically, to the pointers
38:37
unless we allow ourselves a new luxury. Instead of just storing the number 1, 2, 3 in our usual squares,
38:47
I think what I'm going to have to do is cheat and use more memory to store what? The pointers as you proposed.
38:53
So here's a trade off that I promised we would start to see more and more if you want to improve your performance in terms
39:01
of time and avoid stupid copying of data from one place to another again and again and again.
39:06
If you want to save time, you're going to have to give up some space. And there's going to be this trade off between time and space.
39:12
And it's up to you to decide ultimately which is more important. So if you allow yourself not enough memory for the numbers 1, 2 and 3
39:19
but twice as much memory for the numbers 1, 2, and 3 and three pointers, one for each, what could we now do?
39:26
Well, if this node-- and this is a computing term. Node is just a generic term describing a box of memory, a chunk of memory
39:33
in this case. If I've given you this blank slate here, what value would make sense to store here if it's associated with this number one?
39:44
Yeah? AUDIENCE: Maybe the address of the next element. DAVID J. MALAN: Good, maybe the address of the next element.
39:49
So the next element technically is supposed to be the number 2. So at this location, I'm going to store the value 0x, 4, 5, 6.
39:56
What then logically should go here in the second box? 0x, 7, 8, 9.
40:02
And then here's a little non-obvious-- it's the end of the list as of now. So we can't afford to let it be a garbage value
40:08
because a garbage value is a value. And we don't want Oscar to effectively be pointing to some random location
40:14
lest we go there. So what would be a good special value to put here to terminate a list?
40:19
So null, so not null, which we used for strings but same idea, N-U-L-L,
40:24
which we keep using now for pointers, otherwise known as the 0 address, which I could just write for shorthand as 0x0 in this case,
40:32
which is the same thing as null. So here then, even though we've changed nothing about how a computer works--
40:38
this is just my computer's memory-- I'm using more memory now to effectively link one chunk, to the next chunk,
40:45
to the next chunk. So easy, just to note that the downside is more space. But now we don't have to worry about ever copying and moving this data
40:54
around, which maybe over time for really big programs big data sets could very well be a net positive and a win for us.
41:02
So any questions first on this notion of what a linked list actually is?
41:09
No, all right, well, recall from last time too that rarely do we actually care what the specific addresses are.
41:15
So this is one node, two node, and three nodes. And inside of each of these nodes is two values, the actual number
41:21
we care about and then a pointer. And now this is actually an opportunity to introduce a term
41:26
that you might see increasingly nowadays, data, so 1, 2, and 3, which we obviously care about in this case.
41:31
And then we could actually refer to these pointers more generally as metadata. It's actual data because it's helping me solve a problem, get from one
41:39
place to another. But metadata is distinct from data in that I don't fundamentally care about the metadata.
41:44
That's an implementation detail. But it does help me organize my actual data. So this is more of a high-level concept.
41:51
So what, though, is a linked list? It turns out the store linked list will generally use just one more value.
41:57
And I'm going to draw it only as a square, a single box, because if I declare now in my code, as I soon will,
42:03
a variable maybe called list that points to a node, this
42:08
is effectively how I could implement a linked list. I use one node per value.
42:13
And I use one extra pointer to find the first of those nodes.
42:18
And, in fact, here again is where I don't need to care fundamentally where any of these addresses are. It suffices to know that, yes, computers have memory addresses.
42:27
So I could just abstract this away. And this is how I might pictorially represent a linked list, a cleaner version of those three balloons,
42:34
whereby I was here. This was Scully's first balloon, second balloon, third balloon.
42:39
These arrows now just represent pointers or strings with the balloons. So with that said, how can we go about translating this to some actual code?
42:49
Well, here's where we can call into play some of that same syntax from last time and even a couple of weeks ago when we introduced the notion of a structure.
42:58
So here for instance is how we defined a couple classes ago the notion of a person? Why? Well, C doesn't come with a person data type.
43:05
But we concluded it was useful to be able to associate someone's name with their number and maybe even other fields as well.
43:11
So we typedef'd a structure containing these two values. We learned last week that string is technically char star.
43:17
But that doesn't change what the actual structure is. And we call this struct a person. Well, here's what we revealed last time, again taking those training wheels off.
43:26
It's just a char star. Let's keep going in this direction, though. If I want to define not a person but maybe more generically
43:32
something I'll call today a node, like a container for my numbers and my pointers, well, I similarly
43:38
just need two values, not a name and a number, which isn't relevant today but maybe the number as an actual int
43:44
so I can store the 1, the 2, the 3, the 4 and so forth. And this is a little less obvious.
43:50
But conceptually, what should be the second value inside of any of these nodes?
43:55
Yeah? So indeed a pointer. A pointer to what, though? AUDIENCE: Another node. DAVID J. MALAN: A pointer to another node.
44:01
And here's where the syntax gets a little weird. But how do I define there to be a pointer in here to another node?
44:10
Well, you might be inclined to say node *next because this means next is
44:15
the name of the property or the attribute the variable inside the struct. Star means it's a pointer. What is it a pointer to?
44:21
Clearly a node. But here's where C can bite you. The word node does not exist until you get to this last line of code.
44:29
C goes top to bottom, left to right. So you literally can't use the word node here if it's not existing until here.
44:36
The simple fix for this is to actually use a slightly more verbose way of defining a structure. You can actually do this.
44:42
And we didn't bother doing this with person because it didn't solve a problem. But if you actually make your first line a little more verbose
44:48
and say, give me a definition for a structure called node, now in here
44:54
you can actually do this. This is an annoying implementation detail
44:59
when it comes to implementing structures in C. But, essentially, we're leveraging the fact that because C code is read from top to bottom
45:05
if you give this structure a name called struct node, now you can refer to it here.
45:10
But you know what? It's annoying to write struct node, struct node, struct node everywhere in your code. So this last line now just gives you a synonym.
45:17
And it shortens struct node to just node. So long story short, this is a good template
45:23
for any time you implement some notion of a node as we will today. But it's fundamentally the same idea as a person
45:29
just containing now a number and a pointer to the next as opposed to someone's name and phone number.
45:35
So let me go ahead and walk through with some code how we might actually implement this process of allocating a balloon
45:43
and putting a number on it, allocating another balloon and putting a number on it and then connecting those two balloons again
45:49
and again. So we'll do this step by step in a vacuum so you can see the syntax that maps to each of these ideas.
45:55
Then we'll actually pull up VS Code and combine it all and make a demonstrative program. So here, for instance, is the single line of C code
46:03
via which I can give myself the beginning of a linked list that is a pointer that will eventually be pointing to something.
46:10
So metaphorically, it's like creating a pointer. I know we've gotten some complaints about that in the audience.
46:15
We'll use the Harvard one to represent a pointer to something. But if I only do this and I only say give me
46:22
a variable called list that is a pointer to a node, that's going to leave a garbage value.
46:28
So this is like pointing to some random location because it's previously some value. Who knows what it is.
46:33
But we can solve that how? What would be a good initial value to set this equal to?
46:39
So null. At least if it's null, we then know that this isn't a garbage value. This is literally 0x0, a.k.a. null.
46:46
And I'm just going to leave it blank for cleanliness. So this would be the right way to begin to create a linked list of size 0.
46:53
There's nothing there. But at least now that foam finger is not pointing to some bogus chunk of memory,
46:58
some garbage value. So this is how the world might exist now in the computer's memory. How do I go about allocating space now for a node?
47:06
Well, it's just ideas from last week. Once the word node exists as via that typedef,
47:12
I can just use malloc to ask for the size of a node. I don't have to do the math myself.
47:17
I don't care how big a node is. Just let it do the math for me. Then that's going to return presumably the address of a chunk of memory
47:24
big enough for that big rectangle. And I'm going to store that for now in a temporary variable called n
47:30
that itself is a pointer to a node. So this might look like a lot altogether. But this is just like before when I allocated space for a string
47:39
or I allocated space for a bunch of numbers and set it equal to a pointer to integers, for instance, [INAUDIBLE]
47:45
recently. All right, so this gives me a box in memory. This gives me a pointer called n.
47:52
So it's similarly just a single square because it's just an address. And it similarly gives me a bigger chunk of memory
47:57
somewhere in the computer's memory containing enough space for the number that's going to go there, a 1, a 2, or 3, or whatever,
48:04
and a pointer to the next value. So these lines of code collectively, this half creates this in memory.
48:10
This half creates this in memory. And the assignment here, the equal sign, essentially
48:15
does the equivalent of that. I don't care what the address is, the actual number. It's as though n is now pointing to that chunk of memory.
48:22
But this isn't very useful. If I want to store the number 1 here, with what code can I do that?
48:27
Well, I could do this, borrowing an idea from last week. So *n presumes that n is a pointer.
48:34
\*n means go there, go to whatever you're pointing at. The dot operator means if you're pointing at a structure,
48:41
go inside of it to the number field. And we did this a couple of weeks ago with number and person
48:47
when we implemented an address book. So star n is go there. And the dot operator means go to the number field.
48:53
The one on the right hand side and the equal sign means set whatever is there equal to the number 1.
48:58
It turns out this is the syntax, though, that I alluded to being a little bit cryptic and not very pleasant to remember
49:04
or type. Here, though, is where you can synonymously instead use this line of code, which most C programmers would use instead.
49:11
This means n is still a pointer. The arrow literally with a hyphen and a greater than sign means go there.
49:18
It's the exact same thing as the parentheses with the star, with the dot. This just simplifies it to look like these actual pictorial arrows.
49:26
So this would be the most conventional way of doing this. How now do I update the next field? Well, I think I'm going to just say the same thing,
49:33
n go there but go into the next field and set it equal to null.
49:39
Why null? If the whole point here was to allocate just one chunk of memory, one node,
49:44
you don't want to leave this as a garbage value because that value will be mistaken for an arrow pointing to some random location.
49:51
All right, that's a lot. And, again, we're doing it in isolation step by step just to paint the picture on the screen. But any questions on any of these steps?
50:01
Each picture translates to one line of code there. All right, so if you're comfy enough with those lines there,
50:10
what can I proceed to now do? Well, let me propose that what I could now do with this same approach
50:18
is set list itself equal to n. Because if the whole goal is to build up a linked list, and list represents that linked list, list
50:25
equals n is essentially saying whatever address is here, put it here. And pictorially what that means is, temporarily point both pointers
50:32
to the same exact place. Why? Because this is the list that I care about long term. This is maybe my global variable that I'm going to keep around forever
50:39
in my computer's memory. This was just a temporary pointer so that I could get a chunk of memory and go to its locations and update it with those values.
50:46
So, eventually, this is probably going to go away altogether. And this then is a linked list of size 1.
50:51
This is what happened when Scully inflated one balloon, I wrote the number 1 on it, and I pointed at that single balloon.
50:58
All right, if I want to go ahead and do this again and again, we'll do this a little more quickly. But it's the same kind of code for now.
51:05
Here's how I allocate space for another node. Here's how I can temporarily store it in n.
51:10
And I'll re-delcare it here just to make clear that it's indeed just a pointer. So the left hand side of the expression gives me this.
51:15
The right hand side of the expression gives me this. Where could it be? I mean, I put it here. It could have been there. It could have been anywhere else.
51:21
But malloc gets to decide that for us. n equals this, just sets that temporary pointer equal to that chunk of memory.
51:28
I should clean this up. How do I now put the number 2 into this node? Well, I start at n.
51:34
I go there. I go to the number field, which I keep drawing on top. And I set it equal to 2.
51:39
Now, it's a little non-obvious what we should do here. So I'm going to be a little lazy at first.
51:45
And rather than put these numbers into the linked list in sorted order, like ascending order 1, 2, 3, 4, I'm just
51:51
going to plop it at the beginning of the list. Why? Because it's actually a little simpler. Each time I allocate a new node, I just prepend it,
51:58
so to speak, to the beginning of the list even though it's going to end up looking backwards in this case. So, notice, at this point in the story, I've
52:05
got list pointing to the original linked list. I've got n pointing to the brand new node.
52:11
And, ultimately, I want to connect these just as Scully and I did with the strings.
52:16
This is just temporary. So I want to connect these things. Here's how I could do it wrong. If I proceed now and update, rather, after one more line setting this equal
52:25
to null-- sorry, let's at least get rid of that garbage value-- here's how I could proceed to maybe do this wrong.
52:31
Let me go ahead and update, for instance, list equals n. So if I update list equaling n, that's going
52:40
to point the list at this new node. But what has just happened?
52:47
What did I do wrong? Yeah? AUDIENCE: Nothing's pointing to 1. DAVID J. MALAN: So nothing's pointing to 1. And even though you and I obviously have this bird's eye view of everything
52:54
in the computer's memory, the computer doesn't. If you have no variable remembering the location of that node, for all intents and purposes, it is gone.
53:00
So what I've essentially done is this. When I update that pointer to point at the number 2, it's as though--
53:05
this was a much nicer idea in theory when we talked about it. But it's not really working. But this is effectively what we've tried to achieve, which is I've orphaned,
53:13
so to speak, the number 1. And that too is a technical term in the context of memory. If no one is pointing at it if no string is connected to it,
53:20
I have indeed orphaned a chunk of memory, a.k.a. a memory leak. And Valgrind would not, in fact like this.
53:25
And Valgrind would, in fact, notice this. So what would be the better approach?
53:31
Let me rewind. Instead of updating that address to be that of this node, let's rewind to where we were a moment ago where list is still
53:39
pointing at the original, n is still pointing at the new chunk of memory. And what should I do instead? Well, what should I do is maybe this.
53:46
Let's go to the next field of the new node. So follow the arrow.
53:52
Go to the next field. And what should I put here instead? Why don't I put the memory address of the original node?
54:00
How can I get that? Well, that's actually this. So if list is pointing at the original node, I can just copy that address into this next field,
54:08
which has the effect of doing that, albeit in duplicate. I've updated the next field to point at the very thing
54:15
that the original list is already pointing at. And now for the sake of discussion, let me get rid of my temporary node called n.
54:22
And what you'll see, ultimately, is that once we set list equal to n and get rid of it, now
54:30
we can just treat the whole linked list as being connected and linked this way.
54:37
How do we do this? Again, we won't belabor the point with more. But suppose I want to allocate a third node. I have to do the exact same thing.
54:43
But I have to update this next field to point at the existing list before I update list itself.
54:49
Long story short, order of operations is going to be super important. And if I want to stitch these data structures together,
54:55
I would encourage you to think ultimately-- certainly when it comes time to write something like this, think about what it is that we're actually trying to tie together.
55:04
So let me go ahead and do this. I'm going to go over to VS Code here. I'm going to delete the old code for list.c.
55:10
And perhaps now we can transition away from our old approach and actually do something with these pointers instead.
55:18
So I'm going to go ahead, and let's say #include as before, #include standard io.h.
55:26
Let's go ahead and include standard lib.h proactively. And let's go ahead and create that data type.
55:31
So typedef a struct called node. And inside of this node, let's give us an integer called number
55:38
to store the 1, the 2, the 3, the 4. And then let's create a struct node star value called next whose purpose in life
55:44
is going to point to the next node in any such list. I'm going to shorten the name of all of this to just node simply.
55:51
And then in main, let's go ahead and do this. We'll bring back our friend argc and argv
55:56
so that I can actually implement a program this time that lets me construct a linked list using numbers that I just passed at the command line.
56:02
I don't want to bother with getInt again and again or the CS50 library. So let's just use argc and argv.
56:10
But with argv, recall string now as of last week is synonymous with char star. So that's the exact same thing as we've used in week 2 onward for command line
56:20
arguments. So what do I want to do? My goal in life with this demonstration is to create and code this linked list here or at least the beginnings thereof.
56:30
So how can I do this? Let me go back into VS Code. Let me declare a linked list called list but initialize it to null.
56:37
So there's nothing there just yet. How now can I go about building this linked list?
56:44
By taking numbers from the command line. So let's do this. For int i equals 1, i is less than argc i plus plus, let me go ahead
56:55
and do this. I'm going to go ahead, and just for the sake of discussion, let me print out where we're going with this.
57:02
Let me go ahead and print out %s backslash n whatever is in argv bracket
57:07
i. So I'm not doing anything interesting yet. But let's just demonstrate where we're going with this.
57:13
Let me go ahead and make list, ./list. And let me put the numbers 1, 2 and 3 as command line arguments.
57:20
Enter. There, we just have those numbers spit out. I'm just jumping through this hoop to demonstrate how I'm getting those values.
57:26
But notice the values in argv are always strings, a.k.a. char star. So if I actually want to convert a string to an integer like this,
57:37
how can I do this? I want to set the number variable equal to argv bracket i.
57:43
But argv bracket i is a string. How can I convert a string to a number anyone recall?
57:49
Yeah? AUDIENCE: Atoi. DAVID J. MALAN: Atoi, so ASCII to I, so ASCII to integer.
57:54
So if I do atoi, I can actually convert one to the other in this way.
58:00
And now I can actually print this as an int instead of a string. Now, that's not going to change the aesthetics of the program
58:06
if I print it out again. But it does, in fact, give me an integer to work with. But let's not bother printing it.
58:12
Let's instead put this number and any other number at the command line into a linked list.
58:18
So let me go ahead and allocate a pointer called n. Let me set it equal to the return value of malloc
58:25
asking malloc for the size of one node. Ideally that will give me a chunk of memory
58:31
that can fit this number and a pointer. Just for good measure, I'm going to check, well, if n equals equals null,
58:38
then actually this isn't going to work. So we should probably free memory thus far.
58:44
So I'm just going to leave this like this because there's a few steps involved. So free memory thus far.
58:51
And then we can go ahead, for instance, and return 1. All right, if now I don't have an error and n is not in fact null,
58:59
but it's a valid address, I can go into n. I can follow that pointer to the number field
59:05
and set it equal to the actual number. So this is a little strange at first glance that I've got number on the left and number on the right.
59:11
But they're different. n is currently pointing at a chunk of memory big enough to fit a node.
59:17
n arrow number means go to that chunk of memory and go to the top half of the rectangle and update that number
59:24
to be whatever the human typed in after we've converted it on line 16 here to an actual integer.
59:31
All right, what next do I do? n arrow next should probably be at this point initialized to null.
59:39
And how now do I actually add this node n to my original linked list?
59:44
Well, I could just do list equals n. And that would update a la the foam finger my list variable
59:51
to point at this new node. But we said before that that's potentially bad. Why? Because if list is already pointing at something,
59:59
we can't just blow kindly change what it's pointing at because we'll have orphaned any previous numbers. It's not relevant at the moment because we're still
1:00:05
in the first iteration of this loop. But we don't want to orphan or leak any memory. So what do I first want to do?
1:00:11
Before I actually point the linked list at that new node, I'm going to instead say, go to this current node, arrow, next,
1:00:21
and actually set that equal to list. So strictly speaking, I don't actually need to initialize it to null.
1:00:27
I can initialize the next field of this new node to point at the existing list.
1:00:34
So what I'm going to do here is, instead of initializing the next field equal to null, if I want to insert this new node in front of any nodes that
1:00:42
already exist, I can simply say set the node's next field equal to whatever
1:00:48
the list currently is. And now in this last line I can update the list itself to point to n.
1:00:53
So after this, let's just go ahead and do something relatively simple even though the syntax for this is going to look a little complicated at first.
1:01:00
How do I go about printing the whole list? So print whole list.
1:01:06
Well, there's a couple of ways to do this. But if you imagine a world-- if we fast forward to a world in which we now have a linked list of size 3, for instance,
1:01:14
here's where we might be at some point in the computer's memory. We've inserted the 1. Then we inserted the 2.
1:01:20
Then we inserted the 3. But because we're prepending everything, it actually looks like 3, 2, 1. So how could I go about printing this?
1:01:26
Well, ideally, I could do this. If a computer can only look at one location at a time, I can grab my foam finger and point at the 3 and print it out, point at the 2
1:01:36
and print it out, point at the 1 and print it out. And then because this is null, I'm all done pointing and printing.
1:01:42
But how can I translate this to actual code? Well, I could implement that foam finger, so to speak,
1:01:47
in the following way. I could give myself a pointer often abbreviated by computer scientists as ptr, specify that that's indeed a pointer to a node, as per that star,
1:01:57
and initialize that pointer to be the list itself. So this is the code equivalent of, if I have this same picture on the screen,
1:02:05
declaring a pointer variable and point it at whatever the list itself is storing first.
1:02:12
And, now, that's akin to doing this. If I now go back into my code, how can I do this?
1:02:19
Well, so long as that pointer does not equal null-- that is, so long as that pointer is not at the end of the list,
1:02:25
let me go ahead and print out using printf an integer with percent i.
1:02:31
And then let's print out whatever I'm currently pointing at in ptr arrow number.
1:02:37
So whatever I'm pointing at, go there and print the number that you find. After that, what do I want to go ahead and do?
1:02:44
I'm going to set pointer equal to pointer arrow next. So what does this mean?
1:02:50
If I go back to my picture here and I want to actually walk through this thing, that first line of code
1:02:56
ensures that this foam finger, a.k.a. ptr, represented here, is pointing at the first element of the list.
1:03:02
Once I've printed it out with printf, I'm then doing pointer equals pointer next, which is following this next arrow.
1:03:10
So ptr now points at the 2. I then print that out and set pointer equal to pointer next.
1:03:16
That's like following this arrow and updating pointer to point at this node instead. At that point, the next step is going to be to point it to null.
1:03:24
So for all intents and purposes, I'm done. And that's why we can actually get away with this while loop
1:03:30
because while pointer is not null, it's going to print and print and print.
1:03:36
Now, let me go into my terminal window. Let me go ahead and make list and really hope I didn't make any mistakes because this was a lot all at once.
1:03:43
Seems to have compiled OK. When I run ./list of 1, 2, 3--
1:03:48
theoretically, this code is correct, should unbeknownst to me build up an entire linked list in memory.
1:03:53
But what's it going to print out ultimately? What do you think it's going to print?
1:03:59
Yeah? It could print out null if I really screwed up, yes.
1:04:05
What else? AUDIENCE: 3, 2, 1. DAVID J. MALAN: Or it could print out 3, 2, 1. And frankly, that's what I'm hoping for.
1:04:10
So even though I've given it in argv 1, 2, 3, because I'm prepending to the beginning of the list, the beginning of the list,
1:04:18
beginning of the list each time, I think, indeed, we're going to see 3, 2, 1. Now, that's fine.
1:04:24
That's correct. But it's not necessarily what we might want. So how could we actually go about inserting things maybe?
1:04:32
Otherwise, because, in fact, if we consider this algorithm, what's the running time insert?
1:04:38
How many steps are required right now, given a linked list of size n if you want to go ahead and insert one more node--
1:04:43
there's actually a reason I took this lazy approach of prepending prepending. In big O notation, how much does it cost us to insert into a linked list?
1:04:53
Think about it this way. Does it matter how many nodes are already
1:05:00
in the linked list, whether it's 1 or 2 or 3 or 300 or 3,000. If you're prepending, it doesn't matter how long
1:05:06
that chain is, you're just constantly putting it at the beginning, at the beginning, at the beginning. Now, how many steps is this?
1:05:12
I don't know exactly. I'd have to count the lines of code. But it's some small number. It's like two steps, three steps. How many lines of code is it?
1:05:18
It's very few to prepend, prepend. So I would dare say that the running time of insertion into a linked list
1:05:27
is actually constant time. It's big O of 1. And that's super fast because it doesn't matter how big the list is. Boom, boom, boom, you've prepended to the list.
1:05:35
But there's a flip side. What's the running time of searching a linked list, looking for something in it, finding a number in it?
1:05:43
Well, if it looks like this, how long does it take you to find some arbitrary number that the human might ask you for?
1:05:50
How many steps will it take to find me the number 1 if it's there? So big O of n-- because in the worst case, the number you're looking for
1:05:56
might be all the way at the end. And even though you and I, again, have this bird's eye view, and we can obviously see where the 1 is, the only way we can get to the 1
1:06:03
is by starting at the 2. How do you get to the 2? You got to start at the 3. How do you get to the 3? You've got to start at the beginning of the list itself.
1:06:11
And so whereas in the world of arrays where you had this contiguous chunk of memory, just like we had lockers on the stage weeks ago,
1:06:16
and you could jump to the middle and then the middle of the middle and the middle of the middle. That was all predicated on contiguousness.
1:06:23
Why? Because if you know where the first locker was, and you know where the last locker was, you can substract one
1:06:29
from the other, divide by 2, and, boom, you get the index or the location numerically of the middle locker.
1:06:35
And you can do that again and again. I cannot do any such math here. The middle of this linked list is obviously here.
1:06:42
But it doesn't matter what the location of this one is in memory. It doesn't matter what the location of this
1:06:47
is in memory because they could be anywhere in the computer's memory. So you can subtract one from the other, divide by 2,
1:06:52
and that's going to put you in some random location because these chunks of memory are not back to back to back to back.
1:06:58
They're every which way. So this is to say, what algorithm from week zero can we not use on linked lists?
1:07:05
So binary search. So that very algorithm we started the class with was all predicated on contiguous chunks of memory, like an array.
1:07:13
The problem with an array of course, though, is that you paint yourself into this corner. And you have to in advance how many locations you want.
1:07:20
And if you round up, you're wasting space. If you round down, you're wasting time. So you're screwed either way.
1:07:26
A linked list avoids those problems. It's more of a dynamic data structure that can grow. And frankly, if we code it up, it could even shrink.
1:07:32
We could remove these nodes back and forth. And so we're not necessarily wasting time on insertion,
1:07:39
but we are on searching this thing. We're back to Big O of n when it comes to searching a linked list as opposed
1:07:45
to it being log n, which was much, much better. So the upside of prepending the nodes in this way
1:07:52
is that we have constant time insertion of new nodes because we just continually insert, insert, insert into the very beginning of the list.
1:07:58
Of course, a side effect of this is that the numbers might end up in completely reverse order as they have here
1:08:04
because I first inserted 1. But then I prepended 2. And then I prepended 3. Well, we could perhaps take a completely different approach
1:08:11
and append the nodes upon insertion instead. So, for instance, if I start off with an empty list, I could then insert 1.
1:08:17
I can insert 2. And I can insert 3. And, in this case, I actually get a bit lucky that now they are in fact in sorted order.
1:08:23
Now, to be fair, that's not guaranteed. But let's at least consider what the code would look like if we were to take this alternative approach of appending
1:08:30
nodes instead of prepending. Well, rather than write out the code from scratch, let me open up a premade version of list.c that even has some comments
1:08:38
to explain what's going on. Some of this code is pretty much the same. But allow me to scroll down roughly to the middle where
1:08:45
we'll see the actual logic in question. So, first, on line 35 here, we're checking if the list is null.
1:08:51
Because if there's no list yet, it's actually pretty easy to prepend or append. We're just going to go ahead and update the list
1:08:58
variable to point to this new node n. But if the list isn't empty, and there's at least one node there already,
1:09:04
well, then what we're going to do is this in line 45. We're going to iterate over that existing linked list.
1:09:10
And I'm going to do so with a temporary variable called pointer, or ptr for short, that's initialized to the beginning of the list, a foam
1:09:17
finger pointing at that first node initially. I'm going to on every iteration update that pointer variable
1:09:23
to point to the next node, to the next node, pointing one node ahead with that foam finger.
1:09:29
But on each iteration, I'm also going to make sure that the pointer variable is not null. Because if it is null, that means I'm pointing past the end of the list or,
1:09:37
that is, the list has ended. But if inside of that loop I notice that the current node's next field is null,
1:09:46
I actually know logically that I'm at the end of the list without going past it. So at that point, if my goal is to append this new node,
1:09:53
I'm going to go ahead and set pointer arrow next, which is currently null, but set it equal to the address of this new node
1:10:00
effectively appending that node to the end of the list. So, for instance, if we started with a list of 1 and 2, what we've just done
1:10:07
is updated 2's next field to be equal to the address of the node containing 3.
1:10:14
Meanwhile, the node containing 3's next field is null by default because it is now the new end of the list.
1:10:21
Now, what are the implications for maybe performance or efficiency now? Well, we are now appending to the list, which
1:10:28
means we're no longer gaining constant time of insertion. Because any time we prepend it, it took us some finite number of steps.
1:10:36
We just had to update a couple of pointers at the beginning of the list-- beginning of the list. And it doesn't actually matter how much longer the list
1:10:42
is getting because we're never traversing the list when we're prepending. But when we're appending, by definition we're finding the end of the list,
1:10:48
finding the end of the list, finding the end of the list. And so our running time now for insertion is no longer big O of 1 or constant time.
1:10:55
It's now big O of n because if there's n nodes in the list already, just to find the end of it we need to actually traverse the whole list
1:11:02
to actually find where this new node should go. But even so, we've gotten lucky in this appending case
1:11:08
that we inserted 1 then 2 then 3. That's just because of my choice of inputs. Suppose that we don't in advance what the inputs are going to be.
1:11:15
They might be large numbers, small numbers, or anything in between. But they might not necessarily be in order.
1:11:21
But if we want to maintain this linked list in sorted order, I think our logic's actually going to have to change.
1:11:27
So let me actually go ahead and open up a new version of my linked list code,
1:11:33
this one too made in advance. And in this version of my code, as we'll soon see, I've gone about changing the logic just a little bit so that I can actually
1:11:43
now handle this additional case because when inserting nodes in arbitrary
1:11:48
order, if I wanted them to end up being sorted, I have to consider a few possible scenarios.
1:11:53
Maybe there's no list whatsoever. So let's actually look for that. Let me scroll down in this final version of my linked list code.
1:11:59
And, actually, that case here on line 35 is pretty much the same. If there's no list there, and the list variable is null,
1:12:06
well, let's just update it to point to this new node. But things get more interesting when there is at least one node there.
1:12:12
Because if the goal is to maintain sorted order, we now need to decide, does this new node, whatever its number is,
1:12:18
go before the beginning of the list, at the end of the list, in the middle somewhere of the list?
1:12:24
So let's break that down. If we find that the new node's number is less than the list's number here,
1:12:32
well, then it belongs at the beginning of the list because it's smaller than any of the numbers already there. So what I'm going to go ahead and do is update this new node's next field
1:12:41
to point at the current linked list. And then I'm going to update the linked list variable to equal the address of this new node.
1:12:48
The effect then is, no matter how long the existing list is if this new node's number is smaller than everything else in the list,
1:12:55
I want to just splice it in at the beginning. So that's actually pretty straightforward with just a couple of pointer updates.
1:13:02
But the other scenario is that it doesn't just belong at the very beginning of the list. It's somewhere else in the list.
1:13:07
And that itself is two scenarios. Maybe it's in the middle of the list. Maybe it's at the very end of the list. So let's consider those scenarios as well.
1:13:14
Let me scroll down here. And in my else clause, it's a bit bigger this time. Why? Because on line 51, in this case, I'm going to induce another for loop
1:13:23
as before. But this time I'm trying to determine if this node belongs at the end or somewhere in the middle.
1:13:29
So I'm not just looking for the end this time. I'm actually comparing the value, the integer inside of this new node,
1:13:35
against what is currently in the list. So, for instance, if logically I actually find my way
1:13:41
all the way to the end of the list, whereby the next field in the pointer variables node equals null,
1:13:47
well, then logically I didn't find an earlier spot for this node. So let me go ahead and update that pointer's next field
1:13:54
to equal the address of this new node. And then like before, let's just break out because I'm done. I somehow mathematically got all the way to the end of the list
1:14:01
because there is that null pointer. So it must be the case logically here that this new node belongs at the end.
1:14:07
But this is the juicier, slightly more challenging one. But it's what ensures that we can maintain sorted order even
1:14:13
if the new node belongs somewhere in the middle. So down here on line 62, I'm going to ask this question.
1:14:20
If the new node's number is less than the number in the next node-- that
1:14:27
is to say, if my foam fingers pointing here, but the number I'm trying to insert is smaller than the next node over there
1:14:34
and implicitly the same as or greater than the current node's number, well, then I'm going to go ahead and do this.
1:14:41
I'm going to update the new node's next pointer to be equal to whatever the current node I'm pointing at next pointer
1:14:48
so that I can then update that pointer's next field to equal the new node.
1:14:54
And then I can break out altogether, doing a similar splice in the middle of this list but manipulating a node effectively
1:15:03
to the left and the right to make room for this new node. So, collectively, what does this code do?
1:15:08
Well, if we start out with that initially empty list, and maybe we insert the number 2, it just goes right there.
1:15:14
But suppose that we insert next the number 1, which, of course, is smaller, this code now ensures that the 1 is going to get
1:15:19
inserted at the beginning of the list. If we then insert the number 4, well, that's bigger than 1 and bigger than 2.
1:15:25
So it logically is going to end up at the end of the list. And, lastly, in this example, if we insert 3, which, again, is initially
1:15:31
out of order, this code can ensure that we still insert it in sorted order because it's going to end up in between nodes 2 and 4.
1:15:40
So here too in terms of running time, insertion is still big O of n. It's not quite as bad in practice as always adding it
1:15:46
to the end of the list, the end of the list as was the case when we blindly appended new nodes.
1:15:51
But it is going to be in big O of n because, in the worst case here, if we've got n nodes in the list already, then in the worst case
1:15:58
it might indeed be such a big number that it belongs at the end of the list. All right, that was a lot.
1:16:04
Let's go ahead and take a delicious cookie break here. And we'll be back in 10. All right, we are back.

## [Trees](https://youtu.be/0euvEdPwQnQ?t=4571)

1:16:11
And to recap, the problems we've solved and the problems we've created are--
1:16:16
arrays were problematic because they were a fixed size. And that can get us into trouble. Or it causes us to waste more space preemptively
1:16:23
even though we might not ever use it. So we introduce the linked lists again to solve that problem
1:16:29
by being more dynamic and only allocate as much memory as we need on demand step by step. But, of course, we're spending extra space for the pointers.
1:16:36
We might gain performance if we at least prepend all of our elements to it. But we lose time again if we append or insert in sorted order.
1:16:45
So it's not clear, frankly, I think, to me, even hearing these upsides and downsides, if there's a clear win.
1:16:50
But maybe there's a way to get the best of both worlds by trying to capture the upsides of having information that
1:16:58
is kept in sorted order that allows us to maybe divide and conquer still
1:17:03
but still gives us the dynamism to grow or shrink the data structure. And thus we're born trees.
1:17:08
So what we're about to explore are variants of these ideas of arrays and linked lists and see if we can maybe mash up some of those building blocks
1:17:17
and create more interesting, more compelling solutions that are even not just one-dimensional left to right
1:17:25
but are maybe two dimensional and have different axes to them or dimensions. So a tree in the real world, of course, tends
1:17:32
to grow up from the ground like this. But it tends to branch out. And branches branch. And that might already in your mind's eye evoke notions of forks
1:17:41
in the road or conditionals as we've seen. And let me propose that we first consider what the world calls binary search trees.
1:17:47
And so bi is back in that we can do things in half and half and half somehow if maybe we think about arrays a little bit more cleverly.
1:17:54
So here's an array of size 7. And I chose that deliberately because there's a perfect middle. There's a middle of middle and so forth, just like the lockers a few weeks back.
1:18:02
So when the world of arrays-- this was actually pretty efficient because we can do binary search and middle of middle, middle of middle, and so forth.
1:18:09
And that gave us logarithmic running time. But its only size 7. And we concluded that it's going to be like big O of n headache
1:18:17
to copy this into a slightly bigger array, free the old memory, and so forth. And thus were born linked list.
1:18:22
But with linked lists, we lost log of n running time. Why? Because we have to always start at the beginning to
1:18:29
get, for instance, to the middle or to the end of the list in the worst case. But what if we start to think a little more cleverly in multiple dimensions?
1:18:36
So just for the sake of discussion, let me highlight the middle of this here array. Let me highlight the middle of the middle
1:18:41
and then the middle of the middle. So there's implicit structure here. There's a pattern of sorts.
1:18:47
And, in fact, just to make this more obvious, let me not treat this as one dimension left to right but how about two
1:18:53
and give myself a bit of vertical space. So it's the exact same array. But allow me to just think about it now as
1:18:58
though the middle elements way up here. The middle of the middles are slightly lower. And the middle of the middles or the leaves
1:19:03
really are at the bottom of this tree. And that word is deliberate. We actually borrowed vernacular from the world of trees
1:19:09
where the leaf nodes or leaves are the ones at the very bottom. And the root node is the one at the very top.
1:19:16
So for the sake of discussion, computer scientists draw trees like this, instead of this. But it's the exact same idea.
1:19:22
They just tend to grow down in discussions, more like a family tree if you drew those growing up, for instance.
1:19:29
So what's interesting here? Well, at the moment, we've broken the array model
1:19:35
because this memory is absolutely not contiguous because this number is here. This number is here, here, here, and here. It's all over the place.
1:19:41
But we do have pointers now in our toolkit, whereby even if these numbers are anywhere in the computer's memory,
1:19:47
we can stitch them together like we did string and those balloons. Now, it's not sufficient just to have one piece of string
1:19:53
for each node or one pointer. But what if we actually give each of these nodes, not just a number,
1:19:59
like the number 4, the number 2, the number 6-- let's give them each a number and two pointers, a so-called left child
1:20:05
and a right child so to speak. So we could do this. And I'm going to abstract away now.
1:20:12
They're not even rectangles anymore. They're really long rectangles. Or they're upside down Ts that have three boxes to them.
1:20:18
But I'm just going to abstract away nodes now as just simple squares. And it's an implementation detail as to what the structs actually are.
1:20:25
But the arrows suggest that each of these nodes now has two pointers. You don't have to use them.
1:20:31
The leaf nodes have nothing to point to. So those can all be null probably. But each of these nodes now has two pointers.
1:20:38
Now, what's the implication of this? This is what we call a binary search tree
1:20:43
because, one and first and foremost, it's obviously a tree. But it also is a data structure that's kept in sorted order,
1:20:51
whereby notice what is true. If you pick any node in this tree, like the number 4, everything to the left of it, its left subtree so to speak, is smaller.
1:21:00
Everything to the right of it, its right subtree, is larger. And that's true elsewhere. Look at the six.
1:21:05
Everything to the left is smaller. Everything to the right is bigger and same thing over here.
1:21:11
So in some sense, this is a recursive data structure because you can say the same thing about each of these nodes
1:21:17
because each of these subtrees compose a larger tree. Or, conversely, this big tree is a composition
1:21:23
of 1, 2 subtrees plus one more node. So think back to our [INAUDIBLE] example in those bricks.
1:21:29
Well, what's a pyramid of height 4? Well, just a pyramid of height 3 plus one more row. What's a tree of height 3?
1:21:35
Well, it's two subtrees of height 2 plus one more row or really one new root node to connect them.
1:21:41
So this already is a recursive data structure by that logic. How do we translate this into code? Well, we won't sludge through so much low level C code this time around.
1:21:49
But let me propose that we could implement a node now as being similar in spirit to what we did last time where every node used
1:21:56
to have a number and a next pointer. But, now, let's actually make some room for ourselves and redefine a node as still having a number but now having two pointers.
1:22:05
And I'll call them obviously left and right though we could call them anything we want. I could call it next and previous.
1:22:11
But really left and right would seem to make more sense with children of a given node like this.
1:22:16
So this in C is how we might implement, therefore, a node in a binary search tree.
1:22:22
And so let's consider pictorially what the running time is of searching for something. If this here is the tree and it follows that binary search tree
1:22:29
definition where everything to the left is smaller everything to the right is bigger, well, how many steps might it take if you
1:22:35
have n nodes in a tree like this? Well, it's not going to take me n steps because I certainly
1:22:41
don't have to look through every node. And, in fact, just like a linked list starts on the left hand side, so to speak.
1:22:47
So that's just an artist's rendition. Just as a linked list starts on one end and you have to traverse the whole thing, a tree, because it's two dimensional,
1:22:54
always starts in memory at the root node. So this is always where you start any operation, insertion,
1:22:59
deletion, searching. So by that logic, in the worst case if there's n nodes here, how many steps would it seem to take?
1:23:07
It's not big O of n. So it's actually back to bi O of log n.
1:23:12
Why? Because, actually, if you think of the height, there's roughly eight nodes in here. And log base 2 of 8 is actually 3.
1:23:18
And so 1, 2, 3 is the height of this tree. So in the worst case at the moment, it seems
1:23:23
that it's only going to take me like 1 node, 2 nodes, 3 nodes, or really just two steps to get to the very bottom of this tree
1:23:29
to decide is a number there or not. I certainly can ignore this entire subtree.
1:23:35
Why? Because I'm searching for the number 7. Just like the phone book from week 0, I can divide and conquer this problem.
1:23:41
If I'm looking for 7, I don't need to bother wasting any time looking at this entire subtree, which is almost 50%
1:23:48
of the picture on the screen. And so I can focus on this half then this half. And, boom, I'm done.
1:23:54
So we sort have binary search back. We have the metaphor of the lockers back by operating now in two dimensions
1:24:01
to mitigate the reality that our memory is no longer contiguous. But that's fine. We can follow these arrows.
1:24:07
We can use these pointers instead to get anywhere that we actually want. So any questions now on trees or specifically binary search trees,
1:24:16
which I dare say are the best of both worlds, all of the upsides of an array. And it's log n running time.
1:24:21
And all of the upsides of the dynamism of linked list because this thing can grow and shrink and doesn't need to be contiguous.
1:24:29
Any questions on this? All right, well, the code too lends itself to relative simplicity.
1:24:36
And here's where recursion applies not just to the structure of the data but also the code itself.
1:24:42
So just for the sake of discussion, we won't run this code. We'll just look at it on screen here. Suppose you're implementing a function called search whose purpose in life
1:24:49
is to search a tree and return, true or false, I found the number you're looking for. Well, here's the number I'm looking for.
1:24:55
It's one of the arguments. And the first argument more importantly is actually a pointer to the tree
1:25:00
itself a pointer to the root of the tree. And that's all the information we need to search a tree and go left, go right, go left, go right.
1:25:06
How? Well, let me do this. As always, we'll have a base case when it comes to recursion. Because if there's no tree there, then it
1:25:13
makes no sense to even ask me this question. I'm just going to return false. If you hand me null, there's nothing to do, return false.
1:25:19
But suppose that you don't hand me null. And suppose that the number I'm looking for is less than the number in the tree at the moment, the number at that root.
1:25:28
Well, what do I want to do? I effectively want to go left. I want to search the left subtree. How do I do that?
1:25:33
I'm going to return the recursive return value from the same search
1:25:38
function passing in a slightly smaller tree, a so-called subtree but the same number.
1:25:44
And this is where recursion is beautiful. Look at the relative simplicity of this. If search exists, which it doesn't exist in its entirety yet.
1:25:51
But we'll get there. If you want to search half of the tree, just go there. So go to the root of the tree.
1:25:56
Follow the left child pointer and pass that in because it's a tree. It's just a smaller tree but pass in the same number.
1:26:02
What if, though, it's a bigger number? So what if the number you're looking for is bigger than the number at the root of the tree?
1:26:09
Well, then just search the right subtree instead. And now, logically, what's the fourth and final case?
1:26:15
So I can express that as if the number you're looking for equals
1:26:22
equals the number in the tree, that is, the root of the tree, then I'm going to go ahead and return true.
1:26:27
And you might remember from our days with Scratch even this conditional is not necessary. I just did it to be explicit. We can tighten it up as just an else instead.
1:26:35
And that's it. And this is where, again, recursion finally is maybe a little more accessible, a little more obvious in its cleanliness.
1:26:42
There's relatively little logic here. But what's important is that these recursive calls here and here are
1:26:48
dividing and conquering the problem implicitly. Why? Because it's solving the same problem search for a number.
1:26:54
But it's doing it on just half of the tree or the other half of the tree. And because we have this base case here, even
1:26:59
if you get all the way to the bottom of the tree and you try to go down the left child or you try to go down the right child
1:27:05
but those pointers are null, then you know you didn't find it because you would have returned true sooner
1:27:10
if anything had been in fact equal. So that then is recursive code for searching a binary search tree, which
1:27:16
is, again, just to connect the dots of what we introduced last time of actually doing things now recursively
1:27:22
and revisiting some of our own week 0 problems. But I'm kind of lying to you here.
1:27:28
Yes, this is a binary search tree. But it's not always as pretty as this. It's certainly not always seven elements.
1:27:33
But it doesn't actually have to be as well-balanced as this one here is. In fact, suppose that we insert the following numbers
1:27:40
into an empty list starting with 2. I can plop the 2 right there. That's the current root of this tree.
1:27:45
Suppose, though, that I insert next the number-- how about 1? Well, it stands to reason that it should go now to the left.
1:27:52
And so now this is the tree of size 2. Now, I insert the number, say, 3.
1:27:57
It, of course, can go there. So that makes perfect sense. And I just got lucky. Because I inserted these numbers as 2 then one then 3,
1:28:04
I very cleanly got a balanced tree that waited properly left and right.
1:28:10
But what if you have a more perverse set of inputs so to speak. You're not lucky. And the worst possible situation happens in terms
1:28:17
of the order in which the human is inputting data into this data structure. What if the human inserts 1 first?
1:28:22
OK, well, it goes as the root of the tree. But here's where things start to devolve. What if the human then inserts 2?
1:28:29
OK, it goes there. What if the human then inserts 3? Well, according to our definition, it goes there.
1:28:34
It looks like part of a tree because of how I've drawn it. But what is it really if you tilt your head, right?
1:28:42
It looks really just like a linked list. And there really is no second dimension. I've drawn it this way.
1:28:48
But this for all intents and purposes is a linked list of size 3. Why? Because there's no halving. There's no actual choosing left or right.
1:28:56
Now, this is fixable. How could you fix this? It's still the same numbers 1, 2, 3. And it does adhere to the binary search tree definition.
1:29:03
Every number to the right is greater. Every number to the right is greater. Every number to the left is-- well, it's inapplicable.
1:29:09
But it certainly doesn't violate that definition. Could you fix this tree somehow and make it
1:29:14
balanced so it's not devolving into big O of n but is still technically log of n?
1:29:20
What should be the root? AUDIENCE: You just reverse the pointer from 1 to 2. DAVID J. MALAN: So I could reverse the pointer from 1 to 2.
1:29:28
And so sort of pictorially if I take this and I just swing everything over and make 2 the new route,
1:29:35
then, indeed, this could be the new root up here. 1 could be hanging off of it over here and 3 can be hanging off of the 2
1:29:42
as is. So long story short, when it comes to binary search trees, by themselves
1:29:47
they don't necessarily guarantee any balance. So even though theoretically, yes, it's big O of log n, which is fantastic,
1:29:53
not if you get a perverse set of inputs that just happen to be, for instance, the worst possible scenario-- now,
1:29:58
it is fixable. And, in fact, in higher level courses in computer science, specifically on algorithms and data structures,
1:30:03
you'll be introduced, if you go down that road, of how you can tweak the code for insertion and deletion in a binary search tree
1:30:12
to make these fixes along the way. And it's going to cost you a few more steps to fix things when they get out of whack.
1:30:18
But if you do it every insertion or every deletion, at least you can maintain a balanced tree.
1:30:23
And you'll learn about different types of balanced trees. But for our purposes now, we don't necessarily get that property even if we do want log n unless you
1:30:31
keep it balanced along the way. Now, what about other combinations of arrays and linked lists?

## [Dictionaries](https://youtu.be/0euvEdPwQnQ?t=5438)

1:30:38
We can really start to mash these things up and see what comes out of them. Dictionaries are another abstract data type
1:30:45
similar in spirit to stacks and queues in that you can implement them in different ways.
1:30:50
A dictionary is a data structure that stores keys and values. And those are technical terms, keys and values.
1:30:56
The analog in the human world would be literally a dictionary that you'd have in a classroom, a dictionary with words
1:31:03
and definitions, more generally known as keys and values. So that's all a dictionary is.
1:31:09
It associates keys with values. So, for instance, you could think of it almost as like two columns in a spreadsheet, where on the left
1:31:16
you put the key, on the right you put the value. Or, specifically, you put the word in a dictionary and the definition
1:31:21
thereafter. And that's roughly how the printed pages in a dictionary are laid out. So dictionaries associate words with definitions or more generally
1:31:29
keys with values. But it's an abstract data type in that we could implement this in a bunch of ways. We could use maybe two arrays, one array for the keys,
1:31:37
one array for the definitions. And you just hope that they line up. Bracket i in this one maps to bracket i in this one.
1:31:44
But an array is not going to give us the dynamism that we want. You might run out of space when Merriam-Webster or whoever
1:31:52
adds new words to the English language. You might not want to be using an array. You might want to use a linked list.
1:31:57
But, again, linked lists then devolve into big O of n. And that's not good for dictionaries and spell checking.
1:32:02
If you have to check every possible word to find something, getting something that's a little faster than that is compelling.
1:32:08
So let's consider how maybe Apple, maybe Google, maybe others are actually implementing contacts.
1:32:14
Because even though I implied in week 0 and maybe outright said, it's an array-- it's a big list of all of your names of contacts maybe of some
1:32:23
fixed size-- they probably better be using some variant of a linked list, otherwise,
1:32:29
you could never add more friends potentially. You'd max out. And they'd say you have to unfriend someone just to fit it.
1:32:34
As an aside, this is sort of true in the social media world. Once you have 5,000 friends on Facebook, you can't have 5,001.
1:32:40
Once you have some number on LinkedIn, you can't have more connections. That's not necessarily that they're using arrays. But it is the same implication that they've
1:32:47
chosen some finite size for memory. So how might we consider implementing a dictionary specifically
1:32:53
for your address book or your contacts so you can store the names of everyone ideally alphabetically but also their phone numbers and maybe anything else?
1:33:01
Well, ultimately, we want to be able to get at someone's name and lead to their number. So the keys and values for our discussion
1:33:07
here will be names are the keys and phone numbers or the values. But the values themselves could also include email address and a mailing
1:33:14
address and all of that. But we'll keep it simple, names and phone numbers. So here's how you might think about this or draw it
1:33:20
on a chalkboard, two columns or in a spreadsheet, left and right. But how could we actually implement this in memory?
1:33:26
Because, ideally, we don't want it to devolve into something linear. We don't want to have to look through all of my friends
1:33:32
and family and colleagues to find someone whose name starts with Z, for instance, or anything else. It would be nice to have something logarithmic with binary search.
1:33:41
But with binary search again, we have to maybe use a tree instead.
1:33:47
But now we have to use two pointers instead of one. there's a lot of trade offs here. But let's see how else we could solve this same problem.
1:33:54
Because wouldn't it be nice-- and we've not really talked about this before-- if we instead aspire to this Holy Grail of algorithms?
1:34:01
The best algorithm out there is surely one that's big O of 1, like constant time, because what that means
1:34:07
is it doesn't matter if you have 1 friend, 10 friends, 100, 1,000, a million, a billion friends-- it doesn't matter how big n is, your searches will always
1:34:15
take you the same amount of time. It is independent of n. And that's why it's sort of the ultimate goal for performance.
1:34:24
So can we get to this aspiration? Well, a couple of building blocks. There's this notion in computing known as hashing.

## [Hashing and Hash Tables](https://youtu.be/0euvEdPwQnQ?t=5671)

1:34:31
And hashing is a technique, literally a function in math or in code that actually takes any number of inputs and maps
1:34:39
them to a finite number of outputs. So if you think back to high school math, domains, and ranges,
1:34:44
you can take an infinite domain with any values in the world. But it reduces them, a hash function, to a finite range of specific values.
1:34:51
So, for instance, it's no accident that we have these four buckets on the stage now, each of which has a suit from a deck of cards.
1:34:58
We got for visibility's sake the biggest cards we can. These are the super, jumbo playing cards. And in this box are a bunch of randomly ordered playing cards.
1:35:06
And, typically, if you were to ever play some game or you wanted to these for some reason, how would you go about sorting them by suit and also by number?
1:35:14
Odds are if you're like me, you'd probably take some shortcuts and maybe pull out all of the hearts, pull out all of the spades,
1:35:21
pull out all of the clubs, or you bucketize it into categories. And that term is actually technical.
1:35:26
Here are four buckets to make this clear. And, for instance, if the first card I find is the five of hearts,
1:35:32
you know what? Just to make my life easier, I'm going to put that into the hearts bucket. Or here we have 4. Here we have 5.
1:35:39
Here we have 6. Here we have queen. And notice that I'm putting these cards into the appropriate buckets.
1:35:46
Why? Because, ultimately, then I'm going to have four problems but of smaller size, a 13 size problem, 13, 13, 13.
1:35:53
And, frankly, it's just going to be easier cognitively, daresay algorithmically, to then sort each of the 13 cards in these buckets
1:36:00
rather than deal with four suits somehow combined all together. So if you've ever in life made piles-- if you've ever literally used buckets
1:36:07
like this, you are hashing. I'm taking some number of inputs, 52 in this case.
1:36:12
And I'm mapping it to a finite number of outputs, 4 in this case. So hashing, again, just takes in inputs and hashes them
1:36:20
to output values in this way. So beyond that terminology, let's consider what we can now do with hash functions that's
1:36:27
a little more germane to storing things like our friends and family and colleagues in dictionaries.
1:36:33
A hash function is just one that does that. I as the human was just implementing or behaving like a hash function.
1:36:39
But technically a hash function is actually a math function or a function in C or scratch or soon Python or other languages that takes as input some value,
1:36:48
be it a physical card or a name or a number or something else, and outputs some value.
1:36:53
And we can use hashing as an operation to implement what we'll call hash tables.
1:37:00
And that's what that dictionary was. If you think about how I drew it on the screen as two columns, it's like a table of information, keys on the left, values on the right.
1:37:08
So what is a hash table? The simplest way to think about it is that this is an amalgam, a combination of arrays and linked lists right.
1:37:17
We borrowed some ideas of linked lists a moment ago to give us trees in two dimensions.
1:37:22
What if we stick with this idea of having two-dimensional worlds but now use an array initially?
1:37:28
So we get the speed benefits of arrays because everything's contiguous. We can do simple arithmetic and jump to the middle or the middle or the middle
1:37:33
or the first or the last very easily. And then you know what? Let's use the horizontal part of the screen
1:37:39
to give us linked lists as needed. So, for instance, if the goal at hand is to implement the contacts in my cell
1:37:45
phone or my Mac or PC, let me propose that we start at least in English
1:37:50
with an array of size 26. Of course, it's 0 index. So it's really location 0 through 25.
1:37:56
And for the sake of discussion, let me propose that location 0 represents A. Location 25 represents z.
1:38:01
And then everything else in between. Why? We know from C that we can convert thanks to ASCII and Unicode
1:38:07
from letters to numbers and back and forth. So in constant time, we can find location A. In constant time
1:38:13
we can find location Z. Why? Because we're using an array just like in week 2.
1:38:19
All right, well, suppose that I want to think about these more as letters of the alphabet, the English alphabet
1:38:24
rather than numbers. So it's equivalent to label them A through Z. And suppose now I want to start adding friends and family and contacts
1:38:31
to my address book. How might this look? Well, if the first one I want to add is Mario-- Mario's name starts with an M. And so that's A, B, C, D, E, F--
1:38:39
OK, M goes there. So I'm going to put Mario at that location in the array.
1:38:46
After that, I add a second person, for instance, how about Luigi? Well, L comes just before M. So it stands
1:38:51
to reason that it goes there in the array. Meanwhile, if I go and add another character like peach,
1:38:56
she's going to go there a few spots away because her name starts with P. Meanwhile, here's a whole bunch of other Nintendo characters
1:39:03
that happen to have unique letters of their first names. And there's room for everyone, room for everyone on the board A
1:39:10
through Z with some blanks in the middle. But you can perhaps see where this is going. When and where might a problem arise with this array-based approach?
1:39:17
AUDIENCE: When you add [INAUDIBLE]. DAVID J. MALAN: Yeah, so when we add someone else who's name collides with one of these existing characters,
1:39:25
just because by accident, they have a name that starts with the same letter-- So, for instance, there's Lakitu here who collides with Luigi potentially.
1:39:33
Here is Link who collides with both of them. But I've drawn a solution to this along the way.
1:39:38
I could if I was Kronion just remove Luigi from the data structure and put Lakitu in or remove and then put Link in there instead.
1:39:45
But that's stupid if you can only have one friend whose name starts with L. That's just bad design.
1:39:51
But what if we now in the off chance I have two friends whose names start
1:39:56
with the same letter, well, I'll just string them together, link them together, no pun intended, using pointers of sorts.
1:40:03
So my vertical here is an array. And this is just an artist's rendition. There's no actual notion of up, down, left, right in the computer's memory.
1:40:10
But this is my array always of size 26. And each of the elements in this array are now not a simple number.
1:40:17
But it's a pointer to a linked list. And if there's nothing there, it's just null, null, null, null.
1:40:24
But, otherwise, it's a valid address that points to the first node. And you know what? If we have multiple names with the same letters,
1:40:30
we can just string these nodes together together using pointers as well.
1:40:35
So a hash table then as implemented here is an array of linked lists.
1:40:40
And that allows us to, one, get some speed benefit because look how fast we inserted or found Mario, Luigi, and Peach.
1:40:47
But it still covers the scenario where, OK, some people can have the same first letters. Some of these names will collide.
1:40:54
So collisions are an expected problem with a hash table, whereby two values from some domain happen to map to the same value.
1:41:03
And, frankly, you'll see this here too. So these buckets are technically a finite size. They're definitely big enough for 13 cards each.
1:41:09
But you could imagine a world where if I'm using 2 decks, 3 decks, or 4 decks, I'm going to run out of space.
1:41:15
And then my data structure can't fit any more information. But we're not going to have this problem here because the linked lists, as we've seen, can grow and even shrink
1:41:22
as much as they want. In the world of Nintendo there's actually lots of collisions. And these aren't even all of the characters.
1:41:28
So that's then a hash table. So with a hash table in mind, how fast is it?
1:41:34
Did we achieve that Holy Grail of constant time? Well, for some of these names if I back up, yeah, it's kind of constant time.
1:41:41
Yoshi and Zelda, boom, constant time, location 24, location 25. Some of them, though, like Luigi, Link, it's
1:41:48
not quite constant time because I first have to get to Luigi's location. And then I have to follow this linked list.
1:41:54
So, technically, then what's the running time of searching a hash table?
1:42:01
Sometimes you'll get lucky. But sometimes you won't. Consider the worst case.
1:42:06
Big O is often used to describe worst case. So what would be the worst case in your own context?
1:42:11
A little louder. So NY. AUDIENCE: Because you might use [INAUDIBLE].. DAVID J. MALAN: Correct.
1:42:16
And so to summarize in some weird scenario all of your friends and family and contacts could have names that start with the same letter.
1:42:23
And then it doesn't matter that this is a hash table with an array of linked lists. For all intents and purposes, if your friends names only
1:42:30
start with the same letter, all you have is a linked list. Much like with a tree, if you don't keep it balanced, all you have really
1:42:37
is a linked list. So technically speaking, yes, hash tables are big O of n
1:42:44
even if you're good about-- even if you have-- in the worst case, hash tables are big O of n.
1:42:51
Why? Because it can devolve into this perverse scenario where you just have lots and lots of collisions all at the same values.
1:42:57
But there's got to be a way to fix this. How could we chip away at the length of these chains so to speak?
1:43:03
Could I decrease the length of these linked lists so that with much higher probability there's no collisions? Well, maybe the problem is that I started with just 26 buckets.
1:43:12
I mean, four buckets here, 26 here. Maybe the problem is the size of my array. So what if I instead just give myself a bigger array,
1:43:18
and it's too big to fit on the screen-- but what if I instead have a dollar for names that start with Laa and Lab,
1:43:24
and Lac, Lad, do, dot, dot, all the way down? Now, when I hash these names into my hash table,
1:43:33
Lakitu is going to end up at their own location here, link at their own location here, Luigi at their own location here.
1:43:39
And so now I don't have linked lists. I really just have an array of names.
1:43:44
So now I'm actually back to constant time. Why? Because so long as every letter of the alphabet has an ASCII value,
1:43:52
I can get that in constant time. And we did that as far back as week one. And so I can figure out what the arithmetic location
1:43:59
is of each of these buckets just by looking at 1, 2, 3 characters or the total number of letters that I care about,
1:44:05
which is just 3 in this case. So this feels like a solution. Even though I haven't drawn all the names, it feels like we've solved the problem.
1:44:12
But what's the downside or trade off of what we've just done? AUDIENCE: Memory. DAVID J. MALAN: Sorry?
1:44:17
AUDIENCE: Memory. DAVID J. MALAN: Memory. So not pictured here is the dot, dot, dot, and everything above and everything below.
1:44:24
This just exploded in terms of the number of locations in this array. Why?
1:44:29
Because if I'm taking into account not just the first letter but the first, the second, and third, that's 26 to the third power,
1:44:36
26 times 26 times 26. And even though there's going to be a crazy number of names
1:44:42
that just don't exist-- I can't think of a Nintendo character whose name starts with Laa-- you still need that bucket.
1:44:48
Why? Because, otherwise, you don't have contiguousness. You can't just arbitrarily label these buckets.
1:44:53
If you want to be able to use a function that looks at first, second, third letter and then arithmetically figures out where to go, whether it's 0 to 25 or 0 to 26 to the third power minus 1
1:45:04
being the number of buckets there-- so there's a trade off there. You're wasting a huge amount of memory just to give yourself that time.
1:45:11
But that would then give us constant time. So in that sense, if we have an ideal hash function whereby
1:45:17
the function ensures that no values collide, we do actually obtain that that Grail of big O of 1 because it only
1:45:25
takes one or maybe three steps to find that names location. Now, to make this clear, how do we translate this to something like code?
1:45:33
Well, here again is the struct we used last time for that of a person and a person had a name and a number.
1:45:38
Here, for a hash table, we might do something a little bit differently. We might now have a node in a hash table storing the person's name,
1:45:47
person's phone number, and a pointer to the next such person in that chain if needed.
1:45:53
Hopefully this is going to be null most of the time, all of the time. But we need it just in case we do have that collision.
1:45:58
We've seen in our pictures the names, like Mario, Luigi, and so forth. We didn't see the numbers. But that's what's inside of those boxes on the picture.
1:46:05
But that node would give us what we need to build up these linked lists. Meanwhile what is the hash table itself, that vertical strip along the left?
1:46:13
Well, it's really just a variable. We could call it table for short of size 26.
1:46:18
And each of the locations in that array that was on the side here, at least in the simple, small version, was a pointer to a node.
1:46:26
So it's null if there's no one there or it's a valid address of the first node in the linked list.
1:46:32
So this then is a hash table. And each of those nodes, to be clear, would be defined as follows.
1:46:38
So what's the takeaway then with a hash table? Ideally, with a good hash function and with a good set
1:46:44
of inputs where you're not presented with some perverse set of inputs that's all of the friends whose names start with the same letter,
1:46:50
ideally what the hash function will be doing for you is this. The input is going to be someone's name. The algorithm in the middle is going to be the hash function.
1:46:58
And the output is the so-called hash value or location in this case. So, for instance, in the case of Mario, when we had just--
1:47:04
when we had just 26 buckets total, the input to the hash function would be Mario. That hash function would really just look
1:47:11
at the first letter, M in that case, and would ideally output the number 12. I did the same thing.
1:47:16
But in my head, whenever I pulled out a card like the five of diamonds here, I figured out, OK, that's location 0 out of my 0, 1, 2, 3, 4 four total buckets.
1:47:26
Here we're doing it instead alphabetically. And so someone like Luigi meanwhile would have a hash value of 11.
1:47:32
These numbers would be bigger, of course, though, if we're looking at 1, 2, 3 letters instead of just one.
1:47:39
So with that said, if we were to implement this in actual code,
1:47:44
a hash function? I did it physically by acting out the cards. Here is how we might implement this in code
1:47:50
using C. I could have a function called hash whose argument is a string, a.k.a. char star, a name of which is word where the word is
1:47:58
like the first word in their name. We want this function to return an int, which ideally in this case of 26 buckets would be a number from 0 to 26.
1:48:07
And how do we achieve that? Well, if we use our old friend ctype, which had a function like toUpper from a couple of weeks back, we could pass in the first letter of that word,
1:48:17
capitalize it, which is going to give us a number that's 65, 66, 67 on up for the 26 English letters.
1:48:24
And if I subtract 65, a.k.a., quote, unquote-- single quotes because it's a char--
1:48:29
that's going to mathematically give me a number between 0 and 25 inclusive.
1:48:35
There's a potential bug. If I pass in punctuation or anything that's not alphabetical,
1:48:40
bad things will happen. So I should probably have some more error checking, but this is the simplest way in code that I
1:48:45
could implement a hash function that looks only at the first letter of their name. Probably not ideal because I can think of friends in the real world who have
1:48:52
the same first letter of their name. Whether this is better or worse than looking a 2 letters, 3 letters, 4
1:48:57
letters, it's going to depend on how much memory you want to spend and how much time you want to ultimately save.
1:49:02
Let me tweak this though a little bit. It's conventional in C, just so you know, that if you're passing in a string that is a char star to a function
1:49:11
and you have no intention of letting that function change the string, you should probably declare the argument to the function as const.
1:49:18
And that will tell the compiler to please don't let the human programmer actually change
1:49:23
that actual word in this function. It's just not their place to do so. And we can actually do something else. In a hash function because you're using in this case, the output, the integer
1:49:32
as a location in an array, it had better not be negative You want it to be or positive.
1:49:38
And so, technically, if you want to impose that in code, you can specify that the int that's being returned has to be unsigned, that is,
1:49:46
it's 0 on up through the positive numbers. It is not a negative value. So this is slightly better than the previous version
1:49:53
where we didn't have these defenses in place. All right, so what does this actually mean in practice?
1:50:00
You don't get to necessarily pick the hash function based on the names of your friends.
1:50:06
Presumably, Apple and Google and others already chose their hash function independent of what your friends names are.
1:50:11
So ideally, they want to pick a hash function that generally is quite fast, big O of 1.
1:50:17
But practically speaking, in a hash table unless you get really lucky with the inputs, which you generally won't,
1:50:24
really it's big O of n running time. Why? Because in the worst possible scenario, you might have one long linked list.
1:50:30
But in practice, ideally-- and this is a little naive-- but suppose that you have a uniform distribution of friends in the world where 126 of them
1:50:39
have names starting with and then another 126 out of B and then dot, dot, dot Z. That would be a nice uniform distribution of friends.
1:50:47
Technically then, your running time of a hash table for searching it or deleting or inserting
1:50:53
would technically be big O of n divided by k, where k is the number of buckets, a constant. So it's technically big O of n divided by 26.
1:51:00
Now, again, per our discussion of big O notation, that's still the same thing. You get rid of constant factors.
1:51:07
So, yes, it's 26 times faster. The chains are 126 the length. But asymptotically in terms of big O notation, it's still big O of n.
1:51:16
And here's where now we can start to veer away from what is theoretically right versus what is practically right.
1:51:22
In reality, in the real world, if you work for Google, Microsoft, Apple, and others, 26 times faster is actually faster in the real world
1:51:31
even though a mathematician might say, that's really the same thing. But it's not. The real world wall clock time, if you watch
1:51:38
the number of seconds passing on the clock, n over k is a much better running time than big O of n.
1:51:43
So here too we're getting to the point where the conversations need to become a little more sophisticated.
1:51:49
It's not quite as simple as theory versus practice. It depends on what matters ultimately to you.
1:51:54
But ideally and literally if somehow or other they picked an ideal hash function, big O of 1 would really be the ideal here,
1:52:03
would really be the running time we achieve. And what you'll generally find in the real world is that you don't use hash functions that are as simplistic
1:52:09
as just look at the first letter. And, honestly, they won't generally look at the first and the second and the third letter. They'll use some even fancier math to put real downward pressure
1:52:17
on the probability of collisions so that, yes, they will still happen. But most of the time a really good hash function, even if it's not quite ideal,
1:52:25
will be darn close to constant time, which makes hash tables and in turn dictionaries one of the most universally compelling data structures to use.
1:52:35
Now, with that said, we have time for just another data structure or so. And this is not a typo. This one's called and try.

## [Tries](https://youtu.be/0euvEdPwQnQ?t=6761)

1:52:41
And a try is short for retrieval, which is weird because you say retrieval. But you say try. But that's the etymology of try.
1:52:47
And a try is of the weirdest amalgamation of all of these things, whereby a try is a tree of arrays.
1:52:55
So a hash table is an array of linked lists. A try is a tree of arrays.
1:53:03
So at some point computer scientists just started mashing together all of these different inputs, and let's see what comes out of it.
1:53:09
But a try is actually really interesting. And what you're about to see is a data structure that is literally
1:53:14
big O of one time, constant time. But there is a downside. So in a try, every node is an array.
1:53:23
And every location in that array generally represents a letter of the alphabet. But you could generalize this away from words too.
1:53:31
In this case, if we have a root node, that root node is technically a big array with 26 locations.
1:53:37
And if you want to insert names or words more generally into a try, what you do
1:53:42
is this. You hash again and again and again creating one array
1:53:47
for every letter in your word. So what do I mean by that? If we've got 26 elements here, this would
1:53:53
be representing A. This would be representing Z. And initially these are all null by default when you have just this root.
1:53:59
But suppose I want to insert a few friends of mine, including Toad for instance. T-O-A-D is the name.
1:54:05
So how would I do that? I would first find the location for T based on its number 0 through 25.
1:54:12
And if this is T, what would I then do? I would change the null to actually be a pointer to another node, a.k.a.
1:54:18
Another array. And then I would go into the second array and hash on the second letter of Toad's name which is, of course O.
1:54:25
And then I would set a pointer to a third node in my tree, which would be represented here, so another 26 pointers.
1:54:34
Then I would find the pointer representing A. And I would create finally a fourth node, another ray representing
1:54:41
the fourth letter of Toad's name. But because Toad's name ends with D and therefore
1:54:48
I already have four nodes here, we need to specially color though we could probably use an actual variable here.
1:54:55
I need to somehow indicate that Toad's name stops here. So it's not null per se, this actually means that T-O-A-D is in this data
1:55:03
structure. But I did this deliberately because another friend of mine might be Toadette in the Nintendo World. And Toadette, of course, is a superstring
1:55:10
of Toad, that is, it's longer but it shares a common prefix. So Toadette could continue. And I could have another node for the E, another node for the T,
1:55:17
another node for the second T, and another node for the last E. But I somehow have to mark that E as the end of her name as well.
1:55:25
So even though they share a common prefix, the fact that there's two green boxes on the screen means that T-O-A-D is
1:55:33
in this dictionary as a key as T-O-A-D-E-T-T-E is another key.
1:55:38
And technically speaking, what's in these boxes too-- it's not just a pointer. It's probably Toad and Toadette's phone number and email
1:55:44
address and the actual value of the dictionary, which is to say, this too is in fact a dictionary.
1:55:51
A dictionary is just an abstract data type, a collection of key value pairs, just like I claimed a stack and a queue was.
1:55:56
And how you implement it can differ. You could implement it with a hash table an, array of linked lists as we just did, or you can implement a dictionary as a try, a tree of arrays.
1:56:07
And let me add one more name to the mix, Tom, for instance, a valid name from the universe.
1:56:12
T-O-M just means that, OK, that name exists in this structure as well.
1:56:18
Now, what is the implication of storing the names in this way, which is implicitly.
1:56:24
I'm effectively storing Toad and Toadette and Tom in this data structure
1:56:31
without actually storing T or O or A or D or any of the other letters. I'm just implicitly storing those letters
1:56:38
by actually using valid pointers that lead to another node. And so what's the implication of this encode?
1:56:43
Well, encode it might look like this. Every node in a try is now redefined as being an array of size 26--
1:56:52
and I'll call it children just to borrow the family tree metaphor-- and that in each of these nodes there is room for the person's phone number,
1:56:59
for instance, a.k.a. a string or char star. So what does this mean? Well, if there's actually a non-null number there,
1:57:06
that's equivalent to there being a green box. If you actually see plus 1, 617 dash whatever there, that means there's a green box because Toad's number is right here.
1:57:14
Or Toadette's number is down here. Or Tom's is over there. But if this is null, that just means that maybe this is the T or the O
1:57:21
or the E, which are not actually ends of people's names. So that's all these nodes actually are.
1:57:27
And if we think back now to what this data structure looks like, this is in fact a data structure that can be navigated in constant time.
1:57:37
Why? Well, all we need to keep track of this data structure is literally one pointer called try that's a pointer to the first of these nodes, the so-called root
1:57:44
of the try. And when it comes to now thinking about the running time of a try, well, what is it?
1:57:49
Well, if you've got n friends in your contacts already or if there's n keys in that data structure,
1:57:56
how many steps does it take to find anyone? Well, whether I have three names, Toad, Toadette, or Tom or three million names
1:58:03
in that data structure, how many steps will it take me to find Toad ever? T-O-A-D. How many steps for Toadette?
1:58:10
T-O-A-D-E-T-T-E. Eight steps. How about for Tom? 1 2, 3. And, frankly, I'm sure if we looked it up,
1:58:17
there's probably a limit on the number of characters in a Nintendo character's name. Maybe it's 20 characters total or maybe a little longer, 30.
1:58:24
There's some fixed value. It's not unbounded. There's not an infinite number of letters in any Nintendo character's name.
1:58:30
So there's some constant value. Call it k. So no matter whose name you're looking for, it's going to take you maximally k steps.
1:58:36
But k is a constant. And we always said that big O of k is the same thing as big O of 1.
1:58:42
So for all intents and purposes, even though we're taking a bit of liberty here, searching a try, inserting into a try, deleting from a try
1:58:50
is constant time. Because if you have a billion names in the dictionary already,
1:58:55
it's going to take up a huge amount of space. But it does not affect how many steps it takes to find Toad or Toadette or Tom.
1:59:03
That depends only on the length of their names which effectively is a constant value. But there is a downside here.
1:59:09
And it's a big one. In practice, I daresay most computers, most systems,
1:59:14
would actually use hash tables, not tries, to implement dictionaries, collections of key value pairs.
1:59:21
What's the downside of this here data structure might you think?
1:59:26
And this is just a representative picture for Toad, Tom, and Toadette. All the space it takes up--
1:59:32
I mean, even for these three names, look at how many empty pointers there are. So they're null to be sure.
1:59:38
But there's 25 unused spaces here, another 25 unused spaces here, 24 unused spaces here.
1:59:43
And what's not pictured is if I've got more and more names, this thing's just going to blow up with more and more and more and more arrays
1:59:50
even though there's not going to be someone whose name starts with like Laa or Lba or Lbb.
1:59:56
There's going to be so many combinations of letters where it's just going to be null pointers instead. So it takes up a huge amount of space.
2:00:03
But it does give us constant time. And that then is this here trade off. So I would encourage you here on out as we exit the world of C
2:00:11
and so much of today's code in the past several weeks code will soon be reduced in a week's time to just one
2:00:17
line of code, two lines of code. Because Python and the authors of Python will have implemented all of this week's and last week's and prior week's
2:00:24
ideas for us, we'll be able to operate at a higher level of abstraction. And just think about what problems we want to solve
2:00:30
and how we want to do so algorithmically and with data structures. And data structures in conclusion are everywhere.
2:00:37
Has anyone recognized this spot in Harvard Square?
2:00:43
Anyone? What are we looking at? AUDIENCE: Is that Sweetgreen? DAVID J. MALAN: So this is Sweetgreen, a popular salad place.
2:00:49
And this is actually a dictionary or really a hash table of sorts. Why? Well, if you buy a very expensive salad at Sweetgreen,
2:00:56
they put it on the shelf for you if you've ordered via the app or online in advance. And if I, for instance, were to order a salad,
2:01:02
it would probably go under the D heading. If Carter were to order a salad, it would go under C, Julia under y.
2:01:07
And so they hash the salads based on your first name to a particular location on the shelf.
2:01:12
Why is that a good thing? Well, if it were just one long shelf that wasn't even alphabetical, it would be big O of n for me to find my salad
2:01:19
and for Carter and Julia to find theirs. Because they've got 26 letters here, it's big O of 1. It's one step for any of us to find our salads.
2:01:26
Except, again, in perverse situations, where to might this system devolve at like 12:30 PM in the afternoon for instance?
2:01:36
What could go wrong? AUDIENCE: A lot of people with names with the same first letter order a salad. DAVID J. MALAN: Yeah, a lot of people with the same first letters
2:01:42
of their names might order a salad. So there's lots of like D, D, D. Where do we put the next person? OK, well, maybe we overflow to E. What if there's a lot of E people?
2:01:49
It overflows to. F What if it overflows? Then we go to G. And it devolves anyway into a linked
2:01:54
list or really multiple arrays that you have to search in big O of n time? I've even been to Sweetgreen at non-popular times.
2:02:01
And sometimes the staff just don't even choose to use the dictionaries. They just put what's closest to them. So you have to search the same thing anywhere.
2:02:07
But you'll start to see now that you've seen some of these building blocks that data structures are everywhere algorithms are everywhere.
2:02:13
And among the goals of CS50 now are to harness these ideas most efficiently. So that's a wrap. We'll see you next time.
2:02:19
[MUSIC PLAYING]
