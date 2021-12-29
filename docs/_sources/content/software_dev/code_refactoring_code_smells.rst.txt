Code Refactoring: Learn Code Smells
===================================

* `Video link <https://www.youtube.com/watch?v=D4auWwMsEnY>`__
* Speaker: Sandi Metz
* Rating: 5/5

Overview
--------

* Code smells are NOT just "I don't like how you w


Details
-------

* Code smells are NOT just "I don't like your code". Code smells are not necessarily bad.
  Code smells are indications that something **might** be wrong.

* Code smells have specific names, and specific solutions. There are 22 different named code smells from Ken Bent.
  These code smells have been grouped into the following 5 groups (with two thrown away).
  - Bloaters 
  - Tool 
  - Change Preventers 
  - Dispensibles
  - Couplers

* The two thrown away were "comments" and "incomplete library code" (not addressed again in this talk, but enough has been written on 
* Refactorings have names and recipies: if you can identify your code smell, there is a recipe on how to fix it.

Bloaters
~~~~~~~~

"Makes code bigger than it needs to be when used"

Code smells are

- Long Method
- Large class
- Data Clumps
- Long Parameter List
- Primitive Obsession

Primitive Obsession probably the only one that needs elaboration. It is when a primitive is standing in for something else.
For example, if you have different behaviors based on a number or string passed in. 
(e.g. if :code:`order_type` is 6 do this, if :code:`order_type` is 8 do something else).
Basically we can think of this as an ENUM using primatives.
The objects you are talking to are too dumb to 


Tool misuse
~~~~~~~~~~~

Code smells are

- Switch statements
- Refused Bequest
- Alternative Classes with Different Interfaces
- Temporary Field

A **refused bequest** is a problem that occurs when a child class refuses to implement a parent class method.
Generally points to the wrong abstraction getting used in your object model


Change Preventers
~~~~~~~~~~~~~~~~~

"Things that make you not want to change code, or makes code hard to change"

Code smells are

- Divergent Cahnge
- Shotgun Surgery
- Parallel Inheritance


Dispensibles
~~~~~~~~~~~~

""

Code smells are 

- Lazy Class
- Speculative Generality
- Data Class: should have behavior as well as data in classes
- Duplicated Code

Couplers
~~~~~~~~

"Objects that could not be used in another context, they come as a bundle"

Code smells are 

- Feature envy: An object sends more messages to another object than it sends to itself (i.e. really wants some features of another object)
- Inappropriate intimacy: Accessing private methods of another object
- Message Chains: Long chained methods where the types change, and you call a method on the changed type. See below for example
- Middle Man: An object that only exists to pass messages between objects

A small diversion on message chains (aka Law of Dementer violations).
The following is NOT an example:

.. code:: python

    dataframe_selection = (client_df
                             .query('state == "CA"')
                             .query('age < 35')
                             .query('age > 20')
                           )

This code keeps dealing with dataframes. We have accepted that the client code knows how to call methods on dataframes (we have :code:`client_df.XXXXXXX`).
Since :code:`query(....)` returns a dataframe, we have not increased the number of types we need to know about.

This is also NOT an example of a Law of Demeter violation:

.. code:: python

    (n_targeted_clients, _) = (client_df
                                .query('state == "CA"')
                                .query('age < 35')
                                .query('age > 20')
                                .shape)

It also isn't how you would write this code! The :code:`.shape` at the end does transform types (from dataframe to tuple) but we don't call additional methods
on the tuple. We have already accepted that the client code knows about the dataframe API, and we have not extended information to the tuple API (you could argue about
the use of unpacking).

This *is* a violation of the Law of Demeter:

.. code:: python

    n_targeted_clients =  (client_df
                            .query('state == "CA"')
                            .query('age < 35')
                            .query('age > 20')
                            .client_id
                            .nunique()
                          )

We have moved from a dataframe to a series, and then called a method on the series.
Thus our client is expected to know about both the DataFrame API **and** the Series API. 
This indicates that the DataFrame and Series APIs are tightly coupled, which should not be a surprise.
It is a Law of Demeter violation, but probably not one worth addressing as it makes sense for these different Pandas objects to be tightly coupled.

Note the following does NOT fix it

.. code:: python

    # This line is okay, only one type change and no methods called
    clients = (client_df.query('state == "CA"').query('age < 35').query('age > 20').client_id

    # This line (by itself) is also okay, only using Series API
    n_targeted_clients = clients.nunique()

There is no single line that violates the Law of Demeter here, but the lines taken together means the client has to know both the DataFrame API and
the Series API.
The code, taken together, is a violation of the Law of Demeter.

Note that almost all groupby statements in pandas aer going to be law of demeter violations.
This is okay; going back to the opening statement code smells are an indication that something might be wrong.
You might be willing to treat pandas (DataFrame, Series, Grouper) as a whole tightly coupled unit, which would make tagging Law of Demeter violations more useful.


Code example
~~~~~~~~~~~~

At 20:20, the second refactoring for MessageChains begins. There are three classes, that implement something similar to SQLAlchemcy

.. code::ruby
  
  class Foo:
    def expense_total(range)
        Expense.where(date: range).sum('cost')
    end
  end

It is okay for our object to know about Expense (sends the message :code:`where`), but it isn't okay for our object to know about how to use what :code:`where` returns (an ActiveRecord/SqlAlchemy
record).

Way it was described was if testing our object, we would need to mock or implement :code:`Expense` and :code:`range`.
As written, we would also have to know about :code:`ActiveRecord` to implement the :code:`sum` method.
We now have to worry about which methods in :code:`ActiveRecord` we have to mock to make things run.

Answer would be to move the total method into `Expense`

.. code::ruby

   class Expense
     def total(range)
        where(range).sum('cost')   # Okay for expense to know about its collaborators
     end
   end

   class Foo
     def expense_total(range)
        Expense.total(range)       # Okay for Foo to know about its colaborators
     end
   end

The big question that comes up when you do this is, and if you mock out Expense, you don't test the query.
If you don't mock it out, calling :code:`Foo.expense_total` runs the real query, so your tests run really slowly.

We want fast tests, that reflect reality.
Solution presented was to generalize Expense to derive from an ABC or Protocol (e.g. :code:`Totalizable`) and use dependency injection.
Write a mock Totalizable that doesn't require a query.

Pros:

* Tests run really fast
* We are testing our protocol behavior (total returns an object of the right type)

Cons:

* Not testing SQLAlchemy or ActiveRecord (but they have extensive tests)
* Not testing our schemas (argument here is that we have Expense own the queries, so we have a small number of objects that run real queries)
* Makes methods longer (we have to inject the dependency) 


