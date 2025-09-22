---
link: https://youtu.be/ciz2UaifaNM
related_files:
  - week-8-notes.md
  - problemset/week-8-homepage.md
  - problemset/week-8-problemset.md
  - problemset/week-8-trivia.md
title: "Lecture 8: Week 8 - HTML, CSS, JavaScript"
type: transcription
week/lecture: "8"
---

# [Lecture 8: Week 8 - HTML, CSS, JavaScript](https://youtu.be/ciz2UaifaNM)

TABLE OF CONTENTS:

0:00 - Introduction
1:02 - Bingo Board
1:52 - The Internet
6:38 - TCP/IP
14:31 - Ports
18:10 - DNS
21:20 - DHCP
23:35 - HTTP
36:35 - Inspect
43:04 - Status Codes
45:28 - HTML
1:30:57 - Harvard Pep Squad Prank
1:33:47 - Regular Expressions
1:44:07 - CSS
2:02:24 - Bootstrap
2:09:36 - JavaScript
2:22:33 - Autocomplete
2:26:23 - Geolocation

## [Introduction](https://youtu.be/ciz2UaifaNM?t=0)

0:00
[MUSIC PLAYING]

## [Bingo Board](https://youtu.be/ciz2UaifaNM?t=62)

1:02
DAVID MALAN: All right. This is CS50. And this is already Week 8. But this is a CS50 bingo board from one of your classmates at Yale, Shoshannah,
1:11
kindly sent this to us. And she's apparently been taking close notice of certain expressions that I apparently tend to say quite a bit.
1:18
Some of which I'm aware of, but not all of them. And the idea here as she described it is that if and when
1:24
I say any of these expressions on the screen, you can draw a line through that box. And if you get five in a row, you win a fabulous prize.
1:32
It seems only fair, then, if we maybe give away some cookies today if and when I actually do say five such things in a row.
1:38
Perhaps it'll be all the more motivation to keep a rapt ear against everything we're talking about today.
1:44
So if and when that happens, feel free to just yell out bingo. And then please see Carter during the break or after class for adjudication.

## [The Internet](https://youtu.be/ciz2UaifaNM?t=112)

1:52
All right. So today, ultimately though, Week 8 is about the internet and, in turn, how it works and, in fact, how we can start building software on top of it.
1:59
So up until now, of course, we've experimented with Scratch, spent quite a bit of time with C, only really
2:05
spent a week plus so far on Python, and about the same on SQL. But ultimately, we're going to come full circle next week
2:11
and tie all of those languages together. But we're going to do it in the context of the web. And in fact to do that, we're going to introduce
2:17
three different languages today, but only one of which is a proper programming language. The other two are more about presentation, markup languages,
2:25
so to speak. And those languages are HTML and CSS, commonly used in conjunction. Some of you might have done this middle school, high school even, if you ever
2:32
made a personal website of sorts. And JavaScript, a programming language that is very commonly used in the context of browsers
2:39
to make interfaces that are all the more interactive. But it can also be used server side.
2:45
And what you'll find that is our goal this week, like last week, like two weeks ago is really to teach you ultimately
2:51
how to program, how to program procedurally and also with elements of what we'll call functional
2:56
programming, object-oriented programming, concepts that you'll explore more if you pursue more programming or higher level
3:02
classes. But at the end of the day, you will exit this class having learned how to program, particularly
3:08
in a context that's very much in vogue nowadays, be it for the web or be it for mobile devices.
3:13
And all of the ideas thus far will be applicable as we now begin to build on top of the internet.
3:19
So what is it? So back in the late '60s and 1970s, it wasn't much of anything. This is an early diagram depicting a few access points
3:26
on the West Coast of the United States, which represents what was originally called ARPANET. And this was a project from the US Department of Defense
3:33
to begin to internetwork computers by enabling them to exchange data using what's now known as packets,
3:39
packets of information back and forth. It wasn't too long before East Coast was eventually connected through MIT, Harvard, and others.
3:46
And nowadays, fast forward to present day, just a few decades later, everything, it would seem, is somehow interconnected, either with wires or wirelessly.
3:54
But how do you actually get data from any of these points to any of these other points or all of the points that now exist?
4:00
Well, let me stipulate, for today's purposes, that the world nowadays is filled with routers, simply computers, servers whose purpose in life is to route information from
4:09
left to right, top to bottom, geographically, so to speak, to just get data from point A to point B.
4:14
But typically, you're not going to have a direct connection between points A and B. You might have C, D, E. In other words,
4:21
you might have many different servers between you and someone else. So if you have a friend at Stanford University
4:26
and you simply send them an email, well, odds are that email is going to be put inside what we're soon going to call a packet.
4:33
And that packet might actually pass through the hands, so to speak, of any number of routers, typically more than one or two,
4:41
but typically fewer than 30 such routers. And it's up to the IT administrators of the world to figure out how
4:49
to route data between these servers. And we have software nowadays that dynamically figures out the best path. It's not necessarily a straight line, as it
4:55
might be in the world of mathematics. But hopefully, it's the fastest way to get data from point A to point B.
5:01
So the teaching fellows, thanks to Zoom, kindly put together in years past a demonstration of this whereby each of the teaching fellows or TAs
5:08
that you see on the screen here consider representing a router, that is a device on the internet that its purpose in life
5:14
is to get data, North, South. East, or West, between two points ultimately. And if we assume that Phyllis, for instance,
5:20
wants to send a packet of information to Brian up here at top left, from bottom right, it turns out that by design the internet can send that data
5:29
over any number of routes. It can go up and to the left. It can go left and then up. It can double back a little bit.
5:35
Again, it's not necessarily a straight line. And this is a feature, not a bug. The intent of the internet early on was to be
5:41
able to route around downed servers. So if one router is overwhelmed, or if one router is offline,
5:48
the internet can still adapt dynamically and just route it some other direction. So here, for instance, is one representative route
5:54
that our packets might take. Thanks to the team. [CLASSICAL MUSIC PLAYING]
6:01
6:26
So my thanks to the team. And if you've ever used Zoom before, you know that you don't often see exactly the same layout that someone else sees.
6:33
So it took us forever to actually get that right. Because no one actually knew to whom they were necessarily passing it.

## [TCP/IP](https://youtu.be/ciz2UaifaNM?t=398)

6:38
But if all of those TFs and TAs represent routers, well, what is it they were handing? What is it that Phyllis wanted to send to Brian?
6:44
Well, I've called it generically a packet. And a packet is a generic term for some amount of information. But it's kind of analogous to an envelope in the real world.
6:51
If you're still in the habit of sending letters or postal mail, you typically put your information inside of an envelope such as this.
6:58
And then you hand it off to the mail carrier, or you drop it into the mail box. And then humans, in the case of the Postal Service,
7:03
actually get it from point A to point B. But odds are it goes through different cities, different countries, even.
7:09
So you can think of that as roughly analogous to these things called routers. But the technical term for what it is the TFs were just doing
7:15
is they were implementing a protocol that we know as TCP/IP. And this is actually probably a pair of acronyms
7:23
that you've probably seen, maybe on your Mac, PC, or phone, even if you haven't really thought much about it.
7:29
But this is actually a pair of protocols, two protocols that the internet generally uses nowadays and has
7:35
for some time to get data from point A to point B. And let's consider each of these halves so you have a sense of what it is the internet is doing when you do send an email
7:43
or do anything else. Well, first, IP stands for internet protocol. And you've probably even heard this in popular media, since a lot of humans
7:51
are indeed familiar with this notion of IP. And they associate it typically with IP addresses, as you might.
7:58
So I'll stipulate for today that every computer, every internet work device in the world has an IP address, an internet protocol
8:06
address similar in spirit to buildings in the physical world. Here we are at 45 Quincy Street, Cambridge, Massachusetts, 02138, USA.
8:15
That is a unique string, theoretically, that uniquely identifies this building. Similarly, in the world of computers, we use a simpler mechanism, just
8:23
numbers of this format that uniquely represent computers. Now that's a bit of a white lie.
8:29
Because there's actually a way to share IP addresses. And within your home, often within your dorm, or your apartment,
8:35
you'll actually have what appears to be the same IP address as your roommates or family members. But for now, let's keep things simple and assume
8:42
that every Mac, PC, and phone in the world has a unique IP address that's formatted like this, number dot number
8:48
dot number dot number. Each of these number signs represents a value between 0 and 255.
8:55
And even though we haven't played around with this kind of arithmetic in some time, if each of these placeholders is 0 through 255,
9:02
how many bits are being used to represent each number?
9:08
Think back to Week 0, Week 1. Yeah, so 8, in fact. 8 bits in total, or 1 byte.
9:13
So IP addresses are generally 4 bytes or 32 bits. And the other math we kept doing early on is if you've got 4 bytes or 32 bits,
9:21
that's a maximum of 2 to the 32nd power total number of values. How many IP addresses can you have, it would seem, maximally in the world?
9:28
Enough. Actually, not enough would be a better answer nowadays.
9:34
But roughly, 4 billion was the rough math that we typically did anytime 2 to the 32 was involved.
9:41
But it turns out with all of the humans, and all of the devices, servers, clients, PCs, Macs, phones, and everything else,
9:48
internet of things devices nowadays, even 4 billion is not quite enough. So the world is gradually in the process of transitioning
9:56
from this format, which is technically IPv4, version 4, to IPv6.
10:01
And in the world of IPv6, we've actually bumped things up from 32 bits to 128 bits, which is a crazy number of possible permutations, 2 to the 128.
10:11
So you'll gradually see that over time. But those are a lot messier of a format because there's so much larger.
10:17
So we'll use the more commonplace ones IPv4. Now just to get into the weeds briefly, this is some ASCII art.
10:24
That is, someone wrote this up decades ago in a text file to represent the layout of one of these packets.
10:30
So think of this as, like, the digital representation of this here envelope. And even though we won't get into the weeds of what this represents,
10:38
up here you just have some values saying that this is byte 0. This is byte 10. This is byte 20. And this is byte 32, but 0 indexed.
10:45
So that is to say that this is just kind of an artist's rendition of a grid of bits, top to bottom, left to right.
10:52
And what's going to be interesting for us today is not most of these fields. There's a whole bunch of information that's encapsulated inside
11:00
of any one of these packets. But we'll focus initially on these two, source address and destination address.
11:05
Maybe the most important thing IP does is it standardizes what you put, so to speak,
11:11
on the outside of these envelopes. It says that every computer is going to have a unique address of that form,
11:17
something dot something dot something dot something. And so just like in the real world, if I want to send this packet from Phyllis to Brian,
11:23
and suppose that Brian's IP address is a number, like, very simply 1.2.3.4, what Phyllis would do
11:31
is put that IP address in the middle of this envelope, just like you would address a letter in the real world.
11:37
But so that Brian could reply to her, if only to confirm receipt, she's also going to put in the top left of this envelope,
11:44
virtually, her own IP address, which for the sake of discussion is maybe 5.6.7.8.
11:50
In practice, they won't be as pretty as that. But it's the general idea. So you have a source address from which it's coming and a destination |
11:58
to which it's going. And that's what IP does. It sort of standardizes, in addition to a bunch of other numbers and values
12:04
that need to be in this envelope, too. It really just mandates that computers on the internet minimally
12:09
provide a source address and a destination address so that the envelope can get from point A to point B.
12:15
But that's not quite enough. Because it turns out, and if you saw the bloopers from the TFs' Zoom
12:21
session there, you would see that it's very common not only for humans to physically drop an envelope like that,
12:27
and frankly, even in the real world, for mail carriers to lose mail occasionally, undelivered to recipients.
12:33
And so it turns out that IP alone is not enough to guarantee delivery because sometimes the packet just might not get to its destination.
12:41
More technically, that might happen because the router is overwhelmed. It only has so much memory.
12:47
It only has so fast a CPU. And if it's receiving way too many packets because so many people are on the internet at some moment in time,
12:54
well, it might just kind of get overwhelmed and metaphorically drop certain packets in the sense that there's just not
13:01
enough room in its memory to keep up with the traffic. So the effect for the sender is that the packet just doesn't get through.
13:08
And so there's this other protocol, TCP, that humans typically use in conjunction with IP via their Macs,
13:15
PCs, and phones that does a couple of other things for us. One, it guarantees delivery, or really "guarantees" delivery.
13:23
And it does that actually by doing this. It does that by having Phyllis write on the outside of the envelope not
13:30
just the source address and destination address, but also what we'll call a sequence number. So, for instance, this would be packet one of two
13:38
that she might be sending to Brian. So maybe in, like, the memo field, she could write one of two. And then, if she happens to send a second packet to Brian,
13:45
she might write similarly a source address and destination address. But she might write two out of two.
13:51
Because now, logically, if Brian only gets one of these, that sequence number is enough information for him
13:57
to know wait a minute, I need to ask Phyllis to resend number one, or maybe resend number two. If both of them don't get through, I mean, honestly,
14:04
that's probably when Phyllis hits reload or resends the email. But in general, these sequence numbers help with guaranteeing delivery.
14:12
But if Phyllis and Brian are each representing computers in this story, they can be doing different things.
14:17
They can be doing email, chat, video conferencing, direct messaging, or any number of services on the internet nowadays.
14:24
So TCP gives us one other feature, namely port numbers. Because when Brian receives that envelope, assuming he's

## [Ports](https://youtu.be/ciz2UaifaNM?t=871)

14:31
indeed a computer, how does he know that what's inside of that envelope is indeed an email, versus a direct message,
14:37
versus a little bit of video, versus sound, versus any other type of media.
14:43
Ideally, the outside of the envelope would have a bit of a clue for him that indicates this is the type of data herein.
14:49
Or more specifically, this is the program, really, that should open this envelope, the email program, the video conferencing
14:56
program, or whatever else. So what Phyllis would typically do on the outside of this envelope lastly,
15:04
in addition to the source address, destination address, and the memo field, the sequence number, she would also write a port number.
15:13
And it turns out two of the most common port numbers in the world of TCP are these two, 80, which represents the web.
15:20
That is to say, something called HTTP, more on that today, or HTTPS, which most everyone nowadays probably knows means secure,
15:27
so it's some kind of secure version of HTTP. And that number happens to be 443. There's no mathematical significance of these.
15:34
They're just kind of arbitrary. But humans decades ago decided to standardize on these numbers. So what it means for Phyllis is that on the outside of her envelope,
15:42
she should generally put a colon after the destination address and then the number of the port that she wants to receive this packet.
15:51
So if she's actually not sending an email, but maybe making a web request, and Brian is a web server and Phyllis is a web browser,
15:57
she would write colon 80. Or if she's using HTTPS securely, we would change that 80 to a 443.
16:04
There's other stuff on the outside of that envelope. In fact, just like with IP, there might be fields that look like this.
16:10
But just to give you a sense of this, which is a TCP packet, you'll see that indeed sequence numbers are actually really big.
16:18
They use all 32 bits of this part of the picture, which is to say that generally computers are sending way
16:24
more than one packet or two. They might be sending dozens, hundreds, thousands even, depending on the size of the data in question.
16:31
And there's some other features therein, including source port and destination port. Destination port is the 80 or the 443 that I mentioned earlier.
16:39
But long story short, Phyllis also gets to pick a source port to uniquely
16:44
identify this particular request. But more on that another time. For now, just know that TCP is the pair of protocols
16:52
that the internet uses to get data from point A to point B. IP standardizes how the addresses work.
16:58
And TCP guarantees delivery with those sequence numbers and also helps the servers do more than one thing, helps them multiplex,
17:06
so to speak, among email, web, video conferencing by using those port numbers.
17:11
So at the end of the day, everything, even now, weeks into the class, it all boils down somehow to zeros and ones, or in turn, numbers,
17:19
as we might think of them in this case. Questions on any of these building blocks thus far?
17:29
Questions on any of these? No? All right. Well, on the outside of this envelope are just some arbitrary numbers, 1, 2,
17:35
3, 4, 5, 6, 7, 8. That's obviously not what you and I are in the habit of typing. When we actually visit websites, for instance, you and I
17:42
are generally in the habit of typing harvard.edu, or yale.edu, or google.com, or the like, otherwise known as domain names.
17:49
But your Mac, your PC has to, at the end of the day, address those virtual envelopes, AKA packets, with actual IP addresses.
17:58
There is no room for words, letters of the English alphabet in those pictures that we showed on the screen.
18:03
It's just 32 bits, here 32 bits here. So it turns out, on the internet, there's another type of server.

## [DNS](https://youtu.be/ciz2UaifaNM?t=1090)

