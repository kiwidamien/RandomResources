# Line Profiling

How to get profile information without using the @profile decorator:

```python
from line_profiler import LineProfiler

def square(numbers):
  accumulator = []
  for n in numbers:
    accumulator.append(n*n)
  return accumulator

lp = LineProfiler()
profiled_square = lp(square)
profiled_square([1,2,3,4,5,6])
lp.print_stats()
```

This gives
```
Timer unit: 1e-06s

Total time: 3e-05s

Line #    Hits    Time    Per Hit    % Time    Line Contents
============================================================
   1             
   2       1      9.0        9.0       30.0    accumulator = []
   3       7     10.0        1.4       33.3    for n in numbers:
   4       6      9.0        1.5       30.0      accumulator.append(n*n)
   5       1      2.0        2.0        6.7    return accumulator
```
