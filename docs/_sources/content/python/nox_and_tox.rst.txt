Nox and Tox for Python testing
******************************

What are they?
--------------

Tox and Nox are two different tools for solving the same problem:

* running python tests (specifically :code:`pytest` tests) in specific python environment(s)

They both do this by constructing a python environment specifically for tests. This should be similar to how 
remote work starts a brand new container. This ensures that you know *exactly* what environment your tests
passed or failed in.

Tox and Nox both allow you to specify multiple environments.

**Pros:**

* Allows you to be very targeted about the environment that you are testing on
  
  * You might worry about overfitting, but really when we run on our own machine we are testing a specific environment. The solution here means we can _reproduce_ the specific environment.

* Able to run and check multiple environments.


**Cons:**

* Runs significantly slower, because you are constructing a virtual environment.

A good `article <https://python.plainenglish.io/unit-testing-in-python-tox-and-nox-833e4bbce729>`_ on the difference between
tox and nox is here. This article will primarily use nox.


Difference between tox and nox
------------------------------

They both solve the same problem. You do not need to use both of them, and should only pick one.
The difference between them is

1. **tox**: Has a configuration file that drives it called :code:`tox.ini`
2. **nox**: Has a python script that drives it called :code:`noxfile.py`


My normal workflow
------------------

1. When doing local development, run :code:`pytest` in my local dev environment.
2. When about to push to my branch, or at major milestones, run :code:`nox`

Example file
------------

Let's see a noxfile in action!

.. literalinclude:: noxfile.py
   :language: python