18:10
That, unlike routers, which route information from point A to point B, there's another type of server that are all over the place, frankly,
18:17
in your home, on campus, in a company on the internet more broadly, known as DNS servers, domain name system servers.
18:26
So what do these things do? This is just a type of server on the internet whose purpose in life is to answer questions of the form, what is the IP address for this domain name.
18:36
So for instance, if you do pull up your browser on your Mac or PC or your phone, you type in harvard.edu and hit Enter, what your device is designed to do
18:45
is to ask some local DNS server on campus, on your mobile carrier's
18:51
network, on your apartment or dorm's network, what is the IP address of harvard.edu, or yale.edu?
18:57
Whatever you actually typed in, hopefully there is a nearby DNS server that will respond with a numeric address of the form
19:03
something dot something dot something dot something. And that's the number that your computer, your device will actually use on the outside of that virtual envelope.
19:11
So you can think of DNS servers, honestly, as fitting the model that we keep coming back to, this notion of a dictionary,
19:17
or a hash table, more specifically, whereby inside of a DNS server
19:22
is essentially a dictionary, a two column spreadsheet or database table, if you will.
19:27
And in one column are domain names, harvard.edu, yale.edu, google.com. On the right-hand side, right-hand column
19:34
are just the corresponding IP addresses. And that's it. To be technical, if they're not generally called just domain names,
19:40
technically, it's a fully qualified domain name. More on that another time. But domain names as we know them, generally have different parts.
19:47
And we'll soon see how to tease them apart beyond the usual. Questions though, on what DNS server's purpose in life is
19:56
or how this might work? No. All right. So how does your Mac, how does your PC, how does your phone
20:03
know what these IP addresses are? Well, they don't come from the manufacturer this way. And there's this whole hierarchy in the world of DNS servers
20:10
such that your phone, your Mac, your PC, will generally ask the nearest DNS server, which is usually owned by your internet service
20:18
provider at home, in your apartment, or by your university or by your company. But it's a hierarchical system.
20:23
And it's kind of a recursive design. In that if that local DNS server does not have the answer,
20:28
it's going to ask someone bigger, more important than it. If that one doesn't know, it might ask someone, again, recursively for it.
20:34
And throughout the world, there's a finite number of what are called root servers that essentially know about all the dot
20:41
coms in the world, all of the dot edus in the world, all of the dot whatever is in the world.
20:46
And so someone, at the end of the day, knows about those systems. And in fact, if you've ever bought, or in the future might buy a domain name,
20:53
part of that process is paying someone to associate an IP address for you with the actual server that you're going to actually be using.
21:01
So your final projects, for instance, in CS50, it's sometimes common for folks to actually buy for personal use their own domain name
21:07
for a few dollars a year, typically. So you're sort of renting it more than you're buying it. But among the steps you'll go through if you ever
21:13
do that is to essentially inform the world what will be the IP address or IP addresses of your particular domain name that you've

## [DHCP](https://youtu.be/ciz2UaifaNM?t=1280)

21:20
bought for, say, that calendar year. All right. So how does all this get started?
21:26
Well, back in the day, when you arrived on campus here at Yale, anyone, or in the world, you would actually configure your Mac or PC
21:33
to know the IP addresses of your nearest router, of your nearest DNS server.
21:38
So literally, someone would come to your home back in the day when signing up for internet service and configure your Mac or PC for you.
21:45
Of course, nowadays I don't remember anyone really touching my computer recently to configure it for me.
21:50
It all seems to happen automatically. And indeed, there's this other type of server now in the world, another solution to a human made problem known as DHCP.
21:59
And I think this is among the remaining acronyms for today, dynamic host
22:04
configuration protocol. And it's not that intellectually interesting to memorize that. But what DHCP servers do is answer questions
22:11
of the form "what should be my DNS server and router," quote, unquote.
22:17
So nowadays, when you turn on your phone in the morning, if you actually powered it off, if you open
22:23
your laptop lid for the first day of classes or the like, your Mac, your PC, your phone is essentially broadcasting a Hello, World message,
22:30
unbeknownst to you, that's just asking the local network, hey, what IP address should I use for my DNS server and for my router.
22:39
And hopefully, Harvard or Yale or your apartment or your home more generally has a DHCP server nearby whose purpose in life
22:46
is just to hand out answers to that question. And what these DHCP servers also do is they
22:51
tell your Mac, your PC, your phone, what IP address your device should use because that too
22:57
is no longer manually configured. So this all just nowadays happens automatically.
23:03
And in the case of a campus like this or at Yale, it's because, at the very beginning of your visit to campus,
23:09
you did register somehow. You probably logged in. You authenticated against your Harvard account or your Yale account.
23:15
And that is what enabled the DHCP servers henceforth and forever to recognize your particular computer
23:23
and answer those questions for you. All right. So that's it for how the internet works, at least so
23:29
far as we are concerned today. We're going to now start building on top of it. And undoubtedly, the most popular form of the internet

## [HTTP](https://youtu.be/ciz2UaifaNM?t=1415)

23:35
nowadays is something called HTTP. That is the World Wide Web, though most people don't really say it in long form
23:42
anymore. But HTTP is just another protocol that governs how web browsers
23:49
and how web servers speak, just like IP is a protocol that governs how computers address each other on the internet,
23:55
and how TCP governs how computers keep track of sequences of packets from point A to point B and also multiplex among different services
24:03
using those port numbers. And to be clear, what's a protocol-- well, in the human world,
24:09
it's a very common protocol. And I can't reach any of you. But if I were to reach over and say hi, nice to meet you. You presumably, if we weren't five feet apart, would extend your hand.
24:17
We would sort of acknowledge, in this strange cultural convention. But that's a protocol. I know how to do it. You know how to do it.
24:22
I'm initiating. You're responding. And that's exactly what's happening all the time on the internet. You have a client, like me in this case, that's initiating a request.
24:30
You have a server, like you in this case, that's responding to that request. Or analogously, if you're in a restaurant,
24:37
you might be the client sitting down at the table. You want to order food. And there's a server that serves you that food after you have requested it.
24:44
So computers, really, on the internet are implementing that same paradigm. So when it comes very specifically to the web, which is different, of course,
24:52
from email and video conferencing and all of these other services on the internet, the world wide web
24:57
uses this protocol, HTTP, which standardizes what goes inside of those envelopes in order
25:04
to allow a web browser to request and receive information from a web server.
25:09
So we've talked about really the lower level details up until now, the outside of the envelope. Let's now look inside of the envelope when it comes to actual web pages
25:18
that you might visit or soon today, you yourselves might design. So HTTP stands for Hypertext Transfer Protocol, which is another mouthful,
25:27
but, again, just standardizes how we're going to get web traffic from point A to point B, from browser to server and back.
25:33
HTTPS is literally the secure version of that. And what that means for today's purposes is that the connection is somehow
25:41
encrypted, scrambled using very fancy mathematics so that it is very, very, very unlikely that anyone
25:48
who intercepts your traffic, your packets between point A and point B will have any idea what is inside of those envelopes.
25:55
They might intercept the packet itself digitally. They might try to open it up. But it's going to look metaphorically like random zeros
26:02
and ones on the inside when using HTTPS because of what's called encryption.
26:08
But let's look at some canonical URLs. All of us are in the habit of seeing these and typing these all the time.
26:13
Well, let's actually tease apart some of the jargon here. So here is an example URL with all of the usual components.
26:20
So here, for instance, with the yellow slash, this generally means, even though you rarely type it
26:26
and you rarely see it nowadays, this means the default page for the website.
26:34
Give me the root of the website, so to speak. So this is to say this represents a folder,
26:39
like, the default folder inside of which is presumably the default web page. And we'll see what that means more concretely in just a bit.
26:45
If, though, you're visiting a more specific URL, we're going to henceforth call this a path.
26:51
So slash something is representative of a path, maybe a file, maybe a folder, just like in the world of Macs, PCs, and cloud services.
26:58
Specifically, you might sometimes be in the habit of visiting an actual file, something like /file.html.
27:05
Nowadays, this is kind of very '90s, early 2000s. Nowadays most web servers hide the file extension,
27:11
the dot HTML, even if it's there on the server. It just looks a little messy nowadays. It sort of reveals information that's not necessary.
27:18
So very often you won't see dot HTML, even if there is actually a file ending in that suffix.
27:25
You might instead see /folder, with a slash. Maybe not a slash, maybe a slash, but that generally represents a folder on the server.
27:32
And sometimes there are, of course, files in folders. So all of this stuff you're probably familiar with on Macs and PCs and even
27:38
Google Drive and the like. Those same semantics exist in the context of URLs. So there's a mapping between this URL and something on a hard drive somewhere
27:48
on some server. All right. What about the other parts? So this is the fully qualified domain name, so the full domain name.
27:55
Even though you and I, when we say domain name, we typically just mean this example.com, for instance.
28:01
So technically, the W-W-W is what we would typically call a host name.
28:06
A host name is like the name of a specific server that lives somewhere in that domain.
28:12
And this is just a human convention. Even though most URLs still probably start with W-W-W dot something,
28:19
that's not strictly required. That's just a configuration detail. And historically, this was just to kind of signal
28:26
to less technical people in particular, when you would see a URL in print, that oh, this is a web address.
28:31
This is an address on that new world wide web. W-W-W just kind of connotes that. But decreasingly, do you see websites using this?
28:39
I mean, some of CS50's own tools, it's just cs50.dev. It's just CS50.ai. Because most of us are now conditioned to know that,
28:46
oh, OK, that's probably a URL, even though there's no explicit W-W-W. And in fact, even if you type the W-W-W using tricks that we'll soon see,
28:56
you can redirect the user from one to another. Essentially, remove the W-W-W or add it to the server,
29:01
to the address bar in their browser. This thing here is called the top level domain.
29:07
And many of the domain names that you and I are in the habit, certainly in the US nowadays, end in .com, which stands for commercial,
29:14
.edu stands for educational, .gov stands for US government. But of course, there's hundreds of country codes, too, that by convention
29:21
are two letters. So .uk for the United Kingdom, .jp for Japan, and two characters for every other country in the world.
29:29
But even those have kind of been used in clever ways. So .tv, for instance, is actually a country code that's been used by a lot
29:38
of the English-speaking world to represent television, for TV shows and the like. .ai, similarly, does not actually mean artificial intelligence.
29:46
It's a two character country code that has been used by the world nowadays to represent AI.
29:51
.ly for bitly and CS50.ly, too, that's a country code that allows people like us
29:58
to essentially buy domain names in that subdomain. But long story short, back in the day there only
30:04
used to be a few of these top level domains. Now there are hundreds of them. So I do think, over time, it's going to become
30:12
a lot less regimented as it seems to be now as to what URLs actually look like.
30:17
Lastly, beyond the :// here is the scheme, or the protocol.
30:23
And this just means that this URL is going to be securely accessing the server thanks to the HTTPS instead of HTTP.
30:32
Mouthful. But just to get some vocabulary out there. Questions on these here URLs that we've probably
30:38
been taking for granted for years? AUDIENCE: Who approves .edu? DAVID MALAN: Really good question, who approves .edu.
30:45
So you have to be in an accredited educational institution to use .edu. I don't recall the name of the organization that does this.
30:51
But it can't be anyone on the internet. You actually have to apply and be a seemingly legitimate educational institution.
30:57
That is not true of a lot of domain names. Anyone can buy a .com. Anyone can buy .org, a .net, not a .gov, for instance.
31:05
And then different countries might have their own policies over who can be in what domain or subdomain as well.
31:12
All right. So now that we have URLs so defined, there's a couple of verbs with which to be familiar in the context of the web,
31:19
namely GET and POST. And that is to say, there's two different ways to request information from a server.
31:25
That is, there's two different ways to format requests that go inside of this envelope. And the default, daresay, and the most common one is just what's called GET,
31:33
literally the verb, the English verb get. And we'll see in a moment what this means exactly concretely.
31:40
But just know that there's an alternative that we'll play with over time known as POST. And whereas GET, as the verb suggests, is all about just getting information,
31:49
POST, as the verb kind of suggests, is more about sending information. So POST is used when you submit a credit card.
31:56
Because you're sort of sending potentially sensitive information. POST is used when you upload an image to a website or the like,
32:03
but GET is used when you're just clicking on links and visiting web pages and not really pushing any information to the server.
32:09
So for today, we'll focus primarily on GET. So what does this mean?
32:16
Inside of this envelope, probably unbeknownst to you up until now, is our messages that look like this.
32:22
These are HTTP messages that are being put automatically in these virtual envelopes for you by your Mac, your PC, for your phone.
32:30
So for instance, if you were to visit HTTPS://www.harvard.edu,
32:38
you would hit Enter. What your Mac, PC, or phone is going to do is put a textual message that looks literally
32:44
like this inside of a virtual envelope, address it on the outside to the appropriate IP address for harvard.edu using your own IP
32:51
address as the source address, and then hand it off to some nearest router. But inside of this envelope is enough information to the server
32:58
to know what it is you want. So for instance, GET is the verb. So you just want to get some information.
33:04
The information you want to get is /, which I defined earlier as just the default page on the website.
33:09
HTTP/2 just means what version of HTTP we're talking about. You'll see nowadays in the wild, 1.1, you'll see 2,
33:17
you'll start to see version 3 over time. But I'll use 2 for all of my examples here. And you'll see inside of this envelope, too,
33:23
what we're going to start calling an HTTP header, a single line of text that literally tells the server what fully qualified domain name it's looking for.
33:32
And this is important only insofar as nowadays, generally on a server,
33:37
you might have multiple websites being hosted. This is not going to be true probably of Google or of Microsoft
33:44
or Meta or massive companies like that. But it's definitely going to be true of smaller enterprises, even
33:49
places like Harvard that don't need thousands of web servers, but maybe just a couple, or maybe just a few.
33:54
So in this case, this ensures that when the server receives this packet, it knows to serve up harvard.edu and not yale.edu
34:02
or some other website that, by coincidence, might just be hosted on the same server because both Harvard and Yale are maybe
34:08
paying the same cloud provider to host their websites. So dot dot dot just means there's other HTTP headers.
34:14
But notice the colon here is just giving us yet another one of those key value pairs. The key is HOST.
34:20
The value is www.harvard.edu. There, again, are those dictionaries that I
34:25
claimed we would continue to see all over the place. What then comes back from the server?
34:30
If this is what's inside the message from browser to server, what does the server send back?
34:36
Ideally, the server sends back a message that looks like this, an acknowledgment of what version is being used,
34:41
a status code, which is going to be an arcane looking number, like 200. It's going to then have another HTTP header of its own saying
34:48
what type of content is in this envelope, ideally, something called text/html.
34:53
That is hypertext markup language, which we're about to see. And then some other stuff. That's what's coming back from the server to the browser.
35:00
And we can actually now see this. Let me actually go over to VS Code here. Let me maximize my terminal window just so we can see more at once.
35:08
And let me go ahead and type in this command, curl -I https://www.harvard.edu/, so a complete URL that's secure,
35:21
that's got the host name of W-W-W. And curl just means connect to a URL.
35:27
It's a command line program that comes with Linux, comes with Mac OS, Windows. You might have to install it individually.
35:32
And it just lets me simulate being a browser,. It's going to let me simulate sending a packet like this
35:37
without caring what the website actually looks like, so no pictures, no images, no text, no nothing, just what's inside
35:45
of the envelope in terms of the server's response. And here's mostly dot dot dot, the ellipses I raised my hand at earlier?
35:52
There's a lot of these key value pairs. But if I scroll up to the top, you'll see that 200
35:57
is the status code that came back. And you'll see that the content type is indeed text/html.
36:04
And there's a whole lot of other stuff here, clearly. A lot of this is diagnostic. It reveals information about the server that
36:10
might be useful generally to more technical people than me at this point in the conversation, or maybe my Mac or my PC or my phone.
36:17
For now, we can focus really on just the essence of this response, which is this here.
36:22
But here's where even these arcane numbers might start to get a little more familiar, in fact.
36:28
Suppose that I want to see this in my browser. Actually, let me do this. Let me go back to VS Code here.

## [Inspect](https://youtu.be/ciz2UaifaNM?t=2195)

