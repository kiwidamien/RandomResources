Using tmux and vim together
===========================

Reference: [Using tmux sessions, windows, panes, and Vim Buffers together](https://www.youtube.com/watch?v=hbs7tuwpgZA)

Points of confusion
-------------------

Vim windows are views on a buffer, vim tabs contain windows. The same buffer might be viewed in different tabs, but
each window (view) is contained in exactly one tab. i.e. tabs are similar to tabs in firefox.

In tmux, the language is different:

- sessions are akin to different "instances" of running vim (tmux allows you to switch between sessions)
- windows in tmux are like tabs in chrome or vim
- panes in tmux break a "window" into different sections (i.e. they are like windows in vim)


Workspace recommendations
-------------------------

Suppose you have three projects:

1. React project 1
2. React project 2
3. Flask backend project

We would have three tmux sessions, one for each project.

Looking at a react project, we typically need to do the following tasks

- Edit code
- Run a server (which doesn't log much useful output), e.g. `npm run start`
- Manage versioning (git add, commit, push)
- Deploy to prod or staging 
- Maybe a connection to a database for debugging / verifying queries

We can probably break these up into 4 separate "types". 

- Editing
- Serving / logging
- Version control and deploying

We put version contol and deploying together, because if we are deploying we are pretty much always
doing version control stuff as well.
We keep editing away from version control because we only interact with VC once we have decided the
code is in a good place (i.e. VC interaction occurs in "gaps" in the editing process).

We would have three TMUX windows (tabs to everyone else) in this session.

Editing "window"
~~~~~~~~~~~~~~~~

This would probably be a single pane, running a single vim session.
More on this below.

Serving / logging "window"
~~~~~~~~~~~~~~~~~~~~~~~~~~

The npm server doesn't do much, but can display useful error messages.
It might be useful to split this window into two panes, one for the npm output (if there are errors)
and the other to the database connection (to quickly see if empty database errors are really errors)

Version control and deploying window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Presumably we run our testing module before pushing. So maybe a testing pane, a git pane, and a deploy pane.

Editing window recommendations
------------------------------

Within vim, create several tabs for files (technically windows) that you would want to look at together.

For example, 

1. you might be looking at a yaml file, and a file that injests that yaml file (one vim tab, two vim windows/panes)
2. you might be editing at a component `showFiles.js` that has props from two parents sent in, so you want all three in one tab in separate windows (one vim tab, three vim windows/panes)
3. You might have `complexMetaData.yaml` that is really long, and you want to look at multiple places at once. 
   You  could have multple windows/panes in different parts of this file.


Overall project
---------------

So we might have

* TMUX SESSION 1: React-project 1
  * TMUX window 1: name `code`, runs vim
    * vim tab: two window panes (yaml and code)
    * vim tab: three window panes (three related components)
    * vim tab: one yaml file in multiple panes
  * TMUX window 2: name `version`, runs terminal
    * tmux pane: to run tests, look at output
    * tmux pane: to do version control
    * tmux pane: to deploy
  * TMUX window 3: name `serve`
    * tmux pane: the server launched from `npm run start`
    * tmux pane: a possible database connection to help with debugging

* TMUX SESSION 2: React-project 2

(similar layout)

* TMUX SESSION 3: Flask project
  * TMUX window 1: name `code`, runs vim
  * TMUX window 2: name `version`, runs terminal
    * pytest pane
    * git pane
    * deploy pane
  * TMUX window 3: name `serve`
    * gunvcorn server
    * databsae connections
    * ipython debugging session

