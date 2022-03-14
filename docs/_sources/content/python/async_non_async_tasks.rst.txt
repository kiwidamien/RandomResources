How to async
============


If your code is written with :code:`async` in mind, then you are in pretty good shape.
For example, you might be using :code:`aiohttp` in order to do multiple downloads (which is
the right way of doing it). 

But what if you are stuck using some third party library? e.g. Your company has its own wrapper around

* :code:`requests` to get internal API calls
* :code:`boto` to get AWS resources
* :code: `postgres` to get RDS calls

and because you don't have access to the credentials, you are stuck using the original versions.

We can simulate this by asking

> How can we do multiple syncronous downloads using only "requests", a blocking library?

Method 1:
---------

https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor


Method 2:
---------

https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio

Here is a block of Python code that will work for you (3.5+)

.. code::python

  import asyncio
  import requests
  
  async def main():
      loop = asyncio.get_event_loop()
      future1 = loop.run_in_executor(None, requests.get, 'http://www.google.com')
      future2 = loop.run_in_executor(None, requests.get, 'http://www.google.co.uk')
      response1 = await future1
      response2 = await future2
      print(response1.text)
      print(response2.text)
  
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())

The basic trick is to use :code:`run_in_executor`.

Note that we are using :code:`requests.get` in two separate calls. 
This is subtle, so let's dig in a little bit more.

Digging in method 2
===================

Sync version
************

Let's start with a simple syncronous version, where we use an API to
get data about ISBNs for a book

.. literalinclude:: isbn.py
  :pyobject: print_book_info

Note this is a *syncronous* function.

We can get the syncronous version as

.. literalinclude:: isbn.py
  :pyobject: sync_main


This works, but the data requests do not occur in parallel.


Failed async version
********************

Let's try writing an async version of the main function, with
the spoiler alert that it will not work particularly well!

The code is 

.. literalinclude:: isbn.py
  :pyobject: async_main_long


This code is a little harder to execute in a script (in the REPL it is 
just :code:`await async_main_long()`) but it doesn't take advantage of
any of the async behavior.

The reason is when we hit the "await" keyword, we are signaling to Python
it is okay for some *other* task to take control. We only have the one
task -- different iterations of the loop are all sequential behind each
other.

Result: We get the correct result, but it takes just as long as the
syncronous version. If we tried running two copies of this function
at once

Failed async version 2
**********************

We might try having two tasks inside the loop at once:

.. literalinclude:: isbn.py
  :pyobject: async_main_multi_line

This also fails to get the promised speedup from asyncio, as there is
nothing to interput the :code:`await` statement. The code within the 
loop literally waits at the :code:`await` until it returns. 

What the :code:`await` does is allow another process to interrupt while
awaiting.

Successful async version
************************

Let's make each request it's own task, and then use :code:`asyncio.gather` to put all the tasks together.

.. literalinclude:: isbn.py
  :pyobject: async_main_sep_tasks


This version does what we want -- each task is placed separately on the event loop, so the next one can stat while we are :code:`await`-ing the previous one.

Seeing it altogether
********************

Let's put the entire example together in one script to play with

.. literalinclude:: isbn.py      

The results of this code block are

.. code:: python

   sync_main                      took 7.406 seconds
   async_main_long                took 7.399 seconds
   async_main_multi_line_loop     took 7.038 seconds
   async_main_sep_tasks           took 0.690 seconds