36:35
Let me open up incognito mode here, which generally is to give you private browsing, so to speak. And we'll talk more about this next week.
36:41
In incognito mode or private mode, you have no history, you have no cookies,
36:47
you have no sessions, terms we'll define next week. I'm going to use it again and again today to make sure that my browser is essentially
36:53
starting from scratch, freshly, so that I don't have anything in my history from previous examples.
36:58
And what I'm going to do, actually, first is open up, via my browser's menu, so-called developer tools.
37:04
These are going to look a little different in Chrome versus Edge versus Firefox versus Safari versus other browsers as well.
37:12
But almost any modern browser, whatever your favorite is nowadays, has built into it developer tools.
37:17
And you might have to click a different button to access it. But these are tools for developers, like, web developers that want to not just use the browser to go places,
37:26
but use the browser to develop their own websites and web applications. Now there's a whole bunch of tabs here.
37:32
And I'm going to focus on the Network tab initially. Essentially, this is like diagnostic information, kind of like debug50,
37:39
like a debugger. But it's specific to the web and the web browser here. So with my developer tools open and with the Network tab open,
37:46
I'm going to go up to the URL bar and type in https://www.harvard.edu/.
37:53
So the exact same thing that I typed in curl a moment ago in my terminal, I'm just typing in my browser like I would normally do.
38:01
And if I hit Enter, what's interesting about developer tools, and let me go ahead and drag them to the top and maximize the window,
38:07
is you see all of the HTTP requests, all of the virtual envelopes
38:12
that just went instantaneously it would seem back and forth between my Mac here and Harvard's own web server.
38:20
And notice it's way more than a single envelope. It's way more than a single request. Why? For now, assume that each of those rows of output
38:27
represents maybe a sound that was downloaded, a video, an image, some text.
38:32
There's all sorts of media in web pages nowadays. And they might actually be spread across multiple files.
38:38
Browsers are designed, if you will, to recursively get all of the media for a single web page and download it automatically
38:44
with we humans only typing the URL itself once. But watch this.
38:49
At the very top of this output, I scrolled all the way to the top of my network tab. I'll see a request, a row that represents
38:56
my original request for the website. And if I Zoom in here, we'll see that 200 means apparently OK.
39:03
So all is well. Here's the contents of the website. But there's a lot. In fact, if I look at the very bottom of the window,
39:09
harvard.edu is composed of 91 separate files it would seem. And that's just the landing page itself, not
39:16
to mention everything else we might click on ultimately. But 200, OK, is a good thing.
39:22
And odds are you've never actually seen that, because it's, indeed, OK. So let's consider actually what else could
39:28
happen when you make these requests. Well, here, for instance, is a shorter request. Suppose that I omit the W-W-W just because it's faster to type.
39:37
And honestly, you and I are almost always, nowadays I bet, in the habit of just typing something.com, or something.edu.
39:43
We don't bother typing the HTTPS, the so-called scheme or protocol. We probably don't bother typing the W-W-W.
39:48
You can probably think of someone in your life who's very pedantic like that, typing it out in its full. But you don't need to do that typically for a couple of reasons.
39:56
If I, in fact, go back to VS Code here, let me use curl again to connect to another URL that's similar,
40:03
https://harvard.edu. Now notice before I went to W-W-W. And that's indeed Harvard's preferred URL,
40:11
if you will. But harvard.edu will still work. But watch what happens when I hit Enter. I'm going to get back the contents of the virtual envelope
40:19
that Harvard just sent back to me. But it's not OK. It's not 200 anymore. It's actually this number here, 301, which
40:27
actually means something specific. 301 actually means that Harvard's website moved permanently, so to speak.
40:34
In other words, Harvard, Yale, any server can configure itself to redirect the user to another place
40:39
if they prefer to canonicalize on some other URL. So by default for branding purposes, most websites still
40:45
probably use www.something.something. So Harvard is, in fact, doing this. And for reasons we'll talk about next week,
40:52
there's technical motivations to do so related to something called cookies and sessions. But for now, that just seems to be a different status code.
41:01
But if I now open up another browser window and I'll do this again in, let's say, how about incognito mode, just to start fresh with a brand
41:11
new window. Let me open my developer tools again. Let me go to the URL bar and only type https://harvard.edu/ Enter.
41:22
I'm still in my network tab here. And if I scroll to the very top of this, notice, ah, the top row looks a little different now.
41:29
It's not 200 anymore. And I can click on that here. And what I'm now seeing in yellow is that 301, AKA, moved permanently.
41:37
So this is to say you've been able to do this all this time in your browser if you care to. You can see what's going on underneath the hood, if you will.
41:45
Check that off, I think. Underneath the hood so as to just understand what's going on.
41:50
Now for users, this is not that useful or intellectually interesting. But for developers, this can be very useful for understanding things
41:57
and also diagnosing problems ultimately. So that's just a couple of the status codes that can come back, not just 200,
42:05
but perhaps 301. There's also this one now, with which humans generally are familiar, 404.
42:12
Well, it turns out 404 is what happens when a file is not found. So I can simulate that here.
42:17
Let me go back to VS Code and my terminal window. Let me do curl -I https://www--
42:24
because Harvard prefers that-- harvard.edu/cats. Let's see if there's a page about cats within Harvard's website.
42:30
I'm pretty sure there's not. And so, indeed, when I hit Enter, a whole lot of output, a lot of HTTP
42:36
headers. But notice at the top, 404. It's File Not Found. Now what you see in the browser is going to completely depend on the website.
42:44
Some websites just display an error message or a status code number. And that's why you and I have seen probably in the world 404 messages.
42:52
Sometimes they're much more user friendly. Sometimes there are links back to the home page to help you out. It's entirely up to the server.
42:58
But that status code indicates that something has gone wrong. And in fact, there's a whole bunch of these status codes.

## [Status Codes](https://youtu.be/ciz2UaifaNM?t=2584)

43:04
Some of which you'll now start to see in the class. 200's OK. And it's a good thing if you never see that, because it means everything's working.
43:11
404 is not found. 301 is moved permanently. Any of these that start with 3 relate to redirects.
43:17
Long story short, there's different ways to redirect the user from one place to another, as we saw from that location header a moment ago.
43:25
400s are generally bad. It means that the user, the browser somehow did something wrong.
43:30
Like, 403 forbidden probably means you're not logged in.
43:36
500 you're going to start doing next week most likely. 500 is, like, the segfault of the web, if you will.
43:42
So there's no pointers or anything like that. But 500 means that you wrote some buggy code, as invariably we all will
43:48
next week. 418 is an April Fool's joke from years ago. Some servers honor this.
43:53
But someone wrote up literally this long technical document proposing a response that says I'm a teapot for a server,
44:00
even though it was just a joke on April 1 some years ago, so sort of geek humor, if you will.
44:06
So those are then the status codes that are available to us. Let me show you one other.
44:11
Has anyone been to this URL here? So you have? All right. So without spoiling here, let me actually--
44:18
well, let me go into incognito mode here. Someone's pulling it up on their phone, clearly.
44:25
Safetyschool.org/ Enter. Oh, my goodness.
44:31
Another box gets crossed out today, too, I think. So how is that working? Well, if we actually diagnose this with curl-- let me go into VS Code,
44:39
curl -I HTTP-- and it doesn't support HTTPS because this is an old website--
44:45
://safetyschool.org/ Enter, all this server does is return an HTTP 301
44:52
response with a location that literally refers us back to yale.edu.
44:58
And this is amazing. Someone has been paying for this domain name for decades. And all it does is literally this.
45:05
Now I know for our friends at Yale who are watching this, it's not quite fair to poke fun.
45:10
It turns out Yale got us even better. So later today, we'll turn the tables a little bit.
45:15
All right. So let's go ahead and take a look now at what
45:21
it is that composes this web page when it is indeed 200 OK. Let's introduce another language here, or an actual language

## [HTML](https://youtu.be/ciz2UaifaNM?t=2728)

