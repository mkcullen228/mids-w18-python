# Discussion Agenda
Every week I'll be laying out the discussion agenda in this github repository.

## How difficult was the first homework?
Specifically talk about error handling
## Logistics
Homework being sent by email will not be accepted. Do not email homework.
Academic honesty.

## Last Week Outstanding Questions
[Any questions from that remain from last week and that I pulled from discussion.](https://github.com/MIDS-INFO-W18/Course-Syllabus/blob/master/week_1/questions_from_this_week.md)

### Gitbash
Gitbash was proposed initially for this class, I can't quite remember why we ended up going with Babun but please go with gitbash if that's easier for you to work with. The point is not the tool, the point is the command line. For our purposes virtually any command line environment(that approximates unix/linux) will do.

## Responses to the [article](http://mikehadlow.blogspot.com/2015/12/learn-to-code-its-harder-than-you-think.html)?
What do people think? Is this accurate? Should it be? What are your impressions?
- Professionalization, is software development a profession?

## Impressions of the Command Line
What do people think?

## Python 2 vs Python 3

## Demo typical coding workflow

## Overview of git and the Github
[The github repository for this course](https://github.com/MIDS-INFO-W18). Each of you now has your own dedicated repository.
**If you can't see the syllabus anymore, it means you haven't accepted my invite to be a student - this is something you have to accept!**

The Assignment Repository aka [assignment-upstream](https://github.com/MIDS-INFO-W18)

Your Repository = student123 (or whatever numbers identify your repository)

What we're going for here is each week you're going to perform a git pull from the upstream repository, assuming that you're doing things correctly. That means that you're only going to pulling down the changes from the assignment repository. Every week's work should be done only in that week, do not make other folders in there because it made impede your ability to pull down future repositories.

Then what you're going to do is push your changes to your repository. From there we can easily communicate with you and only you. However there are a couple of snags.

1. You're going to need to push to the master branch for us to be able to read your repository.
2. You can push after the deadline however we will only look at the commits prior to the deadline. Remember this is version control so if you submit version y before the deadline but version x after we will only look at version y. Any changes you push up before the deadline is fine.

**This will be frustrating at first however git is absolutely ubiquitous and this is an excellent opportunity to learn how to use it.** It's worth mentioning that there are visual editors that are available, you may use these if you want however I would recommend using the command line. It'll make you a better programmer.

### Typical git workflow
dev branch, then do pull-requests from there. This allows for visibility by others into a project.

[The playground](https://github.com/MIDS-INFO-W18/github-playground/blob/master/README.md)

### Other resources beyond the text
to do...
# Questions From This Week's Work

This is a repository of the questions that come up during this week. This should be a fairly open forum.

## Babun and Windows

This is just a bit of nastiness but also one of the reasons why I asked the question in the diagnostic about troubleshooting issues. It can be more challenging that you think!

## Differences between Windows and Mac Command Lines

My understanding: basically windows long ago made the bet that the majority of applications would be GUI based. Therefore they optimized for that use case rather than trying to focus on building out the command line which was a staple of Unix/Linux which started in the server world. Mac OS X is built on top of Unix and therefore uses virtually all of the same commands [roughly speaking]. Therefore the general file structure is the same and it makes it easier for people to recycle what they use. A shell script that works on mac is likely to work on a server [again very crudely speaking]. Just built for different purposes.

### More References:
 - https://www.quora.com/What-are-the-differences-between-the-Mac-Terminal-and-the-Windows-Command-Line
 - https://www.quora.com/Why-doesnt-Windows-have-a-more-powerful-command-line-terminal
