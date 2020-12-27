Card Problem
============

Question
~~~~~~~~

There are 484 cards, and I get a random distribution of 912 cards (with replacement).
What is the probability that I have at least one example of each?

Answer
~~~~~~

We can select 912 cards in 484^912 different ways.

We need to pick each of the 484 cards once, then for the remaining
912 - 484 = 428 draws I don't care what happens.

For a particular sequence where I call the 484 that I want, and their order, 
the chance is 

(1^484) x (484)^428 / (484)^912 = 1/484^484

This makes sense: getting a particular card is 1/484, and we are doing this in
484 "named" places.

Number of arrangements of 484 places amongst 912: 912!/(912-484)! = 912!/428!

The probability of picking each card exactly once is

(912!/428!) x (1/484^484) = (tiny)


Use the log
-----------

We have
.. code::
   import math
   
   log_of_desired = (
       sum([math.log(num) for num in range(429, 913)])
     - 484*math.log(484)
    )
    print(log_of_desired)
    print(math.e**log_of_desired)

Program for getting number
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::
    import random
    from collections import Counter

    def distinct_cards_single_draw(cards=484, draws=912):
        draw = set([random.randint(1, cards) for _ in range(draws)])
        return len(draw)

    results = [distinct_cards_single_draw() for _ in range(10_000)]

    count = Counter(results)
    count.most_common() 