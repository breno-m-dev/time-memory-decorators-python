# Python Time, Memory & Logging Decorators

## About
A small Python project implementing three decorators for measuring execution
time, tracking memory usage, and logging
function calls.

## Decorators

### 1. Time Decorator
Measures how long a function takes to execute using time.perf_counter().

### 2. Memory Decorator
Tracks current and peak Python memory allocations fora method execution using
tracemalloc.

### 3. Log Decorator
Logs information about function calls...

## Example
Import the decorators and apply them to a function:

```python
from time_decorator import measure_time
from memory_decorator import measure_memory
from log_decorator import log

@log
@measure_time
@measure_memory
def big_list():
    return [x for x in range(1_000_000)]

big_list()
```

The decorators can be combined to measure different aspects of a function's
execution.

## Results

python test.py      
Current memory: 3.12 KB
Peak memory: 1964780.38 KB
big_list took 42.94 seconds to be executed

## Technologies

- Python
- time
- tracemalloc
- functools wraps
