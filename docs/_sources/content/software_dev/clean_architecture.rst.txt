The Clean Architecture in Python
********************************

Talk by `Brandon Rhodes <https://www.youtube.com/watch?v=DJtef410XaM>`_, `slides <>`_

* Immutablilty
* Clean Architecture


Notes
=====

Tables vs Data 
--------------
Timestamp: 32:00

- Amusing anacdote about Knuth "most commonly used words" 10-page Pascal script being replaced with a 6 line shell script by McIlroy.
- Note the importance of doing one thing and generalizing it, so we can pipe together
- Allow the flow of data to be observed throughout the program.

Immutablity
-----------

"The win for immutability is distributed computing" -- Gary Burnhardt

Mapping data structures to data structures, without needing to have side-effects, we are already ready for spreading the work across different machines.


