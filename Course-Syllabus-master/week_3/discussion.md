# Agenda Week 3

## Todo

1. Watch the syllabus
2. Watch the assignment upstream
3. No More babun. It's bad, we messed up. Don't use it!

## Homework Review
Anubhav to talk about what he saw in the homework.

- Late Homework
- Plagiarism - cite your sources
- Easy grading will be slowly reduced [week 2 to probably be the easiest].

## Weekly Awards
I'm going to introduce gold stars for those that I see doing fantastic work for a given week. It might be a well formulated question or a resource for other students.

- Dominic
Dominic provided a really helpful comment to a fellow student for how he set up his git repository.

- Maya
Maya pointed to a helpful git guide that helped her as well as helpful videos that helped her understand the concepts.

http://rogerdudler.github.io/git-guide/

https://www.youtube.com/playlist?list=PLfdtiltiRHWFEbt9V04NrbmksLV4Pdf3j

- Jason
Git for ages four and up
https://www.youtube.com/watch?v=1ffBJ4sVUb4

- Geoff
Geoff is thinking the right way. He asked some really specific questions on the forum that I thought were well focused and articulated. I've been really impressed as he is someone with no programming experience, at all. He was almost the first one in office hours and not even to have a specific question, just to listen. This is the right approach if you're confused.

- Kate
Setting up infrastructure to share assignments and helpful tips and tricks is a good idea. We've created this and I'll talk about it below.

### The challenge of homework at this level
Coming up with creative assignments at this level is a big challenge. You don't know enough to do anything interesting and decoupling my knowledge with what I thought at this time is extra difficult.

Here's the deal, we can't really require any good homeworks at this point because you can't do anything. We tried something we thought might work and it doesn't seem like it did. We're sorry, we won't do it again. We won't do any more shell scripting or anything outside of python.

## Demonstrate an example of why you would use a shell script
Updating Homework

## Formalize Git & Github

Demonstrate the situation in the playground. What's going on and why is it happening?

Use gitbash if you're having lots of authentication issues. If you have to use https version instead of git version, that might be a source of the problem.

![Demonstration Image](https://github.com/MIDS-INFO-W18/Course-Syllabus/blob/master/week_3/images/playground-demo.jpg)

```sh
mkdir Desktop/demo
cd Desktop/demo
mkdir editor1
mkdir editor2
cd editor1
git clone git@github.com:MIDS-INFO-W18/github-playground.git
cd ../editor2
git clone git@github.com:MIDS-INFO-W18/github-playground.git
# now we have two users working on the same repository

# NOW AT TIME 2

cd ..
cd editor2/github-playground
echo "editor 2 making a change to a file. This is definitely a different change that might cause problems." >> edit.md
git add edit.txt
git commit -m "Editor 2 made a change"

# NOW AT TIME 3

cd ..
cd editor1/github-playground
echo "editor 1 making a change to a file" >> edit.md
git add edit.txt
git commit -m "Editor 1 making a change"

# NOW AT TIME 4

cd ..
cd editor2/github-playground
git push origin master
# now take a look at github and you'll see this change

# NOW AT TIME 5

cd ..
cd editor1/github-playground
git push origin master # this command will error
# to fix this, we have to make sure they have a shared
# history

# NOW AFTER TIME 5

git pull origin master
# fix potential merge conflict
# we are at time
git commit -m "fixed merge issue"
git push origin master
```

### Current Set Up
#### To do's
1. NEVER CREATE A PULL REQUEST TO THE ASSIGNMENT REPOSITORY.
2. Delete all forks of
   - assignment-upstream
   - student123
These are all searchable on the internet, meaning that anyone can google for your answers and find them. That is cheating. This is the line in the sand, they must be removed **immediately**.
3. You may have a fork of the syllabus as we want you to be able to propose pull requests to the discussion as well as helpful resources.

#### Demo
![Your Setup](https://github.com/MIDS-INFO-W18/Course-Syllabus/blob/master/week_3/images/ideal-setup.jpg)
Directions for how to do this, command by command are in the readme in the assignments repository. Follow those.

Only make changes inside the week's repository, no other changes should be made. Don't create folders unless explicitly instructed to do so.

#### Anatomy of a Pull Request
This is the overall setup for a fork/clone project. You fork it on github, clone it on your local machine then you can create pull requests to the main repository that you don't have access to.
![Your Setup](https://github.com/MIDS-INFO-W18/Course-Syllabus/blob/master/week_3/images/fork-clone-anatomy.jpg)

This is the overall flow for how a pull request is performed. It's basically mirrored in a couple of places. Keep in mind that at any point, other people may be doing that exact same thing at which point you've got to pull down any changes to your local repository.
![Your Setup](https://github.com/MIDS-INFO-W18/Course-Syllabus/blob/master/week_3/images/pull-request-flow.jpg)

### The force push
[More details](http://stackoverflow.com/questions/5509543/how-do-i-properly-force-a-git-push)

## Assignment Number and Notebook References
Long story short. if it is something like 3.8.1 that means we just threw it in the assignment. No need to know about it or worry about it.

This is an artifact from Paul as he felt the need to name everything right before we turned it in and then change things afterwards. Obviously leading to confusion. Anything you need to do will be in the assignment.

## Class Exercise (15 minutes in Breakout Rooms)

Write a Python script that prompts the user for an integer, N. Display an N × N checkerboard, as shown:

```
Enter a size: 4
X X 
 X X
X X 
 X X
 
Enter a size: 5
X X X
 X X 
X X X
 X X 
X X X
```


## Slip Days Update
You'll be getting a total of 5 slip days.

## Releasing Assignments
We're going to do our best to release assignments earlier. We're going to aim for before the weekend before. Aiming to give you a total of approximately 10 days.

## Sharing old homework
After this class I'm going to create a repository in the organization called homework_share. Students will have write access to this repository and you may organize it however you wish. There are several caveats, any homework that is posted early whether by accident or not will immediately be deducted 75% of their grade for that week and **the entire class will have to complete new homework.**

How things are to be shared among students is out of my control. I would propose a folder with each week and each student posting their individual homework by their specific name or putting it in a folder under their name. This will not be instructor managed.

## Helping each other with resources
In the Course-Syllabus exists a file for each week called helpful resources. Please create a pull request to add information in there. We will include this going forward for new students.

## Slack and slack channel?

## Office hours

##Windows users? What's your flow.

## Study Groups
You all can set up study groups to go over material and work on the homework together. I realize that right now this feels like an incredibly individual exercise but it really shouldn't be. It's ok to work together on the homework.

Any direct copying is a huge issue and will be addressed by us, don't do it. Period.

## This is Berkeley
On a final note, this is a Berkeley master's program.

Berkeley is the:
\#1 Public University in the Nation and in the World

We're not here to crush you, we're here to guide you through the material that you need to know. That doesn't mean that you get to sit back and just absorb material, it means that you're going to have to study and work at things but that we're a resource to enable that.


