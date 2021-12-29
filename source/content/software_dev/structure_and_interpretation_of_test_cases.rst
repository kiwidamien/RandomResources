Structure and Interpretation of Test Cases
==========================================

* `Video Link <https://www.youtube.com/watch?v=APUCMSPiNh4>`__
* Speaker: Kevlin Henney
* Rating: 2/5

Overview
--------

Looks at the question of "what to test" and "how to test".
This talk doesn't have an opinion on language or test framework, but
instead talks about how to write a test that isn't just a reimplementation.


The talk begins with a talk about when unit testing is useful, and some dismissive
comments about mocking out systems.
The talk focuses on unit testing for items where you don't have to mock out.

Kelvin does a "deep dive" on testing whether a given year is a leap year.

The Leap Year Problem
~~~~~~~~~~~~~~~~~~~~~

The leap year problem is to test a function :code:`is_leap_year(yr)`.

The question is how do we test this code? How should we write the tests for this code,
that doesn't end up just reimplementing the function?

The specification of whether a year is a leap year are:

* Any year divisible by 400 is a leap year
* Any year divisible by 4, but is not divisible by 100, is a leap year
* Any other year is not a leap year

We know that the year 2000 is a leap year (and passes the naive test), but the year 1900 is NOT a leap year.

Kevlin advocates that the tests should be along the lines of 

.. code:: python

   # This is the most common case, so start here
   test_years_not_divisible_by_4_are_not_leap_years

   # Next most common, and what many peope are familiar with
   test_years_divisible_by_4_but_not_100_are_leap_years
   
   # Now getting to the cases where people may not know -- many of us have not lived in
   # a year where this would come up (1900 and 2100 are the two closest)
   test_years_divisibile_by_100_but_not_400_are_not_leap_years

   # final test
   test_years_divisible_by_400_are_leap_years

The argument is that if the tests fail, then this indicates exactly what the problem in your code is.
It is also a good way of setting up tests in a way that makes sense for hypothesis test generation.


Stack
~~~~~

It was difficult to take notes for this section, as Kevlin uses Stacks in a lot of his talks.
This wasn't as interesting as some of his other talks including stacks.
One of my favorites was the `immutability talk <https://www.youtube.com/watch?v=APUCMSPiNh4>`__,
which shows how to make a persistent data structure with immutability.

The main view on Stacks were:

- try to specify the pre-conditions and post-conditions 
  - e.g. when pushing onto an empty stack, the stack should have a depth of 1 and the top element should be the thing just pushed
- avoid tests that simply construct the stack, or that check that an empty stack with something pushed is non-empty. Be specific.

There were a lot of observations that an empty stack is "different" from a non-empty stack:

+-----------+-------------+-----------------+
| Operation | Empty stack | Non-empty stack |
+-----------+-------------+-----------------+
| push      | OK          | OK              |
| pop       | ERR         | OK              |
| top       | ERR         | OK              |
| depth     | OK (0)      | OK              |
+-----------+-------------+-----------------+

In *implementation*, Kevlin prefers to have *EmptyStack* and *NonEmptyStack* as different subclasses of *Stack*.
It isn't clear that this implementation detail should affect testing.
However, he argues in this talk that the behavior of empty and non-empty stacks are different enough that the tests should be grouped
in terms of tests for empty stacks and non-empty stacks separately.
There is also some talk about full stacks.

Other comments
~~~~~~~~~~~~~~

* TDD should not just check the code works, they should also act as documentation (Pryce and Freeman, *Are your tests really driving development?*)
  * Kevlin suggests using examples in tests that communicate intent. e.g. 
    * Using :code:`assert is_leap_year(1998)==False` is better than `assert is_leap_year(42)==False` because people will look at `1998` and will be a year (42 doesn't immediately screm year)
    * Using a name as "foo" or "bar" is not great, a name that is recognized as a name (e.g. "Andrew") is better. It also can communicate assumptions about case.
    * Note that this is the opposite of what hypothesis will do, which is to generate gibberish that a human generally wouldn't think of
* Can have tests that could be included in more general parameterized tests, but can emphasize that you have considered them.
  * Example from the leap year example was one test that explicitly tests the years 1 - 10,000; a second test that tests years -1 to -10,000; a third test that tests year 0.

    It isn't clear that year 0 exists (depends on the calendar), but by having a separate test we can emphasize that it has been thought of and the issue hasn't been overlooked,
    which would not be the case if we tested from year -10,000 to 10,000.
* Can make tests of the form **Given .... WHEN .... THEN.....**. Try to get as close to the preconditions and postconditions as possile.
  * Can also be thought of ensure preconditions, and assert postconditions
  * Can be used to show users how the code is set up.
  * Can be used to group tests:
    * Common pre-conditions (GIVEN): use the same fixtures
    * Common post-conditions (THEN): can choose to order the tests by THEN (in code) to help communicate to reader how outcomes can occur
      * e.g. in leap year code, could have tests that return True first; then those that return False
      * e.g. in stack code, could have tests that throw errors first; then those that return results 
