# Agenda

## Awards

![img](https://upload.wikimedia.org/wikipedia/en/d/dc/Academy_Award_trophy.jpg)

- Scott

Scott had some great questions and pointers for others to follow for both 2 and 3. He has took some initiative and set up a study session!

Also Scott had a pull request. Pull requests get automatic awards.

- Giles

Giles too set up a study session to go over stuff with other students, these are really great and really valuable!

- John

John pointed to some great resources about list comprehensions! These things are definitely tricky so it's always great to practice with them!

- Jay

Jay is pointing students to the Slack MIDS group. For what it's worth it might be good to try and join the current slack MIDS group if you haven't found that one already.

- Dominic

Our first pull request to the Course-Syllabus!

## Demo & Share Time

- Homework share repository
- Dominic or Scott, want to demo how to make a pull request?
- A nifty feature you found inside of jupyter notebooks?
- Anyone want to share any tips or tricks that they discovered?

## General Discussion and Q&A 

I wanted to take a break this week and slow things down, we covered a lot of material in the past 4 weeks. You've got from nothing to coding up algorithms and I'm sure it's been a complete whirlwind.

### Specific Homework Feedback

![homework 3](https://raw.githubusercontent.com/MIDS-INFO-W18/Course-Syllabus/master/week_4/homework3feedback.png?token=ABkQB4W-3rbGe2lwRW3dEiLaJH6wT3RJks5WuiFQwA%3D%3D)

I read through the student feedback. Keep in mind that this isn't something other teachers do, nor is it something that is required. I did this because I wanted to see what you guys thought and to try and make adjustments within reason to accomodate issues.

- Ambiguity & Error Handling
  - **we are not expecting try catch blocks or anything like that, at this level, if statements suffice.** With that being said, this is an opportunity to learn so those are great tools to have in your tool box. 
  - Would love to hear more and start a small discussion about this so that we can figure out what makes sense for both of us.
  
All that being said, we can try to be a bit more specific.

- Grading
  - There are too many of you for us to hand out individual feedback however you should be getting a message about why you're getting off points. Anubhav can touch on that feedback mechanism.

### Your Questions & Discussion

Budgetted time for discussion, we can sit in silence or you can ask questions. Up to you!

- Something that you were confused about from this week or last week? 
- General topics?
- We're a couple of weeks into the course, how is everyone feeling?

## Breakout Groups

General guidelines, if you're just sitting in a breakout room or you're having trouble connecting or doing something. This is not the intention, raise your hand and one of us will come help you out.

-----------

There are several ways to solve these problems, we'd like you to try your best to do it with a comprehension. Please save all your work so that when it comes time to talk about your process - you can share what you started with and what you ended with.

[Download this file.](https://gist.githubusercontent.com/anabranch/df2a4eae19c478e70858/raw/682df4aa1cae4bf3afe57146fc1f919f2033253d/Untitled.ipynb) And open it with Jupyter.

0. Load in the data that is available in this repository! Here's how to get started with loading in the data.

```python
import json

with open("data.json") as f:
     temp = json.load(f)
     data = temp['data']
     cols = temp['cols']
```

1. Write a comprehension that will extract out all the names and removes duplicates in doing so. The resulting data structure may be a list or a set.
2. Count the number of people in each state. There are several ways of doing this so I won't give any tips!
3. Write a comprehension that will end up with a key of name and value of phone number. The result should be a dictionary.
4. Write a comprehension to find which letters of the alphabet (if any) are not used as the first letter in their names. Don't just list which ones we have, but which ones we are missing.

Hint for this last one use:
```python
import string
string.ascii_lowercase
```