45:28
called HTML, which is not a programming language but is a mark up language. Which is to say it's all about aesthetics, like,
45:35
mocking up a web page so that you can see the information you care about. But HTML is not going to have functions and loops and conditionals
45:42
and all of that stuff we talked about in Week 0 It's just about presenting information. So here are some of the building blocks of HTML.
45:49
You're about to see really only two vocabulary words. HTML honestly is the kind of language that you learn in, like, 30 minutes
45:56
and then you're just kind of off and running with online tutorials, documentation, and the like. I still remember years ago just learning it
46:02
from a teaching fellow who kind of gave me a crash course and then you kind of fill in the blanks yourself
46:07
because it has relatively few concepts associated with it. Even though, in fairness, it can take years
46:13
to get good at making pretty websites, today we can get good very quickly at making functional websites, so
46:21
that artistic disclaimer. So in the world of HTML, there's really two concepts, tags and attributes.
46:26
And those of you who have played with websites growing up might be familiar with some of these already. So here is some sample HTML.
46:34
HTML is just a text-based language. You type it out with your keyboard. Again, it's not a programming language. So you can't call functions or write logic.
46:41
But you can mock up a web page. And this web page, for instance, is quite simply going to say hello, title in its title bar, or the tab.
46:48
And then the body of it, the big white box, it's going to say hello comma body, just to distill this really into its essence
46:55
before we make more interesting pages. So what's going on in this HTML is enough detail
47:02
that the server can display the information for it. So in fact, let me go ahead and reveal this as follows.
47:09
I'm going to go over to VS Code here. I'm going to create a new file here called, for instance--
47:18
let's just call it hello.html. And I'm going to really quickly whip up that same web page from memory.
47:24
So DOCTYPE html html lang equals quote, unquote "en" close bracket.
47:29
Open head, open title, hello comma title.
47:35
And then down here, open body. And you'll notice I'm actually not quite as fast as I might seem to be. VS Code is configured to automatically finish half of my thought for me.
47:44
So when I open one of these things that we're about to call tags, VS Code is doing some of the heavy lifting for me.
47:50
And in here, I'm going to do hello comma body. But I think this is the entirety of the file
47:55
that I just proposed in the slide version thereof. So this is clearly now a text file in my code space within VS Code.
48:03
How do I actually view it with a web browser? So if this file were created on my Mac or PC,
48:08
I could literally double click it and Chrome or my default browser would open up and show me this web page.
48:14
But this file, technically, is not on my Mac or PC. It's in the cloud. It's in your code space.
48:19
So all that we need to do is actually turn on a web server to serve this file to me or to anyone else in the world, in fact.
48:27
And the command we're going to run now is literally called http-server. This is a piece of software that someone else
48:33
wrote that we pre-installed in everyone's code space. And by running this, it starts a server whose purpose in life
48:40
is to listen for HTTP requests. And as soon as it receives one from a browser, be it mine or anyone else's, it will respond with the contents of that file.
48:48
So let me go into VS Code here. Let me reopen my terminal window. And I'm going to go ahead and literally run http-server Enter.
48:58
And now you'll see a whole bunch of output, most of which isn't germane to our discussion yet. But here is this URL here.
49:05
And if I hover over it, I'll see a little Open URL pop up that I can click on, or on my Mac, I can Command click on the URL itself,
49:14
and that will open up in a new tab this folder. So this is going to look a little esoteric at first glance.
49:22
But this is what's called a directory listing. It's just literally the contents of the folder that I'm in.
49:27
So I'm in my Codespaces default folder. I deleted everything from last week and weeks prior. Your folder will, of course, have many other things
49:33
that you've created and kept. I have a Source 8 directory that I downloaded in advance because it's got all of today's examples made in advance.
49:40
But there's the file I just created. And there's some other information here, like the date and time at which I created this file, and so forth.
49:47
But you'll see that this is just a web page that lives at this URL here. And this is actually somewhat specific to Codespaces,
49:54
the infrastructure we're using. But if I Zoom in up here, you'll see that I am effectively
50:01
running my own web server at this weird looking URL that GitHub dynamically generated for us, for me.
50:08
And you'll have a different unique one as well. You'll see that baked into this URL is actually a port number.
50:13
And they're doing some trickery. Normally, I would have to access this web server at Port 80, or 443,
50:20
or even 8080. And the reason for this is because cs50.dev,
50:25
that is to say Codespaces, the tool that we're using in the cloud, is obviously itself already a web server.
50:30
And it's GitHub's web server that's listening already on Port 80 and 443. So if I want to run my own web server on their web server,
50:38
I just have to pick another port number. And so what you're seeing in the URL here is a hint of that. By convention, the program I just ran, http-server, does not try to use 80.
50:48
It does not try to use 443. It uses 8080 by default. And that's why you see it in the URL here.
50:54
And underneath the hood, that virtual envelope actually contains Port 8080. Because this is not an official web server.
51:00
This is not CS50.dev or GitHub.dev. This is little old me trying to serve up my brand new hello.html file.
51:09
But the point here is this. When I click on this file, I should see the results of my hard work.
51:15
And there is a big white box, otherwise known as the view port, inside of which are the only words in the body of my page, hello, body.
51:22
And if I scroll up further, you'll see in my tab here hello comma title. So this now maps back to the code we just saw.
51:29
Here is the HTML that I just pulled up in my browser. And it is what told the browser what to do visually.
51:36
So let's walk through this top to bottom. This first line here is what's called the document type declaration.
51:41
Honestly, you just copy paste this nowadays. And it means hey, browser, I'm using version 5 of HTML.
51:47
Odds are in some number of years, this line might change over time to indicate different versions. But for now, this just means I'm using the latest version of this HTML
51:55
language. That's kind of anomaly, because you're not going to see this exclamation point again.
52:00
Everywhere else, you're going to see a lot of less than signs and greater than signs or angled brackets, so to speak.
52:05
But they're almost always going to be symmetric, as follows. This tag here, this is an HTML tag, says, hey browser, here comes my HTML.
52:16
And this is what's known as an attribute. So anything after the name of a tag is what we'd call an attribute.
52:22
And attributes can have values. Those values that are associated with the attributes with an equal sign and typically quotation marks, single quotes or double quotes,
52:30
as in this case. So here we, again, have that paradigm of a dictionary, key, value, pairs.
52:35
They're everywhere in computing, even though the syntax obviously keeps changing, whether when we're in SQL, or Python, or now HTML.
52:42
This tag at the very bottom now means hey, browser, that's it for my HTML.
52:47
So when you see a tag that looks like another, but starts with a forward slash-- and you do not need to repeat the attributes, that would just
52:54
be very annoying to have to type it here and here, we keep it succinct-- this is what's known as a close tag, or an end tag that
53:03
conceptually corresponds to this start tag or open tag. So they're sort of symmetric.
53:09
Inside of that are two children, so to speak. So there's actually a notion of a family tree-type hierarchy here, or a tree,
53:15
as we've discussed in data structures. The HTML tag, per the indentation here, has one child called head and another child called body.
53:25
Everything between the start tag and an end tag here is what's also generically known as an element.
53:30
So this is the head element. This is the body element. A bunch of new vocab, but it's not that intellectually interesting.
53:36
It's just jargon that we'll use. Here means hey, browser, here comes the head of my page.
53:42
So like the very top of it, which generally for now means just the title bar. In fact, this means, hey, browser, here comes the title of my page.
53:52
And then here, notice there's no more angle brackets. This is literally raw text. And this is why we saw in the actual gray tab of my browser hello comma
54:01
title. This means, hey, browser, that's it for the title. This means, hey, browser, that's it for the head. Meanwhile, down here, hey, browser, here comes the body of my main page.
54:10
Like, 90-plus percent of the page inside of the so-called viewport, the big rectangular region, hey, browser, here comes the body.
54:16
Hey, browser, sir, that's it for the body. What is in the body? In this super simple case, literally just hello comma body.
54:23
That's it. So HTML really is that pedantic. It just tells the browser start doing this.
54:28
Stop doing this. Start. Stop. Start. Stop. And that's how it knows what to do, top to bottom, left to right when actually reading the code therein.
54:38
All right. Questions about any of this here HTML code.
54:43
And yeah, in front? AUDIENCE: Would browsers be considered a HTML interpreter?
54:49
DAVID MALAN: Say that again? AUDIENCE: Would browsers be considered a HTML code interpreter? DAVID MALAN: Oh, yes.
54:55
I think that's fair. The question is, can browsers be considered HTML interpreters? Yes, I don't think people tend to call it that.
55:02
Interpretation generally implies that you're parsing something that's logical in nature, your functions, loops,
55:08
conditionals, and so forth. Parser is a term you might indeed hear much more often. A parser is a piece of software that analyzes code,
55:16
analyzes text top to bottom, left to right, breaks it down into chunks that have semantic meaning, like the tags,
55:22
like the attributes, like the elements that we're talking about and then it displays them, in this case.
55:27
There's not as much to interpret in quite the same way. But that's reasonable, nonetheless.
55:32
Yeah? AUDIENCE: With all the frameworks, do you think is is worth learning HTML from scratch or just use a Bootstrap [INAUDIBLE]?
55:39
DAVID MALAN: Really good question. With all the frameworks out there, should you bother learning HTML and writing it from scratch or using frameworks,
55:44
like something called Bootstrap. Well, we spent a few minutes today talking about that very framework. But even frameworks like Bootstrap absolutely
55:51
assume that something about HTML, something also about something called CSS, more on that in a bit, and better still,
55:57
something about JavaScript. If you really don't want to know and understand these things, that's when you reach for like a third party service,
56:04
like Squarespace nowadays or Wix, where you really just click and drag and drop and create websites that are, at the end of the day, still HTML.
56:12
But the developers at Wix and Squarespace have automated the process with a graphical user interface
56:18
or GUI of letting you create it. But even then, most web developers, or even just business people
56:23
who want to create their own website and they're not programmers themselves or technical folks, they might still like to know a little something about HTML, CSS,
56:31
and JavaScript because then you can open like the advanced settings and configure things. And indeed, that's a frustration that you'll
56:37
tend to feel if you can't quite drop down conceptually to that level. All right. So just to make this a little more--
56:45
to give you more of a mental model for this, this indentation is not strictly necessary. Kind of, like, in C, where we care, where style50 cares, but not
56:54
Clang, about what your code looks like. Similarly, browsers are pretty tolerant. You can have all of this white space, all of this pretty indentation.
57:01
Or you cannot. It's not going to care, generally, one way or the other. However, this is certainly much more readable.
57:08
But we'll see next week as we start to generate HTML automatically, it's not always important that the code you generate be pretty printed.
57:16
But when you're writing in this format, it absolutely should be when you're collaborating or submitting to other people.
57:22
So this, though, is what we would call a tree representation of this. So here is that hierarchy.
57:27
So if we think of the whole web page as what's generally known as a document, that document has a root element called the HTML element, which
57:34
it's open HTML tag and its closed tag. It has, as I claim, two children. The head tag has one child title.
57:40
And then both of those leaf nodes, or leaves to borrow the family tree vernacular, have text nodes of hello, title
57:49
and hello, body, respectively. So this is going to be useful later today because it turns out,
57:54
with JavaScript, an actual programming language, we can start to modify this tree in the computer's memory or RAM
58:01
and make the page dynamically change by essentially creating new HTML on the fly, even if that didn't come from the server.
58:09
Case in point, many of you use Gmail or maybe Outlook. Generally speaking, you don't have to reload the page
58:15
to see if you've got new mail. It just magically appears at the top of the page in kind of a stack. And it just keeps pushing old mail down, down, down.
58:23
Well, that's going to be the result of some JavaScript code updating this tree in memory.
58:28
And it has the effect of just dynamically generating more and more HTML that represents your email's inbox, for instance.
58:36
All right. So with that said, why don't we go ahead and actually try this out in a couple of ways.
58:42
So let me go back to VS Code here. Let me propose to actually tweak my code here a little bit.
58:50
So let me go into, let's see, my VS Code editor here.
58:55
Let me zoom out. And notice down below, actually, all this time as I was clicking on hello.html, my HTTP server program
59:04
actually is outputting sort of the logs from a server. It turns out any time you request a page with a browser from a server,
59:11
that server is probably logging a little something about you. One, it's probably logging your IP address.
59:16
Two, it's probably logging the type of browser you're using Chrome, or Safari, or Edge, or something like that.
59:22
It's probably logging the operating system version you're using, be it Windows, or Mac OS, or Android, or iOS, or the like,
59:28
and maybe some other information as well. We won't dwell on this today. But there's a lot of information that will be logged about you, even if you
59:36
are in incognito mode or private mode. So more on that next week. And today, unlike all past lectures, even though by default you
59:43
see this in your own code space, you see here a ports tab, which for the most part is not that useful for us today.
59:51
But you will see that this row here mentions HTTP server. Why? Because in my terminal, that command is still running.
59:58
It is a server. And it's just there living to serve now by waiting and waiting and waiting for me to click on more of those links.
1:00:04
And every time I do click on a link, I'll see another line of output here. But it turns out that all this time in your ports tab of VS Code, you
1:00:12
can see all of the TCP ports, for instance, that are in use. Now generally, you haven't needed any of those, at least for your own work.
1:00:20
But notice that HTTP server is indeed listening on Port 8080. CS50 has some of its own customizations.
1:00:26
And this is a bit of a geek Easter egg. But we presume to use Port 1337, which perhaps those more comfortable
1:00:34
will know what it means. This is like leetspeak. So it actually spells Leet if you're cool and use a 1, 7, and 2, 3.
1:00:39
OK. So anyhow, we chose that port number. But there are some conventions. Next week we're going to actually start using Port 5,000, which
1:00:46
isn't in use at the moment. But long story short, you can see this stuff underneath the hood.
1:00:52
And indeed, we're just sort of peeling back some of these layers that have been there now for some time. Well, let's go ahead and do this.
1:00:57
I'm going to go ahead and create another terminal window using my plus icon down
1:01:03
here in the console. Notice that at the right-hand side of my screen, I now have two bash shells.
1:01:08
Bash is the name of your prompt, so to speak, where the dollar sign is. If I click on the first one, there's HTTP server.
1:01:16
It's still running. And I want it to keep running today. But I'd also like to be able to run more commands in my code space.
1:01:22
So I've simply created a second terminal. And I can go back and forth by clicking it right. Let me go ahead now and copy hello.html like that and create a brand new file
1:01:32
called-- how about paragraphs.html? And in paragraphs.html, I'm going to first paste all of that.
1:01:39
I'm going to hide my terminal window now without stopping HTTP server. And I'm going to go ahead and just create some paragraphs of text.
1:01:46
And in fact, let me go ahead and cheat here real quick. I'm going to go ahead and, in my other window here secretly, open up
1:01:54
a whole bunch of text so that I can grab some Latin-like text to copy paste.
1:02:00
So now I'm back. And all I did was secretly copy paste a whole bunch of text. I'm going to make a couple of changes to this file, where I currently
1:02:06
have just a title and a body. One, I'm going to rename this to paragraphs, just so I can keep straight
1:02:12
which file is which. And down here, I'm going to go ahead and paste in a big paragraph of text.
1:02:17
This is not actually Latin. It's sort of lorem ipsum text, which is Latin-like random words that's
1:02:23
meant to look like Latin. And typographers historically used this as sort of placeholders for actual text. But notice this is a pretty decently long paragraph.
1:02:31
And so it's going to make my web page a bit bigger. So let me go back to my other tab, where I have hello.html open from before.
1:02:39
Let me click back. And now notice, in my directory listing, I have a new file, paragraphs.html.
1:02:45
Let me go ahead and open that up. And voila, there is a big paragraph of text.
1:02:50
Just for fun, let me create three such paragraphs. So I'm going to cheat temporarily and just copy and paste two more times.
1:02:58
But I'm going to separate it with a blank line, as you would in, like, Google Docs or Microsoft Word for paragraphs in English or any language.
1:03:04
And I'm going to go back to my paragraphs. Nothing has changed yet because HTTP, just like the exercise with Phyllis
1:03:10
and Brian, requires that we send the packets back and forth if we want to get updated content.
1:03:16
So I have to click my browser's reload button, or hit Control R or Command R, depending on your browser or OS, and notice that when I do that,
1:03:24
I definitely get more text. But it just looks like one big blob, not three separate paragraphs.
1:03:31
What might your intuition be for why that is, even though I've clearly indented this and given blank lines between?
1:03:39
Yeah? AUDIENCE: HTML doesn't care about the whitespace. DAVID MALAN: Yeah. So HTML doesn't care about the whitespace or technically,
1:03:45
more than one whitespace. I can hit as many Enters as I want. All of them are going to be ignored except for a single space.
1:03:52
It's going to be normalized to just a single space. In general, this is useful. Because it means I can pretty print my HTML and indent things visually,
1:04:00
even if I don't want the browser to indent anything manually for me. But here's where we're going to need some more tags.
1:04:05
And it turns out the simplest fix for this problem is to use the paragraph tag. And for short, it's just open bracket p close bracket.
1:04:13
I'm going to be a little pedantic, and even though VS Code is being a little annoying because it's trying to autocomplete my thoughts
1:04:18
but I don't want it to autocomplete just yet, sometimes you have to fight with the text editor. So these autocomplete features have upsides and downsides.
1:04:25
But I'm going to go ahead and put a paragraph tag, open and close around each of these paragraphs.
1:04:31
And I'm going to maintain my indentation, just to keep it visually clean on the screen. And now I'm going to put this one last close tag on this line here.
1:04:40
And so it's a lot more verbose. But notice that it's effectively telling the browser start a paragraph,
1:04:46
end a paragraph, start a paragraph, end a paragraph, and so forth. So if I go back to my other tab and I click Reload,
1:04:53
now we have some semblance of what I expected, which is three separate paragraphs in this case.
1:04:58
All right? So that's the p tag, the paragraph tag. P for short, because as you'll see, many of these tags are abbreviated just because they're slightly faster to type.
1:05:06
Let's do another example. Let me go back to VS Code here. I'm going to copy this text. I'm going to create a new file called--
1:05:13
how about headings.html? And I'm going to paste this, close my terminal just to give me more room.
1:05:21
I'm going to rename the title to be Headings, just to keep straight which is which. I'm going to delete all of these paragraphs to make it-- actually,
1:05:27
no, let's not do that. Let's keep the paragraphs. But like an academic paper or a textbook,
1:05:33
let's give these chapter headings or section headings or the like. Well, I could just do something like this.
1:05:40
How about 1? And then down here I could put 2, and then down here I could put 3.
1:05:47
But of course, if I reload this, it's not really going to look as I-- whoops, if I go back to this directory listing, open up headings.html, it's fine.
1:05:57
It's not super pretty. But it would be nice to give a little more prominence to these headings. And in fact, there's a bunch of tags for this.
1:06:03
I can use H1, for instance, for one really big heading. And then let me close the tag over here and indent.
1:06:10
Then down here-- and, again, whitespace doesn't matter, so I'm going to give myself a little bit of breathing room just so it's clear
1:06:15
which of these is which. For this, maybe it's not Chapter 2, but Section 2. So let me do H2.
1:06:20
And then inside of this, I'm going to go ahead and do 2. And just to be clear, I don't have to put these on their own lines.
1:06:27
I'm just doing that to be a bit pedantic. You can technically just do this and keep everything on one line. But I'll be consistent, at least.
1:06:33
But either approach is fine. And then, down here, I'm going to use maybe a sub subsection. So let me delete this and do h3.
1:06:39
I'm just going to write the word three. And then just to be neat, I'm going to indent everything like this here.
1:06:45
So now if I go back to headings and I reload, I'm going to get some default formatting. It might not be the formatting you want, but it
1:06:51
looks like it's big and bold, but in decreasing order. H1 is the biggest. H2 is smaller.
1:06:57
H3 is even smaller. And you can go down to h6. And it gets smaller and smaller. And at that point, if you've got, like, sub sub sub sub
1:07:04
subsections of your book or paper, you're probably organizing it poorly. So they stop at some point there.
1:07:10
All right. Well, what else can we do in HTML? These things are omnipresent. Let me copy this HTML and close that tab, open my terminal,
1:07:17
and create a new file, like, code list.html. And let's make a list of information.
1:07:23
Let me just paste that HTML, just to save some time today, and change my title to list. Let me get rid of all of these paragraphs, just to simplify things.
1:07:32
So now I'm sort of back to where I began. And then inside of the body of this page, let me go ahead and make a list,
1:07:39
like foo, bar, baz. If you've never heard these words, these are, like, computer scientists go-to words.
1:07:45
A mathematician might choose x, y, and z by default. CS people tend to go with foo, bar, and baz for historical reasons.
1:07:51
So here's a list of three arbitrary words. If I go over to my other tab, go back to my directory listing,
1:07:59
there's my new file. Let's click on list.html, same problem. It's a list. But it's not one after the other.
1:08:06
Last time, of course, we fixed this with paragraphs. But you know what'd be nice? To make it a little prettier, like a bulleted list, which
1:08:11
are kind of everywhere these days. So I could try to simulate this. And you might be in the habit of doing this in some programs.
1:08:18
But of course, if I go back to my other tab, Reload, I'm just sort of making the problem worse visually.
1:08:23
But it turns out-- let me undo that-- there is an unordered list tag, otherwise known
1:08:30
as ul for short, that I can put all three of these words in an unordered list.
1:08:35
Let me go ahead and indent everything consistently. But to have three items in this list, I actually
1:08:41
need another tag, a list item tag. And I'm going to go ahead and add that tag there, list item here and there,
1:08:50
and then another list item tag here. And here's where it's a stylistic choice. I could move foo and bar and baz onto their own lines.
1:08:57
But this is going to start to get excessively tall, like, too much white space. So reasonable people will disagree. But this feels a little more readable to me.
1:09:04
So I'm going to leave it as such. Go back to my other tab. And now when I reload, you get a nice bulleted list by default.
1:09:11
And you see these all over the web. What if I want to have a numbered list, that is to say, ordered list?
1:09:16
Any instincts for changing these bullets to numbers? So ol is a good instinct.
1:09:22
And, indeed, sometimes HTML makes perfect sense. As in this case, if I change ul to ol, I don't have to manually number anything.
1:09:29
Because when I reload, it's going to use Arabic numerals automatically for me like this, top to bottom.
1:09:35
And what's nice about this is, if I go in and I insert things in the middle, I don't have to manually renumber things.
1:09:41
The browser is going to do the counting for me. And if you're doing an outline, you can actually specify whether you want 1, 2, 3, or A, B, C, or I,
1:09:49
double I, triple I, or so forth. There's different numbering systems you can use. But by default, we get our decimal numbers here.
1:09:56
I'm going quickly. But it's hard to get too excited about bulleted lists and such. But any questions on these tags thus far?
1:10:06
We'll by design try to escalate quickly momentarily. All right. So how about just a few other tags to make things more visually interesting?
1:10:14
Let me go ahead here and cheat by opening up a file that I made in advance that's going to demonstrate what a table looks like.
1:10:21
So here let me open a file that I brought with me called table.html. And because I brought it with me, I actually included a comment at the top.
1:10:29
And in fact, if you download today's files from the website, you'll see that they're generally commented, like our C code and Python code was.
1:10:35
It's a little weird. But here is the syntax for a comment in HTML. It's a less than sign, or open bracket, then an exclamation point, then dash
1:10:45
dash, two hyphens. Then at the very end of the comment, it's almost the opposite but not quite.
1:10:50
It's hyphen hyphen close bracket instead. Why these symbols? Humans probably decided years ago that there's
1:10:56
no way someone's going to accidentally type or rather, intentionally type those characters visually.
1:11:02
So let's use them for comment symbols as well. If you really want to type them, there is a way around that. But here is my table title.
1:11:08
And here is just kind of a little, maybe, guessing game. Here is a table tag with a tr child.
1:11:16
And here's the closed child. And then there's a bunch of td tags. So I'll give you tr stands for table row.
1:11:23
td stands for table data, AKA cell, to borrow language from, like, spreadsheet software.
1:11:29
Does anyone want to guess what this file is going to look like if I open table.html in my browser?
1:11:37
What is this reminiscent of? Yeah? AUDIENCE: Num pad. DAVID MALAN: Yeah. So it's like a numeric keypad from a phone, for instance, if you're dialing someone's number manually.
1:11:45
So let me actually go to my other tab. Go back to my directory index. There's table.html.
1:11:50
And it's not going to look very pretty. But it is structured in the way I might expect. And in my browser, I'm going to go ahead and just zoom in.
1:11:56
Command plus or Control plus will generally do this. It does look like it's laid out tabular in rows and columns
1:12:02
with everything very nicely aligned. So that might be useful as we get to larger and larger data sets. Let me go back to VS Code here.
1:12:09
Let me create one more program, for instance. And how about code image.html?
1:12:15
And just to save time, let me paste that code. And also, let me secretly copy over a file
1:12:21
that I brought with me that we've seen in the past. Let me close my terminal. I'm going to delete everything about tables from this file
1:12:28
because I'm just saving time by copying and pasting. But I'm going to rename the top to image. I'm going to get rid of the comment because it's no longer applicable.
1:12:35
But in the body of this page, I'm going to link to maybe an image of the Weeks bridge by the river.
1:12:41
So I'm going to use an image tag, img for short. And now, huh, it's obviously not going to be sufficient to just say image tag.
1:12:49
Because what image? So here is where attributes, again, get useful. This attribute earlier, though I didn't quite highlight it,
1:12:56
seems to indicate that this page is largely in English, as have been my past ones, the Latin one aside.
1:13:01
That attribute on the HTML tag is useful for browsers that have Google Translate
1:13:07
or something similar built in. And also, it's useful for SEO, search engine optimization. Because when Google and Bing sort of automatically
1:13:14
crawl my web page in the future, they'll know what language I intend for most of the content to be in, which might help them index
1:13:20
it and keep track of it for search results. So here, for the image tag, I'm similarly going to need an attribute.
1:13:26
And that attribute is called source, src for short. And what you put inside of its quotes for its value, double quotes
1:13:32
or single quotes, is the name of the image that you want to include. And I include it in advance in my code space,
1:13:39
a file called bridge dot ping from Week 4 when we played around with images. And if I go ahead now and go to my other tab, go back to my directory index
1:13:48
and zoom out, you'll see now not only bridge.png, portable network graphic, which I manually copied in, but also
1:13:55
image.html, which I just created. And voila, here is that same Weeks bridge.
1:14:01
It's a little too big for my browser window. We'll see in a little bit how we can fix things like that.
1:14:06
But indeed, that's an image that's now embedded into the page. But notice, if this image were ever broken,
1:14:13
or if I had visual difficulties such that I might have screen reader software for accessibility installed, it's
1:14:19
generally good practice to also make sure that pages are accessible as possible.
1:14:24
And so some tags have additional attributes you can include. Like, for an image here, there's actually an Alt attribute that specifies alternative text
1:14:32
to describe this image. This is what a human would see if they have a very slow interconnect connection. And before the image downloads, they can see this alternative text.
1:14:40
Or if I'm blind, I need a screen reader, I could have these words recited to me verbally by providing this clue.
1:14:47
So it's best practice to include this, like, photo of bridge so that all users can know what they're looking at, clicking on, or the like,
1:14:54
so keeping that in mind, too. All right. Let's do one other piece of multimedia. Let me close these two tabs.
1:15:01
Let me open my terminal and open up a file called video.html. Let me go ahead and copy, secretly, a file called video.mp4,
1:15:10
which is a common video file format, and close my terminal window and go ahead and paste in here some HTML from before.
1:15:18
But let's now embed a video file, as you might if making a video-based website. Let me rename this one, too, to video.
1:15:25
Let me get rid of the old comment, which is not applicable. And it turns out videos are almost as simple.
1:15:30
There is a video tag. There is a bunch of different attributes we can put on that.
1:15:36
But I'll come back to that in a moment. But videos, because you might want to have high resolution, low resolution,
1:15:42
depending on people's bandwidth, because these things can be big, they actually have source children.
1:15:47
And confusingly, it's actually S-O-U-R-C-E, not S-R-C, in this case.
1:15:52
And even more annoyingly, it takes an attribute called source.src. This is not good design.
1:15:58
But this is what we're stuck with, video.mp4. And then the type of this video, which you could generally
1:16:04
look up if the browser doesn't recognize it, video/mp4. This is what's known as a content type or mime type.
1:16:10
And then, I can actually configure this. And you would only know this by taking a class, reading a book, looking at an online reference.
1:16:16
I can actually add some video controls to the website, like a Play button, a Pause button, and all of that.
1:16:21
I can mute the video by default. And so this is just going to modify the behavior of this video tag.
1:16:26
But this is anomalous. For some attributes, it just doesn't make sense to have values.
1:16:32
Because muted, it sort of says all the information we need. We could do, quote, unquote, "true."
1:16:38
But humans decided years ago not to bother with that. So some attributes do not need value.
1:16:44
So you do not need equal signs or quotation marks. And you would only know this from, say, documentation.
1:16:49
All right. Let me go back to my directory listing. Let me go back here to this here.
1:16:54
You'll see that there's now not only video.mp4, but also video.html. I hope you'll forgive me for this.
1:17:01
There's at least no sound. But when I click on this page, it embeds a video here, which I can then click on the controls for.
1:17:07
And you see some short video file playing here, albeit without sound. All right. None of that, let me go back here to my VS Code.
1:17:14
And let's play around now with what the web is really known for, which is hyperlinks.
1:17:19
So hypertext markup language, HTML, is all about linking one site to another, one page to another.
1:17:26
And nothing we've done thus far is interactive beyond this own video controls. So let me go ahead and do this.
1:17:31
1:17:38
Let me go into VS Code here. And let me go ahead and create the simplest of files
1:17:44
that just allows me to click on a link. So let me go ahead and copy this to save time, open up VS code's terminal window.
1:17:51
Code a file called link.html. I'll close my terminal. Paste this code. Rename video to link.
1:17:57
Get rid of the actual video tag. And in the body of this page, let's do something simple like invite people
1:18:02
to visit, for instance, Harvard. All right. If I now go to my directory index and reload, we'll now see link.html.
1:18:11
And of course, this doesn't really do anything useful, because I literally just used English text.
1:18:17
All right. Well, what if I do what you're in the habit of doing on social media and various websites, visit harvard.edu.
1:18:25
Let me go back to the web page, reload. The text changes. But it's clearly not automatically linking.
1:18:31
I still can't click on this. All right. Well, maybe it needs to be www.harvard.edu.
1:18:36
Let me go back, reload. All right. Still not auto linking. Let me go over here. And maybe it needs https:// and a slash at the end, like a full URL.
1:18:46
Let's go over here, reload. And it's still not working. I can highlight and copy it, but that's not very user friendly.
1:18:52
So what's going on? Well, all of today's social media sites, when you copy paste a URL, someone at the server side wrote code, be it
1:19:00
in Python or JavaScript or anything else, to automatically notice and detect URLs and then
1:19:06
wrap them with HTML tags that actually hyperlink them. So what I actually need to do here is this.
1:19:14
I'm going to introduce an anchor tag, a for short. The hyper reference attribute of which is the URL that I want
1:19:21
to send the user to, so href for short. I'm going to close the tag.
1:19:26
But then, in between the start tag and close tag, I'm now going to put the text that I want the human to see.
1:19:33
So it's a lot more verbose. But this is what websites like social media sites
1:19:38
are generating automatically for you when they just detect with a pattern that you have typed something that indeed looks like a URL.
1:19:45
Let me go back to VS Code. Let me go back to this tab here and reload. And now we actually see a working link.
1:19:52
And this is going to be super small. You're not going to be able to see this quite well. But if you hover over this link, you'll generally see in most browsers
1:19:59
a little clue at the bottom as to where you're going to be directed before you click there. This can help if you're a little suspicious
1:20:04
and might not want to click on the actual link. It's small on my screen, but hopefully more visible on yours. That's not generally the case on mobile in quite, though, the same way.
1:20:13
But notice that this very simple primitive of anchor tags like this can pretty quickly be abused, unfortunately.
1:20:20
In fact, let me go ahead here and go back to VS Code. And I could do something malicious like this,
1:20:26
like, actually trick someone into applying to Harvard instead of Yale by just changing the href to not match the text that the human is seeing.
1:20:35
And if I reload the page here, you'll see that it looks like I'm going to Yale. But notice, super small, bottom left-hand of my screen,
1:20:42
it still says the real URL. But you can get even more malicious. You can not just say Yale. You could literally say https://www.yale.edu/.
1:20:50
You can make it look like a real URL, reload it. And now it's really quite malicious.
1:20:57
And this is representative of what you all probably know already as phishing attacks, P-H-I-S-H-I-N-G, whereby you're being socially engineered.
1:21:05
People are trying to dupe you into clicking something that leads you to your PayPal account, typically,
1:21:10
so that you log into some bogus website. Now you've given them access to your account and you're out some money.
1:21:16
It's this simple because of, unfortunately, these building blocks of HTML.
1:21:22
All right. With that said, any questions on this?
1:21:29
No? All right. How about just for one final flourish before snacks will be served,
1:21:34
let me propose to introduce some final features herein. It turns out, and I'll open some of these premade already.
1:21:42
Let me open up VS Code and open up a file called meta0.html.
1:21:48
This has nothing to do with Meta, the social media company. It has to do with metadata, or specifically, meta tag.
1:21:55
It turns out that in the head of the web pages that we've written thus far, we've only had titles. But it turns out there's actually literally a tag
1:22:02
called meta that has a couple of attributes like name and content. And this one here, it's a little arcane, but it's very common
1:22:09
to copy paste these into the source code for websites nowadays because essentially, this makes them mobile friendly.
1:22:15
Instead of making the font some default small size, it will take into account the width of the phone
1:22:21
or the tablet and sort of scale the font proportionally. So there's some useful accessibility and user friendly tips like this.
1:22:27
There's other use cases for meta tags like this. Let me open a file called meta1.html that I made in advance.
1:22:34
Here are three meta tags inside of this file. They're using a property attribute with a content attribute as well.
1:22:42
And this is a little more specific. But nowadays, too, on social media, when you copy and paste a URL into a message online and hit Enter,
1:22:50
you very often see a preview of that link. It's sort of automatically generated. It makes a nice pretty image and some nice fonts.
1:22:56
Where does that image come from? Where does that information come from? From these meta tags, any web page can have meta tags like this
1:23:04
so that when this page's URL is copy pasted into social media sites or others, those sites
1:23:10
know what preview to show to humans. It comes literally from the values of these tags.
1:23:15
So for instance, this would create some user friendly preview that says CS50, Introduction to The Intellectual Enterprises
1:23:21
of Computer Science and The Art of Programming. And in this case, it would show a picture of a cat as the default image for that particular page.
1:23:28
You have full control as a web developer over those kinds of things.
1:23:33
Lastly, when it comes to features of HTML, let's go ahead and quickly
1:23:39
reimplement Google, if we may. So let me go ahead and create a new file here called search.html.
1:23:47
Let me copy paste some code to save time. Let me go ahead and get rid of all of these meta
1:23:53
tags to make a different point with this one. Let me get rid of that comment. Change this title to be, say, search instead.
1:24:01
And inside of the body here, let's do this. I'm going to introduce a form tag. And now in the form tag, I'm going to create an input, a text input.
1:24:10
And let's go ahead and let's just say that. And now I'm going to have a button that has,
1:24:18
let's say, button, that has a value of search, so super simple and not yet
1:24:25
complete. But let me go to my directory index and back. Let me open up search.html.
1:24:31
And I actually have the beginnings of a search form, an interactive form for the web. But it doesn't actually do anything useful yet.
1:24:37
But let me do this. Let me go to the actual google.com. Let me search for something like cats, C-A-T-S.
1:24:43
And of course, we're going to see a whole bunch of cats here. And we're going to see that the search box was automatically
1:24:50
populated at the very top of the page. Now the URL that Google led me to, even though I started at the very simple google.com, is actually pretty long.
1:24:59
And I'm going to frankly just delete anything I don't understand. Because I'm going to distill this URL to just this one here.
1:25:05
It turns out that in URLs you can also put user input in the form of key value pairs.
1:25:11
So in any URL, you can actually have not only a path like we saw earlier, you can have a path with a key
1:25:18
and a value prefixed with a single question mark. And in fact, if you want to have two keys and values,
1:25:23
you just interpose them with an ampersand instead. So this is to say there is a standard way in HTML
1:25:30
and really HTTP for sending input from a browser to a server. And it's generally formatted like this.
1:25:36
What this means is actually this. Let me zoom out, close that tab, and open a brand new one.
1:25:42
And let me manually go to-- and I'll zoom in-- https://wwww.google.com/search?q=dogs.
1:25:53
Now it has to be q, because that's what Larry and Sergey of Google fame decided two decades ago when they made Google itself.
1:25:59
Q stands for query. But they could have called that key anything they want. I'm going to hit Enter after zooming out.
1:26:05
And what you'll see is that I don't need google.com to search for me. I can literally go to a URL of all of the dog search results manually.
1:26:13
Now no one's normally going to do that. That makes no sense. But it does suggest how simple the mechanics of the web are.
1:26:20
If you want to pass input to a server, you suffix the URL with a question mark, key equals value.
1:26:26
Key equals value may be separated you buy these ampersands, as I proposed. So what does this mean?
1:26:31
Well, Google really did the hard part, the back end, the database. They crawled the internet and found all of these cats and dogs.
1:26:37
But I can make the front end, that is the user interface that still works for it. And I'm going to do this.
1:26:42
I'm going to add an attribute to my form tag that specifies an action attribute of https://www.google.com/search.
1:26:55
And I'm going to specify that the method I want the browser to use is indeed get. This is inconsistent. I capitalized it as all caps before.
1:27:02
In HTML, you actually do it as lowercase. But that's also the default. So strictly speaking, I don't even need to specify that.
1:27:08
But I will, just to be pedantic. Inside of my input, my text box, which used to look like this, just a big white rectangle,
1:27:15
I'm going to actually give it a name of q, because I know that's what Google servers expect. And I'm also going to specify--
1:27:24
eh, just that for now. Let me go back now and reload. And it's going to still look very simple.
1:27:30
But notice this. If I type in cats and click Search, in just a moment,
1:27:35
I'm going to be whisked away from my own Codespaces URL ending in search.html to, after zooming out and clicking Search, the actual google.com.
1:27:45
Which prepopulates the URL with q equals cats up top, prepopulates this text box with the user's input,
1:27:52
which is to say, like, the front end of google.com is trivial, as is most every website.
1:27:58
It's as simple as these key value pairs and things like web forms like that. Now I can make this a little prettier.
1:28:05
And just so you've seen it, if I specified that the type of this input isn't text, which is the default, but is search,
1:28:11
I actually get some nice features. Let me reload this now. And if I start typing in, like, dogs, now I get this little x
1:28:17
to click, which clears it. So a lot of websites have that. It's a little bit of a nicety. If you don't know what you want the user to type in,
1:28:23
you can actually be kind of explicit for them. And you can add a placeholder attribute that says query or keywords
1:28:29
or whatever you want to show them. If I go back to the browser and reload, you'll see a grayed out text that's not actually there.
1:28:36
It goes away if I type in bird, for instance. But it's explanatory, placeholder text for the user.
1:28:41
You'll notice that it wants to autocomplete cats or bird or dog or anything I've typed before.
1:28:46
You can disable that. There is an attribute called autocomplete
1:28:51
whose value can be either on, which is default, or off, which can be explicitly specified.
1:28:57
And notice this, too. When I reload the page, it's actually annoying in terms of user experience.
1:29:03
Before I can search for anything, I have to move my cursor, I have to click in the text box. And now it has focus, so to speak.
1:29:08
It gets highlighted in some color, usually blue. That's not the best website. Why are you making the users pick up their mouse or their trackpad just
1:29:15
to click on the only thing they're going to do anyway? So there's another attribute that's handy, Auto Focus, which will just move the cursor there for the user.
1:29:24
So this is to say, even though a lot of websites don't do this, there's a lot of functionality that you can enable by just
1:29:30
knowing the language all the more. So with that, we now have a pretty useful feature.
1:29:36
In fact, heck, I can say this is Google Search, change the value of that button, reload.
1:29:41
And now I'll go ahead and type in birds, Enter, and voila. Now we have a whole bunch of birds as well.
1:29:49
So that's a lot. I think it's definitely time for a snack. So let's take a 10-minute break for a snack. And when we come back, we'll make all of this look prettier.
1:29:56
All right. So we are back. And it was brought to my attention during break
1:30:02
that we were pretty darn close to clearing one of these rows. And I will concede that your classmates, Darwin and Jude,
1:30:09
socially engineered me into saying one of the remaining squares that they needed. And so I'm sad to say that bingo was declared during break, which Carter
1:30:17
has already confirmed, because I was tricked into giving a long answer to a short question. So congratulations to those two.
1:30:24
I do dare say, too, that whole bit with safetyschool.org probably
1:30:29
isn't going over well in New Haven. So I'm pretty sure we can check off this box here. However, as promised, in fairness, since we love them both equally,
1:30:37
I thought it only fair to resume now with a look at perhaps one of the best Harvard-Yale pranks that was actually on us,
1:30:44
with this 2.5-minute glimpse at how our classmates at Yale pranked Harvard some
1:30:50
years back. If we could dim the lights now for this. [VIDEO PLAYBACK] [MUSIC PLAYING]

