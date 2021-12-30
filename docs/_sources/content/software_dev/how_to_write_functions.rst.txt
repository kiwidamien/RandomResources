HOWTO Write a Function
======================

* `Video link <https://www.youtube.com/watch?v=rrBJVMyD-Gs>`__
* Speaker: Jack Diederich
* Rating: 2/5


Overview
--------


Details
-------

The talk started with some solid advice, particulary around structuring functions.

1. **Input**: Parse input at the top, give errors early, do asserts (help readers of code know what to expect)
2. **Transform**: Exceptions should be exceptional, reader should be bored
3. **Output:** Format the result in a way that is useful to your caller.

There was some nice stuff in there about early returning (e.g. if doing a dry run, put the early return before all
the dangerous stuff, instead of blocking off dangerous calls with :code:`if is not dry_run`, as you need to make sure
you enclose all dangerous blocks).

The things I disagree with started around 15:00. Things like 

- set defaults to integers, rather than named constants.
- use default exceptions, as they have you covered (no discussion about how subclassing exceptions helps you determine if the 
  exception is from you or someone else). Raymond Hettinger has the opposite advice; block lowlevel exceptions and raise your 
  own so they are more readable and relatable.
- The stuff about making the linter happy not being useful effort I disagreed with as well. Not because I think linters are
  ways of producing the highest quality code (e.g. see RH's talk on PEP8 vs beautiful Python code).
  Jack claims that the problem with linters are coworkers that love linters. 
  Coworkers who love linters will be able to generate effort to fix the linting issues.

  This is a sign of a dysfunctional workplace, instead. 
    * By adding linting to the CI, you can lint the code prior to code review, so people don't get distracted by code style.
    * You can all agree on what the linting rules, and then it is done.
    * You can also switch off the linting rules if you are doing something strange (e.g. Jack's example of passing a multable datastructure
      to cache). Here, writing a switch-off statment to the linter also serves the purpose of telling a person that the default mutable object
      is intentional and not an oversight.
- JD's answer to how to refactor by renaming args to :code:`ignore` on how to capture people using keyword arguments. 
  The lack of understanding of the question here really downgraaded the talk for me.

