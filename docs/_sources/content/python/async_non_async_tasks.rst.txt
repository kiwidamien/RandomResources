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