## [Harvard Pep Squad Prank](https://youtu.be/ciz2UaifaNM?t=5457)

1:30:57
1:31:16
[CHEERING] [BAND MUSIC PLAYING]
1:31:23

- All the way at the top and then you pass it down. [CROWD NOISE] - [INAUDIBLE] this for you, Yale.
  1:31:29
  We love you, Yale. - We're here to cheer for Harvard. - Yeah! Go Harvard!
  1:31:34
- Go Harvard! - [INAUDIBLE] one and pass it down? - Pass them down.
  1:31:40
- Great. - It says go Harvard. - We're nice.
  1:31:45
- You see that [BLEEP]? - Look at them. They have the paper! - It's going to happen.
  1:31:51
- It's actually gonna happen! - I can't [BLEEP] believe this! - What do you think of Yale?
  1:31:57
- They don't think good. [LAUGHTER] - It may be a complete mess. I don't know. - Dude, does everyone have it?
  1:32:03
  Does everyone have their stuff? Does everyone have their stuff? - The probability that it's going to be legible it's very small, though.
  1:32:09
- I agree. - It's too complicated. - [INAUDIBLE]. - I know. But it's too complicated. - What houses are you guys in?
  1:32:16
- [INAUDIBLE]. - That's not a real house. - How many extra are there? - Ho-fo. - Yeah.
  1:32:22
- You guys aren't from Harvard, are you? - Fo-ho. - Pforzheimer. - Yeah, but you said ho-fi.
  1:32:28
- Just make sure everyone has it. - Well, she's probably drunk. - It looks like they're still passing. Are all the cards distributed? - [INAUDIBLE].
  1:32:34
- All right. Let's do it now. [CHEERING]
  1:32:47
- Hold up your signs! - [BLEEP]. [CHANTING] - You suck. You suck.
  1:32:53
  You suck. You suck. You suck. You [BLEEP]. - Did it. - [BLEEP].
  1:32:58
- You suck. You suck. You suck. You suck. You suck. You suck.
  1:33:05
- What do you think of Yale, sir? - [INAUDIBLE]. - One more time! One more time!
  1:33:10
  1:33:17
