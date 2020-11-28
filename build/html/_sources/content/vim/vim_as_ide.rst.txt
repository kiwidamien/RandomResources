Vim as IDE
==========

References
----------
* `Vim: tutorial on Editing, Navigation, and File Management (2018) <https://www.youtube.com/watch?v=E-ZbrtoSuzw>`_

Operators and Motion
--------------------

Operators:
~~~~~~~~~~

* Verbs of the VI language
* Act on text objects

+--------------+-------------------------------------+
| Operator     | What it does                        |
+==============+=====================================+
| c            | change
+--------------+-------------------------------------+
| d            | delete
+--------------+-------------------------------------+
| y            | yank into register
+--------------+-------------------------------------+
| ~            | swap case 
+--------------+-------------------------------------+
| gU           | make uppercase
+--------------+-------------------------------------+
| gu           | make lowercase
+--------------+-------------------------------------+
| !            | filter to external program
+--------------+-------------------------------------+
| <            | shift left 
+--------------+-------------------------------------+
| >            | shift right
+--------------+-------------------------------------+
| =            | indent
+--------------+-------------------------------------+


Motions
~~~~~~~

+--------------+-------------------------------------+
| Motion       | What it does                        |
+--------------+-------------------------------------+
| [count]+     | down to first non-blank char of line|
+--------------+-------------------------------------+
| [count]$     | to end of line                      |
+--------------+-------------------------------------+
| [count]f/F[c]| to next occurance of [c]            |
+--------------+-------------------------------------+
| [count]t/T[c]| to prev occurance of [c]            |
+--------------+-------------------------------------+
| [count]]m    | go to beginning of next method      |
+--------------+-------------------------------------+
| [count]w/W   | go a word/WORD to the right         |
+--------------+-------------------------------------+
| [count]b/B   | go a word/WORD to the left          |
+--------------+-------------------------------------+
| [count]e/E   | go to the end of word/WORD          |
+--------------+-------------------------------------+
| %            | go to first matching paren/bracket  |
+--------------+-------------------------------------+

Putting it together:
[count][operator][text object / motion]

Examples:
6+   = 6x go down to line start
gUaW = capitalize a WORD
3ce  = 3x change to end of line
4$   = 4x go to end of line
d]m  = delete to start of next method
%    = jump to match of next paren or bracket

Useful part
Navigation at warp speed + tags

29:40 Project management

Difference between tabs and tuffers

- Tabs for window containers
- Windows for buffer viewports
- Buffers for file proxies

Buffers
-------

Buffers represent file proxies.
There is a buffer for every file visited in your VIM session.

Argument list are the files you opened vim with


Windows
-------

Windows are NOT a mapping to files (those are buffers).
Can have multiple windows on the same file! (e.g. different areas of the file).

+-------------------------+------------------------------+
|                         |                              |
|      Window 1           |          Window 2            |
|                         |                              |
|                         |                              |
|                         |                              |
+-------------------------+------------------------------+
|                                                        |
|                                                        |
|                  Window 3                              |
|                                                        |
|                                                        |
|                                                        |
+--------------------------------------------------------+

Window commands 
~~~~~~~~~~~~~~~

+-----------------------+-----------------------------------+
| Command               | What it does                      |
+=======================+===================================+
| Ctl+w s               | Split window horizontally         |
+-----------------------+-----------------------------------+
| Ctl+w v               | Split window vertically           |
+-----------------------+-----------------------------------+
| Ctl+w q               | Close window                      |
+-----------------------+-----------------------------------+
| Ctl+w w               | Alternate window                  |
+-----------------------+-----------------------------------+
| Ctl+w r               | Rotate windows                    |
+-----------------------+-----------------------------------+
| :window {cmd}         | Execute {cmd} for all windows     |
+-----------------------+-----------------------------------+
| :sf {FILE}            | Split window and :file {FILE}     | 
+-----------------------+-----------------------------------+


Tabs
----

gt go to next tab
gT 

Persistent session management using tmux
----------------------------------------

Efficient workflow navigation
-----------------------------

