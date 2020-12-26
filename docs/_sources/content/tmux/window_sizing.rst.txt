Fixing tmux pane pains
======================

Scrolling
---------

* Enter scoll mode
  :code:`(Ctrl+b) +  [`

* Move in scroll mode
  Just use arrow keys =)

* Quit scroll mode
  :code: `q`

It seems option + up / option + down will do in OSX.



Resize panes
------------
.. code::

        PREFIX : resize-pane -D (Resizes the current pane down)
        PREFIX : resize-pane -U (Resizes the current pane upward)
        PREFIX : resize-pane -L (Resizes the current pane left)
        PREFIX : resize-pane -R (Resizes the current pane right)
        PREFIX : resize-pane -D 20 (Resizes the current pane down by 20 cells)
        PREFIX : resize-pane -U 20 (Resizes the current pane upward by 20 cells)
        PREFIX : resize-pane -L 20 (Resizes the current pane left by 20 cells)
        PREFIX : resize-pane -R 20 (Resizes the current pane right by 20 cells)
        PREFIX : resize-pane -t 2 20 (Resizes the pane with the id of 2 down by 20 cells)
        PREFIX : resize-pane -t -L 20 (Resizes the pane with the id of 2 left by 20 cells)

From :ref:`this list <https://gist.github.com/MohamedAlaa/2961058>`__ of nifty tmux shortcuts