- Oh, and there it goes again! [CHANTING] - Harvard sucks! Harvard sucks!
  1:33:23
  Harvard sucks! Harvard sucks! Harvard sucks! Harvard sucks!
  1:33:30
  Harvard sucks! Harvard sucks! Harvard sucks! Harvard sucks! Harvard sucks!
  1:33:35
  Harvard sucks! [END PLAYBACK] DAVID MALAN: So fair is fair there. So now back to some HTML.
  1:33:41
  And we will transition momentarily then to this other language, CSS, by which we can style things all the more.

## [Regular Expressions](https://youtu.be/ciz2UaifaNM?t=5627)

1:33:47
So there's this feature in HTML that's actually present in Python, even though we didn't use it yet, and that's present in JavaScript
1:33:53
and, really, most modern languages known as regular expressions. Which is otherwise known as regexes, which
1:33:59
is a way of using patterns to validate input or to extract information from strings.
1:34:06
And so by that I mean this. Let me go over to VS Code here. Let me go ahead and create a new file called register.html.
1:34:14
I'm going to copy paste some code from earlier, just to save some keystrokes. And in here, I'm going to go ahead and change my title to register.
1:34:21
And in my code, I'm going to go ahead and create a very simple form representative of a registration form now.
1:34:26
So in this body, I'm going to do a form tag. I'm not going to bother sending it to Google or to any server in particular
1:34:33
here. I'm going to give it an input tag with autocomplete equals off, as before. I'm going to have auto focus on as before.
1:34:40
I'm going to give this form field the name of email this time instead of q. I'm going to give it a placeholder of quote,
1:34:46
unquote "email," just so that the user knows what they're supposed to type. And it turns out that browsers have not only type text or search, but also
1:34:57
type email, whereby you can rely on the browser to ensure that the human has actually typed in an email address.
1:35:02
Now I'm going to go ahead and have a button that this time will be called Register. And now let's go over to my other tab, reload my directory index.
1:35:09
There's register.html. And we'll see a relatively simple form field now. But it's prompting me to register with some email address.
1:35:16
If I go ahead and sort of type in just my name and try Register, you'll notice that the browser sort of yells at me with the built-in error
1:35:22
message saying, oh, please include an at in the email address. And it's pretty good in that if I do mail an at, but nothing more,
1:35:29
which is also not valid, and try to register, it's telling me still that it's incomplete. So built into browsers is some defense against incorrect user input
1:35:39
in this way. If I finally do type in malan@harvard.edu and click Register, then the form would be submitted successfully to the server.
1:35:47
If, though, I want to tolerate only .edu addresses because I'm making an education-themed website for students in the US,
1:35:55
I can actually add another attribute here, which is actually quite useful, too. I can add a pattern attribute.
1:36:01
And inside of its value, I can put one of these things called a regular expression, or a regex.
1:36:07
That is an actual pattern that the browser should match the user's input against and make sure it indeed matches.
1:36:13
And this is going to look a little cryptic. But I'm going to go ahead and do this. .+@.+ backslash dot edu.
1:36:22
Now this looks a little weird. But it turns out I'm using certain building blocks that we'll just scratch the surface of today.
1:36:28
But it's an incredibly useful and powerful feature in programming languages more generally.
1:36:33
Because in the world of regular expressions, there are certain patterns that mean something. And here's a really good URL of some documentation
1:36:40
they're for in the world of the web and JavaScript, specifically. And here's kind of a short cheat sheet, some excerpts thereof.
1:36:46
It turns out in the world of regular expressions or patterns, a dot represents any single character except line terminators,
1:36:52
like backslash n. A star or an asterisk represents 0 or more times.
1:36:58
A plus means one or more times. A question mark means 0 or one time. A number inside of curly braces means n times, or n occurrences.
1:37:07
And then two numbers in curly braces, n comma n, means at least n times, but at most, m times or occurrences.
1:37:15
And then there's a few other, actually. So what does that mean? Well, let me go over to VS Code again.
1:37:21
And let me zoom in on the pattern I used. And it would seem that, in this case, a dot represents any character.
1:37:28
Plus means one or more. So one or more characters to the left of an sign, then literally the at sign.
1:37:34
Then another dot plus means one or more characters to the right of the at sign. But the whole thing has to end in .edu.
1:37:42
But there's this additional backslash before the last dot. And why might that be, intuitively?
1:37:48
Even though I've not said? Because I want a literal dot, a literal period, not any one character there.
1:37:54
So I escape the period to make it have not special significance per this cheat sheet, but rather a literal period.
1:37:59
So what this means is if I go actually back to VS Code here and I try to claim to work at like malan@harvard.com and click Register,
1:38:08
that's a valid-looking email address. But when I click Register now. Whoops! Sorry. It went through because I did not reload the page after making the change.
1:38:16
So I screwed up. Let me go back to the register.html URL.
1:38:21
Let me reload the page and type in malan@harvard.com, for instance,
1:38:26
and even-- sorry. Let me type in malan@harvard.com. And even though it's a valid-looking URL, it does not in fact and in .edu.
1:38:35
So the browser can defend against that in this way. But the more important takeaway for now is
1:38:40
that as useful as this is, as user friendly as this, this is not generally the best technique for validating user input
1:38:47
and protecting against invalid user input. Why? Browsers can't be trusted.
1:38:53
Or more generally, clients can't be trusted. Why? Because the way HTML works as we've seen it thus far
1:38:59
is that everything is happening on my own Mac, or your own PC, or your own phone locally.
1:39:05
Per the envelope story we told earlier, your browser is downloading the HTML, reading it top to bottom, left to right, and then
1:39:11
displaying it on your computer. But we've already seen that my computer, for instance, has built into it these developer tools.
1:39:18
And there among the tabs here, are not just that network tab, let me actually go to the Elements tab, which we haven't seen previously.
1:39:25
In the Elements tab, you actually will see a pretty, printed version of the same HTML.
1:39:31
But what that means is that you can not only see the HTML, you can actually change it. Now you're not going to be able to change it on the server.
1:39:38
But I can absolutely change my own copy thereof. So suppose I'm now a hacker in the story. And I really want to register for this website,
1:39:45
but it's apparently restricted to people with .edu addresses. I don't have a .edu address, let me propose.
1:39:50
So that's fine. Let me actually go into the developer tools. Let me just double click on the attribute
1:39:57
there, highlight it, and boom. Now gone is that pattern entirely.
1:40:02
The web browser now will let me register with malan@harvard.com because the developer tools give you full-fledged access to the underlying
1:40:10
HTML. So if I've changed the HTML, the defense is no longer in place. Now what's the takeaway then is client-side validation
1:40:18
is wonderfully user friendly. But it's not secure. It's not safe. So next week, we'll spend more time server-side
1:40:24
at making sure that even if someone messes with my HTML or my website, they still can't actually get through and do anything bad on the server.
1:40:32
And this is true in general, too. Let me actually, just for fun, go to, maybe, let's say, harvard.edu.
1:40:39
Let me open up my development tools. And let's see where I might go here.
1:40:45
Suppose that I want to hack into harvard.edu. Well, notice that I'm on my elements tab and there's a lot of HTML that composes this page.
1:40:52
And notice that these triangles indicate that most of it's been collapsed. But if I expanded them, I could see more and more of the tags and attributes.
1:40:59
But suppose I'm now a hacker. And I want to maybe delete this menu. Notice that you can also right click or Control
1:41:05
click on any element in a web page, typically. With these developer tools, click Inspect or some similarly named menu
1:41:12
option, and you can actually been whisked away to the actual HTML tags
1:41:18
that implement that feature of the web page. One, it's wonderfully useful for learning how things work, teaching yourself new tricks, and even fixing problems.
1:41:25
Here, though, I'm going to try to use it maliciously. And I'm going to highlight this tag here, div tag, as it's called.
1:41:31
I'm going to delete it. And watch what happens at top right. Gone is the menu. Now, of course, if you go to harvard.edu right now, the menu is still there.
1:41:39
If I reload harvard.edu the menu is back. So it's only my own local copy. But this does speak to how you should not
1:41:45
trust anything happening client side. Because someone can be mutating that same code.
1:41:51
Now it turns out there's other patterns that you can use in regular expressions. For instance, these are what are called character classes.
1:41:58
You can, for instance, specify in square brackets some number of digits or characters that you want to match against.
1:42:04
This is a range of characters, 0 through 9. So it's effectively the same thing as that, but easier to type. There are certain shortcuts, backslash lowercase d means any decimal digit.
1:42:14
Backslash capital d means anything that's not a decimal digit. And dot dot dot, there's bunches of other patterns.
1:42:20
You might use these to maybe validate a phone number in a web page, if you want it to be formatted in a certain way, for better or for worse.
1:42:26
But long story short, regular expressions will be, someday, your friend as you try to solve certain problems with data.
1:42:34
As an aside, it does escalate quickly. So this is typically the regular expression
1:42:39
that browsers nowadays use to validate email addresses. It is way more complicated than . +@.+.
1:42:48
Why? Because you can't have @@@.edu.
1:42:53
There's certain characters you don't want to allow. There are certain characters you do want to allow. So long story short, this is a much larger regular expression
1:43:01
that is more correct when it comes to valid email addresses. All right. So with that said, there's one tool with which you should be familiar.
1:43:10
And that is at this URL here, validator.w3.org. And this is a free web service from the World Wide Web Consortium,
1:43:17
which is the group that essentially standardizes this HTML language. And if you go to their web page, there's a few different ways
1:43:24
to validate your own code. Essentially, check it for correctness by typing in its URL,
1:43:29
otherwise known more generally as a URI, by uploading a file or by direct input. So just for kicks, for instance, I'm going to go into VS Code
1:43:37
and grab my HTML that I just made. I'm going to go back to validator.w3.org and paste it into the direct input box
1:43:44
and click Check. And it's just a nice handy website that, if I scroll down, in green, you will hopefully see this, no errors or warnings to show.
1:43:53
So it's a handy feature just to make sure that at least syntactically your code is correct, even if it's not behaving the way that you might want.
1:44:01
All right. With that said, the second of today's three languages, and we'll just scratch the surface ultimately of JavaScript

## [CSS](https://youtu.be/ciz2UaifaNM?t=6247)

