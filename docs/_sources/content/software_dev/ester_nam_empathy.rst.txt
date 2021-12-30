Empathy: One Weird Trick to Becoming a Better Software Developer
================================================================

* `Video Link <https://www.youtube.com/watch?v=IYWlfVqBQLc>`__
* Speaker: Esther Nam
* Rating: 5/5

Overview
--------

Focuses on the soft skills that software develoers that are needed, rather than technical skills.
The focus is largely on empathy: empathy for coworkers, and empathy for users.

Details
-------


1:00 -- 3:30
~~~~~~~~~~~~
Story 1: Goofus

Works at ACME Co, aced the algo interview, and first project was a resounding success.
She was excited as she built something similar at previous job.
She had made some incorrect assumptions about the spec, which were caught by the PM.
Goofus worked hard without complaint to fix, but the project was delivered several weeks late.

Story II: Gallant

Worked at ACME slightly longer than Goofus, but already has a process in place for new projects.
Sets up a short, daily meeting with client and QA lead, to get feedback on process and change requests right away.

Gallant went to lunch with marketing analysis, who mentioned that Gallant's project could be used for another
project if tracking was added.
Tracking was within the project scope, and adding it ended up doubling ACME's revenue for the year.

Story III:

Goofus was tasked with developing an internal tool, leading 2 jr devs on the project.
She was excited to teach the newbies how to code.
The Jr devs had trouble setting up their environments to get started, and soon stopped going to Goofus
with thier dumb questions.
Instead, they started going to Gallant for help.

Goofus was too busy on optimizatoins to write any docs, Gallant had to message Goofus constantly for 
clarification.
Both Snr Devs spent way too much time helping the junior devs, and delivery date slipped.

Even worse, Gallant missed her deadline because she was busy helping the other devs


3:30 -- 5:40
~~~~~~~~~~~~

What makes a great developer?

Most of us think of technical abilities (data structures, algos), see 
`this SO survey <https://insights.stackoverflow.com/survey/2017/#evaluating-developers>`__.

Great developers ship the right product at the right time.

One metric that isn't on here is: if a dev was leaving the company, would we consider following them?

By being empathetic -- that is keeping the QA person, the PM, and other developers in mind -- can
make us the developer others want to work with.

    Empathy is the experience of understanding another person's condition from their perspective.
    You place yourself in their shoes, and feel what they are feeling.

    Dr. Hyder Zahed

Empathy is marked by the distinction between oneself, and another.

5:40 -- 8:40 
~~~~~~~~~~~~

Two types of empathy
- **emotional empathy** able to feel and act on the emotion of another.
- **cognative empathy** ability to understand something from the perspective of another.

Examples given:

1. Emotional empathy: see a coworker hungry in a long meeting. Sympathy would be feeling sorry for them.
   Emotional empathy would be feeling their hunger, but might do something about it -- bring in a snack,
   suggest to all that the meeting end a little early.
2. Cognative empathy: being a slack poweruser, you send messages to a coworker via slack. 
   You do a good job communicating via slack.
   Empathy would be asking what the preferred mode of communication into account: would they
   prefer email, face-to-face, video?


The real golden rule

    Don't do to others what you would want them to do to you (that's projection)

    Do onto others what you think they would want you to do

8:40 -- 
~~~~~~~~~~~~

Getting better at empathy: 5 ideas

Exercise 1
**********

Other is you in the self/other is you.

Find terrible code, run :code:`git blame`, and found out it was you.
You were not dumb, but past you had a different set of context.

Write documentation and logging with your future self in mind.

e.g. when completing a task, open a file and write down each step that you took.


Exercise 2
**********

Easier to feel empathy for someone similar to you. To practice empathy, try working 
with a coworker that *isn't* a developer.

e.g. work with a QA person, a client, or dev ops person.

Get familiar with edge cases, get more feedback, better understanding on how the code
you are writing gets used.

You will also develop your curiosity.


From Ackoff, *A Lifetime of Systems Thinking*


    "The best thing that can be done to a problem is to solve it".

    False. The best thing that can be done to a problem is to 
    dissolve it, to redesign the entity that has it or its 
    environment so as to eliminate the problem.


Exercise 3
**********

Read code written by others.

Observe the great variety of ways a problem might be solved.
One example is seeing ways of interacting with databases.
In Python, there are two common patterns: SQLAlchemy and Django.

Django uses the ActiveRecord pattern, where you make an almost 1-to-1
associatoin between tables and the objects.

SQLAlchemy separates the logic of objects from the logic of database
operations, using the Unit of Work pattern.

The different perspectives will help you understand what types of solutions
are suitable for which problems.

Highly related to principle of least astonishment.

Writing an interface is a great exercise in cognative empathy, requires thinking 
about the expectations of the user, and what they would expect.
In particular

* Who is the user of this API/Interface?
* What are the most common arguments?
* What does the user expect as the return value?

Tests are useful, because they force you to act as a client to your API.


Exercise 4
**********

Establish grounding, where grounding is the "TCP handshake" of communication.

    Grounding is ... the process of adding material to the common ground between
    speakers .., to ensure that knowledge is properly understood by all participants.

    -- Roque and Traum, *Degreees of Grounding Based on Evidence of Understanding

Simple examples: nodding along, uh-huh, "right right".

Good way to develop is to try to teach something to someone. The five levels of explaination.
When teaching, spend time determining the background of the audience.


Another example is at the end of a meeting, ask others around the table to take a few minutes
to hear what everyone else's takeaways were. This can show if there is enough common understanding,
or if more grounding is needed.

(Short digression on one theory of how empathy developed was to allow more effective and 
unambiguous communication, which could help the tribe deal with threats and opportunities)

Exercise 5
**********

Why is an easy question to ask.
Much harder is listening to the response.

If you have a pre-concieved idea of what the person is saying
