Timing in Notebooks
===================

Jupyter notebooks have a really useful extension that allows you to show the per-cell
execution time. For a long time, this has been missing in Jupyter lab (or at least 
harder to find). 

https://stackoverflow.com/questions/56843745/automatic-cell-execution-timing-in-jupyter-lab

This StackOverflow answer is great at showing how to enable cell-based timings.

The short version:

1. Use pip to install `pip install jupyterlab_execute_time`
2. Reload the notebook (you don't need to shut down the notebook)
3. Go to Settings -> Advanced Settings Editor, select the Notebook settings, and then copy the following 
   JSON blob into the user settings

.. code::

   {"recordTiming": true}

And now you should have timings recorded in each cell!!	
   