1:44:07
to give you a sense of its capabilities, but CSS is something that's worth understanding some of the basic building blocks
1:44:12
thereof. So let me propose that there are some additional terms to know.
1:44:19
In the world of CSS, we're, again, going to have key value pairs. In this world, they're called properties instead of attributes.
1:44:25
Why? It was invented by different people, but it's the same kinds of ideas. In the world of CSS, you're going to have
1:44:31
ways of specifying different selectors, as they're called. That is to say we're going to be able to specify
1:44:36
the font size, the color, the margins and a lot of aesthetics when it relates to tags in our web page.
1:44:43
And there's going to be different ways to select those tags, as we'll soon see. In an HTML page like this, this is our super simple one with which we began,
1:44:51
it turns out that you can also include a style tag in the head of the page that has some
1:44:56
of your stylistic decisions, font sizes, colors, margins, and all of those kinds of aesthetics. We'll also see another approach whereby you can relegate all of that stuff
1:45:05
to a separate file, like styles.css, or something .css. And you can link to it in the head of the page.
1:45:12
Link here does not mean A, like, ideally our anchor tag before would have been called a link.
1:45:17
But it's not. This just means that these two files are linked in some way conceptually. All right.
1:45:23
So that is to say we can use these kinds of tags now to enhance our own code.
1:45:29
So let me propose that we do this. Let me go into VS Code here. Let me go ahead and create a very, very simple home
1:45:35
page for someone like John Harvard by running code of-- how about home.html?
1:45:42
And in home.html, I'm going to copy paste some of my starter HTML from before. And now in the body of this page, I'm going to do a few things.
1:45:50
I'm going to have a web page with a paragraph up here that just says John Harvard as the title thereof.
1:45:57
Another paragraph that says something simple like welcome to my home page exclamation point.
1:46:02
And then, like, a footer at the bottom and a third paragraph that's a copyright, say, John Harvard, for instance.
1:46:10
So super simple, but representative of a header, a main part of the page, and a footer thereof.
1:46:15
If I go into my other tab and reload my directory listing, I will see now home.html.
1:46:23
And it's going to be pretty bare bones, right? It's the same text, same font size. It is three separate paragraphs.
1:46:28
But let me start to stylize this a little bit differently. Let me make the top bigger and bolder, perhaps, or rather,
1:46:35
the top bigger and centered and make this text shrink thereafter. So I'm going to go ahead and do this.
1:46:41
It turns out that you can have not necessarily a style tag, but even more simply, a style attribute on certain tags, like this.
1:46:48
I'm going to add a style attribute that has a font size of maybe large.
1:46:54
And how about a style attribute here, a font size medium.
1:47:00
And then maybe down here-- oops, close quotes. And then down here-- whoops.
1:47:05
Thank you. OK. I owe you some cookies. All right, so style here of font size small, so relatively simple ideas.
1:47:14
And here is just another stupid syntax for key value pairs. Again, left hand is not talking to right hand.
1:47:20
In CSS, cascading style sheets, which is the language we're now talking about, it's key colon value.
1:47:27
In HTML, it's key equals quote unquote value. It's just different techniques for the exact same dictionary-like idea.
1:47:34
All right. If I go back to my other tab and reload, notice that it's a little subtle, but it is large, medium, and small.
1:47:41
I didn't center things yet, so let me do that. It turns out that this thing collectively is what's called a property.
1:47:47
And a property is defined by a key value pair. If you want to have multiple properties for key value pairs,
1:47:52
in CSS, you separate them with semicolons. So those are back. And if I want to center the text, I can do text-align: center.
1:48:00
I could now end my thought with the semicolon. It's not strictly necessary. But I'll keep it just so that I'm consistent.
1:48:06
But it's only necessary if you have more than one. I'm going to go ahead and center everything, though.
1:48:12
So I'm going to go down here and add a semicolon after medium, down here and add a semicolon after small.
1:48:17
So I align, text-align center, center, center for all three paragraphs. If I go back to this other tab and I reload, voila.
1:48:25
Now it is, in fact, centered. But here's where we can start to have a conversation about, maybe, design.
1:48:32
So I claim this is correct. But is this perhaps the best design? Well, maybe not.
1:48:38
I mean, these aren't really paragraphs, first of all, semantically. It's not even complete sentences.
1:48:43
But there are three different divisions of the page, right, like, the header up there, the main part in the middle, and then
1:48:48
the footer. So it turns out, and we saw a glimpse of this in Harvard's source code, there's another tag instead of p for paragraph called div, for division.
1:48:58
And even though this is actually not going to have much of a functional effect at first, it's maybe semantically a bit better.
1:49:04
Because, again, these aren't really paragraphs. So if I really want to nitpick, I do have three divisions of the page.
1:49:09
So div is a very common way to give yourself just a rectangular region of the page to style as you see fit.
1:49:16
If I go back now and reload, notice that it does tighten things up. The paragraph tag gave me some vertical whitespace for free.
1:49:23
So I've lost that. But I could add it back if I really wanted to. But now, let's come to this question of design.
1:49:29
What's redundant about what I've done thus far, even if you've never seen CSS before?
1:49:34
Yeah? AUDIENCE: [INAUDIBLE]. DAVID MALAN: Yeah. I mean, I had to center all three divs, which is just sort of stupid,
1:49:40
it would seem. Copy paste has generally not been necessary. Even though I'm doing it to save time today in general, when the results are copied and pasted, ultimately, this
1:49:48
has not been good practice in any of our languages. So it turns out I can do this. Let me actually delete this one.
1:49:54
And I can keep or get rid of the semicolon, but I'll get rid of it for parity with our first version. I'm going to get rid of this one, too.
1:50:01
And you know what? Here's the C in CSS cascading. It's more like a waterfall effect.
1:50:07
And if I go up to a parent tag here, like, the body is the parent of all three divs, I could put the style attribute here
1:50:15
and say text-align: center there. And that has the effect of cascading down onto all three
1:50:21
of the children that are nested inside of it. So now it's sort of better designed because I've only said text-align: center once.
1:50:27
If I go back to the web page and reload, it has no functional impact visually. But it's better design.
1:50:32
Because if I want to align it left, or right, or center, I can change it in one place and not three independent places.
1:50:39
All right. What else might I change after this here? Well, it turns out that I could do something a little clearer as well.
1:50:48
This copyright symbol? I mean, it's just sort of homemade with two parentheses and a C. It turns out that there are ways to get special symbols in HTML.
1:50:56
And you can use what are called HTML entities. You would only know these by looking them up or memorizing the numbers.
1:51:02
But it turns out that number 169 is the special HTML
1:51:07
entity for an actual copyright symbol. So let me zoom in here and then reload.
1:51:12
And you'll see that the parenthetical C actually becomes the proper mark for copyright, so marginally useful.
1:51:19
Or you could copy paste it from some other website, for instance, if you didn't know how to type it on your own keyboard.
1:51:24
So that's an HTML entity, another feature with which to be familiar. But having three divs on a page isn't necessarily ideal nowadays,
1:51:32
especially for search engine optimization, SEO, for screen readers for accessibility.
1:51:37
Because at a glance, I don't really know which of these divs is the most important. Arguably the footer is generally for the human reader,
1:51:44
like, the least information-bearing piece of content. So why don't I try to signal as much to the browser, to the screen reader,
1:51:51
to the search engine? So it turns out there are what are called semantic tags nowadays. Indeed, we're up to version 5 of HTML.
1:51:58
And one of the relatively newer features is, instead of using generic divs, you can actually use actual names of tags,
1:52:04
like header and main and even footer. And here, too, the visual effect is not going
1:52:10
to be any different if I go here and reload. But there's more semantic information underneath the hood.
1:52:17
So that, again, all of those different types of services, the browser, the screen reader, and the like
1:52:22
just know a little more about the page. And maybe a screen reader now would focus on the main part of the page
1:52:28
before reciting all of the fine print in the footer, for instance, to the human. All right. Well, what else could we do here?
1:52:34
Well, it would be nice at some point to be able to reuse these styles. And if I find myself making not one page but two pages or 10 pages or 100 pages,
1:52:43
it's kind of annoying to have to type out all of the same styles. So wouldn't it be nice to start to factor this stuff out?
1:52:50
Well, I can do that, too. Let me actually go ahead and do this. Let me get rid of this attribute and this attribute and this attribute.
1:52:58
And honestly, too, as I do this, I would argue that the code looks just a little cleaner now.
1:53:04
It's more obvious what is a tag and what the actual data of the page is, metadata and data, if you will.
1:53:09
But I've lost all of my styling. But wouldn't it be nice to preserve some of the styling by doing what I proposed earlier, which is using
1:53:15
not a style attribute, but a style tag. And indeed, you can put a style tag in the head of your web page
1:53:22
where you can put all of those same properties. And you need a little more syntax, a few more keystrokes.
1:53:27
But I can say this. If I want to center the entire body of my page, I can actually do so by specifying text-align: center;.
1:53:38
Here the semi-colons are going to be generally necessary, especially have you multiple properties. Next I'm going to say header.
1:53:44
And inside of these curly braces, font-size: large, unlike C, where you could get away with no curly braces
1:53:51
if there's a single line, you do need them in CSS. In the main tag, let's go ahead and style with font-size: medium.
1:53:58
And then in the footer tag, let's go ahead and style with font-size: small.
1:54:04
Now this looks a little worse. Because it just kind of blew up and it's a lot longer. But it is a step toward factoring this out.
1:54:11
And honestly, when it comes to web pages, I'm not the best artist in the world. I can make the data display.
1:54:17
But friends of mine are certainly better at making things really pretty and pixel perfect, so to speak. So it's kind of nice if I can isolate all of the style to one part of my file
1:54:26
and all of the content to another. Because maybe I could now collaborate with someone else. So if I go back to now the other tab and reload,
1:54:33
functionally, no different still. It still looks exactly the same. But I'm starting to make it a little better designed.
1:54:40
And in fact, there's another way to do this. Suppose that I find myself in the habit of very often centering text on a page.
1:54:47
And honestly, it's just a little annoying to have to type this out for every tag that I want centered. Well, I could create what are called classes as well in CSS.
1:54:57
It turns out you can make up your own words-- but I'm going to choose some reasonably named ones-- by prefixing them with a dot or a period.
1:55:04
And if I want to call this set of properties, even though there's just one, centered, I can literally write .centered there
1:55:11
instead. I can write this .large. I can call this .medium. I can call this .small.
1:55:18
And what this means now is I have reusable sets of properties, kind of like containers whereby anywhere I use the word "centered,"
1:55:25
it's going to get that one text-align: center property applied. Anywhere I use quote, unquote "large," it's going to be made large.
1:55:33
And so if I scroll down now here, I do need to reintroduce another attribute-- but it's a very common one in the world of HTML now-- that of class.
1:55:41
So class equals large. Down here I'm going to do class equals medium.
1:55:46
Down here I'm going to do class equals small. And it's getting a little more verbose, but I'm not polluting all of my HTML
1:55:53
with the actual styles. I'm just kind of having this layer of indirection and of abstraction, if you will, on top of those very specific properties.
1:56:01
And then for the body, I can do the same idea. Class equals centered. And if I go back to my web page here and reload, still looks exactly the same.
1:56:10
But I've kind of centralized where I can do things. And frankly, I could do something like this, color: red;.
1:56:15
I can package up multiple properties, go back to the page here, and reload. And now that has applied to everything.
1:56:22
So I have a reusable set of properties. Even though centered is maybe not the best name now, because it also makes things red.
1:56:28
But I can come up with reusable sets of properties. And honestly, one final flourish here would be let's not assume that my buddy, whether it's
1:56:36
my project partner or a colleague in the real world, it's kind of stupid to try to edit the same file. Because invariably we're going to break things on each other.
1:56:44
So I could actually do this. Let me take all of this. And I'll get rid of the red. Let me go ahead and highlight everything I just did and cut it to my clipboard.
1:56:52
I'm going to get rid of the style tag altogether. But I am going to go into VS Code and create-- how about a file called
1:56:59
home.css, just so I know what's what. And in this file, I'm just going to literally paste everything I just made.
1:57:06
But I'm going to go back to my home page here. And I'm going to add that other tag I proposed earlier, link href="home.css",
1:57:16
and I need one weird attribute, too. The relationship of this link is that of quote, unquote "style sheets."
1:57:24
And that's just the way it is according to the tag. And now one last time, if I reload this page, the red is going to go away.
1:57:30
Because I deleted that. But the font sizes and centering are still there. But what I've done was introduce some basic building
1:57:37
blocks in this language I claim is called CSS that's going to allow me to now centralize all of the styling, the aesthetics now
1:57:46
of my web page. All right. Let me pause here and see if there are any questions on these techniques
1:57:53
thus far. It's just more key value pairs. Questions on this?
1:57:59
No? All right. So here's where things can get prettier quickly. Let me go ahead now and close these two tabs.
1:58:06
Let me go into a file we created earlier called link.html, which you'll recall looked a little something like this.
1:58:12
And now we can make this web page behave a little more like the real world. Let me undo the phishing attack and just literally say Harvard down here.
1:58:19
But let me go ahead and start to style the anchor tag as follows. Previously, this page looked a little boring like this.
1:58:26
The link was blue originally. But because I visited harvard.edu, by default, the browser changes to purple.
1:58:31
Which is fine, but maybe you don't want that. Maybe we want something that's a little more crimson, for instance. So let me do this.
1:58:37
Let me go into the head of this link.html page. Let me add a style tag herein.
1:58:42
And in there, let me style the anchor tag as follows. Inside of this anchor tag, I'm going to do color: red.
1:58:50
And let's go ahead and leave it as such for now. Let me go back to the link page and reload.
1:58:56
And it's going to be a little subtle. But right now it's purple. And now it's definitely red. So I've modified that.
1:59:02
Now underlining links is good for accessibility. But a lot of websites choose to not underline them and instead
1:59:08
underline them when you hover over them. So that is an effect we can achieve, even though it might not be ideal. But let's at least demonstrate how websites are doing that.
1:59:16
I can specify that this link should have text decoration of none. Now I would only know that by having taken a class, read a book,
1:59:24
looked at an online reference. The default is underline. But I can override that by saying none.
1:59:31
So if I now go back to my page, reload, it's still going to be red. But it's now not going to be underlined.
1:59:38
But notice if I hover over it, it changes to a little pointer finger if I zoom in here. But it's clearly not underlining, so that's OK.
1:59:46
Because there's another way of selecting tags here. I can say a:hover.
1:59:51
And then inside of this CSS, I can say text-decoration: underline when the anchor tag is being hovered over with the cursor.
2:00:00
If I go back to my tab here and reload, still looks the same. But watch as my mouse gets close.
2:00:06
It now underlines, as a lot of websites do. So it's a relatively simple idea. It's not as compelling on mobile, especially,
2:00:13
because it doesn't do anything if you hover your finger over the glass of your phone. But it does work on laptops and desktops in this way,
2:00:19
even though it's perhaps a little passé now to do this kind of technique. But there's other ways to select tags on a page.
2:00:25
And in fact, let me go back to this one here. And in this page, let me propose that you can go in one of two places.
2:00:31
Visit Harvard or a href = https://www.yale.edu/ and then
2:00:41
Yale's website. So it's getting a little long. So I'm going to hit Enter. Because the browser won't care that there's some whitespace.
2:00:47
But at least, now I have two links on the page. If I reload this, you'll see that both of them
2:00:52
are red or crimson, which isn't quite right. But that's OK. I can actually distinguish these two somehow.
2:00:59
One way to do this would actually be to add one more HTML attribute that we haven't needed or used before, that of ID.
2:01:06
I can use almost any name for this ID that I want. And I'm going to say, quote, unquote, "Harvard"
2:01:12
is the unique ID of this link. And the unique ID of this link is quote, unquote, "Yale," for instance.
2:01:18
And what I can now do up here is I'm going to get rid of this color red. Because I don't want all anchor tags to be red, but I do
2:01:25
want Harvard tags to be red. So I can say #harvard and then color: red;, and then I can do #Yale
2:01:33
and I can say color: blue;, for instance. The hash symbol here represents an ID.
2:01:39
The dot we saw earlier represents a class. And when you don't have a symbol before it, it represents literally the name of the tag.
2:01:46
So when I mentioned these various selectors earlier, type selector is just the name of the tag.
2:01:51
Class selector is the dot. ID selector is the hash. And there's also ways to select attributes specifically.
2:01:57
So if I go back here in VS Code now, I've added a bunch of CSS here, properties.
2:02:02
But if I reload now, one of these should be red and the other is in fact blue. So in short, just by way of these style attributes and these style tags,
2:02:12
we have a lot more control over how we can actually stylize our pages.
2:02:18
And here's now where this gets interesting. And you asked about Bootstrap, a popular framework or library.

## [Bootstrap](https://youtu.be/ciz2UaifaNM?t=7344)

2:02:24
There do, indeed, in the real world exist a lot of third party frameworks that a lot of smart people have just figured out what
2:02:30
would make our web pages look prettier. And they've come up with design patterns for us that make it way easier and way faster to make pretty looking forms,
2:02:37
pretty looking tables, and the like. And one of these products is indeed called Bootstrap. It's freely available. And you can see its own documentation at getbootstrap.com.
2:02:45
And what I've done in advance is I've actually prepared some of our past data to actually be formatted a little more prettily.
2:02:52
So let me actually go back to VS Code here. And I'm going to open up a terminal. And I'm going to cheat and copy a file I brought with me called phonebook0.html.
2:03:01
And if I open this file, you'll see that it looks like this. It's a big table that has two columns now called name and number.
2:03:09
And I've added some other tags which are not that interesting, but I didn't need them before. But in this table, there's a table head and there's a table body.
2:03:16
So there's, like, a special row at the top and then all of the rest of the data in a CSV or a spreadsheet. And you can probably infer from this table row, from this table row,
2:03:26
from this table row, it kind of looks like, indeed, a phone book. So if I go back to my browser here, go into my directory listing
2:03:33
and open up phonebook0.html, it's not the prettiest thing. But it is tabular. And notice that the browser has automatically put in bold the name,
2:03:42
and the number, and everything's in columns. But it's not very pretty. But what if I do this?
2:03:47
Let me actually go into VS Code here. And let me borrow another file I came with called phonebook1.html.
2:03:55
And that file is going to look a little bit
2:04:01
different than the [INAUDIBLE] in that I've included a link tag in the header.
2:04:06
Now I'm not linking to my own CSS. I actually went to getbootstrap.com. I read some of their documentation.
2:04:12
And I'm linking now to Bootstrap's CSS file, which is actually really,
2:04:18
really big. And in fact, if I open this file here, let me actually open this up in a tab,
2:04:23
and visit this URL here, the folks at Bootstrap have written a crazy amount of properties
2:04:30
by defining their own classes and other such keywords. And you and I and really anyone on the internet
2:04:36
is welcome to use all of this CSS. And the documentation makes clear what all of this does. A normal person would not need to read through any of this in that way.
2:04:44
But I've included this file called bootstrap.min.css. And min just means they got rid of most of the whitespace.
2:04:50
And if I now go back to my other tab and go back to phonebook1.html,
2:04:55
it's the exact same data. But thanks to that link tag, it now looks much prettier.
2:05:01
And I didn't have to figure out how to move things over to the right. I didn't have to figure out how to draw these gray lines.
2:05:06
I didn't have to figure out how to format things in precisely this way. Bootstrap, wonderfully, did most of that for me.
2:05:13
Now this is still a very static table. It's not interactive. I can't sort by names or columns or the like.
2:05:18
So let's revisit one other program that we made in advance together. And this one is actually a new version of the search program.
2:05:26
So if I open up this program, search2.html, and close my terminal
2:05:34
window, you'll see that I've borrowed some of the same content before. Let me go to the essence of it.
2:05:40
Here is the form and the action that I used earlier. But I've added a whole bunch of classes to it.
2:05:46
And this is the essence of these third party frameworks. They generally create a whole bunch of classes that you can use and reuse.
2:05:52
But they figured out all of the relevant properties. So for instance, for my Google search button, I've given it two classes, a class of button, BTN for short,
2:06:00
and button-light. These are not standard HTML or CSS things. These are Bootstrap names that they invented, just like I invented center
2:06:08
and large and medium and small. I've also specified that there are a whole bunch of other classes associated
2:06:17
with pretty much every tag in this file. So if I zoom out here and go back to my directory index
2:06:23
and open this, the first version of search. It was super, super simple because it only contained the HTML form.
2:06:30
Let me go ahead and open up search2.html. And the essence of the form is exactly the same.
2:06:36
Therein is the query at the bottom of the page. But thanks to CSS, I now have a button that looks a little more interesting.
2:06:41
It's gray and it's rounded. I also have an I'm feeling lucky button, which will send a different request and show me by default the very first search result.
2:06:48
So in short, the file that I just opened, even though I made it in advance, it's only 55 lines.
2:06:54
And most of that is whitespace. And it did take me a little bit of time to figure out the classes and read the documentation.
2:06:59
But most of the work is done by this third party framework or library of CSS classes and properties that someone else made for me.
2:07:09
And so as CSS goes, that's kind of it for the basics. It's just a bunch of more key value pairs in the form of these properties,
2:07:17
whereby you can select elements of a web page by way of their ID, or classes, or even the names thereof.
2:07:24
And here's something that's kind of neat, too. Let me go to harvard.edu again. Let me go ahead and open up the inspector, as before,
2:07:32
and draw your attention to one final feature of these developer tools under the Elements tab. So under the Elements tab here is all of the HTML
2:07:39
that composes harvard.edu as of today. But let me go ahead and expand this right-hand portion. It turns out you can also see all of the CSS
2:07:47
that is being applied to the website as of now. So for instance, if I go to a page here-- let's go to Give Now.
2:07:56
Might as well. Let's give them a plug here. Under Give Now, let's see if this is going to go well.
2:08:02
Let's go ahead and highlight this part. Suppose they really want to draw attention to give online.
2:08:07
And I right click on that. I choose inspect, as before. And here now, notice that the developer tools
2:08:13
jumped right to the HTML tag that represents that particular line of text. If I zoom in, it turns out it's an H1 tag.
2:08:20
It's big and bold. Suppose, though, I want to change its color. Well, if I go over on the right here, you can see all of the CSS properties
2:08:27
that currently apply to that specific tag. And most of these we haven't even talked about line, height, margin bottom,
2:08:34
font, weight, margin top, and a bunch of other fairly self-explanatory things. But if I want to experiment, I can go up here in top and say color: red.
2:08:43
And I can literally change that on the web page live to see how it looks. It's not changing the server. It's just changing my copy.
2:08:48
But I can at least make that change. You can do even fancier things where, if you click computed, you can scroll down and figure out, OK, wait a minute.
2:08:55
It's white right now. That's the same thing as this, rgb(255, 255, 255).
2:09:01
That's the same thing as ffffff from weeks prior. But I can click this little arrow and it will even show me where in Harvard CSS
2:09:10
that white color comes from. So if it's actually my site I can actually figure things out and make changes as well.
2:09:16
So in short, if you find that you like the world of web development, in your own browser that you've had all this time,
2:09:22
there's so much darn functionality built in. And it's just up to you now to start experimenting with it, exploring what you can actually do with it.
2:09:30
But let us use our final moments today to introduce you to a final language

## [JavaScript](https://youtu.be/ciz2UaifaNM?t=7776)

2:09:36
called JavaScript, which is itself a proper programming language. And you're about to see a bunch of syntax that's
2:09:42
kind of new, but kind of familiar. And the goal here is not to teach you JavaScript per se,
2:09:47
but to begin to lay the foundation for you yourselves learning a new language on your own.
2:09:52
By the end of CS50, you will not have learned all that is out there, certainly. And the goal here ultimately is to help you
2:09:58
have a sense with a support structure in place, be it the humans or the [INAUDIBLE] involved that you can ask questions of along the way.
2:10:05
Let's go ahead and do this. In my directory index, I'm going to go into the source 8 directory
2:10:12
where I've got all of today's examples ready to go. I'm going to go into VS Code's Explorer, where I can see all of those files.
2:10:19
And in my source 8 directory, let me go ahead and open up hello version 1 dot HTML.
2:10:25
Recall that the last time we played with hello.html, it was literally just HTML. But here's an example of a language called JavaScript.
2:10:32
And at this page, it's going to work as follows. If I open hello 1 dot html in my page, I have a very simple form.
2:10:39
Let me zoom in. Let me type in my name, for instance, D-A-V-I-D, and hit Enter. And voila! This is not a very good user interface.
2:10:45
But you can see that this web page says, quote, unquote, hello, David. So how did I get this form to trigger a pop up?
2:10:51
Well, if I go into VS Code here, you'll see a web form. But I've added another attribute, namely an onsubmit attribute.
2:11:00
And in the world of HTML, onsubmit allows you to write a tiny bit of JavaScript code inside of the quotes
2:11:08
that will be executed whenever the user submits this form. So what this is saying is call a function called greet
2:11:14
and then return false. And what return false means is that don't actually submit this form to the server, like keep the user on this page
2:11:22
so we can just see a pop up. So what is this greet function? Well, it turns out, in the world of HTML,
2:11:28
there's not only a style tag you can put in your head of your page, but also a script tag, inside of which is JavaScript code.
2:11:35
The syntax is a little different from Python and from C. But it's maybe a little closer to Python. Instead of def last week or two weeks ago,
2:11:42
we'll now use function, literally, to begin the definition of a function. And if I want to call this function greet, so be it.
2:11:49
JavaScript comes with a function called alert. And so if I literally do alert, hello, quote, unquote, and then
2:11:56
plus something else, just like in Python, that's going to concatenate, or join the two things left and right.
2:12:02
But here's some functionality that comes with your browser, too. It turns out, per the notion of this whole page being a document,
2:12:09
you can call document.queryselector, which allows you to select any of the tags or elements in the page,
2:12:16
specifically you can select the tag that has an ID of name. So CSS and JavaScript use the same syntax.
2:12:23
If you see hash something, that is referring to the ID of a tag that you created.
2:12:28
If you then, after selecting the element of HTML with that unique ID,
2:12:33
want its value, you just do dot value. So we saw dots a lot in Python and in C to go inside of structures.
2:12:40
You can go inside of that text box and get its value. So notice here if I scroll down, not only
2:12:46
am I using autocomplete and autofocus and so forth, I also, for convenience, gave my input box a unique ID of name.
2:12:54
So what's effectively happening is, when I click Submit, my JavaScript's greet function is called, it queries for that text box,
2:13:02
goes inside of it and gets its value. And then, using this plus operator, just like in Python, concatenates the two together and passes them
2:13:10
to this alert function for an underwhelming, but functional alert
2:13:15
in the window. All right. How else can we do this?
2:13:20
This is generally frowned upon to use onsubmit in this way. Generally speaking, the world does not like
2:13:27
mixing attributes, rather JavaScript code with HTML so closely as this. So let me show you another variant of this,
2:13:34
even though it's going to look a little bit cryptic. But at least it will be representative of how else you can solve this problem.
2:13:41
In hello2.html, we have this code. Notice that at the top of my body now is the form.
2:13:48
But at the bottom of the body is this script tag. So I've just moved it from head to the body of the page.
2:13:54
Because I'm going to then instead do this. If I want to tell the browser to listen for submissions of that form,
2:14:01
I can use this fairly cryptic syntax, but you'll see it again and again over time as follows.
2:14:06
Go into the document. Select with this query the form tag.
2:14:12
And then call this special function that comes with the browser called addEventListener. So tell the browser to listen for a certain type of event for this form.
2:14:21
What event do you want to listen for? The submission of the form, so quote, unquote submit. What do you want to have happen whenever that event is heard?
2:14:29
You want to call this function here. So this is what's known as an anonymous function.
2:14:35
The syntax is a little weird, but I've not given the function a name. It apparently takes an argument as input called event,
2:14:40
but that's per the documentation. And what these two lines of code do essentially is they still call the alert function.
2:14:47
They still output hello comma space. And they still query the HTML for the ID name
2:14:55
to get the value that the humans typed in. And then just for good measure, we prevent the default behavior for any form with this line of code, just so that it doesn't actually
2:15:03
submit anything to the server. It keeps the user actually here. This will be a little scarier, too, but just so you've seen it.
2:15:10
In hello3.html, this is actually a more common technique. Whereby you can listen for one other special event.
2:15:19
It turns out when you load a web page, lots of stuff has to happen. It's got to be read top to bottom, left to right. It's got to download other files, the images, the sounds, the videos, and so
2:15:27
forth. If you want to wait until the whole page has been read into memory essentially,
2:15:32
you can use this event as well, DOMContentLoaded. That tree we drew earlier is what's called a DOM, document object model,
2:15:39
which is just a fancy way of saying a tree in the computer's memory that represents the web page. So this is the syntax that you'll find that people
2:15:46
use to tell the browser once the whole DOM, the whole tree has been loaded,
2:15:52
then go ahead and execute this code. And it means that no matter what, the whole web page will be ready in order
2:16:00
before this code is actually executed. And this ensures, for instance, that even though this script is at the top of my file
2:16:07
and my form is at the bottom of my file, none of this code will get executed until the whole DOM is ready, all of the HTML
2:16:15
has been read top to bottom, left to right. All right. Well, let's go ahead and make this a little more interesting,
2:16:23
just to show you some of the capabilities of JavaScript within a browser nowadays. So if I open up maybe this one here, background.html.
2:16:31
And let me open it up in the browser. And this is going to be super simple in terms of user interface. But here's a big white viewport, big body that's just white in color
2:16:39
by default. But there's three buttons at top left. And if I click R, it makes the background red.
2:16:44
G makes the background green. And B makes the background blue. What's interesting about this demo, sort of underwhelming
2:16:51
as the user interface is, is it demonstrates that you can modify CSS using JavaScript.
2:16:57
And HTML, CSS, and JavaScript are therefore very intertwined in the context of a browser.
2:17:02
How? Here's the raw HTML. Here are the three buttons. And I've given them three separate IDs red, green, and blue,
2:17:08
just so I can refer to the specific button. And notice what I've done here. I've declared a variable in JavaScript, which
2:17:14
uses slightly different syntax of let as the keyword. Instead of int or char or string, you can
2:17:20
use the keyword let, which essentially means let me create this variable called body.
2:17:25
And this is just how, using query selector, I can select the body element from the web page. Because I'm going to use it three separate times.
2:17:31
What do I want to do three separate times? For instance, this. I want to go into the document and select whatever
2:17:38
element has the unique ID of red. I want to tell the browser to listen for this event, click.
2:17:44
So we saw submit before. You can listen for clicks as well. When the click happens on this button, I want this function to be called.
2:17:51
What does this function do? Something super, super simple-- all it does is it changes the body's styles, background color
2:17:59
to be, quote, unquote red instead. So what's going on here? We didn't see this earlier.
2:18:05
But it turns out in CSS there is actually a CSS property called background-color. And I can see it as follows.
2:18:11
Let me reload this page. Open the browser's inspector. Open up elements. And if I hover over the body here, notice
2:18:19
that there's no background color by default. But if I do in, say, lowercase, background color colon yellow,
2:18:28
it immediately changes the background to yellow. Unfortunately, in JavaScript, you can't do background dash color.
2:18:37
Why might this be? Yeah? AUDIENCE: [INAUDIBLE]. DAVID MALAN: It thinks it's minus or subtraction.
2:18:44
Right? So I would wager there was a human at some point in the room designing JavaScript where they realized like, damn it.
2:18:50
We shouldn't have used a hyphen in CSS. Because it's now going to be misinterpreted as a subtraction
2:18:55
operator in JavaScript. So the way the JavaScript world solved this was whatever has a hyphen in it
2:19:01
as background dash color, you change it in the JavaScript version thereof to be camelcase, so to speak, whereby there's this hump in the middle
2:19:09
with it's a capital C, no hyphen, instead of a lowercase C instead. And I do this here, and I do this here so
2:19:16
as to essentially listen for a click on any of those three buttons so that the end result is that it changes it from red to green to blue
2:19:23
based on what I'm clicking. And here's where the developer tools get kind of cool. Notice at bottom right here, notice that as I click on this,
2:19:30
the CSS of the page at bottom right is changing to match whatever is happening. So you can really see and understand what's going on underneath that hood
2:19:39
there. All right. We have time for a few other demonstrations. Back in my day when I learned HTML, there was a bunch of hideous tags
2:19:46
still in circulation. Among them was a blink tag, which literally, if you used blink and put words in between its open tag and close tag,
2:19:55
you would get text on your screen just kind of doing this. Even uglier was what was called the marquee tab, which would actually
2:20:01
scroll text across the screen like this. And no self-respecting website tends to have blinking text or scrolling
2:20:07
text in this way. Because it's just tends to be ugly. However, even though the blink tag is among the few tags that's
2:20:13
ever been removed from the language, you can bring it back with a bit of JavaScript.
2:20:18
So here, for instance, is an example in blink.html. Here's a super simple page. The only thing in the body is hello, world.
2:20:26
But there is a script tag up in my head of my page here. And let's see what's inside of this script tag.
2:20:32
Well, I've defined on line 8 downward, a function called blink. What does it do?
2:20:38
Well. I first declare a variable called body. And I get the body element using queryselector.
2:20:44
I then ask this question. If the body's styles visibility property,
2:20:49
which we haven't talked about yet is quote, unquote, hidden, then change the body's styles visibility property
2:20:56
to be, quote, unquote, visible. Else, if it's not hidden, that is it's visible, change it to hidden instead.
2:21:03
And here, too, this is another one of these left-hand, right-hand situations. I do not know why the opposite of visible is not invisible.
2:21:10
It is, instead, hidden. So, again, arguably poor design, but this is what we have. How is this useful?
2:21:16
Well, there turns out. In your browser, there's a JavaScript function called setinterval that's associated not with the document per se,
2:21:23
but the window, which is another global variable that you just get automatic access to in the browser that
2:21:29
allows you to call a function, any number of milliseconds, again and again and again.
2:21:35
So if I want my text to blink every half a second or 500 milliseconds, I just use window.setinterval to call blink every 500 milliseconds.
2:21:43
And notice, it's very important not to call blink here, as with parentheses, like in C or Python.
2:21:49
Because I don't want to call blink at this moment in time. I just want to inform the setinterval function of the name of the blink function.
2:21:56
So I just pass in the name blink. And if I go back to my directory listing, I open up blink.html,
2:22:04
you'll see what I used to see in the late '90s, when HTML 1 was all the rage, like at the beginnings of a ugly websites,
2:22:11
including my own personal home page at the time. My own personal home page, too, at the time, which is probably findable somewhere online in the archives,
2:22:19
it was back in the days where you wouldn't just show people the content of your page. You had to click a Enter button to enter the web
2:22:25
page and just really ridiculous. There's a lot of things in tech that you can do, but should not do. And the world has learned this as have I, the hard way.

## [Autocomplete](https://youtu.be/ciz2UaifaNM?t=8553)

2:22:33
All right. Let's do a couple of final examples that are now representative of what modern websites do and what you and I take for granted on web apps and mobile apps alike.
2:22:41
For instance, this feature of autocomplete. Case in point, when I went to google.com before and I started searching for cats or dogs or birds,
2:22:48
it was trying to finish my thought and populating a dropdown with a bunch of different suggestions. I can actually do that myself in JavaScript as follows.
2:22:55
Let me open up a file called large.js, which
2:23:01
is a file that I made based on speller's own dictionary. Recall that we gave you a big list of words, like 100,000 plus words.
2:23:09
I copied those into this JavaScript file. But I formatted them in what's called the JavaScript array.
2:23:15
So JavaScript has arrays. They're more like Python lists than they are like C arrays. The syntax is square brackets.
2:23:21
Let is my keyword to say give me a variable called WORDS, which is all caps because I'm going to use it globally.
2:23:27
And here is a 100,000 words from that dictionary in this file. All right?
2:23:32
Now let me close this file and open up the actual HTML file, autocomplete.html.
2:23:38
Let me scroll down to the bottom. And you'll see that in this page in the body are two things.
2:23:44
One, an input, so a text box so I can start typing words. And then, two, an unordered list that's empty.
2:23:51
So there's no actual list items in that unordered list initially,
2:23:56
but there is a lot of JavaScript. Here's how I'm including the large dictionary. And here's how I'm implementing autocomplete.
2:24:03
So let me first show you what this does. Let me go back to my directory index, click on autocomplete.html.
2:24:10
I'll zoom in. And if I type in C, I immediately get an unordered list of all words
2:24:15
starting with C. If I type CA, it gets filtered further. But we can't see the difference because there's so many words starting with CA.
2:24:21
CAT, the list is changing. CATS, the list is changing. And notice that if I were to open my developer tools, what
2:24:29
gets really interesting is you can see this list being made in real time. Let me delete it. Notice that the UL at bottom left is now empty.
2:24:37
But if I type in suddenly CATS, notice that the triangle appears and there
2:24:42
are all of the list items that my JavaScript code is apparently dynamically creating.
2:24:48
And indeed, how do I do this? Well, this one's more of a mouthful, but here's the idea. I used a queryselector function to get that input text box.
2:24:57
I then add a listener to that input, listening for what's called key up.
2:25:02
It turns out you can listen for the finger going down or the finger going up. So I'm waiting until the user lifts their finger off the keyboard, AKA,
2:25:08
key up. When it hears that event, it should do the following. It's going to create a variable, a temp variable called HTML equal to quote,
2:25:15
unquote nothing. In JavaScript, as an aside, you can use single quotes or double quotes for whatever reasons stylistically, JavaScript programmers
2:25:22
tend to use single quotes. I can then say if that input has a value, because the humans typed
2:25:28
in one or more letters, then iterate over all of the words in the dictionary. And we've not seen of before, but it's Javascript's equivalent
2:25:35
of Python's for loop. If that word starts with whatever the input value is, go ahead and add--
2:25:42
that is concatenate to the HTML variable and open tag LI. Then, whatever the word is, using this JavaScript specific syntax, and then
2:25:51
close the tag. And then lastly, using queryselector, grab the UL tag,
2:25:57
go into its inner HTML, so to speak, inside of it, and change it to be this HTML I just created.
2:26:03
And so in this way, using JavaScript, I can dynamically add to and subtract from the HTML in the page.
2:26:10
There are so many other events here, too, clicking, submitting, key up, dragging, and dropping, and so forth.
2:26:16
This is just some of the events that web pages and mobile apps can listen for. But we'll do one final one, which speaks to the power of browsers nowadays

## [Geolocation](https://youtu.be/ciz2UaifaNM?t=8783)

2:26:23
and even the implications for privacy. If I go into geolocation.html, it turns out
2:26:31
you can figure out where in the world a user is with, like, three lines of code nowadays, assuming they've turned on location services
2:26:38
and opted in on their device. Here, albeit cryptically, is a final global variable
2:26:43
that comes with browsers today called navigator. It has a geolocation object associated with it,
2:26:50
which comes with a function called getCurrentPosition. You can then specify or figure out the user's latitude and the user's
2:26:57
longitude. And all I'm going to do is write these to the screen so I can see this demonstration live. So our very final demonstration here of JavaScript
2:27:05
is going to be this one here for geolocation to show you how easy and how invasive even code can be if I click on geolocation and wait.
2:27:15
There are my GPS coordinates, latitude and longitude. And to confirm as much roughly, let's go ahead and open up a browser,
2:27:22
paste in those coordinates, click on the Google Maps result that comes up first. Zoom in, in, turn on satellite mode.
2:27:32
And in-- and I'm not quite in that corner of the building. But I'm presumably close to an access point that Google has known about
2:27:38
and associates with my GPS coordinates. It's that easy when you actually use something like Uber or Lyft or the like
2:27:45
to figure out where the user is by just asking their browser via code like this. So that's it for HTML, CSS, and JavaScript.
2:27:52
In the problem set, you'll explore all of these. One more lecture to go in which we'll combine all of these. But until then we'll see you next time.
2:27:59
[MUSIC PLAYING] Buffering, OK.
2:28:04
Josh, nice. [INAUDIBLE], oh! [LAUGHING]
2:28:13
[INAUDIBLE] No, oh, wait.
2:28:21
That was amazing, Josh.
2:28:26
Sophie! [LAUGHTER]
2:28:34
Amazing. That was perfect. [INAUDIBLE]
2:28:40
[LAUGHTER] I think I--
2:28:45
[INAUDIBLE] AUDIENCE: [INAUDIBLE]. DAVID MALAN: Guy.
2:28:53
That was amazing. Thank you all. AUDIENCE: Good. [APPLAUSE]
